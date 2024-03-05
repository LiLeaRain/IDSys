import pandas as pd
from tqdm import tqdm

# 读取CSV文件
# 源数据所在目录
mergedDataPath = '.\\data\\IDS2017\\merged'
# 源数据文件名
mergedDataFile = 'Labeled_merged_data.csv'
# 统计结果存储文件地址
statResultFile = f'{mergedDataPath}\\{mergedDataFile[:-4]}_label_distribution.txt'
# 读取源数据
df = pd.read_csv(f'{mergedDataPath}\\{mergedDataFile}', encoding='utf-8')

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

# 计算标签在总数中的比例
label_proportions = label_counts / len(last_column)

# 输出统计结果到控制台
print("Label Distribution:")
print(label_counts.to_string())
print("\nLabel Proportions:")
print(label_proportions.to_string())

# 输出统计结果到文件
with open(f'{statResultFile}', 'w', encoding='utf-8') as f:
    f.write("Label Distribution:\n")
    f.write(label_counts.to_string())
    f.write("\n\nLabel Proportions:\n")
    f.write(label_proportions.to_string())