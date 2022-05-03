from kfp.dsl import Dataset, Input, Output
from kfp.v2.dsl import component

from .. import config as cfg


@component(base_image=cfg.DATA_IMAGE_URI)
def data_op(dataset_train: Output[Dataset], dataset_test: Output[Dataset]) -> None:
    from {{cookiecutter.__wanna_project_slug}}.core.data import get_data

    get_data(dataset_train.path, dataset_test.path)


@component(base_image=cfg.DATA_IMAGE_URI)
def train_op(
    {%- if cookiecutter.use_jupyter_notebooks %}
    notebook_input_path: str,
    notebook_output_path: str,
    {%- endif %}
    train_dataset_path: Input[Dataset],
    test_dataset_path: Input[Dataset],
) -> None:
    from {{cookiecutter.__wanna_project_slug}}.core.train import train

    train(
        {% if cookiecutter.use_jupyter_notebooks %}notebook_input_path, notebook_output_path, {% endif %}train_dataset_path.path, test_dataset_path.path
    )


@component(base_image=cfg.DATA_IMAGE_URI)
def on_exit_op() -> None:
    import logging

    logging.getLogger().setLevel(logging.INFO)
    logging.info("This Component will run on exit")
