from flask import Flask, request
import comms
import backtasks as tasks
import time

app = Flask(__name__)

current_state = "Off" #Off, Solid, Backtask
current_mode = "Off" #The specific mode being used

def set_state(mode):
    pass

@app.route('/')
def base_addr():
    return '<h1>TV Backlight Core</h1>\n<h3>You should not be here</h3>'

@app.route('/backlight', methods = 'POST', 'GET')
def backlight_command():
    return 'Backlight set'

def start_server():
	print("Starting server")
	app.run(debug=False, port=8080, host='0.0.0.0')
    print("Cleanup")
    tasks.stop_task()
    comms.cleanup()
	print("Done")

if __name__ == '__main__':
    start_server()
