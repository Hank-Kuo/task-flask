from task.application import create_app
from task.extension.config_extension import get_config

if __name__ == '__main__':
    config = get_config()
    
    app = create_app()
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)