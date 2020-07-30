# glob
# よりスマートなファイル検索

import glob

ワイルドカードファイル検索
glob.glob('*.txt')

正規表現でのファイル検索
glob.glob('*[0-9].*')

再帰的にファイルを検索する
glob.glob('C/**/*.txt', recursive=True)
