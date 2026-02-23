import pandas as pd
import os


def analyze_powerlifting():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "..", "data", "raw", "openpowerlifting.csv")

    df = pd.read_csv(file_path)

    correlation = df['BodyweightKg'].corr(df['Best3SquatKg'])

    print(f"Гіпотеза 1: Кореляція між масою тіла та силою в присіданнях: {correlation:.2f}")

    gender_bench = df.groupby('Sex')['Best3BenchKg'].mean()
    print("\nСередній жим за статтю:")
    print(gender_bench)


if __name__ == "__main__":
    analyze_powerlifting()