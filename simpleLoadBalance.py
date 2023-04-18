from flask import Flask
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

servers = ['Server 1', 'Server 2', 'Server 3']

class LoadBalancer(Resource):
    def get(self):
        return random.choice(servers)

api.add_resource(LoadBalancer, '/')

if __name__ == '__main__':
    app.run(debug=True)


#In this example, the LoadBalancer class is defined as a resource for the Flask RESTful API. When a client makes a GET request to the root endpoint (/), the get method is called, which returns a randomly chosen server from the servers list. This simple load balancing strategy distributes requests evenly across the available servers.

