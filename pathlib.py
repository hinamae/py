# pathlib
# オブジェクト指向のファイル操作モジュール

# -*- coding: utf-8 -*-
from pathlib import Path

def main():

    # カレントディレクトリ取得
    print(Path.cwd())

    # ホームディレクトリ取得
    print(Path.home())

    # Pathオブジェクトの作成
    # p = Path(r"C:\Users\masato\Desktop")
    p = Path(Path.cwd())
    print("p:", p)

    print("p.parent :", p.parent)  # 親ディレクトリ
    print("p.name   :", p.name)    # ディレクトリ名

    # 親要素の配列
    for i in p.parents:
        print(i)

    print("p.exists:",  p.exists())  # パスの存在確認
    print("p.is_dir:",  p.is_dir())  # ディレクトリかどうか
    print("p.is_file:", p.is_file()) # ファイルかどうか

    # ディレクトリ作成
    some_dir = Path(r"C:\Users\masato\Desktop\Some")
    some_dir.mkdir(parents=True, exist_ok=True)

    # ディレクトリ削除
    some_dir.rmdir()

    # パターンマッチ検索
    some_dir = Path(r"C:\Users\masato\Desktop\C")
    print(list(some_dir.glob('*.txt')))
    print(list(some_dir.glob('**/*.txt')))

    # 絶対パス変換
    some_dir = Path(r"./")
    print(some_dir)
    print(some_dir.resolve())

    # ファイルオープン
    some_file = Path(r"A1.txt")
    with some_file.open() as f:
        print(f.readline())

    return

if __name__ == '__main__':
    main()
