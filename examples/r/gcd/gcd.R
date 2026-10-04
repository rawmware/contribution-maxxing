solve <- function(a, b) { while (b != 0) { r <- a %% b; a <- b; b <- r }; a }

cat(sprintf("%.0f\n", solve(0, 0)))
cat(sprintf("%.0f\n", solve(0, 7)))
cat(sprintf("%.0f\n", solve(7, 0)))
cat(sprintf("%.0f\n", solve(48, 18)))
cat(sprintf("%.0f\n", solve(17, 13)))
cat(sprintf("%.0f\n", solve(270, 192)))
