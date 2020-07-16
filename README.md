# Android_App_Testing

## Prerequisite
1. Install JDK. 
    * Add JAVA_HOME
    * Add %JAVA_HOME%\bin to PATH
2. Install Appium http://appium.io/docs/en/about-appium/getting-started/?lang=en
3. Install Nodejs https://nodejs.org/en/download/
4. Install Android SDK by using Android Studio https://developer.android.com/studio.
    * Add ANDROID_HOME
    * Add %ANDROID_HOME%\platform-tools to PATH
    * Add %ANDROID_HOME%\tools to PATH

## Desired Capabilities
1. Execute "adb version" to check environment setting
2. Check device: adb devices
2. platformVersion: adb shell getprop ro.build.version.release
3. deviceName: adb devices -l
4. appActivity: adb shell dumpsys activity | findstr mResume
