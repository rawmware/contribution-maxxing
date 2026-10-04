let solve n = let r = ref 1 in for i = 2 to n do r := !r * i done; !r

let () =
  Printf.printf "%d\n" (solve 0);
  Printf.printf "%d\n" (solve 1);
  Printf.printf "%d\n" (solve 2);
  Printf.printf "%d\n" (solve 5);
  Printf.printf "%d\n" (solve 10);
  Printf.printf "%d\n" (solve 12)
