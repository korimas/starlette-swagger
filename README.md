# starlette-swagger

## requirements:
* starlette_openapi
* starlette_pydantic

## usage:
```python
from typing import Optional
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.routing import Route
from starlette.applications import Starlette
from pydantic import BaseModel
from starlette_pydantic import PydanticEndpoint
from starlette_openapi import OpenApi
from starlette_swagger import SwaggerUI


class RequestBody(BaseModel):
    name: int


class ResponseBody(BaseModel):
    age: int


class Homepage(PydanticEndpoint):

    @staticmethod
    async def get(request):
        return PlainTextResponse("Hello, world!")


class UserDetail(PydanticEndpoint):
    tags = ["user detail"]

    @staticmethod
    async def get(request, username: str = None, page: Optional[str] = None) -> ResponseBody:
        return ResponseBody(age=11)


class User(PydanticEndpoint):
    tags = ["user"]

    @staticmethod
    async def post(request, body: RequestBody) -> ResponseBody:
        return ResponseBody(age=21)


routes = [
    Route("/", Homepage),
    Route("/user", User),
    Route("/user/{username}", UserDetail),
]

app = Starlette(routes=routes)
openapi = OpenApi(app, title="Demo", description="swagger ui demo.")
SwaggerUI(app, openapi)
```

docs url: `http://IP:PORT/docs`