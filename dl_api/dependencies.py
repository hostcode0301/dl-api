import os
from .dl.resnet_utils import CatDogModel

# Init model for detect
dl_model = CatDogModel()


async def init_model():
    return dl_model

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
print("Config var: AWS_ACCESS_KEY_ID = ", AWS_ACCESS_KEY_ID)