Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Solve([long]$n) { if ($n -lt 2) { return 0 }; for ($d = 2; $d * $d -le $n; $d++) { if ($n % $d -eq 0) { return 0 } }; return 1 }

Write-Output (solve 0)
Write-Output (solve 1)
Write-Output (solve 2)
Write-Output (solve 3)
Write-Output (solve 4)
Write-Output (solve 25)
Write-Output (solve 97)
Write-Output (solve 121)
Write-Output (solve 997)
