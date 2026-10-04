use strict;
use warnings;
sub solve { my ($n) = @_; return 0 if $n < 2; for (my $d = 2; $d*$d <= $n; $d++) { return 0 if $n % $d == 0; } return 1; }

print solve(0), "\n";
print solve(1), "\n";
print solve(2), "\n";
print solve(3), "\n";
print solve(4), "\n";
print solve(25), "\n";
print solve(97), "\n";
print solve(121), "\n";
print solve(997), "\n";
