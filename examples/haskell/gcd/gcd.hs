solve :: Integer -> Integer -> Integer
solve a 0 = a
solve a b = solve b (a `mod` b)

main :: IO ()
main = do
  print (solve 0 0)
  print (solve 0 7)
  print (solve 7 0)
  print (solve 48 18)
  print (solve 17 13)
  print (solve 270 192)
