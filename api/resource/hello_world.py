from flask_restful import Resource


class HelloWorld(Resource):

	def __init__(self):
		pass

	def get(self):
		return dict(
			message = "Hello World"
        )