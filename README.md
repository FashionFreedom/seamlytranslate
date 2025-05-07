# Seamly2D Translation Tool

A Python script for translating Seamly2D interface text using Google Translate API.

## Features

- Translates .ts (Qt translation) files for the Seamly2D application
- Uses Google Translate API for accurate translations
- Preserves existing translations
- Supports all languages available through Google Translate
- Simple GUI file selection interface
- Command-line interface for automation

## Requirements

- Python 3.x
- Required packages (install using `pip install -r requirements.txt`):
  - googletrans==3.1.0a0
  - lxml>=4.9.0

## Usage

### Windows
1. Double-click `seamly2d_translate.bat`
2. Or run from command line: `seamly2d_translate.bat [ts_file] [--lang language_code]`

### Command Line
```bash
python seamly2d_translate.py [ts_file] [--lang language_code]
```

### Examples
- Run with file dialog: `seamly2d_translate.bat`
- Translate specific file: `seamly2d_translate.bat ../share/translations/seamly2d_cs_CZ.ts`
- Specify language: `seamly2d_translate.bat --lang fr`

## Notes

- The script only processes source text strings that have empty translation text
- It does not overwrite existing translations
- It removes the 'type="unfinished"' attribute when translation text is present
- Make a backup copy of your .ts files before running the script
- Update the `translations_dir` constant in the script as needed

## License

MIT License - See LICENSE file for details

## Author

slspencer 