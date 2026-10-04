Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Solve([long]$n) { [long]$r = 1; for ($i = 2; $i -le $n; $i++) { $r *= $i }; return $r }

Write-Output (solve 0)
Write-Output (solve 1)
Write-Output (solve 2)
Write-Output (solve 5)
Write-Output (solve 10)
Write-Output (solve 12)
