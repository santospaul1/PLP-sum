import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set a clean plotting style for aesthetics
sns.set_style("whitegrid")

def run_data_analysis():
    """
    Performs data loading, cleaning, analysis, and visualization on the Iris dataset,
    demonstrating error handling and adherence to all task requirements.
    """
    print("--- 📚 Task 1: Data Loading, Inspection, and Cleaning ---")
    
    try:
        # Load the Iris dataset using sklearn (an alternative to file reading)
        iris_data = load_iris(as_frame=True)
        df = iris_data.frame
        
        # Rename columns for simplicity and readability
        df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
        
        # Map species codes to names
        df['species'] = df['species'].map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})
        
        print("\n[1.1] First 5 Rows (Inspection):")
        print(df.head())
        
        print("\n[1.2] Data Structure (Dtypes and Non-Null Counts):")
        df.info()
        
        # Check for missing values (Cleaning Step)
        print("\n[1.3] Missing Value Check:")
        missing_values = df.isnull().sum()
        print(missing_values)
        
        # In the (clean) Iris dataset, there are no missing values.
        # If there were, we would use:
        # df = df.dropna()  # To drop rows with missing data
        # df['column'].fillna(df['column'].mean(), inplace=True) # To fill with mean
        if missing_values.sum() == 0:
            print("\n✅ Dataset is clean (no missing values detected). Cleaning skipped.")
        
    except ImportError as e:
        print(f"🚨 CRITICAL ERROR: Required library not found. Please install: {e.name}")
        return
    except Exception as e:
        print(f"❌ ERROR during data loading/cleaning: {e}")
        return
        
    print("\n\n--- 🔬 Task 2: Basic Data Analysis ---")

    # [2.1] Compute basic statistics for numerical columns
    print("\n[2.1] Descriptive Statistics of Numerical Columns:")
    print(df[['sepal_length', 'petal_length', 'petal_width']].describe())
    
    # [2.2] Perform groupings (Mean of a numerical column per categorical group)
    grouped_stats = df.groupby('species')['petal_length'].mean().sort_values(ascending=False)
    
    print("\n[2.2] Average Petal Length Grouped by Species:")
    print(grouped_stats)

    # [2.3] Identify patterns or interesting findings
    print("\n[2.3] Key Findings:")
    print(" - The 'describe()' output shows a clear difference in scale: petal length and width have smaller mean values than sepal length and width.")
    print(f" - The mean petal length across species varies significantly, from {grouped_stats.min():.2f} (Setosa) to {grouped_stats.max():.2f} (Virginica).")
    print(" - This strong separation suggests 'petal length' is an excellent feature for classifying the different Iris species.")
    
    
    print("\n\n--- 📈 Task 3: Data Visualization ---")
    
    # Set up a figure and subplots (2 rows, 2 columns)
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Iris Dataset Exploratory Data Analysis (EDA)', fontsize=20, y=1.02)
    
    # --- Plot 1: Bar Chart (Comparison Across Categories) ---
    axes[0, 0].set_title('Comparison of Average Petal Length by Species', fontsize=14)
    sns.barplot(x=grouped_stats.index, y=grouped_stats.values, ax=axes[0, 0], palette="viridis")
    axes[0, 0].set_xlabel("Species")
    axes[0, 0].set_ylabel("Average Petal Length (cm)")
    axes[0, 0].tick_params(axis='x', rotation=15)
    
    # --- Plot 2: Histogram (Distribution) ---
    axes[0, 1].set_title('Distribution of Sepal Length', fontsize=14)
    sns.histplot(df['sepal_length'], kde=True, bins=15, color='skyblue', ax=axes[0, 1])
    axes[0, 1].set_xlabel("Sepal Length (cm)")
    axes[0, 1].set_ylabel("Frequency")
    
    # --- Plot 3: Scatter Plot (Relationship between two numerical columns) ---
    axes[1, 0].set_title('Relationship: Sepal Length vs. Petal Length (by Species)', fontsize=14)
    # Use seaborn scatterplot for easy categorical coloring
    sns.scatterplot(
        x='sepal_length', 
        y='petal_length', 
        hue='species', 
        data=df, 
        s=100, # Size of points
        palette='tab10', 
        ax=axes[1, 0]
    )
    axes[1, 0].set_xlabel("Sepal Length (cm)")
    axes[1, 0].set_ylabel("Petal Length (cm)")
    axes[1, 0].legend(title='Species')
    
    # --- Plot 4: Line Chart (Trend over Index/Time Proxy) ---
    # Since Iris is not time-series data, we use the sample index (row number) as a proxy
    # for 'time' to show a trend. We plot the cumulative mean of Petal Length.
    df['cumulative_mean_petal'] = df['petal_length'].expanding().mean()
    axes[1, 1].set_title('Cumulative Mean Petal Length Over Sample Index (Trend)', fontsize=14)
    sns.lineplot(
        x=df.index, 
        y=df['cumulative_mean_petal'], 
        color='red', 
        linewidth=2.5, 
        ax=axes[1, 1]
    )
    axes[1, 1].set_xlabel("Sample Index (Time Proxy)")
    axes[1, 1].set_ylabel("Cumulative Mean Petal Length (cm)")
    
    # Adjust layout to prevent overlap and display the plot
    plt.tight_layout(rect=[0, 0, 1, 0.98])
    plt.show()

if __name__ == "__main__":
    run_data_analysis()
