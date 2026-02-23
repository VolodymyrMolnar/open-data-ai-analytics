import pandas as pd

def check_quality():
    df = pd.read_csv("../data/raw/openpowerlifting.csv")
    print("--- Перевірка на пропуски ---")
    print(df.isnull().sum())
    print("\n--- Типи даних ---")
    print(df.dtypes)

if __name__ == "__main__":
    check_quality()