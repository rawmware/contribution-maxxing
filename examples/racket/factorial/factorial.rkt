#lang racket

(define (solve n) (for/fold ([r 1]) ([i (in-range 2 (+ n 1))]) (* r i)))

(displayln (solve 0))
(displayln (solve 1))
(displayln (solve 2))
(displayln (solve 5))
(displayln (solve 10))
(displayln (solve 12))
