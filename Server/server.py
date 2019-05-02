import os

from app import create_app

from config import Config

if __name__ == '__main__':
    app = create_app(Config)

    app.run('0.0.0.0', port=6060, debug=True)