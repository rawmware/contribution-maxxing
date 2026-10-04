solve :: Integer -> Integer
solve n | n < 2 = 0
        | otherwise = trial 2
  where trial d | d*d > n = 1
                | n `mod` d == 0 = 0
                | otherwise = trial (d+1)

main :: IO ()
main = do
  print (solve 0)
  print (solve 1)
  print (solve 2)
  print (solve 3)
  print (solve 4)
  print (solve 25)
  print (solve 97)
  print (solve 121)
  print (solve 997)
