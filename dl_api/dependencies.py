from .dl.resnet_utils import CatDogModel

# Init model for detect
dl_model = CatDogModel()


async def init_model():
    return dl_model
