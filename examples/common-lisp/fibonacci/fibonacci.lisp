(defun solve (n) (loop with a = 0 with b = 1 repeat n do (psetf a b b (+ a b)) finally (return a)))

(format t "~D~%" (solve 0))
(format t "~D~%" (solve 1))
(format t "~D~%" (solve 2))
(format t "~D~%" (solve 3))
(format t "~D~%" (solve 10))
(format t "~D~%" (solve 20))
(format t "~D~%" (solve 30))
