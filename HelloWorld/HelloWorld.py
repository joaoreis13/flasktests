from flask import Flask,jsonify

ftHelloWorld = Flask(__name__)
ftHelloWorld.config.from_object('config')

@ftHelloWorld.route('/')
def hello_world():
    ret = jsonify( {"Helo World! fase 2 ":ftHelloWorld.config['CONFIG_VAR']} )
    ret.status_code = 202
    ret.headers.pop['server']
    return ret

if __name__ == '__main__':
	ftHelloWorld.run()