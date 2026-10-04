(defun solve (a b) (if (zerop b) a (solve b (mod a b))))

(format t "~D~%" (solve 0 0))
(format t "~D~%" (solve 0 7))
(format t "~D~%" (solve 7 0))
(format t "~D~%" (solve 48 18))
(format t "~D~%" (solve 17 13))
(format t "~D~%" (solve 270 192))
