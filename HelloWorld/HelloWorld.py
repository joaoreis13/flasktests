from flask import Flask

application = Flask(__name__)
application.config.from_object('config')

@application.route('/')
def hello_world():
	return "Helo World! fase 2"+application.config['CONFIG_VAR']

if __name__ == '__main__':
	application.run()
