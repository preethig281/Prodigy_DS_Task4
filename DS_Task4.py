import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import re
import seaborn as s 
import matplotlib.pyplot as plt

from textblob import TextBlob
data= pd.read_csv(r"C:\Users\VENKATESH\OneDrive\Desktop\project\twitter_training.csv")
data=pd.DataFrame(data)
#data=data.head(2000)
port = PorterStemmer()
def sx(con):
    a=re.sub('[^a-zA-Z]',' ', str(con))
    a=a.lower()
    a=a.split()
    a=[port.stem(x) for x in a if not x in stopwords.words('english')]
    a = ' '.join(a)
    return a 


data['Polarity']= data['Review'].apply(sx)
        
print(data.columns)


"""
for  i in data['Review']:
    a=re.sub('[^a-zA-Z]','', data['Review'])
    a=a.lower()
    a=a.split()
    a=[port.stem(x) for x in a if not x in stopwords.words('english')]
    a = ' '.join(a)
    data['Polarity']=a
 """   

def polarized_data(d):
    polarity1=TextBlob(d)
    if polarity1.sentiment.polarity>0:
        return 'positive'
    if polarity1.sentiment.polarity<0:
        return 'negative'
    else:
        return 'neutral'


data['polarized_data']=data['Polarity'].apply(polarized_data) 
"""
s.barplot(x='Company',y='polarized_data', hue='Company', data=data, width=0.1)
plt.show()
"""
