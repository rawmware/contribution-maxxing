use strict;
use warnings;
sub solve { my ($n) = @_; my $r = 1; for my $i (2..$n) { $r *= $i; } return $r; }

print solve(0), "\n";
print solve(1), "\n";
print solve(2), "\n";
print solve(5), "\n";
print solve(10), "\n";
print solve(12), "\n";
