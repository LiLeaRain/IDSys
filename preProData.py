import os

import pandas as pd

mergedDataPath = '.\\data\\IDS2017\\merged'  # 替换为你的目录路径
dataFileExtension = '.csv'  # 指定后缀名


def get_files_with_extension(directory, extension):
    """
    获取指定目录下指定后缀名的所有文件的相对路径

    参数：
    - directory (str): 目录路径
    - extension (str): 指定的文件后缀名，如 '.txt', '.csv'

    返回值：
    - files (list): 包含指定后缀名文件相对路径的列表
    """
    # 获取目录下所有文件和子目录
    files = []
    for root, _, filenames in os.walk(directory):
        # 筛选出指定后缀名的文件并添加到列表中
        for filename in filenames:
            if filename.endswith(extension):
                # 使用相对路径
                relative_path = os.path.relpath(os.path.join(root, filename), directory)
                files.append(relative_path)
    return files


# 示例用法


def writeData(f):
    print("Loading raw data...")
    raw_data = pd.read_csv(f, header=None, low_memory=False)
    return raw_data


# 按行合并多个Dataframe数据
def mergeData():
    frame = []
    files = get_files_with_extension(mergedDataPath, dataFileExtension)
    for i in files:
        frame.append(writeData(i))

    # 合并数据
    result = pd.concat(frame)
    dirty_list = clearDirtyData(result)
    result = result.drop(dirty_list)
    return result


# 清除CIC-IDS数据集中的脏数据，第一行特征名称和含有Nan、Infiniti等数据的行数
def clearDirtyData(df):
    drop_list = df[(df[14] == "Nan") | (df[15] == "Infinity")].index.tolist()
    return drop_list


rawData = mergeData()
file = 'data/total.csv'
rawData.to_csv(file, index=False, header=False)
