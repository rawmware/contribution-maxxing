solve :: Integer -> Integer
solve n = product [2..n]

main :: IO ()
main = do
  print (solve 0)
  print (solve 1)
  print (solve 2)
  print (solve 5)
  print (solve 10)
  print (solve 12)
