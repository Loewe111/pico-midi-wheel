$currDir = Get-Location
$targetDir = "D:"
 
Write-Host "Uploading main.py from $currDir to $targetDir"
Remove-Item $targetDir\main.py -Force
Copy-Item $currDir\main.py $targetDir\ -Force