#lang racket

(define (solve n) (let fib ([i n] [a 0] [b 1]) (if (zero? i) a (fib (- i 1) b (+ a b)))))

(displayln (solve 0))
(displayln (solve 1))
(displayln (solve 2))
(displayln (solve 3))
(displayln (solve 10))
(displayln (solve 20))
(displayln (solve 30))
