# -*- coding: utf-8 -*-
"""기본.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pH_WjNQRaaLYQgD1vtAdBsH4vj5DFSLR
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.model_selection import train_test_split

base_src='./drive/MyDrive'
df=pd.read_excel(base_src+'/COVID-19-Constructed-Dataset.xlsx') #read csv file and store in df
print(df)

# Print dataset statistical data.
print("Statistical data: ")
print(df.describe())

# Print Columns names.
print("Columns names: ")
print(df.columns.values)

# Print Columns data types.
print("Columns data types: ")
print(df.dtypes)

#학생들의 성적을 코로나 전학기와 후학기로 나누고 학생 ID가 같으면 데이터를 합쳤습니다.
df["timeperiod"] = [1 if i >= 3 else 0 for i in df["timeperiod"]]
before_Covid_groupID = pd.DataFrame(columns=df.columns)
print(before_Covid_groupID)
for i in range(1,1401):
  condition = (df.timeperiod == 0) & (df.studentID==i)
  k=df.loc[condition]
  #print(pd.Series(k.sum(axis=0)/3))
  before_Covid_groupID=before_Covid_groupID.append(pd.Series(k.sum(axis=0)/3),ignore_index=True)
print("before_Covid_groupID______________________________________")
print(before_Covid_groupID)

after_Covid_groupID = pd.DataFrame(columns=df.columns)
print(after_Covid_groupID)
for i in range(1,1401):
  condition = (df.timeperiod == 1) & (df.studentID==i)
  k=df.loc[condition]
  #print(pd.Series(k.sum(axis=0)/3))
  after_Covid_groupID=after_Covid_groupID.append(pd.Series(k.sum(axis=0)/3),ignore_index=True)
print("after_Covid_groupID______________________________________")
print(after_Covid_groupID)

#평균과 합
before_Covid_groupID['total']=before_Covid_groupID['readingscore']+before_Covid_groupID['writingscore']+before_Covid_groupID['mathscore']+before_Covid_groupID['readingscoreSL']+before_Covid_groupID['writingscoreSL']+before_Covid_groupID['mathscoreSL']
#print(df['total'])
before_Covid_groupID['mean']=(before_Covid_groupID['total'])/6
print(before_Covid_groupID)

after_Covid_groupID['total']=after_Covid_groupID['readingscore']+after_Covid_groupID['writingscore']+after_Covid_groupID['mathscore']+after_Covid_groupID['readingscoreSL']+after_Covid_groupID['writingscoreSL']+after_Covid_groupID['mathscoreSL']
#print(df['total'])
after_Covid_groupID['mean']=(after_Covid_groupID['total'])/6
print(after_Covid_groupID)

# 두 가지 feature를 대상
before_data = before_Covid_groupID[['mean', 'total']]
after_data = after_Covid_groupID[['mean', 'total']]

# 정규화 진행
scaler = MinMaxScaler()
before_data_scale = scaler.fit_transform(before_data)
after_data_scale = scaler.fit_transform(after_data)

#Elbow를 통한 최적의 k를 구함
model = KMeans()
#visualizer = KElbowVisualizer(model, k=(1,10))
#visualizer.fit(data_scale)

k = 3

# 그룹 수, random_state 설정
model = KMeans(n_clusters = k, random_state = 10)

# 정규화된 데이터에 학습
model.fit(before_data_scale)

# 클러스터링 결과 각 데이터가 몇 번째 그룹에 속하는지 저장
before_Covid_groupID['cluster'] = model.fit_predict(before_data_scale)
after_Covid_groupID['cluster'] = model.fit_predict(after_data_scale)

print(before_Covid_groupID.shape)
plt.figure(figsize = (8, 8))

#산점도출력
for i in range(k):
    plt.scatter(before_Covid_groupID.loc[before_Covid_groupID['cluster'] == i, 'mean'], before_Covid_groupID.loc[before_Covid_groupID['cluster'] == i, 'total'], label = 'cluster ' + str(i))
  
plt.legend()
plt.title('K = %d results'%k , size = 15)
plt.xlabel('Mean', size = 12)
plt.ylabel('Total', size = 12)
plt.show()

#Covid 이전 아이디와 mean cluster분류
before_Covid_Only_mean = before_Covid_groupID[['studentID', 'mean','cluster']] #before_Covid_groupID에서 'studentID', 'mean' column만 추출 후 before_Covid_Only_mean 데이터 프레임 생성 
before_Covid_Only_mean.rename(columns={'mean':'before_Covid_mean'}, inplace=True) #before_Covid_Only_mean 데이터 프레임에서 'mean' column을 before_Covid_mean 이름 변경
print(before_Covid_Only_mean) #출력후 확인

#Covid 이후 아이디와 mean cluster분류
after_Covid_Only_total = after_Covid_groupID[['studentID', 'total','cluster']] #after_Covid_groupID에서 'studentID', 'mean' column만 추출 후 after_Covid_Only_mean 데이터 프레임 생성 
after_Covid_Only_total.rename(columns={'total':'after_Covid_total'}, inplace=True) #after_Covid_Only_mean 데이터 프레임에서 'mean' column을 after_Covid_mean으로 이름 변경
print(after_Covid_Only_total) #출력후 확인

#before_Covid_Only_mean, after_Covid_Only_mean 두 프레임 합치기
merge_df = pd.merge(before_Covid_Only_mean, after_Covid_Only_total,on="studentID")
print(merge_df)

processed_df = merge_df.copy() #합친 merge_df 데이터 프레임 바로 사용하지 않고 processed_df 생성후 copy해서 사용
#print(processed_df)

#cluster가 변한 숫자 확인
number_count=0
for i in range(0,1400):
  if merge_df.iloc[i,2]!=merge_df.iloc[i,-1]:
    number_count+=1
print(number_count)

#cluster_id 값에 따라 cluster_0_df, cluster_1_df, cluster_2_df 데이터 프레임 생성
cluster_0_df = processed_df[processed_df['cluster_x'] == 0]
cluster_1_df = processed_df[processed_df['cluster_x'] == 1]
cluster_2_df = processed_df[processed_df['cluster_x'] == 2]


#after cluster 값에 따라 cluster_0_df_y, cluster_1_df_y, cluster_2_df_y 데이터 프레임 생성
cluster_0_df_y = processed_df[processed_df['cluster_y'] == 0]
cluster_1_df_y = processed_df[processed_df['cluster_y'] == 1]
cluster_2_df_y = processed_df[processed_df['cluster_y'] == 2]

#train, test 데이터 분류
data = processed_df['before_Covid_mean'].to_numpy()
target=processed_df['after_Covid_total'].to_numpy()
print(data)
print(target)

train_total_data,test_total_data,train_total_target,test_total_target=train_test_split(data , target , test_size=0.2)

train_total_data = train_total_data.reshape(-1,1)
test_total_data = test_total_data.reshape(-1,1)

#선형회귀 모델
lf = LinearRegression()
lf.fit(train_total_data,train_total_target)
print(lf.score(train_total_data , train_total_target))
print(lf.score(test_total_data , test_total_target))
print(lf.predict(test_total_data))
predict_data=lf.predict(test_total_data)

#산점도 출력
plt.scatter(test_total_data , test_total_target)
plt.scatter(test_total_data,predict_data)
plt.plot( [50,100], [50*lf.coef_ +lf.intercept_ ,100*lf.coef_ + lf.intercept_])
plt.scatter(61.518926 , 372.113553 ,marker="^",color="black")
plt.show()

#covid 이전 성적기준으로 cluster 산점도 보여주기
plt.title("K=3 Clustering")
plt.xlabel('before_Covid_mean') #x축 before_Covid_mean
plt.ylabel('after_Covid_mean') #y축 after_Covid_mean
plt.scatter(cluster_0_df['before_Covid_mean'], cluster_0_df['after_Covid_total'], c="red") #cluster_id 값 0인 산점도 빨간색
plt.scatter(cluster_1_df['before_Covid_mean'], cluster_1_df['after_Covid_total'], c="green") #cluster_id 값 1인 산점도 녹색
plt.scatter(cluster_2_df['before_Covid_mean'], cluster_2_df['after_Covid_total'], c="blue") #cluster_id 값 2인 산점도 파란색
plt.plot( [50,100], [50*lf.coef_ +lf.intercept_ ,100*lf.coef_ + lf.intercept_])
plt.xlabel('Mean', size = 12)
plt.ylabel('Total', size = 12)
plt.show()

#covid 이후 성적기준으로 cluster 산점도 보여주기
plt.title("K=3 Clustering")
plt.xlabel('before_Covid_mean') #x축 before_Covid_mean
plt.ylabel('after_Covid_mean') #y축 after_Covid_mean
plt.scatter(cluster_0_df_y['before_Covid_mean'], cluster_0_df_y['after_Covid_total'], c="red") #cluster_id 값 0인 산점도 빨간색
plt.scatter(cluster_1_df_y['before_Covid_mean'], cluster_1_df_y['after_Covid_total'], c="green") #cluster_id 값 1인 산점도 녹색
plt.scatter(cluster_2_df_y['before_Covid_mean'], cluster_2_df_y['after_Covid_total'], c="blue") #cluster_id 값 2인 산점도 파란색
plt.plot( [50,100], [50*lf.coef_ +lf.intercept_ ,100*lf.coef_ + lf.intercept_])
plt.xlabel('Mean', size = 12)
plt.ylabel('Total', size = 12)
plt.show()