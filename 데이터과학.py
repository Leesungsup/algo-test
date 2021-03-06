import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return i, False
    return n, True
n=int(input())
num,p=isPrime(n)
if p:
    print(num,"is Prime")
else:
    print(n,"is not Prime",num,"can divide")

#def makeDict(K,V):
#    D=dict()
#    for i in range(len(K)):
#        if K[i] not in D:
#            D[K[i]]=V[i]
#    print(D)
#    return D

#makeDict(('한국어', '수학', '영어'),(90.3, 85.5, 92.7))
import numpy as np
weight=[]
for i in range(100):
    x = np.random.uniform(40.0, 90.0)
    weight.append(x)
#print(weight)
height=[]
for i in range(100):
    x = np.random.randint(140.0, 200.0)
    height.append(x)
#print(height)
bmi=[]
for i in range(100):
    BMI = weight[i] / (height[i]/100)**2
    bmi.append(BMI)
print(bmi)
#print("bmi array : ",bmi[:10])
import matplotlib.pyplot as plt
import numpy as np
weight=[]
for i in range(100):
    x = np.random.uniform(40.0, 90.0)
    weight.append(x)
#print(weight)
height=[]
for i in range(100):
    x = np.random.randint(140.0, 200.0)
    height.append(x)
#print(height)
bmi=[]
for i in range(100):
    BMI = weight[i] / (height[i]/100)**2
    bmi.append(BMI)
#print(bmi)
#print("bmi array : ",bmi[:10])
underweight=0
healthy=0
overweight=0
obese=0
x = np.arange(4)
for i in range(len(bmi)):
    if bmi[i] <= 18.5:
        underweight+=1
    elif bmi[i] <= 24.9:
        healthy+=1
    elif bmi[i] <= 29.9:
        overweight+=1
    else:
        obese+=1

plt.bar(x, [underweight,healthy,overweight,obese])
plt.xticks(x, ['underweight','healthy','overweight','obese'])
plt.show()

plt.hist(bmi, label='bins=4',bins=4)
#plt.hist(weight, bins=30, label='bins=30')
plt.legend()
plt.show()

ratio = [underweight,healthy,overweight,obese]
labels = ['underweight','healthy','overweight','obese']
plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False)
plt.show()

plt.show()
plt.scatter(weight, height)
plt.show()

import numpy as np
import pandas as pd
ar = np.array([[3, '?', 2, 5], ['*', 4, 5, 6,], ['+', 3, 2, '&'],[ 5, '?', 7, '!']])
df = pd.DataFrame(ar)
#print("DataFrame")
#print(df)
#df1 = df.apply(pd.to_numeric, errors='coerce')
#print("NAN")
#print(df1)
#print("isna")
#print(df1.isna())
#print("isna, any")
#print(df1.isna().any())
#print("isna, any, any : ",df1.isna().any().any())
#print("isna, sum")
#print(df1.isna().sum(axis=1))
#print("isna, sum, sum : ",df1.isna().sum().sum())
#print("dropna(how='all')")
#print(df1.dropna(axis=0,how='all'))
#print("dropna(axis=0,how='any')")
#print(df1.dropna(axis=0,how='any'))
#print("dropna(axis=1,how='any')")
#print(df1.dropna(axis=1,how='any'))
#print("dropna(axis=0,thresh=1)")
#print(df1.dropna(axis=0,thresh=1))
#print("dropna(axis=0,thresh=2)")
#print(df1.dropna(axis=0,thresh=2))
#print("dropna(axis=0,thresh=3)")
#print(df1.dropna(axis=0,thresh=3))
#print(df1.fillna(100))
#print("df1.mean(axis=0)")
#print(df1.fillna(df1.mean(axis=0)))
#print("df1.median(axis=0)")
#print(df1.fillna(df1.median(axis=0)))
#print("fillna(method='bfill')")
#print(df1.fillna(method="bfill"))
#print("fillna(method='ffill')")
#print(df1.fillna(method="ffill"))
import nltk
#nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from nltk.corpus import stopwords
import re
s=PorterStemmer()
n=WordNetLemmatizer()
text="Dear Sir, SEEKING YOUR IMMEDIATE ASSISTANCE. Please permit me to make your acquaintance in so informal a manner. My name is. DAN PATRICK of the Democratic Republic of Congo and One of the close aides to the former President of the Democratic Republic of Congo LAURENT KABILA of blessed memory, may his soul rest in peace."
text=text.lower()
text = re.sub(r"[^a-zA-Z0-9]", " ", text)
stop_words = set(stopwords.words('english'))
words = text_to_word_sequence(text)
result=[]
result1=[]
result2=[]
for w in words:
    if w not in stop_words:
        result.append(w)
print([n.lemmatize(w) for w in result])
for w in result:
    result1.append(n.lemmatize(w))
print(result1)
print([s.stem(w) for w in result])
for w in result1:
    result2.append(s.stem(w))
print(result2)
import pandas as pd
import numpy as np
import featuretools.variable_types as vtypes
import featuretools as ft
import warnings
warnings.filterwarnings('ignore')
base_src='./drive/MyDrive'
clients_src=base_src+'/clients.csv'
clients = pd.read_csv('./clients.csv', parse_dates = ['joined'])
loans = pd.read_csv('./loans.csv', parse_dates = ['loan_start', 'loan_end'])
payments = pd.read_csv('./payments.csv', parse_dates = ['payment_date'])
stats = loans.groupby('client_id')['loan_amount'].agg(['mean', 'max', 'min','sum'])
print(clients)
print(loans[(loans['client_id']==26945)])
stats.columns = ['mean_loan_amount', 'max_loan_amount', 'min_loan_amount','total_loan_amount']
clients=clients.merge(stats, left_on = 'client_id', right_index=True, how = 'left')
print(clients)
# Create new entityset
#es = ft.EntitySet(id = 'clients')
#es = es.add_dataframe(dataframe_name='clients', dataframe = clients, index = 'client_id', time_index = 'joined')

#es = es.entity_from_dataframe(entity_id = 'clients', dataframe = clients,index = 'client_id', time_index = 'joined')
#es = es.add_dataframe(dataframe_name = 'loans', dataframe = loans, variable_types = {'repaid': ft.variable_types.Categorical},index = 'loan_id', time_index = 'loan_start')

