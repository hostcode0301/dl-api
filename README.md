# Deep learning model with Pytorch and Fastapi framework

> This is an cat dog detection model using Pytorch and Fastapi. Any configuration can be reused. I do not train the model so it's just using for demo not for production

## Install

To install project libraries run:

```
poetry install
```

_If there is an error about not found **Poetry** you can read Poetry install guide at the last part_

## Run the app in development

The app can be run through:

```
uvicorn dl_api.app:app --reload
```

## Publish to production through Docker

1. Build an image

```
docker build -t dl_api .
```

2. Build a container

```
docker run -p 8000:80 dl_api
```

_If there is an error about not found **Docker** you can read Docker install guide at the last part_

## Q&A

-   Install Poetry

Read [this link](https://python-poetry.org/docs/) for further information to install Poetry

-   Install Docker

Read [this link](https://docs.docker.com/get-docker/) for further information to install Docker
