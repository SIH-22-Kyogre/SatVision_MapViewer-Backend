from flask import Flask
from flask_restful import Api 

from api.resource.hello_world import HelloWorld

API_ROUTE = "/api/{path}"

# wrap around the App with API
app = Flask(__name__)
api = Api(app)

# Register resource routes
api.add_resource(
	HelloWorld, 
	API_ROUTE.format(
		path = "hello"
	)
)

# main event loop
if __name__ == '__main__':
	app.run(debug=True)