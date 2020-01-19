
import sklearn.datasets as skd

categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
news_train = skd.load_files('\\Users\\Neelima\\Desktop\\Fetch20newsgroup\\train\\', categories= categories, encoding= 'ISO-8859-1')
news_test = skd.load_files('\\Users\\Neelima\\Desktop\\Fetch20newsgroup\\test\\', categories= categories, encoding= 'ISO-8859-1')


from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

text_clf = Pipeline([('vect', TfidfVectorizer()),('clf', SGDClassifier(loss='hinge', penalty='l2',
                                                                       alpha=1e-3, random_state=52,
                                                                       max_iter=10, tol=None)),
                    ])



text_clf.fit(news_train.data, news_train.target)


predicted = text_clf.predict(news_test.data)

from sklearn import metrics
from sklearn.metrics import accuracy_score

def output():

output=print("Accuracy is :", accuracy_score(news_test.target, predicted))
def output1()
output1 =print(metrics.classification_report(news_test.target, predicted, target_names=news_test.target_names)),
metrics.confusion_matrix(news_test.target, predicted)
