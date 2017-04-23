from flask import Flask
import json
from flask_restful import Api,reqparse,abort,Resource,fields, marshal
import socket
app=Flask(__name__)
api=Api(app)
@app.route("/")
def hallo():
    return "hallo"

class Machines(Resource):


    def get(self,ip):
        x = socket.gethostbyaddr(ip)

api.add_resource(Machines, '/machine_stat/<ip>')


if __name__ == "__main__":
    app.run(debug=True)
