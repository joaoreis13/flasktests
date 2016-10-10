from flask import Flask

ftHelloWorld = Flask(__name__)

@ftHelloWorld.route('/')
def hello_world():
	return "Helo World!"

if __name__ == '__main__':
	ftHelloWorld.run()