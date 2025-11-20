<div align="center">

# 🕵️‍♂️ MetaSpy

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

<p>
  <strong>Extract hidden EXIF metadata and GPS coordinates from images.</strong>
</p>

[Report Bug](https://github.com/your-username/metaspy/issues) · [Request Feature](https://github.com/your-username/metaspy/issues)

</div>

---

## 📖 Description

**MetaSpy** is a Python-based OSINT (Open Source Intelligence) tool designed to extract EXIF metadata from image files. 

Modern digital cameras and smartphones embed hidden data inside images, including device models, timestamps, and often **precise GPS coordinates**. MetaSpy reads this data and, if GPS info is available, generates a direct **Google Maps link** to the location where the photo was taken.

### ✨ Key Features

* **📍 GPS Extraction:** Converts raw GPS data into a clickable Google Maps link.
* **📷 Device Info:** Identifies the camera make, model, and software used.
* **🕒 Timestamp Analysis:** Reveals the exact date and time the photo was captured.
* **🐍 Python Powered:** Lightweight and easy to use via CLI.

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/metaspy.git](https://github.com/your-username/metaspy.git)
   cd metaspy
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

Run the tool by providing an image path using the `-i` flag.

**Basic Command:**
```bash
python3 metaspy.py -i photo.jpg
```

**Sample Output:**
```text
🔎 Analyzing: photo.jpg
----------------------------------------
📂 Make: Apple
📂 Model: iPhone 13
📂 DateTimeOriginal: 2023:10:25 14:30:00
----------------------------------------
🌍 GPS Data Found!
📍 Latitude : 41.0082
📍 Longitude: 28.9784

🗺️  Google Maps Link:
[https://www.google.com/maps?q=41.0082,28.9784](https://www.google.com/maps?q=41.0082,28.9784)
```

---

## ⚠️ Disclaimer

This tool is developed for **educational and operational security (OpSec) awareness purposes only**. Do not use this tool to violate anyone's privacy. The developer is not responsible for any misuse of this software.

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
