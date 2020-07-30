# optparse：コマンドラインオプションをパースするモジュール

# -*- coding: utf-8 -*-
from argparse import ArgumentParser

def main():

    parser = ArgumentParser()

    parser.add_argument(
        '-n', '--number',
        type = int,          # 値の型
        dest = 'number',     # 変数名
        required = True,     # 必須項目
        help = '処理の回数'   # --help時の表示内容
    )

    args = parser.parse_args()

    for i in range(args.number):
        print(i)

    return

if __name__ == '__main__':
    main()









# optparse：コマンドラインオプションをパースするモジュール
# ※引数の型の指定

# -*- coding: utf-8 -*-
from argparse import ArgumentParser

def main():

    parser = ArgumentParser()

    parser.add_argument(
        '-n', '--number',
        type = int,          # 値の型
        dest = 'number',     # 変数名
        required = True,     # 必須項目
        help = '処理の回数'   # --help時の表示内容
    )

    parser.add_argument(
        '-s', '--string',
        type = str,          # 値の型
        dest = 'string',     # 変数名
        required = True,     # 必須項目
        help = '表示文字列'   # --help時の表示内容
    )

    args = parser.parse_args()

    for i in range(args.number):
        print(str(i)+":"+args.string)

    return

if __name__ == '__main__':
    main()








