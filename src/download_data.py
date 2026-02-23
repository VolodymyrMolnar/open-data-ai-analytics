import kagglehub
import pandas as pd
import os


def load_data():
    print("Завантаження датасету з Kaggle...")
    path = kagglehub.dataset_download("open-powerlifting/powerlifting-database")

    source_file = os.path.join(path, "openpowerlifting.csv")

    target_folder = os.path.join("data", "raw")
    target_file = os.path.join(target_folder, "openpowerlifting.csv")

    os.makedirs(target_folder, exist_ok=True)

    print("Обробка великого файлу ...")
    df = pd.read_csv(source_file, nrows=100000)

    df.to_csv(target_file, index=False)
    print(f"Файл збережено у: {target_file}")
    print(df.head())


if __name__ == "__main__":
    load_data()