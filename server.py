import uvicorn

if __name__ == '__main__':
    uvicorn.run("decoupled_dj.asgi:application", reload=True)
