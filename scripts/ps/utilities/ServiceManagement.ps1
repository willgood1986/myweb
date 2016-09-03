# define params
# 0 - start, 1 - stop
param([Int32]$actionFlag = 0)

$actionStart = 0
$actionStop = 1

function StartService(
[parameter(Mandatory = $true)]
[String]$serviceName
) 
{
    Write-Host Try to start service $serviceName ...
    try 
    {
        Start-Service $serviceName
        Write-Host Successful to start service $serviceName ...
    }
    catch [Exception]
    {
        $ErrorActionPreference = "Stop"
        Write-Error Exception occurred, message: $_.Exception.Message
    }
}

function StopService(
[parameter(Mandatory = $true)]
[String]$serviceName
) 
{
    Write-Host Try to stop service $serviceName  ...
    try 
    {
        Stop-Service $serviceName
        Write-Host Successful to stop service: $serviceName ...
    }
    catch [Exception]
    {
        $ErrorActionPreference = "Stop"
        Write-Eror Exception occurred, message: + $_.Exception.Message
    }
}

function StartServices(
[parameter(Mandatory = $true)]
[String[]] $services
)
{
    foreach ($service in $services)
    {
        StartService($service);
    }
}

function StopServices(
[parameter(Mandatory = $true)]
[String[]] $services
)
{
    foreach ($service in $services)
    {
        StopService($service);
    }
}
