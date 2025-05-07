#!/usr/bin/env python3
"""!
@file seamly2d_translate.py
@brief Script for translating Seamly2D interface text using Google Translate API
@details This script translates .ts (Qt translation) files for the Seamly2D application.
        Run this file from a cmd or bash terminal
        Alternatively, run the seamly2d_translate.bat file (Windows)
        It uses the synchronous googletrans library version 3.1.0a0 for translation. Later versions are asynchronous.
        It can be run from the command line with a .ts file and a language code
        If no language code is provided, the language code is extracted from the filename.
        If no file is provided, a file dialog is used to select the .ts file and the language code is extracted from the filename.
        It only processes the source text strings that have empty translation text, does not overwrite existing translations.
        It removes the type attribute 'type="unfinished"' if translation text is present
        It overwrites the original file with the translated file. Make a backup copy before running the script if needed
        Update the translations directory (translations_diras needed
        Example: python seamly2d_translate.py  
        Example: python seamly2d_translate.py ../share/translations/seamly2d_cs_CZ.ts 
@note Required package: pip install googletrans==3.1.0a0
@author slspencer
@date 2025-05-06
@license MIT
"""

# install libraries needed for this script with pip
#pip install -r requirements.txt

import os, sys
import argparse
import time
import traceback
from googletrans import Translator
from lxml import etree
from tkinter import Tk, filedialog

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
# open the file explorer in the translations directory
# update this as needed
translations_dir = "../seamly2d/share/translations"

# Math functions that should not be translated
math_functions = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'atan2',
                  'sinh', 'cosh', 'tanh', 'asinh', 'acosh', 'atanh',
                  'sinD', 'cosD', 'tanD', 'asinD', 'acosD', 'atanD', 'atan2D',
                  'sinhD', 'coshD', 'tanhD', 'asinhD', 'acoshD', 'atanhD',
                  '_deg', '_rad', '_cm', '_mm', '_in', '_ft', '_pt', '_px',
                  'sqrt', 'exp', 'pow', 'log', 'log2', 'log10', 'ln',
                  'abs', 'rint', 'mod', 'fmod', 'sign', 'floor', 'ceil', 'min', 'max',
                  'sum', 'avg', 'round', 'random',
                  'lor', 'land', 'lxor', 'lnot',
                  'pi', 'e']

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def get_lang_code_from_filename(ts_file):
    base = os.path.basename(ts_file)
    lang_code = base[-8:-6]
    print(f"Language code (from filename): {lang_code}")
    return lang_code


def select_ts_file():
    root = Tk()
    root.withdraw()
    ts_file = filedialog.askopenfilename(
        title="Select a .ts file for translation",
        filetypes=[("Qt Translation Files", "*.ts")],
        initialdir=translations_dir
    )
    root.destroy()
    return ts_file


def try_translate(translator, text, src, dest, max_attempts=5):
    delay = 1
    for attempt in range(1, max_attempts + 1):
        try:
            result = translator.translate(text, src=src, dest=dest)
            return result.text
        except Exception as e:
            print(f"[Attempt {attempt}] Translation failed: {e}")
            if attempt == max_attempts:
                raise
            time.sleep(delay)
            delay *= 2
    return None


def translate_ts_file(ts_file, lang_code):
    translator = Translator()
    tree = etree.parse(ts_file)
    root = tree.getroot()
    changed = False

    for message in root.findall('.//message'):
        source = message.find('source')
        src_text = source.text or ""
        translation = message.find('translation')
        tr_text = translation.text or ""
        comment = message.find('comment')
        com_text = comment.text if comment is not None else ""

        if not src_text:
            print(f"Empty source: line #{message.sourceline}")
        elif tr_text:
            if "type" in translation.attrib:
                del translation.attrib['type']
                changed = True
        else:
            print(f"\nSource: '{src_text}'\nTranslation: '{tr_text}'\nComment: '{com_text}'")
            if lang_code == 'en' or src_text in math_functions or com_text in ['Book Name', 'Author Name']:
                translation.text = src_text
                translation.attrib.pop('type', None)
                changed = True
                print("Copied source to translation.\n")
            else:
                try:
                    orig_text = src_text.split('/')[-1] if com_text == 'System Name' and '/' in src_text else src_text
                    translated = try_translate(translator, orig_text, src='en', dest=lang_code)
                    translation.text = translated
                    translation.attrib.pop('type', None)
                    changed = True
                    print(f"Translated: '{src_text}' → '{translated}'\n")
                except Exception as e:
                    print(f"ERROR on line {message.sourceline}: {e}")
                    print(traceback.format_exc())
                    sys.exit(1)

    if changed:
        tree.write(ts_file, encoding='utf-8')
        print(f"Updated: {ts_file}")
    else:
        print(f"No changes made to: {ts_file}")

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Translate a Qt .ts file using Google Translate"
    )
    parser.add_argument("file", nargs="?", help=".ts file to translate")
    parser.add_argument("--lang", help="Language code override (e.g. fr, de, es)")

    args = parser.parse_args()

    ts_file = args.file
    lang_code = args.lang

    if not ts_file:
        print("No file specified. Opening file dialog...")
        ts_file = select_ts_file()
        if not ts_file:
            print("No file selected.")
            sys.exit(0)

    if not lang_code:
        lang_code = get_lang_code_from_filename(ts_file)

    print(f"Selected file: {ts_file}")
    print(f"Target language: {lang_code}")
    translate_ts_file(ts_file, lang_code)

    # open the translated file in notepad on windows or gedit on linux or textedit on mac
    if sys.platform.startswith('win'):
        os.system(f'notepad {ts_file}')
    elif sys.platform.startswith('linux'):
        os.system(f'gedit {ts_file}')
    elif sys.platform.startswith('darwin'):
        os.system(f'textedit {ts_file}')
