import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

# Set working directory
os.chdir(r'C:\Users\SAMUEL ADJEI\Desktop\Disease Prediction\Disease_Prediction')

def run_model_pipeline(file_path):
    # 1. Load data
    df = pd.read_csv(file_path)
    
    # 2. Pre-processing
    # Impute single missing Gender value with mode
    if df['Gender'].isnull().any():
        df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
    
    # 3. Split data
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    
    # Train: 70%, Val: 15%, Test: 15%
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp)
    
    # 4. Initialize Models
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "SVM": SVC(probability=True, random_state=42)
    }
    
    results = []
    
    plt.figure(figsize=(12, 10))
    
    for name, model in models.items():
        print(f"Training {name}...")
        # Train
        model.fit(X_train, y_train)
        
        # Predict
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]
        
        # Metrics
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_prob)
        
        results.append({
            "Model": name,
            "Accuracy": acc,
            "Precision": prec,
            "Recall": rec,
            "F1": f1,
            "AUC": auc
        })
        
        # ROC Curve
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        plt.plot(fpr, tpr, label=f'{name} (AUC = {auc:.3f})')
        
        # Save model
        joblib.dump(model, f'{name.replace(" ", "_").lower()}_model.pkl')
        
    # Finalize ROC plot
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves - All Models')
    plt.legend()
    plt.savefig('roc_curves_all.png')
    plt.close()
    
    # 5. Save Results
    results_df = pd.DataFrame(results)
    results_df.to_csv('model_results_all.csv', index=False)
    
    # Save a nice summary text
    with open('model_summary_all.txt', 'w') as f:
        f.write("Model Performance Summary (All Models)\n")
        f.write("======================================\n")
        f.write(results_df.to_string())
        
        for name in models:
            f.write(f"\n\nConfusion Matrix ({name}):\n")
            cm = confusion_matrix(y_test, models[name].predict(X_test))
            f.write(str(cm))

    print("Model development and evaluation (all models) completed. Files generated: model_results_all.csv, model_summary_all.txt, roc_curves_all.png")

if __name__ == "__main__":
    run_model_pipeline('clean_diabetes_dataset.csv')
