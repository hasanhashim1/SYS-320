# By Hasan Hashim

# Here I added the websites that containe threat intel
$urls = @("https://rules.emergingthreats.net/blockrules/emerging-botcc.rules", "https://rules.emergingthreats.net/blockrules/compromised-ips.txt")

# Here I'm trying to loop through the URLs to check fot rules list
foreach ($UR in $urls) {
    # Getting the file name readable
    $temp = $UR.Split("/")

    # The last element in the array plucked off is the filename
    $fname = $temp[-1]

    if (Test-Path $fname) {
        continue
    }
    else {
        # Here I'm downloading the rules list
        Invoke-WebRequest -Uri $UR -OutFile $fname
    }
}

# Here are the filenames inside an array
$input_paths = @(".\compromised-ips.txt", ".\emerging-botcc.rules")

# Getting the the IP addresses
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Adding the IP addresses in to a IP lists
#useful sources: https://stackoverflow.com/questions/69845450/selecting-string-within-foreach-object
# https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/foreach-object?view=powershell-7.3
Select-String -Path $input_paths -Pattern $regex_drop | `
ForEach-Object { $_.Matches } | `
ForEach-Object { $_.Value } | Sort-Object | Get-Unique | `
Out-File -FilePath "ips-bad.tmp"

Write-Host "This program made by Hasan Hashim" -ForegroundColor Green
# Asking the user input to choose ether Windows or IPTables
#$rule_type = Read-Host -Prompt "Please enter Windows or IPTables: " -ForegroundColor Green
$rule_type = $(Write-Host "Please enter Windows or IPTables: "  -ForegroundColor yellow -NoNewLine; Read-Host).trim()


# Here we are using switch to take the user inputes and do the following
switch ( $rule_type.ToLower() ) {
    # If the user picked the iptables than it will get the content from the bad ips that we have and save in to a new file called rules
    # and then it will connect into the kali box to send the rules.out file
    "iptables" {
        (Get-Content -Path ".\ips-bad.tmp") | ForEach-Object `
        { $_ -replace "^", "iptables -A INPUT -s " -replace "$", " -j DROP" } | `
            Out-File -FilePath "rules.out"
        # - Using Powershell, SCP the IPTables rules over to 192.168.6.71 Port 2222.
        Set-SCPItem -ComputerName "192.168.229.131" -Port 22 -Credential (Get-Credential kali) `
            -Path "./Rules.out" -Destination "/home/kali/sys320"
    }
    "windows" {
        (Get-Content -Path ".\ips-bad.tmp") | ForEach-Object `
        { $_ -replace "^", "netsh advfirewall firewall add rule dir=in action=block name='Block bad ips' remoteip=" } | `
            Out-File -FilePath "Rules.out"
    }
}