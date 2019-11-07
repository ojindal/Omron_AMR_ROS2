
(cl:in-package :asdf)

(defsystem "om_aiv_util-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Service" :depends-on ("_package_Service"))
    (:file "_package_Service" :depends-on ("_package"))
    (:file "ServiceExample" :depends-on ("_package_ServiceExample"))
    (:file "_package_ServiceExample" :depends-on ("_package"))
  ))