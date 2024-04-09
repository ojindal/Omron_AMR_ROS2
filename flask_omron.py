from flask import Flask, request, jsonify
from threading import Thread
import lazer_subscriber as lazer_subscriber
import status_subscriber as status_subscriber
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import subprocess
import atexit
import signal
import asyncio 

app = Flask(__name__)

# Start the background script
script_path = "src/om_aiv_navigation/om_aiv_navigation/goto_point.py"
process = subprocess.Popen(['python3', script_path])

def cleanup():
    print("Terminating the background script...")
    process.terminate()
    process.wait()

atexit.register(cleanup)

def handle_sigterm(*args):
    cleanup()
    exit(0)

signal.signal(signal.SIGTERM, handle_sigterm)
signal.signal(signal.SIGINT, handle_sigterm)

def generate_plot_base64(response_container, radius):
    plot_base64 = lazer_subscriber.main(radius=radius)
    response_container['plot_base64'] = plot_base64

def generate_status(response_container):
    status_str = status_subscriber.main()
    response_container["status_str"] = status_str

class GotoPointPublisher(Node):
    def __init__(self):
        super().__init__('goto_point_publisher')
        self.publisher_ = self.create_publisher(String, '/goal_point', 10)

    def publish_message(self, message):
        msg = String()
        msg.data = message
        self.publisher_.publish(msg)

@app.route('/om_image', methods=['POST'])
def get_image():
    data = request.get_json()
    radius = data.get('radius', 2)
    response_container = {}
    thread = Thread(target=generate_plot_base64, args=(response_container, radius))
    thread.start()
    thread.join()
    plot_base64 = response_container.get('plot_base64')
    if plot_base64:
        return jsonify({"image": plot_base64})
    else:
        return jsonify({"error": "No data generated from laser subscriber."}), 500

@app.route('/om_status', methods=['POST'])
def get_status():
    response_container = {}
    thread = Thread(target=generate_status, args=(response_container,))
    thread.start()
    thread.join()
    status_str = response_container.get('status_str')
    if status_str:
        return jsonify({"status": status_str})
    else:
        return jsonify({"error": "No data generated from status subscriber."}), 500

@app.route('/om_goto_point', methods=['POST'])
def goto_point_action():
    data = request.get_json()
    message = data.get('message', '')
    try:
        rclpy.init(args=None)
        node = GotoPointPublisher()
        node.publish_message(message)
        rclpy.shutdown()
        return jsonify({"message": "Message published to /goto_point topic"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/om_dock', methods=['POST'])
async def dock_action():
    script_path = "src/om_aiv_navigation/om_aiv_navigation/dock.py"
    try:
        process = await asyncio.create_subprocess_exec("python3", script_path, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        if process.returncode == 0:
            return jsonify({"message": f"Script executed successfully: {script_path}", "status": "success"}), 200
        else:
            error_message = stderr.decode().strip() if stderr else "Unknown error"
            return jsonify({"error": f"Script execution failed: {error_message}", "status": "failure"}), 500
    except Exception as e:
        return jsonify({"error": str(e), "status": "failure"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
