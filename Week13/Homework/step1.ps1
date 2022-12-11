
# Delete the contents of step2.exe, create update.bat,  
$writeBatFile = @'
del "C:\Users\Hasan\Desktop\Champlain-classes\SYS-320\Week13\Homework\step2.exe"
'@ | out-file -FilePath "./update.bat"

./update.bat


