use strict;
use warnings;
sub solve { my ($n) = @_; my ($a, $b) = (0, 1); for (1..$n) { ($a, $b) = ($b, $a + $b); } return $a; }

print solve(0), "\n";
print solve(1), "\n";
print solve(2), "\n";
print solve(3), "\n";
print solve(10), "\n";
print solve(20), "\n";
print solve(30), "\n";
