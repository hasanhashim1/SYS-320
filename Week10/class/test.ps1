#By Hasan Hashim
# Get a list of running processes 
# Get-process

# Get a list of members
#Get-process | get-member

# Get a list of proceses: name, id, path 
#Get-process | Select-object ProcessName, id, Path

# Save the Output to CSV file
# Get-process | Select-object ProcessName, id, Path | Export-csv -Path `
# "C:\Users\Hasan\Desktop\Champlain-classes\SYS-320\SYS-320\Week10\class\test.csv"

$outputName = "C:\Users\Hasan\Desktop\Champlain-classes\SYS-320\SYS-320\Week10\class\Runningservices.csv"
#$outputName1 = "C:\Users\Hasan\Desktop\Champlain-classes\SYS-320\SYS-320\Week10\class\services.csvs"

# System Services and properties
#Get-service | get-member
# Get-service | select-object Status, Name, DisplayName, BinaryPathName, Path | Export-csv -Path `
# $outputName

#Get a list of running servies 
Get-service | Where-object {$_.Status -eq "Running "} | Select-Object Status,Name,DisplayName | Export-csv -Path $outputName
#Get-service | Where-object {$_.Status -eq "Running "}
# check if the file exists

if (Test-path $outputName ){
    write-host -backgroundcolor "Green" -ForegroundColor "white" "Services file was created!"
} else {
    write-host -backgroundcolor "red" -ForegroundColor "white" "Services file was not created!"
}