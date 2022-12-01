# By Hasan Hashim
# Create commandline parameters to copy a file and place into an evidence directory
param(
    ## In terminal you will be prompted to enter an int
    [Parameter(Mandatory = $true)]
    [int]$reportNo,
    ## In terminal you will be prompted to enter a string
    [Parameter(Mandatory = $true)]
    [string]$filePath

)

# Create a directory with the report number
$reportDir = "rpt$reportNo"

# Creating a new director
mkdir $reportDir

# Copy the file into the new directory
Copy-Item $filePath $reportDir
