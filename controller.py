# 1 install git on raspberry
# 2 install flask on raspberry

from flask import Flask

from raspberry_service import RaspberryService

app = Flask(__name__)

raspberry_service = RaspberryService()


@app.route('/api/v1/raspberry/on', methods=['GET'])
def on():
    return "On Pin: " + str(raspberry_service.on)


@app.route('/api/v1/raspberry/off', methods=['GET'])
def off():
    return "Off Pin: " + str(raspberry_service.off)


app.run(host='0.0.0.0')
