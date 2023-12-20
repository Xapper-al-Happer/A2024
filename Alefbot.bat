@echo off

::timeout /t 3
::call pic.py
:: takes and stores picture 

call noanswer.py
:: main function (reads and understands picture)

timeout /t 10

::call dimage.py 
:: deletes the image 

:: was gonna be multi function 


:: timeout /t 3
:: call pic.py

:: SET /p AlefBot="WA - MA - WEA? "
:: IF /i "%AlefBot%" == "WA" GOTO withanswer
:: IF /i "%AlefBot%" == "MA" GOTO multianswer
:: IF /i "%AlefBot%" == "WEA" GOTO noanswer

::noanswer
::call noanswer.py

::multianswer
::echo "multianswer!!!!"

::withanswer
::echo "WITH ANSWERRRR!!!!"