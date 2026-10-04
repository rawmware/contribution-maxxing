<?php
declare(strict_types=1);
function solve(int $n): int { $a = 0; $b = 1; for ($i = 0; $i < $n; $i++) [$a, $b] = [$b, $a + $b]; return $a; }

echo solve(0), PHP_EOL;
echo solve(1), PHP_EOL;
echo solve(2), PHP_EOL;
echo solve(3), PHP_EOL;
echo solve(10), PHP_EOL;
echo solve(20), PHP_EOL;
echo solve(30), PHP_EOL;
