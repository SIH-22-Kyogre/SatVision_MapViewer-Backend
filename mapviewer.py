from flask import Flask
from flask_restful import Api 

from api.hello_world import HelloWorld

# wrap around the App with API
app = Flask(__name__)
api = Api(app)

# Register resource routes
api.add_resource(HelloWorld, '/hello')

# main event loop
if __name__ == '__main__':
	app.run(debug=True)