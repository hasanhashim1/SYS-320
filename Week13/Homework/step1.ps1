<#
# Creates random number between 1000-9876 to add to end of EnNob file
$getRand = Get-Random -Maximum 9876 -Minimum 1000

# Copies powershell.exe to my Week11\Homework directory
Copy-Item -Path "/Users/sarahfornaldes/Desktop/SYS-320-01/Week13/Homework/powershell.exe" `
-Destination "/Users/sarahfornaldes/Desktop/SYS-320-01/Week13/Homework/EnNoB-$getRand.exe"

# Renames copied file.
$newFileName = "/Users/sarahfornaldes/Desktop/SYS-320-01/Week13/Homework/EnNoB-$getRand.exe"

# Checks if copied file exists
if (Test-Path -Path $newFileName){
    write-host "The File is Found"
}
else{
    write-host "Error"
}
#>

## Delete the contents of step2test.ps1, create update.bat,  
$writeBatFile = @'
rm "C:\Users\Hasan\Desktop\Champlain-classes\SYS-320-01-main\Week13\Homework\step2test.ps1"
'@ | out-file -FilePath "./update.bat"

## Executes update.bat
sh "./update.bat"
## In terminal/commandline do: chmod +x update.bat

