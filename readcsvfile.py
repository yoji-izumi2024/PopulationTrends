from csvlib import *

# 福岡市データフレーム作成(CSVファイル作成のため)
fukuoka_df = pd.DataFrame()

# 福岡市の区ごとのデータフレームを格納用配列変数
fukuoka = []

# CSVファイルでループ
for data in data_list:

    # CSVファイルを読み込み、データフレームを取得
    df = readCsv(data['file_name'], data['data_type'])

    # 時点の文字列編集（2022年3月31日→2022年）
    df['時点'] = df['時点'].astype(str).str[:5]

    # 区ごとに集計するため、データフレーム作成
    new_df = pd.DataFrame(df[[POINT_IN_TIME, COLUMN_NAME]])

    # 福岡市の区でループ
    for district in district_fukuoka_city:
        # 区ごとに集計して、データフレームに追加(CSVには同じ区で細かく分かれている)
        new_df[district] = df[[col for col in df.columns if col.startswith(district)]].sum(axis=1)

    # 福岡市データフレームに追加
    fukuoka_df = pd.concat([fukuoka_df, new_df], ignore_index=True)

    # 配列変数に追加
    fukuoka.append(new_df)

# 福岡市の区ごとにグラフ表示
for i, data in enumerate(fukuoka):

    # グラフ描画
    plot(data, plot_marker[i], data_list[i]["data_type"], POINT_IN_TIME, data_list[i]["data_type"])

# 福岡市データフレームより、CSVファイル作成
fukuoka_df.to_csv(CSV_FILE)
