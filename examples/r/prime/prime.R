solve <- function(n) { if (n < 2) return(0); d <- 2; while (d*d <= n) { if (n %% d == 0) return(0); d <- d+1 }; 1 }

cat(sprintf("%.0f\n", solve(0)))
cat(sprintf("%.0f\n", solve(1)))
cat(sprintf("%.0f\n", solve(2)))
cat(sprintf("%.0f\n", solve(3)))
cat(sprintf("%.0f\n", solve(4)))
cat(sprintf("%.0f\n", solve(25)))
cat(sprintf("%.0f\n", solve(97)))
cat(sprintf("%.0f\n", solve(121)))
cat(sprintf("%.0f\n", solve(997)))
