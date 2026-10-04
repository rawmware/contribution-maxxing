let solve n = let rec fib i a b = if i = 0 then a else fib (i-1) b (a+b) in fib n 0 1

let () =
  Printf.printf "%d\n" (solve 0);
  Printf.printf "%d\n" (solve 1);
  Printf.printf "%d\n" (solve 2);
  Printf.printf "%d\n" (solve 3);
  Printf.printf "%d\n" (solve 10);
  Printf.printf "%d\n" (solve 20);
  Printf.printf "%d\n" (solve 30)
