################################ SHAP first round  ####################### 

import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# Load your dataset
dataa = pd.read_csv('vector_cas_first_round.csv', low_memory=False)
data1 = dataa.iloc[3:, 0:]
Xa = data1.drop('bits', axis = 1)
X = Xa.drop('label', axis = 1)
y = Xa['label']

# Initialize an empty DataFrame to store the SHAP values
SHAP_df = pd.DataFrame()

# Number of splits you want to perform
num_splits =15  # Adjust this number as needed
for i in range(num_splits):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, shuffle=True)
    
    print(f"Split number: {i+1}")

    # Train a Random Forest classifier for each split
    rf_model = RandomForestClassifier(n_estimators = 500)
    rf_model.fit(X_train, y_train)
    
    # Calculate SHAP values using SHAP explainer for the current split
    explainer = shap.TreeExplainer(rf_model)
    shap_values = explainer.shap_values(X_train)

    feature_names = X_train.columns

    # Calculate mean absolute SHAP values for each feature
    mean_abs_shap_values = np.mean(np.abs(shap_values), axis=(0, 1))

    # Put it in a dataframe
    shap_df = pd.DataFrame({'Feature': feature_names, 'Split_{}_mean_abs_shap_values'.format(i+1): mean_abs_shap_values})

    # Concatenate the current shap_df to SHAP_df
    SHAP_df = pd.concat([SHAP_df, shap_df.set_index('Feature')], axis=1)

# Calculate average importance across all runs and add it as the last column
SHAP_df['Average_Mean_Absolute_SHAP'] = SHAP_df.mean(axis=1)

# Sort the DataFrame based on mean SHAP from highest to lowest
SHAP_df.to_csv("Aggregated_SHAP.csv")
