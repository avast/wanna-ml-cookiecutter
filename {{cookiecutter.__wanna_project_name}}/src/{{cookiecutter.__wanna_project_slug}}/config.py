import json
import os

from caseconverter import snakecase

# Env exported from wanna pipeline build cli command
for k, v in os.environ.items():
    if k.startswith("WANNA_") and k.endswith("_PIPELINE_NAME"):
        WANNA_ACTIVE_PIPELINE = v
        break
else:
    if (active_pipeline:= os.getenv("ACTIVE_PIPELINE")) is not None:
        WANNA_ACTIVE_PIPELINE = active_pipeline
    else:
        raise Exception("Could not find WANNA_*_PIPELINE_NAME nor ACTIVE_PIPELINE in environment variables")

PIPELINE_NAME_PREFIX = snakecase(WANNA_ACTIVE_PIPELINE).upper()
WANNA_ENV = os.getenv("WANNA_ENV", "local")
PROJECT_ID = os.getenv(f"{PIPELINE_NAME_PREFIX}_PROJECT_ID")
BUCKET = os.getenv(f"{PIPELINE_NAME_PREFIX}_BUCKET")
REGION = os.getenv(f"{PIPELINE_NAME_PREFIX}_REGION")
PIPELINE_NAME = os.getenv(f"{PIPELINE_NAME_PREFIX}_PIPELINE_NAME")
PIPELINE_EXPERIMENT = os.getenv(f"{PIPELINE_NAME_PREFIX}_PIPELINE_EXPERIMENT")
PIPELINE_JOB_ID = os.getenv(f"{PIPELINE_NAME_PREFIX}_PIPELINE_JOB_ID")
PIPELINE_LABELS = json.loads(os.getenv(f"{PIPELINE_NAME_PREFIX}_PIPELINE_LABELS", "{}"))
PIPELINE_SERVICE_ACCOUNT = os.environ.get(f"{PIPELINE_NAME_PREFIX}_PIPELINE_SERVICE_ACCOUNT")

# Pipeline config
MODEL_NAME = f"{PIPELINE_NAME.lower()}"  # type: ignore
PIPELINE_ROOT = f"{BUCKET}/pipeline_root/{MODEL_NAME}"

# custom training image
DATA_IMAGE_URI = os.environ["DATA_DOCKER_URI"]

TASK_CONFIG = {
    "service_account": PIPELINE_SERVICE_ACCOUNT,
}
