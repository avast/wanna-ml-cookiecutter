# wanna-ml-cookiecutter

cookiecutter template for wanna-ml projects


# How to set up a WANNA ML project

## 1. GCP infrastructure setup

In order to set up a WANNA ML project, one must have the following things:
- group of GCP projects with suffixes per environment (usually `-test`, `-stage`, `-prod`), we call them GCP project bundles
- a bucket with name `wanna-<project_name>-<env>`
- a service account with name `sa-wanna-<project_name>`
- a pubsub notification channel named `ms-teams-wanna-<project name>-topic`

## 2. Bootstrap
Assuming all terraform is done and deployed we can quickly bootstrap a wanna-ml project using cookiecutter and answer a few questions like so:

### Quick python setup

* `pipx` is installed or alternatively you have `cookiecutter` in your `$PATH` 
  * ```pipx install cookiecutter```

### Launch the cutter
```bash
cookiecutter https://github.com/avast/wanna-ml-cookiecutter.git

Project name without wanna- prefix (project_name): genie-ai
project_owner_fullname (Joao Da Silva):
project_owner_email (joao.dasilvacunha@gendigial.com):
project_version (0.0.0):
project_description (Link to project page on Confluence):
gcp_project_id (your-gcp-project-id):
GCP Project bundle without tenant name (wanna):
gcp_region (europe-west1):
gcp_network_name (europe-west1-net):
gcp_subnetwork_name (europe-west1-subnet):
gcp_service_account_name (sa-wanna-genie-ai):
use_jupyter_notebooks [y/n] (y):
```

Or you can use the [wanna init command](https://avast.github.io/wanna-ml/tutorial/pipeline/#initialize-wanna-project)
```bash
wanna init -t https://github.com/avast/wanna-ml-cookiecutter.git --output-dir wanna_awesome
```
which will create a folder `wanna_awesome` with the same content as the `cookiecutter` command above.

You may notice that with few fields we can bootstrap a project, whilst leaving the others to default will do just fine.

* `project_name` does not contain any `wanna` words in it
* `gcp_project_id` the initial `test` gcp project id
* `gcp_project_bundle_name` the gcp project bundle where wanna-ml project will be deployed to. Just the project bundle, not the tenant name.

Once you have completed the cookiecutter you can `cd` to the newly created folder, 
read and run the README.md top down to explore how wanna-ml works and what it can do for you.
