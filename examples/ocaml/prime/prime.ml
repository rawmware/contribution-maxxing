let solve n = let rec trial d = if d*d > n then 1 else if n mod d = 0 then 0 else trial (d+1) in if n < 2 then 0 else trial 2

let () =
  Printf.printf "%d\n" (solve 0);
  Printf.printf "%d\n" (solve 1);
  Printf.printf "%d\n" (solve 2);
  Printf.printf "%d\n" (solve 3);
  Printf.printf "%d\n" (solve 4);
  Printf.printf "%d\n" (solve 25);
  Printf.printf "%d\n" (solve 97);
  Printf.printf "%d\n" (solve 121);
  Printf.printf "%d\n" (solve 997)