#es = es.entity_from_dataframe(entity_id = 'loans', dataframe = loans,variable_types = {'repaid': ft.variable_types.Categorical},index = 'loan_id',time_index = 'loan_start')
#es = es.add_dataframe(dataframe_name = 'payments', dataframe = payments,variable_types = {'missed': vtypes.Categorical},make_index = True, index = 'payment_id',time_index = 'payment_date')

#es = es.entity_from_dataframe(entity_id = 'payments',dataframe = payments,variable_types = {'missed': ft.variable_types.Categorical},make_index = True,index = 'payment_id',time_index = 'payment_date')

#print(es)
import pandas as pd
import numpy as np
import sklearn
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
base_src='./drive/MyDrive'
housing = pd.read_csv('./California_Houses.csv')
print(housing.head())
housing_ind = housing.drop("Median_House_Value",axis=1)
housing_ind['Longitude']=housing_ind['Longitude']*-1
print(housing_ind.head())
housing_dep = housing["Median_House_Value"]
value_house=housing.loc[:,['Median_House_Value']]
print("Medain Housing Values")
print(value_house.head())
bestfeatures = SelectKBest(score_func=chi2, k=13)
fit = bestfeatures.fit(housing_ind,value_house)
dfcolumns = pd.DataFrame(housing_ind.columns)
dfscores = pd.DataFrame(fit.scores_)
featureScores = pd.concat([dfcolumns, dfscores],axis=1)
featureScores.columns = ['Specs','Score'] #name the dataframe columns
print(featureScores.nlargest(13,'Score')) #print 10 bestfeature
#print(housing_dep.head())
#sklearn.datasets.fetch_california_housing(*, data_home=None, download_if_missing=True, return_X_y=False, as_frame=False)
import sklearn
from sklearn.ensemble import ExtraTreesClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
base_src='./drive/MyDrive'
housing = pd.read_csv('./California_Houses.csv')
housing_ind = housing.drop("Median_House_Value",axis=1)
housing_ind['Longitude']=housing_ind['Longitude']*-1
housing_dep = housing["Median_House_Value"]
value_house=housing.loc[:,['Median_House_Value']]
model = ExtraTreesClassifier()
model.fit(housing_ind,value_house.values.ravel())
print(model.feature_importances_)
feat_importances = pd.Series(model.feature_importances_, index=housing_ind.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

base_src='./drive/MyDrive'
df=pd.read_csv(base_src+'/bmi_data_lab3.csv') #read csv file and store in df

print("BMI DATA File")
print(df) #print the data

print("Describtion: ")
print(df.describe()) #print df statistical info

print("Column values: ")
print(df.columns.values) #print df value of columns

print("Types: ")
print(df.dtypes) #print df coulumns types

# Plot height histograms (bins=10) for each BMI value.
grid = sns.FacetGrid(df, col='BMI')
grid.map(plt.hist, 'Height (Inches)', bins=10)
plt.show()

# Plot weight histograms (bins=10) for each BMI value.
grid1 = sns.FacetGrid(df, col='BMI')
grid1.map(plt.hist, 'Weight (Pounds)', bins=10)
plt.show()

la = LabelEncoder()
la.fit(df['Sex'])
df['Sex'] = la.transform(df['Sex'])
print(df)#Converting Sex from categorical data to numeric data

standardScaler = preprocessing.StandardScaler() #Create standard scaler withfunction
standardScaled_df = standardScaler.fit_transform(df)
standardScaled_df = pd.DataFrame(standardScaled_df, columns = ['Sex', 'Age','Height (Inches)', 'Weight (Pounds)', 'BMI'])

minmaxScaler = preprocessing.MinMaxScaler()#Create minmax scaler with function
minmaxScaled_df = minmaxScaler.fit_transform(df)
minmaxScaled_df = pd.DataFrame(minmaxScaled_df, columns = ['Sex', 'Age', 'Height (Inches)', 'Weight (Pounds)', 'BMI'])

robustScaler = preprocessing.RobustScaler() #Create robust scaler with function
robustScaled_df = robustScaler.fit_transform(df)
robustScaled_df = pd.DataFrame(robustScaled_df, columns = ['Sex', 'Age', 'Height (Inches)', 'Weight (Pounds)', 'BMI'])

fig,(ax1, ax2, ax3, ax4) = plt.subplots(ncols = 4, figsize=(14,4)) #create 4subplot box with size 14,4
ax1.set_title('Before Scaling')
sns.kdeplot(df['Height (Inches)'], ax=ax1) #Show kdeplot of height
ax2.set_title('After Standard Scaling')
sns.kdeplot(standardScaled_df['Height (Inches)'], ax=ax2) #Show height in standard scaling result
ax3.set_title('After MinMax Scaling')
sns.kdeplot(minmaxScaled_df['Height (Inches)'], ax=ax3)#Show height in Min-Max scaling result
ax4.set_title('After Robust Scaling')
sns.kdeplot(robustScaled_df['Height (Inches)'], ax=ax4)#Show height in robust scaling result
plt.show()

fig, (ax5, ax6, ax7, ax8) = plt.subplots(ncols=4, figsize=(10, 5))  # Create subplot for outputting 4 plots
ax5.set_title('Before Scaling')
sns.kdeplot(df['Weight (Pounds)'], ax=ax5)  # Plot scaling results for weight
ax6.set_title('After Standard Scaling')
sns.kdeplot(standardScaled_df['Weight (Pounds)'], ax=ax6)  # Show weight in standard scaling result
ax7.set_title('After MinMax Scaling')
sns.kdeplot(minmaxScaled_df['Weight (Pounds)'], ax=ax7)  # Show weight in Min-Max scaling result
ax8.set_title('After Robust Scaling')
sns.kdeplot(robustScaled_df['Weight (Pounds)'], ax=ax8)  #Show weight in robust scaling result
plt.show()

# The number of NAN for each row
print("The number of NAN for each row: ")
print(df.isnull().sum(axis=1))

# The number of NAN for each column
print("The number of NAN for each column:")
print(df.isna().sum())

# Extract all rows without NAN
print("Extract all rows without NAN: ")
print(df.dropna())

# Fill NaN with mean
print("Fill NaN with mean")
print(df.fillna(df.mean()))

# Fill NaN with median
print("Fill NaN with median")
print(df.fillna(df.median()))

# Fill NaN using ffill method
print("FFill")
print(df.fillna(axis=0, method='ffill'))

# Fill NaN using bfill method
print('BFill')
print(df.fillna(axis=0, method='bfill'))

# The parentheses in the column name restrict the coding. Therefore, change the name
df.rename(columns={'Height (Inches)' : 'Height', 'Weight (Pounds)' : 'Weight'}, inplace=True)

df1 = df.dropna()  # Create a data frame with a NAN value dropped for linear regression fitting

# Assignment for Coordination
x1 = df1['Height']
y1 = df1['Weight']


# Apply data to linear regression
E = linear_model.LinearRegression()
E.fit(x1.values.reshape(-1, 1), y1)  # Reshape because it needs to be in two dimensions.

# Draw a line with forecasts obtained by fitting
plt.plot(x1, E.predict(x1.values.reshape(-1, 1)))

# Coefficients and intercept Outputs obtained by fitting
print('Coeffficients : ', E.coef_)
print('Intercept : ', E.intercept_)


# Declare a function that replaces nan with the predicted value when it finds it.
def nanTopreWeight(k):
    if np.isnan(k.Weight):
        # If nan is found in the weight column of the dataframe
        k.Weight = (E.predict([[k.Height]]))  # Replace with forecasts obtained by linear regression
    return k.Weight

# a = intercept, b = coefficient
a = float(E.intercept_)
b = float(E.coef_)

# Prediction of height through linear regression equation and weight value
def nanTopreHeight(k):
    if np.isnan(k.Height):  # If nan is found in the height column of the dataframe
        #Linear function: y=a(intercept)+b(coefficient)x, so x = (y - a) / b
        k.Height = (float(k.Weight) - a) / b  # Replace with forecasts obtained by linear regression
    return k.Height

# Update nan values ​​in dataframe with predictions using previously defined function
df['Weight'] = df.apply(nanTopreWeight, axis=1)
df['Height'] = df.apply(nanTopreHeight, axis=1)

print(df)

# Print a scatterplot of the dataframe with dropped nan values.
# Dataframe with nan values ​​filled with predictions of different colors.
x = df['Height']
y = df['Weight']
plt.title("Scatter Plot", fontsize=15)
plt.scatter(x, y, color='r')
plt.scatter(x1, y1, color='b')
plt.show()

# For male dataset
base_src='./drive/MyDrive'
dm = pd.read_csv(base_src+'/bmi_data_lab3.csv')  # Read the csv file and save it to the pandas data frame.

# The parentheses in the column name restrict the coding. Therefore, change the name
dm.rename(columns={'Height (Inches)' : 'Height', 'Weight (Pounds)' : 'Weight'}, inplace=True)

dfm1 = dm.query("Sex=='Male'")  # Only import gender as male.
dm = dfm1.copy()  # Because SettingWithCopyWarning pops up, make a new copy and manage it.
dm1 = dm.dropna()  # Create a data frame with a NAN value dropped for linear regression fitting

# Assignment for Coordination
xm1 = dm1['Height']
ym1 = dm1['Weight']

# Apply data to linear regression
dm_E = linear_model.LinearRegression()
dm_E.fit(xm1.values.reshape(-1, 1), ym1)  # Reshape because it needs to be in two dimensions.

# Draw a line with forecasts obtained by fitting
plt.plot(xm1, dm_E.predict(xm1.values.reshape(-1, 1)))

# Linear function: y=a(intercept)+b(coefficient)x
print('Coefficient : ', dm_E.coef_)
print('Intercept : ', dm_E.intercept_)


# Declare a function that replaces nan with the predicted value when it finds it.
def nanTopreWeight_male(k):
    if np.isnan(k.Weight): # If nan is found in the weight column of the dataframe
        k.Weight = (dm_E.predict([[k.Height]]))  # Replace with forecasts obtained by linear regression
    return k.Weight


# a = intercept, b = coefficient
a = float(dm_E.intercept_)
b = float(dm_E.coef_)


# Prediction of height through linear regression equation and weight value
def nanTopreHeight_male(k):
    if np.isnan(k.Height): # If nan is found in the height column of the dataframe
        # Linear function: y=a(intercept)+b(coefficient)x, so x = (y - a) / b
        k.Height = (float(k.Weight) - a) / b  # Replace with forecasts obtained by linear regression
    return k.Height

# Update nan values ​​in dataframe with predictions using previously defined function
dm['Weight'] = dm.apply(nanTopreWeight_male, axis=1)
dm['Height'] = dm.apply(nanTopreHeight_male, axis=1)

print(dm)

# Print a scatterplot of the dataframe with dropped nan values.
# Dataframe with nan values ​​filled with predictions of different colors.
xm = dm['Height']
ym = dm['Weight']
plt.title("Scatter Plot(male)", fontsize=15)
plt.scatter(xm, ym, color='r')
plt.scatter(xm1, ym1, color='b')
plt.show()


# For female dataset
base_src='./drive/MyDrive'
dff = pd.read_csv(base_src+'/bmi_data_lab3.csv')  # Read the csv file and save it to the pandas data frame.

# The parentheses in the column name restrict the coding. Therefore, change the name
dff.rename(columns={'Height (Inches)' : 'Height', 'Weight (Pounds)' : 'Weight'}, inplace=True)

dfm1 = dff.query("Sex=='Female'")  # Only import gender as female.
dfe = dfm1.copy()  # Because SettingWithCopyWarning pops up, make a new copy and manage it.
dfe1 = dfe.dropna()  # Create a data frame with a NAN value dropped for linear regression fitting

# Assignment for Coordination
xf1 = dfe1['Height']
yf1 = dfe1['Weight']

# Apply data to linear regression
dfe_E = linear_model.LinearRegression()
dfe_E.fit(xf1.values.reshape(-1, 1), yf1)  # Reshape because it needs to be in two dimensions.

# Draw a line with forecasts obtained by fitting
plt.plot(xf1, dfe_E.predict(xf1.values.reshape(-1, 1)))

# Linear function: y=a(intercept)+b(coefficient)x
print('coef', dfe_E.coef_)
print('intercept', dfe_E.intercept_)


# Declare a function that will replace the nan values with the predicted values when they are found
def nanTopreWeight_female(k):
    if np.isnan(k.Weight):  # If nan is found in the weight column of the dataframe
        k.Weight = (dfe_reg.predict([[k.Height]]))  # Replace with forecasts obtained by linear regression
    return k.Weight


# Linear function: y=a(intercept)+b(coefficient)x, so x = (y - a) / b
a = float(dfe_E.intercept_)
b = float(dfe_E.coef_)


# Predict height values through linear regression equations and weight values
def nanTopreHeight_female(k):
    if np.isnan(k.Height):  # If nan is found in the height column of the dataframe
        k.Height = (float(k.Weight) - a) / b  # Replace with forecasts obtained by linear regression
    return k.Height

# Update nan values of data frames to predictions using the functions defined previously
dfe['Weight'] = dfe.apply(nanTopreWeight_female, axis=1)
dfe['Height'] = dfe.apply(nanTopreHeight_female, axis=1)

print(dfe)

# Output the Scatter Plot of the data frame with the nan values dropped,
# and the data frame with the nan values filled with forecasts in different colors.
xf = dfe['Height']
yf = dfe['Weight']
plt.title("Scatter Plot(female)", fontsize=15)
plt.scatter(xf, yf, color='r')
plt.scatter(xf1, yf1, color='b')
plt.show()

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

base_src='./drive/MyDrive'
df=pd.read_excel(base_src+'/bmi_data_phw3.xlsx') #read csv file and store in df
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

# Plot the height histogram (bins=10) for each BMI value.
grid = sns.FacetGrid(df, col='BMI')
grid.map(plt.hist, 'Height (Inches)', bins=10)
plt.show()

# Plot a weighted histogram (bins=10) for each BMI value.
grid1 = sns.FacetGrid(df, col='BMI')
grid1.map(plt.hist, 'Weight (Pounds)', bins=10)
plt.show()

# Convert Categories data to numbers.(sex(male, female) to 0, 1)
LabelEncoder = LabelEncoder()
LabelEncoder.fit(df['Sex'])
df['Sex'] = LabelEncoder.transform(df['Sex'])

# Normalize data frames to Standard Scaler
standardScaler = preprocessing.StandardScaler()
standardscaled_df = standardScaler.fit_transform(df)
standardscaled_df = pd.DataFrame(standardscaled_df, columns=['Sex', 'Age', 'Height (Inches)', 'Weight (Pounds)', 'BMI'])

# Normalize data frames to Min-Max Scaler
minmaxScaler = preprocessing.MinMaxScaler()
minmaxscaled_df = minmaxScaler.fit_transform(df)
minmaxscaled_df = pd.DataFrame(minmaxscaled_df, columns=['Sex', 'Age', 'Height (Inches)', 'Weight (Pounds)', 'BMI'])

# Normalize data frames to Robust Scaler
robustScaler = preprocessing.RobustScaler()
robustscaled_df = robustScaler.fit_transform(df)
robustscaled_df = pd.DataFrame(robustscaled_df, columns=['Sex', 'Age', 'Height (Inches)', 'Weight (Pounds)', 'BMI'])

#4 The plot output was previously scaled to height.
fig, (ax1, ax2, ax3, ax4) = plt.subplots(ncols=4, figsize=(10, 5))  # Create subplot for outputting 4 plots
ax1.set_title('Before Scaling')
sns.kdeplot(df['Height (Inches)'], ax=ax1)  # Plot scaling results for height

ax2.set_title('After Standard Scaling')
sns.kdeplot(standardscaled_df['Height (Inches)'], ax=ax2)  # Standard scaling results for height

ax3.set_title('After MinMax Scaling')
sns.kdeplot(minmaxscaled_df['Height (Inches)'], ax=ax3)  # Min-Max scaling results for height

ax4.set_title('After Robust Scaling')
sns.kdeplot(robustscaled_df['Height (Inches)'], ax=ax4)  # Robust scaling results for height

plt.show()

# 4 The plot output was previously scaled to weight
fig, (ax5, ax6, ax7, ax8) = plt.subplots(ncols=4, figsize=(10, 5))  # Create subplot for outputting 4 plots
ax5.set_title('Before Scaling')
sns.kdeplot(df['Weight (Pounds)'], ax=ax5)  # Plot scaling results for weight

ax6.set_title('After Standard Scaling')
sns.kdeplot(standardscaled_df['Weight (Pounds)'], ax=ax6)  # Standard scaling results for weight

ax7.set_title('After MinMax Scaling')
sns.kdeplot(minmaxscaled_df['Weight (Pounds)'], ax=ax7)  # Min-Max scaling results for weight

ax8.set_title('After Robust Scaling')
sns.kdeplot(robustscaled_df['Weight (Pounds)'], ax=ax8)  # Robust scaling results for weight

plt.show()

# Parentheses in column names restrict coding. So change the name.
df.rename(columns={'Height (Inches)': 'Height', 'Weight (Pounds)': 'Weight'}, inplace=True)

# Assignment for Coordination
x = df['Height']
y = df['Weight']

# Apply data to linear regression
E = linear_model.LinearRegression()
E.fit(x.values.reshape(-1, 1), y)  # Change the shape as it should be 2D.

# Create new columns with predictions obtained by linear regression
df['Weight(predict)'] = df.apply(lambda x: float(E.predict([[x.Height]])), axis=1)

# Normalize the e values
normalize = []
e = df['Weight'] - df['Weight(predict)']
# Calculate linear regression equations from predictions
for value in e:
    ze = (value - np.mean(e)) / np.std(e)
    normalize.append(ze)

# Plot a histogram showing the distribution of ze (~10 bins)
plt.hist(normalize, bins=10)
plt.title('Weight Reference Histogram')
plt.xlabel('Ze')
plt.ylabel('frequency')
plt.show()

#If it is less than -2, it is 0, if more than -2 and less than -1, it is 1, if it is more than -1 and less than 0, it is 2, if it is more than 0 and less than 2, it is 3, if it is 2 or more, it is 4
# Determine the record with ze, set BMI
bmi = []
for i in normalize:
    if i < -2:
        bmi.append(0)
    elif i>=-2 and i<-1:
        bmi.append(1)
    elif i>=-1 and i<0:
        bmi.append(2)
    elif i>=0 and i<2:
        bmi.append(3)
    elif i>=2:
        bmi.append(4)
df['BMI(predict)'] = bmi

#Check how well the existing bmi matches the predicted bmi.
print('Total number of bmi : ')
print(len(df.values))
count=0
print('Corret Count : ')
for i in df.values:
    if i[4]==i[6]:
        count+=1
print(count)
print(df[(df['BMI(predict)']==0)])
print(df[(df['BMI(predict)']==4)])

# For male dataset
base_src='./drive/MyDrive'
dfm = pd.read_excel(base_src+'/bmi_data_phw3.xlsx')  # Read the xlsx file and save it to the pandas data frame.

# The parentheses in the column name restrict the coding. Therefore, change the name
dfm.rename(columns={'Height (Inches)': 'Height', 'Weight (Pounds)': 'Weight'}, inplace=True)

dfm1 = dfm.query("Sex=='Male'")  # Only import gender as male.
dm = dfm1.copy()  # Because Setting With Copy Warning pops up, make a new copy and manage it.

# Assignment for Coordination
dm_x = dm['Height']
dm_y = dm['Weight']

# Apply data to linear regression
dm_E = linear_model.LinearRegression()
dm_E.fit(dm_x.values.reshape(-1, 1), dm_y)  # Change the shape as it should be 2D.

# Create new columns with predictions obtained by linear regression
dm['Weight(predict)'] = dfm1.apply(lambda x: float(dm_E.predict([[x.Height]])), axis=1)

# Normalize the e values
normalize_m = []
dm_e = dm['Weight'] - dm['Weight(predict)']
# Calculate the male's e by subtracting the original weight from the expected weight.
for value in dm_e:
    ze_m = (value - np.mean(dm_e)) / np.std(dm_e)
    normalize_m.append(ze_m)

# Plot a histogram showing the distribution of ze (~10 bins)
plt.hist(normalize_m, bins=10)
plt.title("Weight Reference Histogram(only male)")
plt.xlabel('ze')
plt.ylabel('frequency')
plt.show()

#If it is less than -2, it is 0, if more than -2 and less than -1, it is 1, if it is more than -1 and less than 0, it is 2, if it is more than 0 and less than 2, it is 3, if it is 2 or more, it is 4
# Check records with ze, set BMI
bmi_m = []
for i in normalize_m:
    if i < -2:
        bmi_m.append(0)
    elif i>=-2 and i<-1:
        bmi_m.append(1)
    elif i>=-1 and i<0:
        bmi_m.append(2)
    elif i>=0 and i<2:
        bmi_m.append(3)
    elif i>=2:
        bmi_m.append(4)
dm['BMI(predict)'] = bmi_m

#Check how well the existing bmi matches the predicted bmi.
print('Total number of male bmi : ')
print(len(dm.values))
count=0
print('Correct Count : ')
for i in dm.values:
    if i[4]==i[6]:
        count+=1
print(count)
print(dm[(dm['BMI(predict)']==0)])
print(dm[(dm['BMI(predict)']==4)])

# For female dataset
base_src='./drive/MyDrive'
dff = pd.read_excel(base_src+'/bmi_data_phw3.xlsx')  # Read the xlsx file and save it to a pandas dataframe.

# Parentheses in column names restrict coding. So change the name.
dff.rename(columns={'Height (Inches)': 'Height', 'Weight (Pounds)': 'Weight'}, inplace=True)

dff1 = dff.query("Sex=='Female'")  # Only import gender as female.
dfe = dff1.copy()  # A setting with a copy warning appears, so make a new copy and manage it.

# Assignment for Coordination
dfe_x = dfe['Height']
dfe_y = dfe['Weight']

# Apply data to linear regression
dfe_E = linear_model.LinearRegression()
dfe_E.fit(dfe_x.values.reshape(-1, 1), dfe_y)  # Change the shape as it should be 2D.

dfe['Weight(predict)'] = dff1.apply(lambda x: float(dfe_E.predict([[x.Height]])), axis=1)  # Predict a woman's weight using the equation.

dfe_e = dfe['Weight'] - dfe['Weight(predict)']
# Calculate the woman's e by subtracting the original weight from the expected weight.

normalize_f = []
# Normalized Data
for value in dfe_e:
    ze_f = (value - np.mean(dfe_e)) / np.std(dfe_e)
    normalize_f.append(ze_f)

# Plot a histogram showing the distribution of ze (~10 bins).
plt.hist(normalize_f, bins=10)
plt.title("Weight Reference Histogram(only female)")
plt.xlabel('ze')
plt.ylabel('frequency')
plt.show()

#If it is less than -2, it is 0, if more than -2 and less than -1, it is 1, if it is more than -1 and less than 0, it is 2, if it is more than 0 and less than 2, it is 3, if it is 2 or more, it is 4
# Check records with ze, set BMI
bmi_f = []
for i in normalize_f:
    if i < -2:
        bmi_f.append(0)
        continue
    elif i>=-2 and i<-1:
        bmi_f.append(1)
    elif i>=-1 and i<0:
        bmi_f.append(2)
    elif i>=0 and i<2:
        bmi_f.append(3)
    elif i>=2:
        bmi_f.append(4)
dfe['BMI(predict)'] = bmi_f

#Check how well the existing bmi matches the predicted bmi.
print('Total number of female bmi : ')
print(len(dfe.values))
count=0
print('Correct Count : ')
for i in dfe.values:
    if i[4]==i[6]:
        count+=1
print(count)
print(dfe[(dfe['BMI(predict)']==0)])
print(dfe[(dfe['BMI(predict)']==4)])
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import seaborn as sns

dataset1=np.array([2400,2650,2350,4950,3100,2500,5106,3100,2900,1750])
dataset2=np.array([41200,50100,52000,66000,44500,37700,73500,37500,56700,35600])
dataset3=[[2400,41200],[2650,50100],[2350,52000],[4950,66000],[3100,44500],[2500,37700],[5106,73500],[3100,37500],[2900,56700],[1750,35600]]
dataset3.sort()

#Dataset input
dataset1=np.array([2400,2650,2350,4950,3100,2500,5106,3100,2900,1750])
dataset2=np.array([41200,50100,52000,66000,44500,37700,73500,37500,56700,35600])
dataset3=[[2400,41200],[2650,50100],[2350,52000],[4950,66000],[3100,44500],[2500,37700],[5106,73500],[3100,37500],[2900,56700],[1750,35600]]
dataset3.sort()
#Plot scatterplots and linear regression
x_1=pd.DataFrame(dataset3,columns=['spends','income'])
x=pd.DataFrame(dataset1)
y=pd.DataFrame(dataset2)
sns.scatterplot(x='spends', y='income', data=x_1)
sns.regplot(x='spends', y='income', ci=None, data=x_1)


#Linear Regression Prediction
E=LinearRegression()

E.fit(x_1.loc[:,'spends'].values.reshape(-1,1),x_1.loc[:,'income'])
new_dataset=np.array([3500,5300])
new_x=pd.DataFrame(new_dataset)
new_y=E.predict(new_x.values.reshape(-1,1))

#Plot scatterplots and linear regression with new data added
for i in range(len(new_x)):
    dataset3.append([new_x.values.reshape(-1,1)[i][0],new_y[i]])
dataset3.sort()

x_1=pd.DataFrame(dataset3,columns=['spends','income'])
sns.scatterplot(x='spends', y='income', data=x_1)
sns.regplot(x='spends', y='income', ci=None, data=x_1)

#Dataset input
x1=[]
y1=[]
dataset4=[[2400,41200],[2650,50100],[2350,52000],[4950,66000],[3100,44500],[2500,37700],[5106,73500],[3100,37500],[2900,56700],[1750,35600]]
dataset4.sort()
for i in dataset4:
    x1.append(i[0])
    y1.append(i[1])

#Sigma x
def sum(x):
    result=0
    for i in x:
        result+=i
    return result
#Sigma x**2
def sum2(x):
    result=0
    for i in x:
        b=i*i
        result+=b
    return result
#Sigma x*y
def sumxy(x,y):
    result=0
    for i in range(len(x)):
        result+=x[i]*y[i]
    return result
sigma_x=sum(x1)
sigma_y=sum(y1)
sigma_x_sqr=sum2(x1)
sigma_y_sqr=sum2(y1)
sigma_xy=sumxy(x1,y1)


#Linear regression formula
def make_a(sigma_x,sigma_y,sigma_xy,sigma_x_sqr):
    son=(len(x1)*sigma_xy)-(sigma_x*sigma_y)
    mom=(len(x1)*sigma_x_sqr)-(sigma_x*sigma_x)
    return son/mom
def make_b(sigma_y,a,sigma_x):
    son=sigma_y-(a*sigma_x)
    return son/len(x1)
a=make_a(sigma_x,sigma_y,sigma_xy,sigma_x_sqr)
b=make_b(sigma_y,a,sigma_x)
#print(a,b)

#Plot scatterplots and linear regression
plt.scatter(x1,y1)
plt.xlabel('spends')
plt.ylabel('income')
reg_y=[]
for i in x1:
    reg_y.append(a*i+b)
plt.plot(x1,reg_y,c = 'r', label = 'reg')
plt.legend()

#Plot scatterplots and linear regression with new data added
new_data_y=[]
new_data_x=[3500,5300]
for i in new_data_x:
    new_data_y.append((a*i) + b)
for i in range(len(new_data_x)):
    dataset4.append([new_data_x[i],new_data_y[i]])
dataset4.sort()
x2=[]
y2=[]
for i in dataset4:
    x2.append(i[0])
    y2.append(i[1])
plt.scatter(x2, y2)
plt.xlabel('spends')
plt.ylabel('income')
new_reg_y=[]
for i in x2:
    new_reg_y.append(a*i+b)
plt.plot(x2,new_reg_y,c = 'r', label = 'reg')
plt.legend()

import numpy as np #to work with arrays
import pandas as pd #to read the dataset
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt #to plot stats
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
%matplotlib inline
base_src='./drive/MyDrive'
housing = pd.read_csv(base_src+'/California_Houses.csv')
X = housing[housing.columns.difference(['Median_House_Value'])]
y = housing[['Median_House_Value']]
#print(X.head())
scaler = StandardScaler()
# 데이터 학습
scaler.fit(X)
# 변환
scaler_data = scaler.transform(X)
pca = PCA(n_components = 2)
pca.fit(scaler_data)
d=pca.transform(scaler_data)
#print(d)
df_X = pd.DataFrame(X)
#print(df_X.columns)
print(pd.DataFrame(pca.components_,columns=df_X.columns,index = ['PC-1','PC-2']))
data2 = pd.DataFrame(data = pca.transform(scaler_data), columns=['pc1', 'pc2'])
#print(data2.head())
from sklearn.cluster import KMeans
x = []   # k 가 몇개인지
y = []   # 응집도가 몇인지
for k in range(1, 12):
    kmeans = KMeans(n_clusters = k)
    kmeans.fit(data2)
    x.append(k)
    y.append(kmeans.inertia_)
#plt.plot(x, y)
kmeans = KMeans(n_clusters=2)
kmeans.fit(data2)
data2['labels'] = kmeans.predict(data2)
data2.head()
sns.scatterplot(x='pc1', y='pc2', hue='labels', data=data2)

import pandas as pd
import numpy as np
import sklearn
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split

base_src='./drive/MyDrive'
housing = pd.read_csv(base_src+'/California_Houses.csv')
housing['Longitude'] = housing['Longitude']*-1
X = housing[housing.columns.difference(['Median_House_Value'])]
y = housing[['Median_House_Value']]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
print(housing.shape)
print(housing.head())
# target(Price)와 가장 correlated 된 features 를 k개 고르기.
## f_regresison, SelectKBest 불러오기.
from sklearn.feature_selection import f_regression, SelectKBest
## selctor 정의하기.
selector = SelectKBest(score_func=f_regression, k=5)
## 학습데이터에 fit_transform
X_train_selected = selector.fit_transform(X_train, y_train)
## 테스트 데이터는 transform
X_test_selected = selector.transform(X_test)
print(X_train_selected.shape, X_test_selected.shape)
all_names = X_train.columns
## selector.get_support()
selected_mask = selector.get_support()
## 선택된 특성(변수)들
selected_names = all_names[selected_mask]
## 선택되지 않은 특성(변수)들
unselected_names = all_names[~selected_mask]
print('Selected names: ', selected_names)
print('Unselected names: ', unselected_names)


import pandas as pd
import numpy as np
import sklearn
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import f_regression
base_src='./drive/MyDrive'
housing = pd.read_csv(base_src+'/California_Houses.csv')
housing['Longitude'] = housing['Longitude']*-1
X = housing[housing.columns.difference(['Median_House_Value'])]
y = housing[['Median_House_Value']]
housing_ind = housing.drop("Median_House_Value",axis=1)
#print(housing_ind.head())
value_house=housing.loc[:,['Median_House_Value']]
#print("Medain Housing Values")
#print(value_house.head())
bestfeatures = SelectKBest(score_func=chi2, k=13)
fit = bestfeatures.fit(housing_ind,value_house)
dfcolumns = pd.DataFrame(housing_ind.columns)
dfscores = pd.DataFrame(fit.scores_)
featureScores = pd.concat([dfcolumns, dfscores],axis=1)
featureScores.columns = ['Specs','Score']
print(featureScores.nlargest(5,'Score'))


import sklearn
from sklearn.ensemble import ExtraTreesClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
base_src='./drive/MyDrive'
housing = pd.read_csv(base_src+'/California_Houses.csv')
housing=housing.loc[:3500]
print(housing)
housing_ind = housing.drop("Median_House_Value",axis=1)
housing_ind['Longitude']=housing_ind['Longitude']*-1
housing_dep = housing["Median_House_Value"]
value_house=housing.loc[:,['Median_House_Value']]
model = ExtraTreesClassifier()
model.fit(housing_ind,value_house.values.ravel())
print(model.feature_importances_)
feat_importances = pd.Series(model.feature_importances_, index=housing_ind.columns)
feat_importances.nlargest(5).plot(kind='barh')
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
base_src='./drive/MyDrive'
housing = pd.read_csv(base_src+'/California_Houses.csv')
housing_ind = housing.drop("Median_House_Value",axis=1)
housing_ind['Longitude']=housing_ind['Longitude']*-1
housing_dep = housing["Median_House_Value"]
value_house=housing.loc[:,['Median_House_Value']]
housing_ind['Median_House_Value']=value_house
print(housing_ind)
corrmat = housing_ind.corr() #corr() computes pairwise correlations of features in a Data Frame
top_corr_features = corrmat.index
plt.figure(figsize=(13,13))
#plot the heat map
g=sns.heatmap(housing_ind[top_corr_features].corr(),annot=True,cmap="RdYlGn")
print(g)

data = pd.DataFrame({"no_insects":["True","True","True","False","True","True","True","True","True","False"],
                     "no_dead":["True","True","False","True","True","True","False","False","True","False"],
                     "no_wilting":["True","True","True","True","True","True","False","True","True","True"],
                     "no_diseases":["True","True","False","True","True","True","False","False","True","True"],
                     "tree_health":["Good","Good","Poor","Good","Good","Good","Poor","Poor","Good","Poor"]},
                    columns=["no_insects","no_dead","no_wilting","no_diseases","tree_health"])
# 기술 속성(descriptive features)
features = data[["no_insects","no_dead","no_wilting","no_diseases"]]
# 대상 속성(target feature)
target = data["tree_health"]
print(data)

# 엔트로피
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts = True)
    entropy = -np.sum([(counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
    return entropy

print('H(x) = ', round(entropy(target), 5))

# 정보이득
def InfoGain(data,split_attribute_name,target_name):
    # 전체 엔트로피 계산
    total_entropy = entropy(data[target_name])
    print('Entropy(D) = ', round(total_entropy, 5))
    # 가중 엔트로피 계산
    vals,counts= np.unique(data[split_attribute_name],return_counts=True)
    Weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*
                               entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name])
                               for i in range(len(vals))])
    print('H(', split_attribute_name, ') = ', round(Weighted_Entropy, 5))
    # 정보이득 계산
    Information_Gain = total_entropy - Weighted_Entropy
    return Information_Gain
