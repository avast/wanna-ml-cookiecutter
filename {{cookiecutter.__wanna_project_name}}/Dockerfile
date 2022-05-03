FROM gcr.io/deeplearning-platform-release/workbench-container:latest

# Basic conda setup for compatability with Vertex AI
LABEL maintainer="joao.dasilvacunha@gendigital.com"

ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    POETRY_VIRTUALENVS_CREATE=false

RUN mamba create --override-channels \
    -c https://your.conda.repo.example.com/conda-forge/ \
    -n {{cookiecutter.__wanna_project_name}} python=3.10 \
    -y && mamba config --set auto_activate_base false

RUN ${DL_ANACONDA_HOME}/envs/{{cookiecutter.__wanna_project_name}}/bin/python -m pip install "poetry==1.8.3"

# Install project related deps
WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN ${DL_ANACONDA_HOME}/envs/{{cookiecutter.__wanna_project_name}}/bin/python -m poetry install --only main --no-root
{%- if cookiecutter.use_jupyter_notebooks %}
RUN ${DL_ANACONDA_HOME}/envs/{{cookiecutter.__wanna_project_name}}/bin/python -m ipykernel install --user --name {{cookiecutter.__wanna_project_name}} \
    && echo '. /app/bin/kernel.sh' >> ~/.bashrc
{%- endif %}

COPY . .

RUN ${DL_ANACONDA_HOME}/envs/{{cookiecutter.__wanna_project_name}}/bin/python -m poetry install --only-root

ENV PATH="${DL_ANACONDA_HOME}/envs/{{cookiecutter.__wanna_project_name}}/bin:$PATH"
