import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# 定数
POINT_IN_TIME = "時点"
COLUMN_NAME = "種別"
CSV_FILE = "fukuoka_city.csv"

# 集計する単位となる福岡市の区
district_fukuoka_city = ["中央","博多","東","南","城南","早良","西"]

# 折れ線グラフのマーカー
plot_marker = ["o", "s", "^", "v", "d", "d"]

# CSVファイル情報（CSVファイル名,データ種別）
data_list = [
            {"file_name": "zinnkousuu.csv", "data_type": "人口数"},
            {"file_name": "setaisuu.csv", "data_type": "世帯数"},
            {"file_name": "tennnyuusyasuu.csv", "data_type": "転入者数"},
            {"file_name": "tennsyutusyasuu.csv", "data_type": "転出者数"},
            {"file_name": "syussyousyasuu.csv", "data_type": "出生者数"},
            {"file_name": "sibousyasuu.csv", "data_type": "死亡者数"},
]

#
# データ種別を指定回数分のリストを取得
# 引数1 : データ種別名
# 引数2 : リストの要素数
# 戻り値 : 指定した要素数のデータ種別名のリストを返す
#
def rowData(value_name, count):
    list = []
    for i in range(count):
        list.append(value_name)
    return list

#
# CSVファイル読み込み
# 引数1 : 読み込むCSVファイル名
# 引数2 : データ種別名
# 戻り値 : 読み込んだCSVファイル内容のデータフレーム
#
def readCsv(file_name, value_name):

    # CSVファイルの読み込み（この時点ではデータフレームにデータ種別がない）
    df = pd.read_csv(file_name, encoding="shift_jis")

    # データフレームに追加するため、データ種別のリストを取得
    list = rowData(value_name, len(df))

    # データフレームに、データ種別の列を追加
    df.insert(1, COLUMN_NAME, list)

    # CSVファイルの内容をデータフレームで返す
    return df

#
# グラフを描画する
# 引数1 : グラフの元となるデータフレーム
# 引数2 : グラフ上のマーカー
# 引数3 : グラフ上のタイトル
# 引数4 : グラフ上のX軸ラベル
# 引数5 : グラフ上のY軸ラベル
# 戻り値なし
#
def plot(data, marker, title, xlabel, ylabel):

    # グラフ画面のタイトルとサイズを設定
    plt.figure(title, figsize=(13, 6))

    # X軸とY軸のデータをプロット
    plt.plot(data[POINT_IN_TIME], data.iloc[:, [2, 3, 4, 5, 6, 7, 8]], marker=marker)

    # ラベルを設定
    for i, col in enumerate(data.columns[2:]):
        plt.text(data[POINT_IN_TIME].max(), data.iloc[:, i+2].iloc[-1], district_fukuoka_city[i])

    # グラフ上のタイトル
    plt.title(title)

    # X軸のラベル
    plt.xlabel(xlabel)

    # Y軸のラベル
    plt.ylabel(ylabel)

    # グラフを表示
    plt.show()
