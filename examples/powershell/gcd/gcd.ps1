Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Solve([long]$a, [long]$b) { while ($b -ne 0) { $r = $a % $b; $a = $b; $b = $r }; return $a }

Write-Output (solve 0 0)
Write-Output (solve 0 7)
Write-Output (solve 7 0)
Write-Output (solve 48 18)
Write-Output (solve 17 13)
Write-Output (solve 270 192)
