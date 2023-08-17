@echo off
setlocal

echo IMPORTANT! MAKE SURE THE PATH FILE ON THE LogFileCleaner.py PYTHON FILE IS SET TO YOUR VOICEMOD PROGRAMME DATA PATH!
echo This will clear all your log files in "C:\ProgramData\Voicemod" directory
echo This has been tested for only Windows 10. This function should work with more recent versions of Windows. Hopefully!
echo Would you like to proceed with the cleanup? (Y/N)
choice /c yn /n

if errorlevel 2 (
    echo Okay, if you have any concerns of this being malware. Have no fears! It's open-sourced and you can look at the code!
    pause
    exit
) else (
    echo Okay then. Let's proceed!
    echo One last thing! Would you like this script to repeat over and over again, until the programme has been closed? (Y/N)
    choice /c yn /n

    if errorlevel 2 (
        cls
        echo Cleaning log files...
        python LogFileCleaner.py

        echo Exiting script. Thank you for using!
        pause
        exit
    ) else (
        :loop
        cls
        echo Cleaning log files...
        python LogFileCleaner.py
        
        echo Looping again...
        echo Press Ctrl+C to stop the script.
        timeout /t 5 >nul
        goto loop
    )
)
endlocal
