############## SHAP first Round Feature Selection #########################

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score as acc_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.model_selection import train_test_split


#######Now select the top6 features and build a dataframe ###################
X_top6 = X[["bit2419","bit2420","bit2418","bit2421","bit2422","bit2417"]] 

# Create an empty list to store results
results = []

# Define the parameter grid for GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 
    'max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],  
    'min_samples_split': [2, 5, 10, 15, 20], 
    'min_samples_leaf': [1, 2, 4, 6, 8, 10]}

for i in range(15):
    X_train_top6, X_test_top6, y_train, y_test = train_test_split(X_top6, y, test_size=0.2, stratify=y, shuffle=True)
 
    #Build your model (Random Forest Classifier in this case)
    model = RandomForestClassifier()
    
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy')
    
    #Train the model on the scaled training data
    model.fit(X_train_top6, y_train)
    
    #Make predictions on the scaled testing data
    y_pred = model.predict(X_test_top6)
    
    accuracy = accuracy_score(y_test, y_pred)
    print("accuracy:",accuracy)
    conf_matrix = confusion_matrix(y_test, y_pred)
    tp = conf_matrix[1, 1]
    fp = conf_matrix[0, 1]
    fn = conf_matrix[1, 0]
    tn = conf_matrix[0, 0]
    precision = tp / (tp + fp)
    #print("precision", precision)
    recall = tp / (tp + fn)
    #print("recall:", recall)
    specificity= tn/(tn+fp)
    #print("specificity:", specificity)
    f1 = 2 * (precision * recall) / (precision + recall)
    #print("f1:", f1)
    # Append results to the list
    results.append({'Accuracy': accuracy,'Specificity': specificity,'Precision': precision,'Recall': recall,'F1 Score': f1})

#Create DataFrame from the results list
results_df = pd.DataFrame(results)
results_df

results_df.to_csv("sample_pdb/results_first_round.csv")