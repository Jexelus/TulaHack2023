from config import cfg
import app


def run():
    _app = app.create_app()
    host_info = {'host': cfg['SERVER_IP'], 'port': 5000, 'debug': False}
    _app.run(**host_info)


if __name__ == '__main__':
    run()
