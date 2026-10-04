<?php
declare(strict_types=1);
function solve(int $a, int $b): int { while ($b != 0) { [$a, $b] = [$b, $a % $b]; } return $a; }

echo solve(0, 0), PHP_EOL;
echo solve(0, 7), PHP_EOL;
echo solve(7, 0), PHP_EOL;
echo solve(48, 18), PHP_EOL;
echo solve(17, 13), PHP_EOL;
echo solve(270, 192), PHP_EOL;
