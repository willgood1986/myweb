powershell.exe -file StartService.ps1 -actionFlag 0
Write-Host "Press any key to continue ..."
$Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")