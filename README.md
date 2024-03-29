
# リポジトリ名

**PopulationTrends**は、人口推移という意味で命名しました。
  
# ファイル構成

- readcsvfile.py        メインプログラムファイル
- csvlib.py             定数や関数の定義ファイル
- zinnkousuu.csv        人口数のCSVファイル
- setaisuu.csv          世帯数のCSVファイル
- tennnyuusyasuu.csv    転入者数のCSVファイル
- tennsyutusyasuu.csv   転出者数のCSVファイル
- syussyousyasuu.csv    出生者数のCSVファイル
- sibousyasuu.csv       死亡者数のCSVファイル
- fukuoka_city.csv      福岡市の区ごとに集計したCSVファイル(出力ファイル)  

  ※人口数と世帯数のみ2010年～2023年で、その他は2010年～2022年です。
  
# CSVファイル

### 自治体オープンデータ CKAN
https://ckan.open-governmentdata.org/dataset?organization=fukuoka-city&res_format=CSV&page=3

CSVファイルは、上記のサイトからダウンロードしました。
