#lang racket

(define (solve n) (if (< n 2) 0 (let trial ([d 2]) (cond [(> (* d d) n) 1] [(zero? (remainder n d)) 0] [else (trial (+ d 1))]))))

(displayln (solve 0))
(displayln (solve 1))
(displayln (solve 2))
(displayln (solve 3))
(displayln (solve 4))
(displayln (solve 25))
(displayln (solve 97))
(displayln (solve 121))
(displayln (solve 997))
