from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
	return "Helo World! fase 2"

if __name__ == '__main__':
	application.run()
