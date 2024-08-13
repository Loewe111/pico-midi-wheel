$currDir = Get-Location
$targetDir = "D:"
 
Write-Host "Uploading files from $currDir to $targetDir"
Remove-Item $targetDir\* -Recurse -Force
Copy-Item $currDir\* $targetDir\ -Recurse -Force