print('InfoGain( no_insects ) = ', round(InfoGain(data, "no_insects", "tree_health"), 5), '\n')
print('InfoGain( no_wilting ) = ', round(InfoGain(data, "no_wilting", "tree_health"), 5), '\n')
print('InfoGain( no_diseases ) = ', round(InfoGain(data, "no_diseases", "tree_health"), 5))

# ID3 알고리즘
def ID3(data,originaldata,features,target_attribute_name,parent_node_class = None):

    # 중지기준 정의

    # 1. 대상 속성이 단일값을 가지면: 해당 대상 속성 반환
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]

    # 2. 데이터가 없을 때: 원본 데이터에서 최대값을 가지는 대상 속성 반환
    elif len(data)==0:
        return np.unique(originaldata[target_attribute_name]) \
            [np.argmax(np.unique(originaldata[target_attribute_name], return_counts=True)[1])]

    # 3. 기술 속성이 없을 때: 부모 노드의 대상 속성 반환
    elif len(features) ==0:
        return parent_node_class
    # 트리 성장
    else:
        # 부모노드의 대상 속성 정의(예: Good)
        parent_node_class = np.unique(data[target_attribute_name]) \
            [np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])]
        # 데이터를 분할할 속성 선택
        item_values = [InfoGain(data,feature,target_attribute_name) for feature in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        # 트리 구조 생성
        tree = {best_feature:{}}
        # 최대 정보이득을 보인 기술 속성 제외
        features = [i for i in features if i != best_feature]
        # 가지 성장
        for value in np.unique(data[best_feature]):
            # 데이터 분할. dropna(): 결측값을 가진 행, 열 제거
            sub_data = data.where(data[best_feature] == value).dropna()
            # ID3 알고리즘
            subtree = ID3(sub_data,data,features,target_attribute_name,parent_node_class)
            tree[best_feature][value] = subtree
        return(tree)
# numpy.unique: 고유값 반환
print('numpy.unique: ', np.unique(data["tree_health"], return_counts = True)[1])
# numpy.max: 최대값 반환
print('numpy.max: ', np.max(np.unique(data["tree_health"], return_counts = True)[1]))
# numpy.argmax: 최대값이 위치한  인덱스 반환
print('numpy.argmax: ', np.argmax(np.unique(data["tree_health"], return_counts = True)[1]))
tree = ID3(data, data, ["no_insects","no_wilting","no_diseases"], "tree_health")
from pprint import pprint
pprint(tree)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
base_src='./drive/MyDrive'
tshirt = pd.read_csv(base_src+'/Training Dataset.csv')
tshirt.head()
tshirt.describe()

#Creating Training dataset
dataset = tshirt.iloc[:, 0:2].values
labels = tshirt.iloc[:, 2].values

#testing data
new_data=[161,61]

def knn_algo(new_data, dataset, labels, K):
    #Calculate the distance between the coordinates of the new data and the coordinates of all known data sets.
    dists = dataset - new_data
    dists = np.array(np.sqrt(dists[:,0]**2 + dists[:,1]**2))

    #sort length in ascending order
    sorted_index = np.argsort(dists)

    #Extract the K classification items from the data with the shortest distance from new data
    sorted_labels = np.array(labels[sorted_index[:]])
    K_nearest_labels = sorted_labels[:K]

    #Find the most classification of K data
    count_dict = {}
    for label in K_nearest_labels:
        count_dict[label] = count_dict.get(label,0) + 1

    #return classification
    _labels, count_labels = np.array(list(count_dict.keys())), np.array(list(count_dict.values()))
    return _labels[count_labels.argmax()]

knn_algo(new_data,dataset,labels,5)

import pandas as pd
import numpy as np
import math
from sklearn import preprocessing

df = pd.read_excel('C:/python_file/k_nearest_dataset.xlsx',index_col=None)

#If the value of the T-shirt is M, 0 and L, change to 1
for i in range(len(df)):
    if df.loc[i,"T_shirt_size"] =='M':
        df.loc[i,"T_shirt_size"]=0
    elif df.loc[i,"T_shirt_size"] =='L':
        df.loc[i,"T_shirt_size"]=1

df_list=df.values.tolist()

#Enter your predicted height and weight
height=int(input("Enter the Height(cm): "))
weight=int(input("Enter the Weight(kg): "))
value_to_predict=[]
value_to_predict.append(height)
value_to_predict.append(weight)


scaler = preprocessing.StandardScaler()

#Normalize by inserting data to predict
df_temp=df.copy()
df_temp.loc[len(df)]=[height, weight,-1]
height = np.array(df_temp['Height(cm)'])
weight = np.array(df_temp['Weight(kg)'])
height = scaler.fit_transform(height.reshape(-1, 1))
df_temp['Height(cm)'] = height
weight = scaler.fit_transform(weight.reshape(-1, 1))
df_temp['Weight(kg)'] = weight
#Change Normalized Data to List
scaled_df_temp = df_temp.values.tolist()



#Normalize without Predicting Data
df_temp2=df.copy()
height = np.array(df_temp2['Height(cm)'])
weight = np.array(df_temp2['Weight(kg)'])
height = scaler.fit_transform(height.reshape(-1, 1))
df_temp2['Height(cm)'] = height
weight = scaler.fit_transform(weight.reshape(-1, 1))
df_temp2['Weight(kg)'] = weight
#Change Normalized Data to List
scaled_df = df_temp2.values.tolist()
scaled_dataframe= pd.DataFrame(df_temp2, columns=['Height(cm)','Weight(kg)',"T_shirt_size"])



#To find the distance between two points
def distance(p1,p2):
    d=math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return d

#The function of finding the k points closest to the target.
def find_neighbor(dataset, target, k):
    distance_list=list()
    for point in dataset:
        d=distance(target, point)
        distance_list.append((point,d))

    #Sort using distance.
    distance_list.sort(key=lambda tup: tup[1])
    neighbor_list=list()

    for i in range(k):
        neighbor_list.append(distance_list[i][0])
    return neighbor_list




#A function that predicts using the values of the neighbors found,
def predict(dataset, target, k):
    #Find nearby k neighborhood data
    neighbor_list=find_neighbor(dataset, target, k)
    print("\nNearest",k,"data")
    for i in neighbor_list:
        print(i)
    output=[]
    for i in neighbor_list:
        output.append(i[-1])
    prediction = max(set(output), key=output.count)
    #Change the pre-diction value to size
    if prediction==0:
        size="M"
    elif prediction==1:
        size="L"
    return size



prediction = predict(scaled_df, scaled_df_temp[-1], 3)
print('\nIt was predicted that a person with \na height {}cm and a weight {}kg would have to wear a T-shirt size {}.'.format(value_to_predict[0],value_to_predict[1],prediction))

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# Uploads data
base_src='./drive/MyDrive'
df = pd.read_csv(base_src+"/mnist_train.csv")
df.head()


# Splitting our dataset into two parts
data=df.values
X=data[:40,1:]
Y=data[:40,0]
X = pd.DataFrame(X)
Y = pd.DataFrame(Y)
print(data.shape)
print(X)
print(Y)

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2)

