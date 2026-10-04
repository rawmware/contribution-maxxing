(defn solve [n] (loop [i n a 0 b 1] (if (zero? i) a (recur (dec i) b (+ a b)))))

(println (solve 0))
(println (solve 1))
(println (solve 2))
(println (solve 3))
(println (solve 10))
(println (solve 20))
(println (solve 30))
