# By Hasan Hashim
# List the files in a directory and
#Get-ChildItem -recurse -Path ./Documents
#Get-ChildItem -recurse -Include *.docx,*.pdf,*.txt -Path ./Documents
#Get-ChildItem -recurse -Include *.docx,*.pdf,*.txt -Path ./Documents | Select FullName

Get-ChildItem -recurse -Include *.docx,*.pdf,*.txt -Path ./Documents | Export-Csv -Path files.csv

# Import CSV file
$fileList = Import-Csv -Path ./files.csv -header FullName
## To see if fileList was created
#$fileList

# Loop through the results
foreach ($f in $fileList) {
    Get-ChildItem -Path $f.FullName

}

