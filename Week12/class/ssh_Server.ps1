cls
#Login to a rmote SSH Server 
#New-SSHSession -ComputerName '192.168.74.130' -Credential (Get-Credential kali)


<#
while ($true) {

#Add a prompt to run commands
$the_cmd = Read-Host -Prompt "Please enter a commadn: "


#Run Commadn on remote ssh server
(Invoke-SSHCommand -index 0 $the_cmd).output

}
#>

Get-SCPItem -ComputerName '192.168.74.130' -Credential (Get-Credential kali)
-Destination '/home/kali' -Path 'log.png'


