import pandas as pd
import matplotlib.pyplot as plt
import os


def create_plot():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "..", "data", "raw", "openpowerlifting.csv")

    df = pd.read_csv(file_path, low_memory=False).head(50000)

    df_clean = df[df['Best3SquatKg'] > 0].dropna(subset=['BodyweightKg', 'Best3SquatKg'])

    plt.figure(figsize=(10, 6))
    plt.scatter(df_clean['BodyweightKg'], df_clean['Best3SquatKg'], alpha=0.2, color='red', s=5)
    plt.title('Залежність присідання від власної ваги атлета')
    plt.xlabel('Вага тіла (кг)')
    plt.ylabel('Присідання (кг)')
    plt.grid(True)

    output_path = os.path.join(base_dir, "..", "reports", "figures", "squat_plot.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    print(f"Графік збережено у {output_path}")


if __name__ == "__main__":
    create_plot()