use strict;
use warnings;
sub solve { my ($a, $b) = @_; while ($b != 0) { ($a, $b) = ($b, $a % $b); } return $a; }

print solve(0, 0), "\n";
print solve(0, 7), "\n";
print solve(7, 0), "\n";
print solve(48, 18), "\n";
print solve(17, 13), "\n";
print solve(270, 192), "\n";
