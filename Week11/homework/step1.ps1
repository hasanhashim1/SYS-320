#  integer ranging between 1000 and 9876.
$ran = Get-random -Minimum 1000 -Maximum 9876

# Here is path of the powereshell.exe
$dir = "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe"
# Here where we are adding the copyed file the file into a new path and also we renamed it.
$des = "C:\Users\Hasan Hashim\OneDrive\Desktop\champlain\SYS-320\Week11\homework\EnNoB-$ran.exe"
# Here is the process of the copying 
Copy-Item $dir -Destination $des
# from line 11 to line 15 trying to check if the file were copyed or not
if (Test-Path -Path $des){
    Write-Output "File were Found!"
}else {
    Write-Output "File were not Found!"
}

