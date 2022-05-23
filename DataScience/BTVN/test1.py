import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib inline
train = pd.read_csv('titanic.csv')
train.head()
sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
sns.histplot(train['Age'].dropna(), kde=False, color='darkred', bins=30)
figure = train['Fare'].hist(bins=50)
figure.set_title('Fare')
figure.set_xlabel('Fare')
figure.set_ylabel('No of passenger')
sns.set_style('whitegrid')
sns.countplot(x='Survived', data=train, palette='RdBu_r')
# Median
# train['Age'].fillna(train['Age'].median(),inplace=True)

# Mean
# train['Age'].fillna(train['Age'].mean(),inplace=True)

# Mode
# train['Age'].fillna(train['Age'].mode(),inplace=True)

#Random
# random_samples = train['Age'].dropna().sample(n=train['Age'].isnull().sum(),random_state=0)
# random_samples.index = train[train['Age'].isnull()].index
# train['Age_random']=train['Age']
# train.loc[train['Age'].isnull(), 'Age_random']=random_samples
# train['Age']= train['Age_random']

# End of dist
# train['Age'].fillna((train['Age'].mean()+3*train['Age'].std()),inplace=True)

# Fix value
train['Age'].fillna(35,inplace=True)


sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
train.drop(['Cabin', 'SibSp', 'Pclass', 'Parch','Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)
train.head()
train['Age'].describe()
upper_boundary = train['Age'].mean() + 3 * train['Age'].std()
lower_boundary = train['Age'].mean() - 3 * train['Age'].std()
print("Lower_boundary: {}".format(lower_boundary))
print("Upper_boundary: {}".format(upper_boundary)),
print("Mean: {}".format(train['Age'].mean()))
IQR = train['Fare'].quantile(0.75)-train['Fare'].quantile(0.25)
#### Extreme outliers
lower_bridge = train['Fare'].quantile(0.25)-(IQR*3)
upper_bridge = train['Fare'].quantile(0.75)+(IQR*3)

print("Lower_bridge: {}".format(lower_bridge))
print("Upper_bridge: {}".format(upper_bridge)),
data = train.copy()

data.loc[data['Age'] >= 73, 'Age'] = 73
data.loc[data['Fare'] >= 100, 'Fare'] = 100
figure = data.Age.hist(bins=50)
figure.set_title('Age')
figure.set_xlabel('Age')
figure.set_ylabel('No of passenger')
figure = data.Fare.hist(bins=50)
figure.set_title('Fare')
figure.set_xlabel('Fare')
figure.set_ylabel('No of passenger')
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler, RobustScaler
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
#scale input value
## StandardScaler
# scaler = StandardScaler()
# data = scaler.fit_transform(data)

# ## Min-Max Scaler
# min_max = MinMaxScaler()
# data = pd.DataFrame(min_max.fit_transform(data), columns=data.columns)

## Robust Scaler
# scaler = RobustScaler()
# data = pd.DataFrame(
#     scaler.fit_transform(data), columns=data.columns)
accuracy_scores = []
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(
        data[['Age', 'Fare']].fillna(0), data['Survived'], test_size=0.3, random_state=i)

    # Standard Scale
    # scaler = StandardScaler()
    # X_train = scaler.fit_transform(X_train)
    # X_test = scaler.transform(X_test)

    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    print("Accuracy_score{}: {}".format(i,accuracy_score(y_test, y_pred)))
    accuracy_scores.append(accuracy_score(y_test, y_pred))
print("mean: {}".format(np.mean(accuracy_scores)))
