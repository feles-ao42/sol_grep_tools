import os
from bs4 import BeautifulSoup

# HTML ファイルが格納されているディレクトリのパス
directory = "./html/"

# ディレクトリ内のすべてのファイルに対して処理を行う
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        # HTML ファイルのパス
        filepath = os.path.join(directory, filename)

        # HTML ファイルを開く
        with open(filepath, "r", encoding="utf-8") as file:
            html = file.read()

        # BeautifulSoup を使用して HTML を解析
        soup = BeautifulSoup(html, "html.parser")

        # タイトルを取得
        title = soup.title.string

        # 本文を取得
        body = ""
        for paragraph in soup.find_all("p"):
            body += paragraph.text + "\n"

        # 結果を表示
        # print("ファイル:", filename)
        # print("タイトル:", title)
        print("本文:\n", body)
        print("---")
