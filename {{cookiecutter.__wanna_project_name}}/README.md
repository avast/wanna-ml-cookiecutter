# {{ cookiecutter.project_name }} wanna project

## Environment Setup

Before you start, make sure you have your interpreter set to Python 3.10.

### On MacOS using pyenv

Prepare the base environment
```bash
# Install & setup pyenv
brew install pyenv && pyenv init

# Setup a python 3.10 env, currently wanna-ml is limited to python 3.10
pyenv install 3.10 && pyenv local 3.10

# Install wanna-ml via pipx
pip install pipx
```

or see https://pipx.pypa.io/stable/installation/ for other ways to install it

setup the environment variables

```bash
# set default wanna profile for shorter cli commands
# aka no need to allways pass the --profile <project_name>-test to all commands
export WANNA_GCP_PROFILE_NAME={{cookiecutter.gcp_project_bundle_name}}-test

# Disable GCP remote validations faster wanna-ml loading
# Validations such as checking VM name, VM sizes, GPU names and so on are disabled
export WANNA_GCP_ENABLE_REMOTE_VALIDATION=false
```

### On Windows using conda

```shell
conda create -n {{cookiecutter.__wanna_project_name}} python=3.10.14
conda activate {{cookiecutter.__wanna_project_name}}

# Install pipx
scoop install pipx

$env:WANNA_GCP_PROFILE_NAME="{{cookiecutter.gcp_project_bundle_name}}-test"
# Disable GCP remote validations for faster wanna-ml loading
# Validations such as checking VM name, VM sizes, GPU names and so on are disabled
$env:WANNA_GCP_ENABLE_REMOTE_VALIDATION="false"
```

### shared setup

```shell
pipx install poetry==1.8.3

# Install all dependencies from pyproject.toml including your project to a poetry managed virtual env
poetry shell && poetry install

# Setup GCP credentials when working from  workstation
gcloud auth login

# Setup GCP credentials when working from  workstation
gcloud auth application-default login

# Setup the region docker registry
gcloud auth configure-docker europe-west1-docker.pkg.dev

# Set the billing project
gcloud config set project {{cookiecutter.gcp_project_id}} 
gcloud auth application-default set-quota-project {{cookiecutter.gcp_project_id}} 

# set default wanna profile for shorter cli commands
# aka no need to allways pass the --profile <project_name>-test to all commands
export WANNA_GCP_PROFILE_NAME={{cookiecutter.gcp_project_bundle_name}}-test

# Disable GCP remote validations faster wanna-ml loading
# Validations such as checking VM name, VM sizes, GPU names and so on are disabled
export WANNA_GCP_ENABLE_REMOTE_VALIDATION=false

# Create some local dir for quick data
mkdir -p data/local

# Format code
poetry run poe format-code

# Run tests
poetry run pytest
```

### Turning off the tabular rich stack trace

on unix:
```powershell
export _TYPER_STANDARD_TRACEBACK=1
```
on windows:
```powershell
$env:_TYPER_STANDARD_TRACEBACK=1
```

see https://typer.tiangolo.com/tutorial/exceptions/#disable-pretty-exceptions for more info

## Create Vertex AI Notebooks

### User managed notebooks

User managed notebooks are under our control and are way cheaper than the Google managed one. A caveat is that we can't assign it to a Google VPC with access to internet, which in for huggingface cases is a nice to have for experimentation on new models.

`wanna notebook create --name {{cookiecutter.__wanna_project_name}}`

Once you land in the JupyterLab UI you can open a terminal and run `sh /app/bin/workbench-setup.sh`.

This will copy some datasets to local disk and symlink the src to your home.

#### Notebook VM SSH && remote Jupyter

To simply ssh into the VM run `wanna notebook ssh --name {{cookiecutter.__wanna_project_name}}`.
After running this command, you will be prompted to enter a passphrase – do not fill in anything and just press "enter".

For remote Jupyter development run `wanna notebook ssh --background --name {{cookiecutter.__wanna_project_name}}` and then visit `http://localhost:8080/lab` to access the UI.

For integration via editors check the info in [wanna-ml docs](https://avast.github.io/wanna-ml/tutorial/notebook/#connecting-with-vscode).

## Running tasks locally
To check local environment is correct and all is fine and dandy

Since all src and dependencies are managed by poetry project one can actually run any module locally.
Same applies to pytest and jupyter notebooks.

```bash 
# Prepare data
python -m {{cookiecutter.__wanna_project_slug}}.core.data \
  --train-dataset-path data/local/train \
  --test-dataset-path data/local/test

# Train model from a notebook
python -m {{cookiecutter.__wanna_project_slug}}.core.train \
  --notebook-input-path notebooks/train.ipynb \
  --notebook-output-path data/local/train-out.ipynb \
  --train-dataset-path data/local/train \
  --test-dataset-path data/local/test
```

## Run WANNA custom job in Vertex AI

If you need to run a larger job as part of an experiment or development and don't want to have a Jupyter Notebook running all the time nor want to run it from your local workstation.
For this use cases we can use [Vertex AI custom jobs](https://cloud.google.com/vertex-ai/docs/training/create-custom-job).

This is rather useful as to run your code changes in same environment (container, hardware) as a pipeline task would.

`wanna job --help`  has got you [covered](https://avast.github.io/wanna-ml/tutorial/job/).

Jobs are defined in `wanna.yaml` and allow you to override its arguments from the CLI. 

This project provides a generic job that will allow you to run any python module.

```bash
# Prepare data using Vertex AI Custom jobs
wanna job run --name {{cookiecutter.__wanna_project_name}} python -m {{cookiecutter.__wanna_project_slug}}.core.data \
  --train-dataset-path data/local/train \
  --test-dataset-path data/local/test

# Train model using Vertex AI Custom jobs via Notebok
wanna job run --name {{cookiecutter.__wanna_project_name}} python -m {{cookiecutter.__wanna_project_slug}}.core.train \
  --notebook-input-path notebooks/train.ipynb \
  --notebook-output-path data/notebook-output.ipynb \
  --train-dataset-path data/local/train \
  --test-dataset-path data/local/test
```

## Run WANNA ML Pipeline in Vertex AI
Once you have verified you training is working as expected you can run the Vertex AI pipeline.

```bash 
# Build Vertex AI Pipeline locally without building container, just to validate Kubeflow IO / stages
wanna pipeline build --name {{cookiecutter.__wanna_project_name}} --mode quick

# Build Vertex AI Pipeline locally including containers via cloud build
wanna pipeline build --name {{cookiecutter.__wanna_project_name}}

# Run Vertex AI Pipeline on GCP directly from your local machine based on wanna.yaml
wanna pipeline run --name {{cookiecutter.__wanna_project_name}} --params params/params.test.yaml

# Build & Publish Docker containers as well as pipeline manifests to GCP
wanna pipeline push --name {{cookiecutter.__wanna_project_name}} --params params/params.test.yaml

# Deploy pipeline so that scheduling and monitoring is setup
wanna pipeline deploy --name {{cookiecutter.__wanna_project_name}} --env test

# Run Vertex AI versioned Pipeline based on a wanna-manifest.json and one can change params for multiple (re)runs
wanna pipeline run-manifest \
  --manifest gs://{{cookiecutter.__wanna_project_name}}-test/wanna-pipelines/{{cookiecutter.__wanna_project_name}}/deployment/dev/manifests/wanna-manifest.json \
  --params params/params.test.yaml
```
