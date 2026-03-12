import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Set working directory to the project folder
os.chdir(r'C:\Users\SAMUEL ADJEI\Desktop\Disease Prediction\Disease_Prediction')

def perform_eda(file_path):
    df = pd.read_csv(file_path)
    
    # Basic info
    info_str = f"Shape: {df.shape}\n"
    info_str += f"Columns: {list(df.columns)}\n"
    info_str += f"Missing Values:\n{df.isnull().sum()}\n"
    info_str += f"Target Distribution (Outcome):\n{df['Outcome'].value_counts(normalize=True)}\n"
    
    with open('eda_stats.txt', 'w') as f:
        f.write(info_str)
        f.write("\nHead:\n")
        f.write(df.head().to_string())
        f.write("\nDescription:\n")
        f.write(df.describe().to_string())

    # Correlations
    plt.figure(figsize=(12, 10))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Feature Correlation Heatmap')
    plt.savefig('correlation_heatmap.png')
    plt.close()

    # Feature distributions
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    plt.figure(figsize=(15, 10))
    df[num_cols].hist(bins=20, figsize=(15, 10))
    plt.suptitle('Feature Distributions')
    plt.savefig('feature_distributions.png')
    plt.close()

    print("EDA completed successfully. Files generated: eda_stats.txt, correlation_heatmap.png, feature_distributions.png")

if __name__ == "__main__":
    perform_eda('clean_diabetes_dataset.csv')
