APPIUM_LOG="/var/log/appium.log"

echo "Connecting to: host.docker.internal:$EMULATOR_PORT"
adb connect host.docker.internal:$EMULATOR_PORT
echo "Success!"

appium --log $APPIUM_LOG  --relaxed-security