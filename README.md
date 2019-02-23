# OSX_IME_Parser

Parser for JapaneseInputMethod database on Mac OSX

## Description

`OSX_IME_Parser` is a CLI tool to extracts JapaneseInputMethod database such bellow in `/Users/USERNAME/Library/Dictionaries/JapaneseInputMethod/` directory.
- DynamicBigramPhraseLexicon_ja_JP.db
- DynamicPhraseLexicon_ja_JP.db
- LexicalLearning_ja_JP.db
- NonLexicalLearning_ja_JP.db

Please refer this [blog](https://blog.hatena.ne.jp/kasasagi_f/padawan-4n6.hatenablog.com/edit?entry=17680117126971800903) about these database.

## Requirement
- python3 
 
## Usage for MacOS
1. Go to the path where JapaneseInputMethod database exists.

   `$ cd ~/Library/Dictionaries/JapaneseInputMethod/`
 
2. Parse the database and output to csv file: 

    `$ python osx_ime_parser.py -f DynamicBigramPhraseLexicon_ja_JP.db`

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