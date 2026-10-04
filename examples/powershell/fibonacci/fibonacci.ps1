Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Solve([long]$n) { [long]$a = 0; [long]$b = 1; for ($i = 0; $i -lt $n; $i++) { $t = $a + $b; $a = $b; $b = $t }; return $a }

Write-Output (solve 0)
Write-Output (solve 1)
Write-Output (solve 2)
Write-Output (solve 3)
Write-Output (solve 10)
Write-Output (solve 20)
Write-Output (solve 30)
