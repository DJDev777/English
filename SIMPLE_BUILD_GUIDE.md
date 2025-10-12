# 🚀 Simple Guide: Build Your APK in 5 Steps

## What You Need

Your React Native project is ready at: `/app/LumosEnglish/`

## The 5 Steps

### 1️⃣ Download the Code
Download the `/app/LumosEnglish/` folder to your computer (or the .tar.gz file)

### 2️⃣ Install Required Software (One-time setup)

#### On Windows:
1. **Node.js**: Download from https://nodejs.org (click "Download LTS")
2. **Java JDK 17**: Download from https://adoptium.net/temurin/releases/ (choose JDK 17)
3. **Android Studio**: Download from https://developer.android.com/studio

#### On macOS:
1. **Node.js**: Download from https://nodejs.org
2. **Java JDK 17**: Download from https://adoptium.net/temurin/releases/
3. **Android Studio**: Download from https://developer.android.com/studio

#### On Linux:
```bash
sudo apt update
sudo apt install nodejs npm openjdk-17-jdk
# Then download Android Studio from https://developer.android.com/studio
```

### 3️⃣ Setup Android Studio (One-time)

1. Open Android Studio
2. Click "More Actions" → "SDK Manager"
3. In "SDK Platforms" tab:
   - Check ✅ "Android 14.0" or "Android 13.0"
4. In "SDK Tools" tab:
   - Check ✅ "Android SDK Build-Tools"
   - Check ✅ "Android SDK Platform-Tools"
5. Click "Apply" and wait for download to complete

### 4️⃣ Build Your APK

Open Terminal (or Command Prompt on Windows) and run:

```bash
# Go to your project folder
cd path/to/LumosEnglish

# Install dependencies (first time only)
npm install

# Build the APK
cd android
./gradlew assembleDebug
```

**On Windows, use:** `gradlew.bat assembleDebug` instead of `./gradlew`

**Wait:** This takes 5-15 minutes the first time (downloads build dependencies)

### 5️⃣ Find and Install Your APK

**APK Location:**
```
LumosEnglish/android/app/build/outputs/apk/debug/app-debug.apk
```

**Install on Phone:**
1. Copy `app-debug.apk` to your phone
2. Open the file on your phone
3. Allow "Install from Unknown Sources" when asked
4. Install and enjoy! 🎉

## 📱 Alternative: Test Without Building

If you have an Android device or emulator, you can test immediately:

```bash
cd LumosEnglish
npm install
npx react-native start
# In another terminal:
npx react-native run-android
```

This requires:
- Android device with USB debugging enabled, OR
- Android Studio emulator running

## ⏱️ Time Required

- **Installing software:** 20-30 minutes (one-time)
- **Building APK:** 5-15 minutes (first time), 1-3 minutes (subsequent builds)
- **Total:** ~30-45 minutes for first build

## 🆘 Common Issues

**Problem:** "SDK location not found"
**Solution:** Create file `android/local.properties` with:
```
sdk.dir=/path/to/Android/Sdk
```

**Problem:** Can't find Android SDK path?
- **Windows:** `C:\Users\YourName\AppData\Local\Android\Sdk`
- **macOS:** `/Users/YourName/Library/Android/sdk`
- **Linux:** `/home/YourName/Android/Sdk`

**Problem:** "gradlew: command not found"
**Solution:** Make it executable (macOS/Linux):
```bash
chmod +x gradlew
./gradlew assembleDebug
```

**Problem:** Java version error
**Solution:** Make sure Java 17 is installed:
```bash
java -version  # Should show version 17
```

## ✅ Success Checklist

Before building, verify:
```bash
node --version     # Should show v18 or higher
npm --version      # Should show 9 or higher
java -version      # Should show version 17
```

## 📞 Need Help?

- Check the full guide: `/app/BUILD_INSTRUCTIONS.md`
- React Native setup: https://reactnative.dev/docs/set-up-your-environment
- Android Studio help: https://developer.android.com/studio/intro

---

**That's it!** Your app will be ready to install on any Android device. 🚀
