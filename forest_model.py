from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import warnings
warnings.filterwarnings('ignore')
import pickle
import pandas as pd
import numpy as np
import imblearn
from imblearn.over_sampling import SMOTE
smote = SMOTE()

data = pd.read_csv('processed_forestfire_data.csv', index_col=0)
data = np.array(data)
X, y = data[:,:-1],data[:,-1]
X_resample, y_resample = smote.fit_resample(X,y)
print(X_resample.shape)
print(y_resample.shape)
# X = X.astype('int')
# y = y.astype('int')

X_train, X_test,y_train,y_test = train_test_split(X_resample, y_resample, test_size=0.2,random_state=0)

tree = XGBClassifier()
model = BaggingClassifier(base_estimator=tree, n_estimators=40, random_state=0)
model.fit(X_train,y_train)
pickle.dump(model, open('model.pkl','wb'))

