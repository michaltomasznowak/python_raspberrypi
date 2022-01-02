# 1 install git on raspberry
# 2 install flask on raspberry

from flask import Flask

from raspberry_service import RaspberryService

app = Flask(__name__)

raspberry_service = RaspberryService()


@app.route('/api/v1/raspberry/init', methods=['GET'])
def init():
    return raspberry_service.test()


app.run()
