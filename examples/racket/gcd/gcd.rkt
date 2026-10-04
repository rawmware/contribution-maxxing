#lang racket

(define (solve a b) (if (zero? b) a (solve b (remainder a b))))

(displayln (solve 0 0))
(displayln (solve 0 7))
(displayln (solve 7 0))
(displayln (solve 48 18))
(displayln (solve 17 13))
(displayln (solve 270 192))
