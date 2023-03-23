import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

import operator

from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score, accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, log_loss
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.model_selection import cross_val_score, cross_validate, StratifiedKFold
from sklearn.metrics import precision_recall_curve, precision_score, recall_score, f1_score, accuracy_score
from sklearn.metrics import roc_curve, auc, roc_auc_score, confusion_matrix, classification_report

/*
Добрый день! Есть комплекс искусственных нейронных сетей. В одном файле. В основе его работы заложены 5 методов:
1. Random Forest (RF);
2. k Nearest Neighbor (KNN);
3. Logical regression (LogReg);
4. Implement Multilayer Perceptron (MLP);
5. Support Vector Machines» (SVM).

Необходимо составить объединенную структурную схему комплекса нейронных сетей.
К каждой сети составить структурную схему. 1 метод - 1 сеть.
По всем сетям составить UML-диаграммы:
1. последовательностей;
2. состояний;
3. классов;
4. деятельности.

Ко всем схемам и диаграммам подготовить описание.
Всего 26 схем и диаграмм.

26 это 20 uml-диаграмм и 6 структурных схем (общая и по каждой сети),
Пусть будет бесплатная программа. 
Ссылка на нее также должна быть. 
Чтобы я могла смотреть схемы в программе. 
Схемы и UML-диаграммы сохраняйте и в виде файла программы, и в виде рисунка, например, png.
*/ 

df = pd.read_csv('1.csv', sep=';')          #Считываем файл как таблицу данных с разделением [;] 

y = df['Number_User']                       #y - data frame содержащий   

X = df.drop(['Number_User'], axis = 1)      #удаление верхней строки (в которой метаданные типа frequency, amplityda и т.д.

X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y,
                                                    random_state=1, 
                                                    test_size=0.2)
scaler = StandardScaler()
scaler.fit(X_train)                         #   
X_train = scaler.transform(X_train)         # 
X_test = scaler.transform(X_test)           # 

from sklearn.metrics import f1_score, accuracy_score, classification_report, confusion_matrix

def sk_evaluate(model, features, labels):   #
    y_pred = model.predict(features)        #
    y_true = labels                         # 
    
    print('Score on dataset...\n')
    print('Confusion Matrix:\n', confusion_matrix(y_true, y_pred))
    print('\nClassification Report:\n', classification_report(y_true, y_pred))
    print('\naccuracy: {:.3f}'.format(accuracy_score(y_true, y_pred)))
    print('f1 score: {:.3f}'.format(f1_score(y_true, y_pred, average='weighted')))

    return y_pred, y_true
    
# define several lists and dataframe to store the CV results and evaluation results on testing data
model_names_list = []
cv_fit_time_mean_list = []
cv_accuracy_mean_list = []
cv_precision_mean_list = []
cv_recall_mean_list = []
cv_f1_mean_list = []

test_accuracy_list = []
test_precision_list = []
test_recall_list = []
test_f1_list = []
model_names = ['SVM','LogReg', 'KNN', 'RF', 'MLP']

