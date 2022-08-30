import os

import uvicorn


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'decoupled_dj.settings.development')
    uvicorn.run("decoupled_dj.asgi:application", reload=True)


if __name__ == '__main__':
    main()
