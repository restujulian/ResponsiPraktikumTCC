from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, 
socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>RESPONSI PRAKTIKUM TCC</h3><hr/>" \
           "<b>NIM :</b> 165610057<br/>" \
           "<b>Nama :</b> Restu Julian<hr/>"
    return html.format(name=os.getenv("165610057", "RESTU"), 
hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

