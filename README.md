arm64-v8a libEarnToDie2.so → these offsets/OG/MOD patches ✅
armeabi-v7a libEarnToDie2.so → different patch set required ❌

Earn to Die 2 — ".so" Modding Tool

A lightweight Python script for modifying the "libEarnToDie2.so" library from Earn to Die 2 on Android using Pydroid 3.

The tool does not include, provide, or extract the game's ".so" file. You must obtain/export "libEarnToDie2.so" yourself from your own copy of the game.

---

✨ Features

- 📱 Designed for Android
- 🐍 Runs with Pydroid 3
- 🔧 Applies modifications to "libEarnToDie2.so"
- 📂 Simple Downloads-folder workflow
- 💾 Keeps the original ".so" untouched
- 📤 Creates a separate "libEarnToDie2_mod.so"
- ⚡ No PC required for the modification step
- 🛠️ Useful for personal Android modding and binary-patching experiments

---

⚠️ Important

This repository does not contain the original Earn to Die 2 game files.

You must provide your own:

libEarnToDie2.so

The ".so" file is not supplied, downloaded, or extracted by this tool.

Only use files from a copy of the game that you own or have permission to modify.

---

📋 Requirements

- Android device
- Pydroid 3
- Your own "libEarnToDie2.so"
- The required "libEarnToDie2.ini"
- The Python script from this repository

---

📥 Installation

1. Install Pydroid 3

Install Pydroid 3 on your Android device.

2. Obtain the library yourself

Export/extract your own "libEarnToDie2.so" from your permitted copy of Earn to Die 2.

The tool does not do this step for you.

3. Prepare the Downloads folder

Place the required files in your Android Downloads folder:

Downloads/
├── script.py
├── libEarnToDie2.so
└── libEarnToDie2.ini

Make sure the filenames are exactly correct.

---

🚀 Usage

1. Obtain your own "libEarnToDie2.so".
2. Put "libEarnToDie2.so" in your Downloads folder.
3. Put "libEarnToDie2.ini" in the same folder.
4. Put the Python script in the same folder.
5. Open the script with Pydroid 3.
6. Run the script.
7. The script will create:

libEarnToDie2_mod.so

The original "libEarnToDie2.so" remains unchanged.

Using the modified library

After the script finishes:

libEarnToDie2_mod.so

can be renamed to:

libEarnToDie2.so

You can then use the modified library in your own permitted APK/modding project.

Always keep a backup of your original library.

---

🔧 Troubleshooting

"FileNotFoundError"

Make sure all required files are in the same folder:

script.py
libEarnToDie2.so
libEarnToDie2.ini

Check the spelling and capitalization of each filename.

"PermissionError"

Give Pydroid 3 permission to access your files through Android's app permissions.

"libEarnToDie2.so" is missing

The tool does not provide or extract the library.

You must export/extract your own copy and place it in the Downloads folder.

No "libEarnToDie2_mod.so" appears

Check the Pydroid console for errors and make sure the script has completed successfully.

Modified library doesn't work

The patches may depend on the exact game/library version. Make sure you are using the version the modifications were designed for.

Also verify that the file was copied correctly and that you kept the original library as a backup.

---

🛡️ Disclaimer

This project is provided for educational, research, and personal modding purposes.

This repository does not distribute:

- The Earn to Die 2 APK
- "libEarnToDie2.so"
- Other copyrighted game assets
- Extracted game files

You are responsible for ensuring that you have the necessary rights and permissions to modify and use any files with this tool.

---

📜 Credits

Project: Earn to Die 2 ".so" Modding Tool

Platform: Android / Pydroid 3

Target: Earn to Die 2

Created for Android modding and binary-patching experimentation.

---

⭐ Contributing

Suggestions, bug reports, and improvements are welcome.

Feel free to open an Issue or submit a Pull Request.

---

📄 License

See ""LICENSE"" (LICENSE) for the license governing this project.
