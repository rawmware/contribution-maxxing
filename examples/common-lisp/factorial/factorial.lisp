(defun solve (n) (loop with r = 1 for i from 2 to n do (setf r (* r i)) finally (return r)))

(format t "~D~%" (solve 0))
(format t "~D~%" (solve 1))
(format t "~D~%" (solve 2))
(format t "~D~%" (solve 5))
(format t "~D~%" (solve 10))
(format t "~D~%" (solve 12))
