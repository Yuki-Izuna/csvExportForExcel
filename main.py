import pandas as pd
import shutil
import os
from glob import glob

# ファイルリスト取得
csv_filepaths = glob('source/*.csv')

for csv_filepath in csv_filepaths:

    # ファイルパスからファイル名だけ抜き取る
    filename = os.path.splitext(os.path.basename(csv_filepath))[0]
    graf_filepath = './source/' + filename + '.xlsx'

    # テンプレートファイルを別名でコピー
    shutil.copy('./source/graf_template.xlsx', graf_filepath)

    # CSVをグラフ用のExcelに展開する
    _df = pd.read_csv(csv_filepath)
    _df.to_excel(graf_filepath, sheet_name='Sheet1', index=False, header=False)