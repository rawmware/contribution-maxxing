solve <- function(n) { r <- 1; if (n >= 2) for (i in 2:n) r <- r * i; r }

cat(sprintf("%.0f\n", solve(0)))
cat(sprintf("%.0f\n", solve(1)))
cat(sprintf("%.0f\n", solve(2)))
cat(sprintf("%.0f\n", solve(5)))
cat(sprintf("%.0f\n", solve(10)))
cat(sprintf("%.0f\n", solve(12)))
