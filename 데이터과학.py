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