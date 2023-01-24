import pandas as pd


train_data = pd.read_csv('data/train.csv')
# test_data = pd.read_csv('data/test.csv')

# train_data = train_data.drop(['Cabin','Name','Ticket','PassengerId','Embarked'],axis=1)
# train_data = train_data[train_data['Age'].notna()]


# fare = train_data['Fare']
# train_data = train_data.drop('Fare',axis=1)

# train_data.loc[(train_data['Age']>0)  & (train_data['Age']<=15),'Age']=-1
# train_data.loc[(train_data['Age']>15) & (train_data['Age']<=30),'Age']=-2
# train_data.loc[(train_data['Age']>30) & (train_data['Age']<=45),'Age']=-3
# train_data.loc[(train_data['Age']>45) & (train_data['Age']<=60),'Age']=-4
# train_data.loc[(train_data['Age']>60) & (train_data['Age']<=100),'Age']=-5

# train_data.loc[train_data['Sex']=='male','Sex']=1
# train_data.loc[train_data['Sex']=='female','Sex']=0

print(train_data['Survived'])