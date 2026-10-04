(defn solve [n] (reduce * 1 (range 2 (inc n))))

(println (solve 0))
(println (solve 1))
(println (solve 2))
(println (solve 5))
(println (solve 10))
(println (solve 12))
