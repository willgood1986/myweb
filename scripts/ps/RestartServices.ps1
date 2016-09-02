# Get current ps directory
$scriptPath = $PSScriptRoot
$utilityPath = $scriptPath + "\utilities\"
$serviceManagementScript = $utilityPath + "ServiceManagement.ps1"
# import ps
. $serviceManagementScript
StopUCDServices
StartUCDServices