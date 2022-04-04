from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .routers import items, upload
from .dependencies import init_model


# Create FastAPI instance with global Denpendency for model


app = FastAPI(dependencies=[Depends(init_model)])

# region Routers

app.include_router(items.router)
app.include_router(upload.router)

# endregion

# region CORS

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# endregion


# Home demo


@app.get("/")
async def root():
    return {"message": "Hello World"}
