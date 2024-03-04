import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

# 1. 准备数据集
data = pd.read_csv(".\\data\\IDS2017\\CSVs\\IDS2017.csv")

# 2. 数据预处理
# 进行数据清洗、特征选择、标签编码等操作
# ...

# 3. 特征缩放
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data.drop('label', axis=1))

# 4. PCA特征提取
pca = PCA(n_components=10)  # 假设选择10个主成分
pca_data = pca.fit_transform(scaled_data)

# 5. 设置滑动窗口
window_size = 100
X = []
y = []
for i in range(len(pca_data) - window_size):
    X.append(pca_data[i:i+window_size])
    y.append(data['label'][i+window_size])

X = np.array(X)
y = np.array(y)

# 6. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. 建立模型
model = RandomForestClassifier()

# 8. 模型训练
model.fit(X_train, y_train)

# 9. 模型评估
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 10. 调整和优化
# 可以尝试不同的模型、调整滑动窗口大小、调整PCA的主成分数量等来优化模型性能

# 11. 部署模型
# 将训练好的模型部署到实际环境中进行网络入侵检测
