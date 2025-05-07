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
- Required packages 
  - googletrans==3.1.0a0
  - lxml>=4.9.0

## Installation

- Clone repo
- Install requirements. Run in cloned repo directory: `pip install -r requirements.txt`
- Linux: make the script executable: `chmod +x seamly2d_translate.py`


## Usage

### Command Line for Windows, Linux, MacOS
```
python seamly2d_translate.py [ts_file] [--lang language_code]
```

* If no filename is specified a popup file explorer appears to select a file
* If no language_code is specified it uses the filename to derive the language_code
* Run from command line. Windows also allows the option of double clicking on the **seamly2d_translate.bat** file. 


### Windows .bat file option
* Double-click `seamly2d_translate.bat`
* Or run from command line:  
```
seamly2d_translate.bat [ts_file] [--lang language_code]
```   

### Examples
- Run with file dialog (Windows): `seamly2d_translate.bat`
- Run with file dialog (Windows, Linux, MacOS): `python seamly2d_translate.py`
- Run on a specific file (Windows, Linux, MacOS): `python seamly2d_translate.py ../share/translations/seamly2d_cs_CZ.ts`
- Run with file dialog and convert to a specific language (Windows, Linux, MacOS): `python seamly2d_translate.py --lang fr`


## Notes

- The script only processes source text strings that have empty translation text
- It does not overwrite existing translations
- It removes the 'type="unfinished"' attribute when translation text is present
- It overwrites the original .ts file
- Update the `translations_dir` constant in the script as needed


## Future script ideas

- Copy an existing .ts file, delete translation strings, then run the seamly2d_translate.py file. Good for creating a new translation file.
- Update a text string in a dialog and all .ts files, then run the seamly2d_translate.py file on all .ts files. Good for fixing typos.

## License

MIT License - See LICENSE file for details
