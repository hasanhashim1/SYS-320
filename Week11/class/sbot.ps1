# Send an email using powershell

$toSend = @('dunston@champlain.edu', 'ston@champlain.edu','duns@champlain.edu')

# Message body
$msg = "Hello"

while ($true) { 
    
    foreach($email in $toSend) {

        # Send the email
        write-host "Send-MailMessage -from 'dunston@champlain.edu' -To $email -Subject 'Tisk Tisk' `
        -Body $msg -SmtpServer X.X.X.X"

        # Pause for 1 second
        #start-sleep 1
    }
}