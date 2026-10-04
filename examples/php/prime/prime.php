<?php
declare(strict_types=1);
function solve(int $n): int { if ($n < 2) return 0; for ($d = 2; $d * $d <= $n; $d++) if ($n % $d == 0) return 0; return 1; }

echo solve(0), PHP_EOL;
echo solve(1), PHP_EOL;
echo solve(2), PHP_EOL;
echo solve(3), PHP_EOL;
echo solve(4), PHP_EOL;
echo solve(25), PHP_EOL;
echo solve(97), PHP_EOL;
echo solve(121), PHP_EOL;
echo solve(997), PHP_EOL;
