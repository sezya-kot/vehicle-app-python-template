param(
    [switch]$InPipeline,
    [switch]$UseDockerCompose
)

Function Enter-Group
{
    param(
        [Parameter(Position=0)]
        [string]$Name
    )
    if ($InPipeline) 
    {
        Write-Output ("::group::{0}" -f $Name)
    }
}

Function Exit-Group
{
    if ($InPipeline) 
    {
        Write-Output "::endgroup::"
    }
}

Function Start-VehicleAppWithDockerCompose
{
    Enter-Group "build vehicleApp"
    docker-compose up --build -d 
    Exit-Group
    
    Enter-Group "get vehicleApp logs"
    Start-Sleep 5
    docker-compose logs
    Exit-Group
    
    Enter-Group "stopping vehicleApp"
    docker-compose down
    Exit-Group
}

Function Start-VehicleAppWithDaprCli
{
    Write-Output ("Starting vehicleApp as job")
    $Job = Start-Job { dapr run --app-id nodeapp --app-port 3000 --dapr-http-port 3500 node receiver/app.js }
    Write-Output ("Started job {0} ({1})" -f $Job.Id, $Job.Command)
    
    Write-Output ("Sending new order")
    Start-Sleep 15
    dapr invoke --app-id nodeapp --method neworder --data-file receiver/sample.json   
    
    Write-Output ("Stopping vehicleApp")
    dapr stop --app-id nodeapp   
    
    Enter-Group "job output"
    Write-Output "Getting job output "
    Write-Output "## Job output start ########################################################################################################################"
    $Job | Wait-Job | Receive-Job
    Write-Output "## Job output end ##########################################################################################################################"
    Exit-Group
    
    Write-Output "## Removing job"
    Write-Output "List of jobs before remove"
    Get-Job
    Write-Output ("Removing job {0}" -f $Job.Id)
    $Job | Remove-Job
    Write-Output "List of jobs after remove"
    Get-Job
}

if ($UseDockerCompose) {
    Start-VehicleAppWithDockerCompose
} else {
    Start-VehicleAppWithDaprCli
}