from flask import Flask
import json
from flask_restful import Api,reqparse,abort,Resource,fields, marshal
import socket
import sys
sys.path.insert(0, '/Users/emirozbir/Desktop/LinuxScriptsAndDocs/python-nmap-0.6.1/nmap')
import pandas as pd
import nmap
import os

app=Flask(__name__)
api=Api(app)
@app.route("/")
def hallo():
    return "hallo"

def host_control_status(ip):

    x = int(os.system("ping -c 2 {}".format(ip)))

    if bool(x) is True:
        return False
    elif bool(x) is False:
        return True


class Machines(Resource):
    def get(self):
        hosts_file=open("/Users/emirozbir/Desktop/LinuxScriptsAndDocs/fabric/hosts_and_users")
        x=[]
        meta_suite={"machine_name":fields.String,"status":fields.Boolean}
        for i in hosts_file:
            name,ip=str(i).split(",")
            meta_data={'machine_name':"{}".format(name),'status':"{}".format(host_control_status(ip))}
            x.append(meta_data)

        return x




api.add_resource(Machines, '/machines')


if __name__ == "__main__":
    app.run(debug=True)
