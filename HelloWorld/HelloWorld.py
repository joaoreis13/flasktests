from flask import Flask

ftHelloWorld = Flask(__name__)
ftHelloWorld.config.from_object('config')

@ftHelloWorld.route('/')
def hello_world():
	return "Helo World! fase 2"+ftHelloWorld.config['CONFIG_VAR'],202

if __name__ == '__main__':
	ftHelloWorld.run()