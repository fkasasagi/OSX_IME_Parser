# OSX_IME_Parser

Parser for JapaneseInputMethod database on Mac OSX

## Description

`OSX_IME_Parser` is a CLI tool to extracts JapaneseInputMethod database such bellow in `/Users/USERNAME/Library/Dictionaries/JapaneseInputMethod/` directory.
- DynamicBigramPhraseLexicon_ja_JP.db
- DynamicPhraseLexicon_ja_JP.db
- LexicalLearning_ja_JP.db
- NonLexicalLearning_ja_JP.db

Please refer this [blog](https://padawan-4n6.hatenablog.com/entry/2019/02/23/231749) about these database.

## Requirement
- python3 
 
## Usage for MacOS
1. Go to the path where you work.

   `$ cd ~/work`
 
2. Parse the database and output it as csv format in the current directory(python osx_ime_parser.py -f targetfile): 

    `$ python osx_ime_parser.py -f /Users/USERNAME/Library/Dictionaries/JapaneseInputMethod/DynamicBigramPhraseLexicon_ja_JP.db`

- Note: Timestamp in the output filename means modification time of the database file.

## Installation
```
$ git clone https://github.com/fkasasagi/OSX_IME_Parser.git
$ cd OSX_IME_Parser
```
## Licence
This software is released under the MIT License, see LICENSE.

## Authors
fkasasagi & niimosky
