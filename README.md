# BlockstoBytes
This Tool makes blocks of nintendo to bytes 

## Building from Source

### Requirements

- Windows 10 or later
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
