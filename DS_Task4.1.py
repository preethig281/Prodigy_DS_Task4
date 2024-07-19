import pandas as pd
from sqlalchemy import create_engine
import seaborn as s
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
#connection=create_engine(database='edu',host='localhost', user='root', passwd='root')
data= pd.read_csv(r"C:\Users\VENKATESH\OneDrive\Desktop\project\twitter_training.csv")


#data.to_sql('twitter', con=connection, index=False, if_exists='replace')


data= pd.DataFrame(data)


sa=data[data['Company']=='Amazon']


plt.figure(figsize=(9, 7))
crosstab = pd.crosstab(index=data['Company'], columns=data['Opinion'])
s.heatmap(crosstab, cmap = 'jet')
plt.show()


from wordcloud import WordCloud

# Note that topics are the index of crosstab DF
nltk.download('stopwords')
stop = stopwords.words('english')

topic = ' '.join(crosstab.columns)

# topic_list = dataset['Topic'].values.tolist()

wc = WordCloud(stopwords=stop,width=1000, height=500).generate(topic)

plt.imshow(wc, interpolation='bilinear')

"""

s.countplot(x='Opinion', hue='Opinion', data=sa)
plt.show()
"""
for i in data['Company'].unique():
    sa=data[data['Company']==i]
    s.countplot(x='Opinion', hue='Opinion', data=sa)
    
    
    a = int(input('enter 1 to continue to view other companies sentimental graphs \n'))
    
    plt.title(f'Review of {i}')
    plt.xlabel('Review')
    plt.ylabel('count of each reviews')    
    if a==1:
        plt.show()
        plt.close()
    

#s.to_csv('C:\\Users\\Dell\\Desktop\\prodigy_intern\\borderlands.csv')
"""
for i in data['Company'].unique():
    data[data['Company']==i].to_csv(f'C:\Users\VENKATESH\OneDrive\Desktop\project\{i}.csv')
 """