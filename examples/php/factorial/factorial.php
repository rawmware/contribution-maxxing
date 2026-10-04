<?php
declare(strict_types=1);
function solve(int $n): int { $r = 1; for ($i = 2; $i <= $n; $i++) $r *= $i; return $r; }

echo solve(0), PHP_EOL;
echo solve(1), PHP_EOL;
echo solve(2), PHP_EOL;
echo solve(5), PHP_EOL;
echo solve(10), PHP_EOL;
echo solve(12), PHP_EOL;
