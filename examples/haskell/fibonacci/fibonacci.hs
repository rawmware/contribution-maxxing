solve :: Integer -> Integer
solve n = fib n 0 1
  where fib 0 a _ = a
        fib i a b = fib (i-1) b (a+b)

main :: IO ()
main = do
  print (solve 0)
  print (solve 1)
  print (solve 2)
  print (solve 3)
  print (solve 10)
  print (solve 20)
  print (solve 30)
