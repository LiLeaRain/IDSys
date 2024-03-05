import pandas as pd
from tqdm import tqdm

# 读取CSV文件
mergedDataPath = '.\\data\\IDS2017\\merged'
mergedDataFile = 'Labeled_merged_data.csv'
statResultFile=f'{mergedDataPath}\\{mergedDataFile[:-4]}_label_distribution.txt'
df = pd.read_csv(f'{mergedDataPath}\\{mergedDataFile}')

# 获取最后一列数据
last_column = df.iloc[:, -1]

# 创建一个进度条
with tqdm(total=len(df), desc="Processing data") as pbar:
    # 统计数据分布并实时显示
    for i, value in enumerate(last_column):
        # 更新进度条
        pbar.update(1)

        # 暂停一小段时间，以便控制台输出刷新
        pbar.refresh()

# 关闭进度条
pbar.close()

# 统计标签分布
label_counts = last_column.value_counts()


# 输出统计结果到文件
with open(f'{statResultFile}', 'w') as f:
    f.write("Label Distribution:\n")
    f.write(label_counts.to_string())
