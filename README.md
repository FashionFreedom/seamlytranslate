# Seamly2D Translation Tool
<a title="Seamly2D" href="https://private-user-images.githubusercontent.com/578399/441370466-d8cfe4ea-3c7e-4da0-83ab-14743ffbefb6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY2Mzk0MzIsIm5iZiI6MTc0NjYzOTEzMiwicGF0aCI6Ii81NzgzOTkvNDQxMzcwNDY2LWQ4Y2ZlNGVhLTNjN2UtNGRhMC04M2FiLTE0NzQzZmZiZWZiNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUwN1QxNzMyMTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03ZjFhMzY0YzE0NzQ5OTZmZTQ0OTY3ZGY0OWEwOGY1MjU1YWZiNWEyNzljMzNmOWY1M2Q4ZDA2ZDk1Njk1N2VlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.wqBv5vtlg9INxrW2p7ulTY-gLPJ3VTDUlA_ngeGoza0"><img width="64" alt="Seamly2D" src="https://private-user-images.githubusercontent.com/578399/441370466-d8cfe4ea-3c7e-4da0-83ab-14743ffbefb6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY2Mzk0MzIsIm5iZiI6MTc0NjYzOTEzMiwicGF0aCI6Ii81NzgzOTkvNDQxMzcwNDY2LWQ4Y2ZlNGVhLTNjN2UtNGRhMC04M2FiLTE0NzQzZmZiZWZiNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUwN1QxNzMyMTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03ZjFhMzY0YzE0NzQ5OTZmZTQ0OTY3ZGY0OWEwOGY1MjU1YWZiNWEyNzljMzNmOWY1M2Q4ZDA2ZDk1Njk1N2VlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.wqBv5vtlg9INxrW2p7ulTY-gLPJ3VTDUlA_ngeGoza0"></a><a title="Google Inc., Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Google_Translate_logo.svg"><img width="64" alt="Google Translation Services" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Google_Translate_logo.svg/512px-Google_Translate_logo.svg.png?20210606111727"></a>

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
*-* Run with file dialog (Windows):  
```
seamly2d_translate.bat
```
- Run with file dialog (Windows, Linux, MacOS):  
```
python seamly2d_translate.py
```
- Run on a specific file (Windows, Linux, MacOS):  
```
python seamly2d_translate.py ../share/translations/seamly2d_cs_CZ.ts
```
- Run with file dialog and convert to a specific language (Windows, Linux, MacOS):  
```
python seamly2d_translate.py --lang fr
```


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
