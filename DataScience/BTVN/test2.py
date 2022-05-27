from prettytable import PrettyTable
import seaborn as sns
import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
df.head()
df.isnull().sum()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def use_logistic_reg(data, has_new_feature=False):
    """
    Hàm áp dụng Logistic Regression cho bài toán Titanic
    data : dataset
    has_new_feature : có tạo thêm đặc trưng mới hay không
    """
    acc = []
    for i in range(0, 10):
        # Nếu có tạo thêm đặc trưng thì sử dung thêm cột Age_NAN
        if has_new_feature:
            X_train, X_test, Y_train, Y_test = train_test_split(
                data[['Age', 'Fare', 'Age_NAN']].fillna(0), data['Survived'],
                test_size=0.3, random_state=i)
        else:
            X_train, X_test, Y_train, Y_test = train_test_split(
                data[['Age', 'Fare']].fillna(0), data['Survived'],
                test_size=0.3, random_state=i)
        # Tạo bộ phân loại và huấn luyện
        classifier = LogisticRegression()
        classifier.fit(X_train, Y_train)
        # Kết quả dự đoán
        Y_pred = classifier.predict(X_test)
        # Thêm vào mảng kết quả
        acc.append(accuracy_score(Y_test, Y_pred))
    # Lấy trung bình
    return np.mean(acc)
print(f"{round(use_logistic_reg(df) * 100, 1)} (%)")
def median_way(df):
    data1 = df.copy()
    median = data1['Age'].median()
    data1['Age'] = data1['Age'].fillna(median)
    return data1
def mean_way(df):
    data2 = df.copy()
    mean = data2['Age'].mean()
    data2['Age'] = data2['Age'].fillna(mean)
    return data2
def mode_way(df):
    data3 = df.copy()
    mode = data3['Age'].mode()[0]
    data3['Age'] = data3['Age'].fillna(mode)
    return data3
def random_way(df):
    data4 = df.copy()
    # Loại bỏ các giá trị trống của cột Age và lấy ra ngẫu nhiên K giá trị
    # K là số lượng phần tử trống đã bị loại bỏ
    random_samples = data4['Age'].dropna().sample(n=data4['Age'].isnull().sum(), random_state=0)
    # Gán chỉ số của K giá trị ngẫu nhiên đó thành chỉ số K phân tử trống cột Age
    random_samples.index = data4[data4['Age'].isnull()].index
    # Thay thế K phần tử trống cột Age thành K giá trị ngẫu nhiên đã chọn
    data4.loc[data4['Age'].isnull(), 'Age'] = random_samples
    return data4
def end_of_dist_way(df):
    data5 = df.copy()
    # Giá trị đuôi phân bố = mean + 3 * std
    extreme = data5["Age"].mean() + 3 * data5["Age"].std()
    data5["Age"] = data5["Age"].fillna(extreme)
    return data5
def arbitrary_way(df, ar_age):
    data6 = df.copy()
    data6["Age"] = data6["Age"].fillna(ar_age)
    return data6
def new_feature_way(df):
    data7 = df.copy()
    # Tạo cột Age_NAN
    data7['Age_NAN'] = np.where(data7['Age'].isnull(), 1, 0)
    # Thay thế dữ liệu trống cột Age thành giá trị median
    data7["Age"].fillna(data7["Age"].median(), inplace=True)
    return data7
# Age có dạng phân bố chuẩn
# Biên dưới : mean - 3 * std   ;   Biên trên : mean + 3 * std
upper_boundary = df['Age'].mean() + 3* df['Age'].std()
lower_boundary = df['Age'].mean() - 3* df['Age'].std()
print(lower_boundary, upper_boundary)

# Fare có dạng phân bố lệch
# Biên dưới : 1st Quantile - 3 * IQR   ;   Biên trên : 3rd Quantile + 3 * IQR
IQR = df["Fare"].quantile(0.75) - df["Fare"].quantile(0.25)
lower_bridge = df['Fare'].quantile(0.25) - (IQR*3)
upper_bridge = df['Fare'].quantile(0.75) + (IQR*3)
print(lower_bridge, upper_bridge)
df_not_outlier = df.copy()
df_not_outlier.loc[df_not_outlier['Age'] >= 73, 'Age'] = 73
df_not_outlier.loc[df_not_outlier['Fare'] >= 100, 'Fare'] = 100
# Có Outlier
data_median = median_way(df)
data_mean = mean_way(df)
data_mode = mode_way(df)
data_random = random_way(df)
data_endofdist = end_of_dist_way(df)
data_arbitrary = arbitrary_way(df, ar_age=27)
data_newfeature = new_feature_way(df)
# Không có Outlier
data_median_outlier = median_way(df_not_outlier)
data_mean_outlier = mean_way(df_not_outlier)
data_mode_outlier = mode_way(df_not_outlier)
data_random_outlier = random_way(df_not_outlier)
data_endofdist_outlier = end_of_dist_way(df_not_outlier)
data_arbitrary_outlier = arbitrary_way(df_not_outlier, ar_age=27)
data_newfeature_outlier = new_feature_way(df_not_outlier)
def acc(data):
    # Làm tròn
    return round(use_logistic_reg(data) * 100, 1)


table = PrettyTable(["TYPE","Median","Mean","Mode","Random",
                    "End of Dist","Arbitrary","New feature"])

table.add_row(["ORIGIN", acc(data_median), acc(data_mean), acc(data_mode), acc(data_random), 
                acc(data_endofdist), acc(data_arbitrary), acc(data_newfeature)])

table.add_row(["OUTLIER-PROCESS", acc(data_median_outlier), acc(data_mean_outlier),
                acc(data_mode_outlier), acc(data_random_outlier), acc(data_endofdist_outlier),
                acc(data_arbitrary_outlier), acc(data_newfeature_outlier)])

print(">> Đơn vị độ chính xác : %")
print(table)
from sklearn.preprocessing import StandardScaler

def zscore_norm(data):
    scaler = StandardScaler()
    df_zscore = data[['Age', 'Fare']].copy()
    df_zscore = pd.DataFrame(scaler.fit_transform(df_zscore), columns=df_zscore.columns)
    df_zscore['Survived'] = data['Survived']
    return df_zscore
from sklearn.preprocessing import MinMaxScaler

def minmax_norm(data):
    min_max = MinMaxScaler()
    df_minmax = data[['Age', 'Fare']].copy()
    df_minmax = pd.DataFrame(min_max.fit_transform(df_minmax), columns=df_minmax.columns)
    df_minmax['Survived'] = data['Survived']
    return df_minmax
from sklearn.preprocessing import RobustScaler

def robust_norm(data):
    scaler = RobustScaler()
    df_robust = data[['Age', 'Fare']].copy()
    df_robust = pd.DataFrame(scaler.fit_transform(df_robust), columns=df_robust.columns)
    df_robust['Survived'] = data['Survived']
    return df_robust
data_random_outlier_zscore = zscore_norm(data_random_outlier)
data_random_outlier_minmax = minmax_norm(data_random_outlier)
data_random_outlier_robust = robust_norm(data_random_outlier)
table = PrettyTable(["TYPE","Random"])
table.add_row(["z-score", acc(data_random_outlier_zscore)])
table.add_row(["min-max", acc(data_random_outlier_minmax)])
table.add_row(["robust", acc(data_random_outlier_robust)])

print(">> Đơn vị độ chính xác : %")
print(table)