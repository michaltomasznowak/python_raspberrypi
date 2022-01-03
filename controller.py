# 1 install git on raspberry
# 2 install flask on raspberry

from flask import Flask


from raspberry_service import RaspberryService

app = Flask(__name__)

raspberry_service = RaspberryService()


@app.route('/api/v1/raspberry/on', methods=['GET'])
def on():
    return "Working on pin: " + str(raspberry_service.on)


app.run(host='0.0.0.0')
