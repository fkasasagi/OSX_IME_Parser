from __future__ import print_function
import sys
import argparse
import csv
import os
import sqlite3
import datetime


class ParseIMELexicon:

    # --------------------------------------------------------------------
    def __init__(self, sqlite_db_path):

        self.sqlite_db_path = sqlite_db_path

        # Get modification time of the database.
        mtime = datetime.datetime.fromtimestamp(os.stat(args.file).st_mtime)
        self.file_name = os.path.basename(args.file) + '_{0:%Y%m%d_%H%M%S}.csv'.format(mtime)
        self.list_data = []
        self.list_column_names = []

    # Check arguments to see if dbfile exists
    def check_dbfile_present(self):

        print('[+] Attempting connection to {} database'.format(self.sqlite_db_path))
        if not os.path.exists(self.sqlite_db_path) or not os.path.isfile(self.sqlite_db_path):
            print('[-] Database does not exit or is not a file')
            sys.exit(1)

    def parse_IME_Lexicon(self):

        # Connect to SQLite DB
        connect = sqlite3.connect(self.sqlite_db_path)
        c = connect.cursor()

        # Query DB for Column Name and Date of IME Lexicon db
        c.execute('pragma table_info(Words)')
        tuple_columns = c.fetchall()
        self.list_column_names = [column[1] for column in tuple_columns]
        self.list_data.append(self.list_column_names)

        # Extract DB contents & Convert from HEX to Japanese
        c.execute('select * from Words')
        tuple_data = c.fetchall()
        for tuple_recode in tuple_data:
            list_recode = [
                val.decode('utf-16', 'replace') if tuple_columns[index][2] == 'BLOB' and val is not None
                else val
                for index, val in enumerate(list(tuple_recode))
            ]
            self.list_data.append(list_recode)

    def write_csv(self):
        print("[+] Writeing IME_Lexicon's Word to {}".format(self.file_name))
        with open(self.file_name, 'w', encoding="utf_8_sig") as file:
            writer = csv.writer(file, delimiter=",", lineterminator='\n')
            writer.writerows(self.list_data)


if __name__ == '__main__':

    # usage:
    #     python osx_ime_parser.py -f db_file
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('-f', '--file',
                             help="please input sqlite3 db file path",
                             type=str,
                             default=os.path.expanduser('~') + '/Library/Dictionaries/JapaneseInputMethod/DynamicBigramPhraseIME_Lexicon_ja_JP.db')
    args = args_parser.parse_args()

    print("[+] parse_IME_Lexicon DB for Mac OSX 14.x Ver.0.1")
    print("[+] You must mount image on your system before you run it.")
    parse_IME_Lexicon = ParseIMELexicon(args.file)
    parse_IME_Lexicon.check_dbfile_present()
    parse_IME_Lexicon.parse_IME_Lexicon()
    parse_IME_Lexicon.write_csv()
    print("[+] finish")