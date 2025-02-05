from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics
import pandas as pd

import joblib

df = pd.read_excel('dataset.xlsx')
texts = df['input'].tolist()
labels = df['output'].tolist()

X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

vecterizer = CountVectorizer()
train_vector = vecterizer.fit_transform(X_train)
print(train_vector.shape)
print('shape of Xtrain is', len(X_train))
print('shape of y train is ', len(y_train))

model = make_pipeline(CountVectorizer(ngram_range=(1, 3)), MultinomialNB())

model.fit(X_train, y_train)
joblib.dump(model, 'model.pkl')