def train_model(X_train,
                y_train,
                X_test, 
                y_test):
    
    parameters = [
        {
            'clf__estimator': [SGDClassifier(n_jobs=-1, tol=1e-3)], # SVM 
            'clf__loss': ['hinge', 'modified_huber'],
            'clf__max_iter': (10, 100, 1000),
            'clf__alpha': np.logspace(0.00001, 0.1, 4),
            'clf__learning_rate': ['optimal', 'invscaling'],
            'clf__eta0': np.logspace(0.00001, 1, 4),
            'clf__penalty': ['l1', 'l2', 'elasticnet'],
        },
        {
            'clf__estimator': [SGDClassifier(n_jobs=-1, tol=1e-3)], # LogReg
            'clf__loss': ['log'],
            'clf__max_iter': [10, 100, 1000],
            'clf__alpha': np.logspace(0.00001, 0.1, 4),
            'clf__learning_rate': ['optimal', 'invscaling'],
            'clf__eta0': np.logspace(0.00001, 1, 4),
            'clf__penalty': ['l1', 'l2', 'elasticnet'],
        },
        {
            'clf__estimator': [KNeighborsClassifier(n_jobs = -1)], # KNN
            'clf__n_neighbors': [3, 5, 7, 9, 15, 31],
            'clf__weights': ['uniform', 'distance'],
        },
        {
            'clf__estimator': [RandomForestClassifier(n_jobs = -1)], # Random Forest
            'clf__n_estimators': [10, 100, 250, 500, 1000],
            'clf__max_depth': [None, 3, 7, 15],
            'clf__min_samples_split': [2, 5, 15],
        },
        {
            'clf__estimator': [MLPClassifier(max_iter=5000)], # MLP
            'clf__hidden_layer_sizes': [(10,), (10, 30, 10), (20,)],
            'clf__activation': ['tanh', 'relu'],
            'clf__solver': ['sgd', 'adam'],
            'clf__alpha': [0.0001, 0.05],
            'clf__learning_rate': ['constant', 'adaptive'],
        },
    ]
    
    result=[]
    for model_name, params in zip(model_names, parameters):

        #classifier
        clf = params['clf__estimator'][0]

        #getting arguments by
        #popping out classifier
        params.pop('clf__estimator')
        
        print(f'{clf}')

        #pipeline
        pipeline = Pipeline([ 
            ('clf', clf),
        ])
        
        # find the best parameters 
        grid_search = GridSearchCV(pipeline, 
                                   param_grid=params, 
                                   scoring='f1_macro', 
                                   n_jobs=-1,
                                   cv=5,
                                   verbose=10)

        grid_search.fit(X_train, y_train)
        
        print('Best score: %0.3f' % grid_search.best_score_)
        print('Best parameters set:')
        best_parameters = grid_search.best_estimator_.get_params()
        for param_name in sorted(params.keys()):
            print('\t%s: %r' % (param_name, best_parameters[param_name]))

        print('Train score:')
        sk_evaluate(grid_search, X_train, y_train)

        print('Test score:')
        sk_evaluate(grid_search, X_test, y_test)

        #storing result
        result.append({
                'grid': grid_search,
                'classifier': grid_search.best_estimator_,
                'best score': grid_search.best_score_,
                'best params': grid_search.best_params_,
                'cv': grid_search.cv})
        
        
        # ==== Step 1: Cross-validation =====
        # define  Stratified 5-fold cross-validator
        cv = StratifiedKFold(n_splits=5, 
                             shuffle=True, 
                             random_state=42)

        # define metrics for evaluating
        scoring = ['accuracy', 'precision_micro', 'recall_micro', 'f1_micro']

        # perform the 5-fold CV and get the metrics results
        cv_results = cross_validate(estimator=clf,
                                    X=X_train,
                                    y=y_train,
                                    scoring=scoring,
                                    cv=cv,
                                    return_train_score=False)  # prevent to show the train scores on cv splits.

        # calculate the mean values of those scores
        cv_fit_time_mean = cv_results['fit_time'].mean()
        cv_accuracy_mean = cv_results['test_accuracy'].mean()
        cv_precision_mean = cv_results['test_precision_micro'].mean()
        cv_recall_mean = cv_results['test_recall_micro'].mean()
        cv_f1_mean = cv_results['test_f1_micro'].mean()

        # store CV results into those lists
        model_names_list.append(model_name)
        cv_fit_time_mean_list.append(cv_fit_time_mean)
        cv_accuracy_mean_list.append(cv_accuracy_mean)
        cv_precision_mean_list.append(cv_precision_mean)
        cv_recall_mean_list.append(cv_recall_mean)
        cv_f1_mean_list.append(cv_f1_mean)

        # ==== Step 2: Evaluation on Testing data =====

        # fit model
        clf.fit(X=X_train, y=y_train)

        # predition on testing data

        # predicted label or class
        y_pred_class = clf.predict(X=X_test)  

        # predicted probability of the label 1
        # y_pred_score = clf.predict_proba(X=X_test)[:, 1]

        # accuracy
        accuracy_ontest = accuracy_score(y_true=y_test, y_pred=y_pred_class)

        # precision score
        precision_ontest = precision_score(y_true=y_test, y_pred=y_pred_class, average = 'micro')

        # recall score
        recall_ontest = recall_score(y_true=y_test, y_pred=y_pred_class, average = 'micro')

        # F1 score
        f1_ontest = f1_score(y_true=y_test, y_pred=y_pred_class, average = 'micro')


        # store the above values
        test_accuracy_list.append(accuracy_ontest)
        test_precision_list.append(precision_ontest)
        test_recall_list.append(recall_ontest)
        test_f1_list.append(f1_ontest)


    #sorting result by best score
    result = sorted(result, key=operator.itemgetter('best score'),reverse=True)
    
    return result
best_clf = train_model(X_train, y_train, X_test, y_test)

results_dict1 = {'Model Name': model_names_list,
                'CV Fit Time': cv_fit_time_mean_list,
                'CV Accuracy mean': cv_accuracy_mean_list,
                'CV Precision mean': cv_precision_mean_list,
                'CV Recall mean': cv_recall_mean_list,
                'CV F1 mean': cv_f1_mean_list,
                'Test Accuracy': test_accuracy_list,
                'Test Precision': test_precision_list,
                'Test Recall': test_recall_list,
                'Test F1': test_f1_list,
                }

results1_df = pd.DataFrame(results_dict1)

# sort the results according to F1 score on testing data
results1_df.sort_values(by='Test F1', ascending=False)

Model   Name	CV Fit Time	    CV Accuracy mean    CV Precision mean	CV Recall mean	    CV F1 mean	    Test Accuracy	Test Precision	Test Recall	    Test F1
3	    RF	    0.060803	    0.898574	        0.898574	        0.898574	        0.898574	    0.904762	    0.904762	    0.904762	    0.904762
2	    KNN	    0.000201	    0.797861	        0.797861	        0.797861	        0.797861	    0.880952	    0.880952	    0.880952	    0.880952
1	    LogReg	0.006200	    0.755080	        0.755080	        0.755080	        0.755080	    0.857143	    0.857143	    0.857143	    0.857143
4	    MLP	    0.315208	    0.899109	        0.899109	        0.899109	        0.899109	    0.833333	    0.833333	    0.833333	    0.833333
0	    SVM	    0.005000	    0.767558	        0.767558	        0.767558	        0.767558	    0.761905	    0.761905	    0.761905	    0.761905
 
