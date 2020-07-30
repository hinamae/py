# shutil
# 高水準のファイル操作

import shutil

ファイルのコピー
	shutil.copyfile("A1.txt", "A2.txt")

ディレクトリごとコピー
	shutil.copytree("C", "C2")

ファイルの移動
	shutil.move("A1.txt", "C2/A1.txt")

ディレクトリを（ファイルごと）削除
	shutil.rmtree("C2")

ディスクの利用状況取得
	shutil.disk_usage(path)