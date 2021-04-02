Prerequisites:
Recommended resolution for Android Emulator -- 540x1060
Android API 27, 28, 29

Guide for MacOS:
1. Check that you have Java
`java -version`
2. Check that you have ruby to use "brew"
`ruby -v`
4. Install "brew" (Installer for next steps)
`ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"`
`brew -v`
5. Install node
`brew install node`
6. Check that Node Package Manager was installed
`npm -v`
7. Install appium and check that it was successful (An open-source tool for automating)
`npm install -g appium`
`appium -v`
8. Install python and check version (Project was created for 3.7)
`brew install python`
Install pip (Package manager for python)
`sudo easy_install pip`
9. Install selenium
`pip install -U selenium`
10. Add ANDROID_HOME and JAVA_HOME to "~/.bash_profile"
Then save it and reload with command
`source .bash_profile`
11. Install appium-doctor
`npm install -g appium-doctor`
12. Check appium environment with this command
`appium-doctor`
13. Install BDD-python-based library
`pip install behave`
14. Install Appium-Python-Client
`pip install Appium-Python-Client`
15. Add apk-file `/apps/apk/midhub.apk`
16. Install Allure
`brew install allure`
17. Allure Behave Formatter
`pip install allure-behave`
18. Install Android Emulator 
https://developer.android.com/studio/run/emulator

Run locally (Emulators / Real Devices):
1. Open two terminals. Run appium server in one terminal
`appium --relaxed-security`
2. Go to the folder Midhub and run test in another terminal for local running
`behave -D --format plain`
To run on the local server (all examples further will be with local server)
`behave -D local_server_ip=192.168.0.110 --format plain`
Add tag to run particular test
`behave -D local_server_ip=192.168.0.110 --format plain --tags=tutorial`
To create report in Allure use this command
`behave -D local_server_ip=192.168.0.110 -f allure_behave.formatter:AllureFormatter -o ./reports/report/ ./features/`
3. To see result in Allure run this
`allure serve ./reports/report/`

DOCKER
====================================================================
Docker run (Only emulators):
0. For emulators with non-default port, please set port in .env file
1. To start docker:
1.1 run emulator
1.2 `docker network create mh-network`
1.3 `docker-compose up --build -d`
2. To run tests:
2.1 `docker exec -ti behave /bin/sh`
2.2 Inside shell run behave with necessary parameters. Default is:
`behave -D local_server_ip=192.168.0.110 -D app_uri=/root/tmp/sample_apk/midhub.apk -D appium_host=appium --format plain`
The alternative for allure reports:
`behave -D local_server_ip=192.168.0.110 -D app_uri=/root/tmp/sample_apk/midhub.apk -D appium_host=appium -f allure_behave.formatter:AllureFormatter -o ./reports/report/ ./features/`
3. To stop:
`docker-compose down`

If you want change Android API version, please stop previous set with `docker-compose down`

More information about how it works:
https://docs.google.com/document/d/1COvOE-adJxN4iZvnBhjmAqz4aiWOUHnrvQSAfNGmBi0/edit#heading=h.qi4i7oeh6o59

Doc templates for scenarios:
https://docs.google.com/spreadsheets/d/1Lyb_Jp14KL39bes7993IWrvwkw9GKoyXlUB7TjmIqOY/edit#gid=0

