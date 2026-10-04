solve <- function(n) { a <- 0; b <- 1; for (i in seq_len(n)) { t <- a+b; a <- b; b <- t }; a }

cat(sprintf("%.0f\n", solve(0)))
cat(sprintf("%.0f\n", solve(1)))
cat(sprintf("%.0f\n", solve(2)))
cat(sprintf("%.0f\n", solve(3)))
cat(sprintf("%.0f\n", solve(10)))
cat(sprintf("%.0f\n", solve(20)))
cat(sprintf("%.0f\n", solve(30)))
