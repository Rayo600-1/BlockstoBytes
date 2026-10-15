# BlockstoBytes
This Tool makes blocks of nintendo to bytes 

## Building from Source

### Requirements

### Operating System Compatibility

| Operating System | Python Version | Notes |
|---|---|---|
| Windows 11 / 10 | Python 3.10+ | Recommended for current builds |
| Windows 8.1 | Python 3.12 or older | Requires compatible dependency versions |
| Windows 7 | Python 3.8 | Requires older compatible dependency versions |

**Important:**
- The latest versions of Python and build tools may not support older Windows versions.
- For Windows 7 and Windows 8.1, use compatible versions of Pillow, Nuitka or PyInstaller.
- Successful compilation does not automatically guarantee that the generated executable will run on every Windows version.
- Windows 7 and Windows 8.1 are no longer supported by Microsoft.

#You need to compile or use the py
- Python 3.10 or newer
- Tkinter with Tcl/Tk support
- Pillow
- Nuitka or PyInstaller

### 1. Clone the repository

```bash
git clone https://github.com/Rayo600-1/BlockstoBytes.git
cd BlockstoBytes
```

### 2. Install dependencies

```powershell
py -m pip install -r requirements.txt
```

### 3. Compile with Nuitka

```powershell
py -m nuitka --standalone --onefile --windows-console-mode=disable --enable-plugin=tk-inter --include-package=PIL --output-filename=block2byte.exe blocktobyte.py
```

### Alternative: Compile with PyInstaller

```powershell
py -m PyInstaller --onefile --windowed --name block2byte blocktobyte.py
```

### Output

- **Nuitka:** The executable will be generated as `block2byte.exe`.
- **PyInstaller:** The executable will be generated at `dist/block2byte.exe`.

### Notes

- Tkinter must be available in your Python installation.
- Nuitka requires a supported C compiler.
- PyInstaller normally does not require a separate C compiler.
- An Internet connection is required to download the GitHub profile image in the About / Credits window.
