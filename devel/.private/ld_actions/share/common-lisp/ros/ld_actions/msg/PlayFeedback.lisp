; Auto-generated. Do not edit!


(cl:in-package ld_actions-msg)


;//! \htmlinclude PlayFeedback.msg.html

(cl:defclass <PlayFeedback> (roslisp-msg-protocol:ros-message)
  ((received_data
    :reader received_data
    :initarg :received_data
    :type cl:string
    :initform ""))
)

(cl:defclass PlayFeedback (<PlayFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PlayFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PlayFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ld_actions-msg:<PlayFeedback> is deprecated: use ld_actions-msg:PlayFeedback instead.")))

(cl:ensure-generic-function 'received_data-val :lambda-list '(m))
(cl:defmethod received_data-val ((m <PlayFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ld_actions-msg:received_data-val is deprecated.  Use ld_actions-msg:received_data instead.")
  (received_data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PlayFeedback>) ostream)
  "Serializes a message object of type '<PlayFeedback>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'received_data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'received_data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PlayFeedback>) istream)
  "Deserializes a message object of type '<PlayFeedback>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'received_data) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'received_data) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PlayFeedback>)))
  "Returns string type for a message object of type '<PlayFeedback>"
  "ld_actions/PlayFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PlayFeedback)))
  "Returns string type for a message object of type 'PlayFeedback"
  "ld_actions/PlayFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PlayFeedback>)))
  "Returns md5sum for a message object of type '<PlayFeedback>"
  "0db3bc19eeede9e4ee493e93f03da761")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PlayFeedback)))
  "Returns md5sum for a message object of type 'PlayFeedback"
  "0db3bc19eeede9e4ee493e93f03da761")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PlayFeedback>)))
  "Returns full string definition for message of type '<PlayFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Feedback~%string received_data~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PlayFeedback)))
  "Returns full string definition for message of type 'PlayFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Feedback~%string received_data~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PlayFeedback>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'received_data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PlayFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'PlayFeedback
    (cl:cons ':received_data (received_data msg))
))
