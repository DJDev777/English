# 📥 How to Download and Build Your Android APK

## Quick Overview

Your React Native mobile app is **ready** in the `/app/LumosEnglish/` directory. Here's how to get it and build your APK.

## Option 1: Download from This Environment

If this system provides file download capability:

1. **Download the entire project folder:** `/app/LumosEnglish/`
2. Or download the compressed archive (if created): `/app/LumosEnglish-Source.tar.gz`

## Option 2: Connect via Git/GitHub

If this environment is connected to Git:

```bash
cd /app/LumosEnglish
git init
git add .
git commit -m "Initial React Native WebView app"
# Push to your repository
```

## Option 3: Copy Individual Files

If you need to recreate the project:

### Key Files to Copy:

#### 1. Main App Component
**File:** `/app/LumosEnglish/App.tsx`
- Contains the WebView implementation
- Handles navigation and loading states

#### 2. Android Configuration
**Files:**
- `/app/LumosEnglish/android/app/build.gradle` (package name config)
- `/app/LumosEnglish/android/app/src/main/res/values/strings.xml` (app name)
- `/app/LumosEnglish/android/app/src/main/java/com/lumos/english/MainActivity.kt`
- `/app/LumosEnglish/android/app/src/main/java/com/lumos/english/MainApplication.kt`

#### 3. Dependencies
**File:** `/app/LumosEnglish/package.json`
- Lists all required packages including react-native-webview

## 🛠️ Building the APK on Your Computer

Once you have the project files on your local machine:

### Step 1: Install Prerequisites

#### Windows:
1. **Node.js:** https://nodejs.org/en/download/
   - Download and install LTS version (20.x or higher)
   
2. **Java JDK 17:** https://adoptium.net/
   - Download "JDK 17 (LTS)"
   - Set JAVA_HOME environment variable

3. **Android Studio:** https://developer.android.com/studio
   - Download and install
   - Open Android Studio
   - Go to More Actions → SDK Manager
   - Install "Android SDK Platform 34"
   - Install "Android SDK Build-Tools 34.0.0"

#### macOS:
```bash
# Install Homebrew first (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js
brew install node

# Install JDK
brew install openjdk@17

# Download Android Studio
# https://developer.android.com/studio
```

#### Linux (Ubuntu/Debian):
```bash
# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install JDK
sudo apt-get install openjdk-17-jdk

# Download Android Studio
# https://developer.android.com/studio
```

### Step 2: Configure Android SDK

1. Open Android Studio
2. Click "More Actions" → "SDK Manager"
3. In "SDK Platforms" tab:
   - ✅ Check "Android 14.0 (UpsideDownCake)" (API Level 34)
4. In "SDK Tools" tab:
   - ✅ Check "Android SDK Build-Tools 34"
   - ✅ Check "Android SDK Platform-Tools"
   - ✅ Check "Android SDK Tools"
5. Click "Apply" and wait for installation

### Step 3: Set Environment Variables

#### Windows:
```
ANDROID_HOME = C:\Users\YourUsername\AppData\Local\Android\Sdk
JAVA_HOME = C:\Program Files\Eclipse Adoptium\jdk-17.x.x-hotspot
```
Add to Path:
```
%ANDROID_HOME%\platform-tools
%ANDROID_HOME%\tools
%JAVA_HOME%\bin
```

#### macOS/Linux:
Add to `~/.bashrc` or `~/.zshrc`:
```bash
export ANDROID_HOME=$HOME/Library/Android/sdk  # macOS
# export ANDROID_HOME=$HOME/Android/Sdk  # Linux
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/tools
export JAVA_HOME=/Library/Java/JavaVirtualMachines/temurin-17.jdk/Contents/Home
```

Then run: `source ~/.bashrc` (or `~/.zshrc`)

### Step 4: Build Your APK

```bash
# Navigate to your project
cd path/to/LumosEnglish

# Install dependencies
npm install

# Build the APK
cd android
./gradlew assembleDebug
# On Windows use: gradlew.bat assembleDebug
```

### Step 5: Find Your APK

The APK will be located at:
```
LumosEnglish/android/app/build/outputs/apk/debug/app-debug.apk
```

### Step 6: Install on Your Phone

**Method 1: Direct Transfer**
1. Copy `app-debug.apk` to your phone
2. Open the file on your phone
3. Allow installation from unknown sources when prompted
4. Install and enjoy!

**Method 2: Using ADB**
```bash
# Connect phone via USB with USB debugging enabled
adb install android/app/build/outputs/apk/debug/app-debug.apk
```

## ⚡ Quick Build Commands

### For Debug APK (testing):
```bash
cd LumosEnglish
npm install
cd android && ./gradlew assembleDebug
```

### For Release APK (production):
See `BUILD_INSTRUCTIONS.md` for signing and release build instructions.

## 🐛 Common Issues & Solutions

### Issue: "SDK location not found"
**Solution:** Create `android/local.properties`:
```
sdk.dir=C:\\Users\\YourName\\AppData\\Local\\Android\\Sdk  # Windows
# sdk.dir=/Users/YourName/Library/Android/sdk  # macOS
# sdk.dir=/home/YourName/Android/Sdk  # Linux
```

### Issue: "gradlew: command not found"
**Solution:** 
```bash
chmod +x gradlew  # Make it executable (macOS/Linux)
./gradlew assembleDebug  # Run with ./
```

### Issue: Build fails with Java version error
**Solution:** Make sure Java 17 is installed and JAVA_HOME is set correctly:
```bash
java -version  # Should show version 17.x.x
```

### Issue: "Unable to locate tools.jar"
**Solution:** You need JDK, not JRE. Install JDK 17 from https://adoptium.net/

## 📱 Testing Before Building

You can test the app without building APK:

```bash
# Start Metro bundler
npx react-native start

# In another terminal, run on connected device or emulator
npx react-native run-android
```

This requires:
- Android device with USB debugging enabled, OR
- Android emulator running in Android Studio

## 🎯 Build Times

- **First build:** 5-15 minutes (downloads dependencies)
- **Subsequent builds:** 1-3 minutes
- **Build size:** ~50-70 MB for debug APK

## ✅ Verification

To verify everything is set up correctly:

```bash
# Check Node.js
node --version  # Should show v18+ or v20+

# Check npm
npm --version

# Check Java
java -version  # Should show version 17

# Check Android SDK
echo $ANDROID_HOME  # Should show SDK path
```

## 📞 Need More Help?

- **React Native Environment Setup:** https://reactnative.dev/docs/set-up-your-environment
- **Android Studio Guide:** https://developer.android.com/studio/intro
- **Troubleshooting:** Check `BUILD_INSTRUCTIONS.md` in your project

---

## 🎊 Summary

1. **Download** the LumosEnglish folder from `/app/LumosEnglish/`
2. **Install** Node.js, JDK 17, and Android Studio on your computer
3. **Configure** Android SDK in Android Studio
4. **Build** using `./gradlew assembleDebug` in the android folder
5. **Install** the APK on your Android device
6. **Enjoy** your mobile app! 🚀

**Estimated Time:** 30-60 minutes (mostly installation and first build)  
**Difficulty:** Easy to Medium (follow step-by-step)  
**Result:** Professional Android APK ready to install!
