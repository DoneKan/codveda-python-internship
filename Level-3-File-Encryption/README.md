
# File Encryption/Decryption Tool

## 📋 Project Description
A Python-based file encryption and decryption tool that uses the Fernet symmetric encryption algorithm. Provides both command-line and GUI interfaces for securing sensitive text files.

## ✨ Features
- ✅ Secure file encryption using Fernet (symmetric encryption)
- ✅ File decryption with key validation
- ✅ Automatic encryption key generation
- ✅ Key file management (save/load keys)
- ✅ Support for text files (.txt, .md, .py, etc.)
- ✅ Beautiful GUI interface
- ✅ Error handling for invalid keys and corrupted files
- ✅ User-friendly interface for both CLI and GUI

## 🛠️ Technologies Used
- Python 3.x
- `cryptography` library (Fernet encryption)
- `tkinter` for GUI

## 🔐 Security Features
- **Fernet Encryption**: Uses symmetric encryption with 128-bit AES in CBC mode
- **Key Generation**: Cryptographically secure random key generation
- **File Integrity**: Built-in authentication to detect tampering

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/codveda-python-internship.git
cd codveda-python-internship/Level-3-File-Encryption
```

2. Install required dependencies:
```bash
python -m pip install cryptography
```

## 🚀 Usage

### Command-Line Version:
```bash
python encryption_cli.py
```

**Features:**
- Generate new encryption key
- Encrypt text files
- Decrypt encrypted files
- Save/load encryption keys

### GUI Version:
```bash
python encryption_gui.py
```

**Features:**
- Drag-and-drop interface (browse files)
- Visual key management
- One-click encryption/decryption
- Status updates and error messages

## 📸 Screenshots
![Encryption Tool Screenshot](screenshot.png)
*File Encryption GUI Interface*

## 🎯 How It Works

1. **Key Generation**: A unique encryption key is generated using Fernet
2. **Encryption**: The file content is encrypted using the key
3. **Decryption**: The encrypted file can only be decrypted with the correct key
4. **Key Storage**: Keys are saved as `.key` files for future use

## ⚠️ Important Security Notes
- **Keep your encryption keys safe!** Without the key, encrypted files cannot be recovered
- Store keys separately from encrypted files
- Never share your encryption keys
- Make backups of important keys

## 📝 Supported File Types
- Text files (.txt)
- Markdown files (.md)
- Python files (.py)
- Configuration files (.conf, .ini)
- Any text-based files

## 🎯 Learning Outcomes
- Understanding encryption and decryption concepts
- Working with the cryptography library
- File I/O operations in Python
- Key management and security best practices
- Error handling for cryptographic operations
- Building secure applications

## 👨‍💻 Author
Duncan Kimuli Kigozi
- Internship: Codveda Technology
- LinkedIn: https://www.linkedin.com/in/duncan-kigozi-101923215/
- GitHub: https://github.com/DoneKan

## 📝 License
This project is part of the Codveda Technology Python Development Internship.

---

**#CodvedaJourney #CodvedaExperience #PythonDevelopment #Cybersecurity #Encryption**
