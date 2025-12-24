# PDF to Text EXE
## Simple PDF to Text app for Windows and macOS

### How it works
When you run the program, it opens a native file picker. Select a PDF and the app
extracts the text and writes a `.txt` file alongside the PDF.

### Build on macOS
```
# Install packages
python -m pip install -r requirements.txt

# Build the macOS executable
python build.py
```

### Build on Windows
```
# Install packages
py -m pip install -r requirements.txt

# Build the Windows executable
py build.py
```

Build output lands in `dist/mine_pdf/` (the app is `mine_pdf` on macOS and
`mine_pdf.exe` on Windows).
