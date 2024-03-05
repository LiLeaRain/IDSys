import pandas as pd
import numpy as np
import os
from tqdm import tqdm

# 指定包含多个CSV文件的文件夹路径
folder_path = '.\\data\\IDS2017\\TrafficLabelling_'
merged_path = 'merged_data.csv'


# 定义处理单个CSV文件的函数
def clean_csv(file_path):
    """
    参数：
    - file_path (str): CSV文件的路径

    返回值：
    - df (DataFrame): 清洗后的DataFrame对象
    """
    try:
        df = pd.read_csv(file_path)
    except UnicodeDecodeError:
        print(f"Skipping file due to encoding error: {file_path}")
        return None

    # 去除含有NaN和Inf的行
    df = df.dropna()
    df = df[~df.isin([np.nan, np.inf, -np.inf]).any(axis=1)]  # 指定轴为1，以确保逐行进行检查
    df.reset_index(drop=True, inplace=True)  # 重置索引

    return df


# 定义合并多个CSV文件的函数
def merge_csv_files(folder_path):
    """
    参数：
    - folder_path (str): 包含多个CSV文件的文件夹路径

    返回值：
    - merged_df (DataFrame): 整合后的DataFrame对象
    """
    all_dfs = []
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    # 使用tqdm来显示进度条
    processed_files = tqdm(files, desc="Processing CSV files")
    for filename in processed_files:
        file_path = os.path.join(folder_path, filename)
        # 显示当前处理的文件名
        processed_files.set_postfix_str(filename)
        df = clean_csv(file_path)
        if df is not None:
            all_dfs.append(df)

    merged_df = pd.concat(all_dfs, ignore_index=True)
    return merged_df


# 合并多个CSV文件
merged_data = merge_csv_files(folder_path)

# 将整合后的数据保存到新的CSV文件中
merged_data.to_csv(f'{folder_path}\\{merged_path}', index=False)

# 显示处理结果
print("数据处理完成！合并后的数据已保存到 merged_data.csv 文件中。")
