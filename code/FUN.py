import pandas as pd
import os


def progress_table():
    # 取得目前工作目錄
    current_dir = os.getcwd()

    # Excel 檔案路徑
    file_path = os.path.join(current_dir, 'code/data', '影指中心開發清單大表.xlsx')
    df = pd.read_excel(file_path, sheet_name=0)

    # 回傳 df
    return df