kfold=KFold(n_splits=5, shuffle=True, random_state=0)

#Visualizing training data
def drawImg(sample):
    img=sample.reshape((28,28))
    plt.imshow(img,cmap='gray')
    plt.show()

# define the parameter values that should be searched
k_range = list(range(1, 10))
p=[1,2]
# create a parameter grid: map the parameter names to the values that should be searched
param_grid = dict(n_neighbors=k_range,p=p)

# instantiate model
knn = KNeighborsClassifier(n_neighbors=5)

#Create new KNN object
knn_2 = KNeighborsClassifier()
#Use GridSearch
grid = GridSearchCV(knn_2, param_grid, cv=10)

pipeline = Pipeline([
    ('knn', KNeighborsClassifier())
])

param_grid = {
    "knn__n_neighbors":range(1,11),
    "knn__p":[1,2]
}

gs = GridSearchCV(pipeline,
                  param_grid=param_grid,
                  cv=5)
#gs.fit(X_train,Y_train)
best_model = grid.fit(X,Y.values.ravel())
#enumerate splits
for train,test in kfold.split(X):
    X_train=X.iloc[train]
    Y_train=Y.iloc[train]
    X_test=X.iloc[test]
    Y_test=Y.iloc[test]
    X_train=X_train.values
    Y_train=Y_train.values
    X_test=X_test.values
    Y_test=Y_test.values
    drawImg(X_train[3])
    #X_test=X_test[:50]   # Taking the first 50 rows from X_test
    #Y_test=Y_test[:50]   # Taking the first 50 rows from Y_test
    base_model=knn.fit(X_train, Y_train)


#calculate_accuracy
print("Label:",base_model.predict(X_test) )
print("Score : ",base_model.score(X_test, Y_test))

#calculate_accuracy
print("Label:",best_model.predict(X_test) )
print("Score : ",best_model.score(X_test, Y_test))
