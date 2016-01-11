from boto.dynamodb2.fields import HashKey
from boto.dynamodb2.table import Table
from flask import Flask
from flask.ext.dynamo import Dynamo
import boto
import boto3
app = Flask(__name__)



app.config['DYNAMO_TABLES'] = [
    Table('users', schema=[HashKey('username')]),
    Table('groups', schema=[HashKey('name')]),
]
dynamo = Dynamo(app)

# @app.route('/create_user')
# def create_user():
#     dynamo.users.put_item(data={
#         'username': 'rdegges',
#         'first_name': 'Randall',
#         'last_name': 'Degges',
#         'email': 'r@rdegges.com',
#     })
#
#     # or ...
#
#     dynamo.tables['users'].put_item(data={
#         'username': 'rdegges',
#         'first_name': 'Randall',
#         'last_name': 'Degges',
#         'email': 'r@rdegges.com',
#     })
#
# with app.app_context():
#     for table_name, table in dynamo.tables.iteritems():
#         print table_name, table
#
# # app.py
#
# with app.app_context():
#     dynamo.destroy_all()
#



@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
