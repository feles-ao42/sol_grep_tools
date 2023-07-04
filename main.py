import os
from bs4 import BeautifulSoup

# HTML ファイルが格納されているディレクトリのパス
directory = "./html/"

# 出力ファイルのパス
output_file = "./output.txt"

# ディレクトリ内のすべてのファイルに対して処理を行う
with open(output_file, "w", encoding="utf-8") as file:
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            # HTML ファイルのパス
            filepath = os.path.join(directory, filename)

            # HTML ファイルを開く
            with open(filepath, "r", encoding="utf-8") as html_file:
                html = html_file.read()

            # BeautifulSoup を使用して HTML を解析
            soup = BeautifulSoup(html, "html.parser")

            # タイトルを取得
            title = soup.title.string

            # 本文を取得
            body = ""
            for paragraph in soup.find_all("p"):
                text = paragraph.text.strip()  # 空白文字を除去
                if text:  # 空でない場合のみ追加
                    body += text + "\n"

            # 結果をテキストファイルに出力
            if title:
                #file.write("ファイル: {}\n".format(filename))
                #file.write("タイトル: {}\n".format(title))
                if body:
                    file.write("本文:\n{}\n".format(body))
                file.write("---\n")
