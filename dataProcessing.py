import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

# 加载数据
raw_data_filename = ".\\data\\IDS2017\\merged\\ML_merged_data.csv"
print("Loading raw data...")
raw_data = pd.read_csv(raw_data_filename, header=None, low_memory=False)

# 随机抽取比例，当数据集比较大的时候，可以采用这个，可选项
raw_data = raw_data.sample(frac=0.03)

# 查看标签数据情况
last_column_index = raw_data.shape[1] - 1
print("print data labels:")
print(raw_data[last_column_index].value_counts())

# 将非数值型的数据转换为数值型数据
# print("Transforming data...")
raw_data[last_column_index], attacks = pd.factorize(raw_data[last_column_index], sort=True)

# 对原始数据进行切片，分离出特征和标签，第1~78列是特征，第79列是标签
features = raw_data.iloc[:, :raw_data.shape[1] - 1]  # pandas中的iloc切片是完全基于位置的索引
labels = raw_data.iloc[:, raw_data.shape[1] - 1:]

# 特征数据标准化，这一步是可选项
features = preprocessing.scale(features)
features = pd.DataFrame(features)

# 将多维的标签转为一维的数组
labels = labels.values.ravel()

# 将数据分为训练集和测试集,并打印维数
df = pd.DataFrame(features)
X_train, X_test, y_train, y_test = train_test_split(df, labels, train_size=0.8, test_size=0.2, stratify=labels)

# print("X_train,y_train:", X_train.shape, y_train.shape)
# print("X_test,y_test:", X_test.shape, y_test.shape)
