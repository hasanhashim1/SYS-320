#By Hasan Hashim
# Here I added the message from the assignment.
$m = "If you want your files restored, please contact me at dunston@champlain.edu. I look forward to doing business with you."
# Here is the destnation to the README.READ file 
$des = "C:\Users\Hasan Hashim\OneDrive\Desktop\champlain\SYS-320\Week11\homework\README.READ"



# adding the message inside the README.READ file
Add-Content $des $m

# Here trying to check if the file were copyed or not
if (Test-Path -Path $des) {
    Write-Output "it is found"
} else {
    Write-Output "error"
}