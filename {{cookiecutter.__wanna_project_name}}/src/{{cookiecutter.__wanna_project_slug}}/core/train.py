import click
{%- if cookiecutter.use_jupyter_notebooks %}
import papermill as pm
{%- endif %}


def train(
    {%- if cookiecutter.use_jupyter_notebooks %}
    notebook_input_path: str,
    notebook_output_path: str,
    {%- endif %}
    train_dataset_path: str,
    test_dataset_path: str,
) -> None:
    {%- if cookiecutter.use_jupyter_notebooks %}
    pm.execute_notebook(
        notebook_input_path,
        notebook_output_path,
        parameters=dict(
            train_dataset_path=train_dataset_path, test_dataset_path=test_dataset_path
        ),
    )
    {%- else %}
    # here implement your training algorithm
    pass
    {%- endif %}


@click.command()
{%- if cookiecutter.use_jupyter_notebooks %}
@click.option("--notebook-input-path", type=str)
@click.option("--notebook-output-path", type=str)
{%- endif %}
@click.option("--train-dataset-path", type=str)
@click.option("--test-dataset-path", type=str)
def train_cli(
    {%- if cookiecutter.use_jupyter_notebooks %}
    notebook_input_path: str,
    notebook_output_path: str,
    {%- endif %}
    train_dataset_path: str,
    test_dataset_path: str,
) -> None:
    {%- if cookiecutter.use_jupyter_notebooks %}
    train(notebook_input_path, notebook_output_path, train_dataset_path, test_dataset_path)
    {%- else %}
    train(train_dataset_path, test_dataset_path)
    {% endif %}


if __name__ == "__main__":
    train_cli()
