let rec solve a b = if b = 0 then a else solve b (a mod b)

let () =
  Printf.printf "%d\n" (solve 0 0);
  Printf.printf "%d\n" (solve 0 7);
  Printf.printf "%d\n" (solve 7 0);
  Printf.printf "%d\n" (solve 48 18);
  Printf.printf "%d\n" (solve 17 13);
  Printf.printf "%d\n" (solve 270 192)
