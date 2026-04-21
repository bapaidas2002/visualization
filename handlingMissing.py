import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Desktop\git\python\DMV\salary.csv")

print("--- Missing Values Before ---")
print(df.isnull().sum())

df = df.fillna(df.mean(numeric_only=True))

print("\n--- Cleaned Data ---")
print(df.to_string())
print(df.mean())