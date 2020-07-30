# CSVファイルの読み書き
# csvモジュール（標準ライブラリ）
# PandasによるCSVファイル操作

# CSVファイルの読み込み
import csv

def main():

    with open('Some.csv', 'r') as f:
        reader = csv.reader(f)
        # header = next(reader)

        for row in reader:
            print(row)

    return

if __name__ == '__main__':
    main()




# CSVの書き込み
import csv

def main():

    with open('SomeA.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['Name', 'English', 'Math', 'History'])
        writer.writerow(['John', '87', '47', '98'])
        writer.writerow(['Mike', '67', '77', '95'])
        writer.writerow(['Paul', '76', '92', '37'])

    return

if __name__ == '__main__':
    main()





# PandasによるCSV読み込み
# pip install pandas

import pandas as pd

def main():

    df = pd.read_csv('Some.csv')

    print(df)
    print(df['Name'])
    print(df['English'])
    print(df.iloc[1])

    return

if __name__ == '__main__':
    main()




# PandasによるCSV書き込み
import pandas as pd

def main():

    df = pd.read_csv('Some.csv')
    df.to_csv('SomeB.csv')

    return

if __name__ == '__main__':
    main()
