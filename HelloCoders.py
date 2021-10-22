#Import Flask Library
from flask import Flask

#Initialize your app from Flask

app = Flask(__name__)

#Define your route that could be called

@app.route('/')
def hellocoders():
    return "<B>Enjoy Big Data and Dev Conference"

#Run the app.
app.run()

