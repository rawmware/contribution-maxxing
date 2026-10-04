(defn solve [a b] (if (zero? b) a (recur b (mod a b))))

(println (solve 0 0))
(println (solve 0 7))
(println (solve 7 0))
(println (solve 48 18))
(println (solve 17 13))
(println (solve 270 192))
