from flask import Flask, request
import comms
import backtasks as tasks
import time

app = Flask(__name__)

def set_state(mode):
    print ("stopping task")
    tasks.stop_task()
    if mode == "White" or mode == "white":
        comms.pins_only(["white"])
    elif mode == "off":
        comms.pins_only([])
    elif mode == "red":
        comms.pins_only(["red"])
    elif mode == "green":
        comms.pins_only(["green"])
    elif mode == "blue":
        comms.pins_only(["blue"])
    elif mode == "purple":
        comms.pins_only(["blue", "red"])
    elif mode == "turquoise":
        comms.pins_only(["blue", "green"])
    elif mode == "yellow":
        comms.pins_only(["red", "green"])
    elif mode == "warm" or mode == "on":
        comms.pins_only(["wwhite"])
    elif mode == "train" or mode == "siren" or mode == "rainbow" or mode=="christmas" or mode=="Christmas":
        tasks.start_task(mode)
    else:
        tasks.stop_task()
        comms.pins_only([])
        #print "stopping task"

@app.route('/')
def base_addr():
    return 'No'

@app.route('/backlight')
def backlight_command():
    mode = request.args.get('mode')
    #mode = 0
    if mode == None:
        return 'Null error'
    else:
        #print "setting state with arg", mode
        set_state(mode.strip())
    return 'Backlight set'

if __name__ == '__main__':
    comms.pins_only(["red"])
    time.sleep(1)
    comms.pins_only(["green"])
    time.sleep(1)
    comms.pins_only(["blue"])
    time.sleep(1)
    comms.pins_only([])
    app.run(debug=False, port=8080, host='0.0.0.0')
    print ("cleanup")
    tasks.stop_task()
    comms.cleanup()
