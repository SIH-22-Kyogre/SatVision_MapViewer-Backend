from flask import Flask
from flask_restful import Api 

from api.resource.hello_world import HelloWorld
from api.resource.cover_class import CoverClass
from api.resource.sat_image import SatImage

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

api.add_resource(
	CoverClass, 
	API_ROUTE.format(
		path = "classify/<clf_name>"
	)
)

api.add_resource(
	SatImage, 
	API_ROUTE.format(
		path = "fetch"
	)
)


# main event loop
if __name__ == '__main__':
	app.run(debug=True)