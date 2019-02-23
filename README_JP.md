# OSX_IME_Parser

Mac OSXのJapaneseInputMethodデータベースのパーサです。

## 説明

`/Users/USERNAME/Library/Dictionaries/JapaneseInputMethod/`のディレクトリ配下にある、以下のデータベースの中身を展開し、CSVとして出力します。
- DynamicBigramPhraseLexicon_ja_JP.db
- DynamicPhraseLexicon_ja_JP.db
- LexicalLearning_ja_JP.db
- NonLexicalLearning_ja_JP.db

上記のデータベースの詳細は[ブログ](https://blog.hatena.ne.jp/kasasagi_f/padawan-4n6.hatenablog.com/edit?entry=17680117126971800903)を参照してください。

## 環境
- python3 
 
## 使い方(MacOX)
1. 作業用のディレクトリに移動します。

   `$ cd ~/work`
 
2. データベースを読み込み、csvに出力します(python osx_ime_parser.py -f targetfile)。

    `$ python osx_ime_parser.py -f DynamicBigramPhraseLexicon_ja_JP.db`

- 注意: 作成されるファイル名には日時が追記されています。この日時はデータベースの更新日時を示しています。

## インストール方法

```
$ git clone https://github.com/fkasasagi/OSX_IME_Parser.git
$ cd OSX_IME_Parser
```

## ライセンス
MITライセンス

## 作者
fkasasagi & niimosky
