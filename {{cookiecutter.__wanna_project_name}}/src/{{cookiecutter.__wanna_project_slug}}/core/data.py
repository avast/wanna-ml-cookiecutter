import click
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split as tts


def get_data(dataset_train_path: str, dataset_test_path: str) -> None:
    data_raw = datasets.load_breast_cancer()
    data = pd.DataFrame(data_raw.data, columns=data_raw.feature_names)
    data["target"] = data_raw.target

    train, test = tts(data, test_size=0.3)

    train.to_csv(dataset_train_path)
    test.to_csv(dataset_test_path)


@click.command()
@click.option("--train-dataset-path", type=str)
@click.option("--test-dataset-path", type=str)
def get_data_cli(train_dataset_path: str, test_dataset_path: str) -> None:
    get_data(train_dataset_path, test_dataset_path)


if __name__ == "__main__":
    get_data_cli()
