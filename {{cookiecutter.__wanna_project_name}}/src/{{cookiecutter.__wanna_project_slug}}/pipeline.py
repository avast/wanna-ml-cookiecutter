from kfp.v2 import dsl

from . import config as cfg
from .core.components import (
    data_op,
    on_exit_op,
    train_op,
)


@dsl.pipeline(
    # A name for the pipeline. Use to determine the pipeline Context.
    name=cfg.PIPELINE_NAME,
    pipeline_root=cfg.PIPELINE_ROOT,
)
def {{cookiecutter.__wanna_project_slug}}_pipeline(
    {%- if cookiecutter.use_jupyter_notebooks %}train_notebook_input_path: str, train_notebook_output_path: str{% endif %}
) -> None:
    # ===================================================================
    # Get pipeline result notification
    # ===================================================================
    # collect datasets provided by sklearn
    exit_task = on_exit_op().set_display_name("On Exit Dummy Task").set_caching_options(False)

    with dsl.ExitHandler(exit_task):
        # ===================================================================
        # collect datasets
        # ===================================================================
        # collect datasets provided by sklearn
        data_task = data_op()

        # ===================================================================
        # train model
        # ===================================================================
        # simple model training directly in component
        _ = train_op(
            {%- if cookiecutter.use_jupyter_notebooks %}
            notebook_input_path=train_notebook_input_path,
            notebook_output_path=train_notebook_output_path,
            {%- endif %}
            train_dataset_path=data_task.outputs["dataset_train"],
            test_dataset_path=data_task.outputs["dataset_test"],
        )
