import asyncio

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from controller.CourseList import courseList
from controller.md import md
from controller.token import token

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(courseList, prefix="/Course", tags=["课程列表"])
app.include_router(token,tags=["获取凭证"])
app.include_router(md,tags=["获取凭证"])

async def main():
    config = uvicorn.Config(app, host='127.0.0.1', port=3000)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())

