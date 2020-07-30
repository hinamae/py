# os
# ファイル・ディレクトリ操作（標準ライブラリ）
import os

カレントディレクトリの取得
	os.getcwd()

ディレクトリ作成
	os.mkdir('./SomeDirectory')

ファイル・ディレクトリの存在確認
	os.path.exists("./SomeDirectory")

ディレクトリの削除
	os.rmdir("./SomeDirectory")
	※ディレクトリ内にファイルが存在しているとエラーとなる

ファイルの削除
	os.remove("./SomeFile.txt")

ファイル・ディレクトリ名の変更
	os.rename("./A.txt", "./B.txt")

ファイル名の取得
	path = r"C:\Users\masato\Desktop\SomeFile.txt"
	os.path.basename(path)

ディレクトリ名の取得
	os.path.dirname(path)

ファイルかどうか確認
	os.path.isfile(path)

ディレクトリかどうか確認
	os.path.isdir(path)

ディレクトリのファイルのリストを取得
	os.listdir(path)

ファイルの拡張子を取得
	os.path.splitext(path)

ディレクトリ名とファイル名を結合
	path      = r"C:\Users\masato\Desktop"
	file_name = r"SomeFile.txt"
	os.path.join(path, file_name)

