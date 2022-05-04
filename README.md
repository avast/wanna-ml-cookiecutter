# wanna-ml-cookiecutter

cookiecutter template for wanna-ml projects

## Get started

Ensure Avasts' pypi repositories are enabled. 
Add to `~/.pip/.pip.conf`
```
[global]
index-url=https://artifactory.ida.avast.com/artifactory/api/pypi/pypi-remote/simple
extra-index-url = https://artifactory.ida.avast.com/artifactory/api/pypi/pypi-local/simple
```


# Install 

```
pip install cookiecutter wanna
```

# Launch to cutter
```
wanna init
```
or without wanna, manually
```
cookiecutter https://git.int.avast.com/bds/wanna-ml-cookiecutter
```

# Answer the following question, values will be used to in your wanna-ml config

```
project_name [project_name]: 
project_owner_fullname [project owner]: 
project_owner_email [you@avast.com]: 
project_version [0.0.0]: 
project_description [Link to WANNA project page on CML]: 
project_slug [project_name]: 
gcp_project_id [us-burger-gcp-poc]: 
gcp_service_account [wanna-ml-testing@us-burger-gcp-poc.iam.gserviceaccount.com]: 
gcp_bucket [wanna_ml]: 
```

# cd into your project_slug
cd project_name
