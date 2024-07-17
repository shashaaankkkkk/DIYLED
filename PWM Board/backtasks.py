from threading import Thread
import time
import comms
import random

class BackgroundTask:
    def __init__(self):
        self._running = True
        self._active = False
    
    def terminate(self):
        self._running = False
    
    def is_active(self):
        return self._active
    
    def do_async_task(self):
        pass
    
    def run(self):
        #print "started second thread"
        self._active = True
        self.do_async_task()
        self._active = False

class BackgroundSiren(BackgroundTask):
    def __init__(self):
        BackgroundTask.__init__(self)
    
    def do_async_task(self):
        while self._running:
            #print "siren"
            comms.pin_only(comms.left, "red")
            comms.pin_only(comms.right, "blue")
            time.sleep(0.5)
            comms.pin_only(comms.left, "blue")
            comms.pin_only(comms.right, "red")
            time.sleep(0.5)

class BackgroundTrain(BackgroundTask):
    def __init__(self):
        BackgroundTask.__init__(self)
    
    def do_async_task(self):
        while self._running:
            #print "train"
            comms.pin_only(comms.left, "red")
            comms.pin_only(comms.right, "none")
            time.sleep(0.5)
            comms.pin_only(comms.left, "none")
            comms.pin_only(comms.right, "red")
            time.sleep(0.5)

class BackgroundChanging(BackgroundTask):
    def __init__(self):
        BackgroundTask.__init__(self)
        self.time_left = 1
        self.colour = 0
        
    def do_async_task(self):
        #print("Start Rainbow")
        while self._running:
            #print("Begin top loop")
            self.time_left = random.randint(4*60, 5*60)
            self.colour = random.randint(0, 5)
            #print("Set time to ", self.time_left, "and colour", self.colour)
            self.apply_colour()
            while self._running and self.time_left > 0:
                #print("Wait loop", self.time_left)
                time.sleep(1)
                self.time_left -= 1
    
    def apply_colour(self):
        if self.colour == 0:
            comms.pins_only(["red"])
        elif self.colour == 1:
            comms.pins_only(["green"])
        elif self.colour == 2:
            comms.pins_only(["blue"])
        elif self.colour == 3:
            comms.pins_only(["red", "green"]) #Yellow
        elif self.colour == 4:
            comms.pins_only(["red", "blue"]) #Magenta
        elif self.colour == 5:
            comms.pins_only(["green", "blue"]) #Turquoise
        else:
            comms.pins_only([])

##Module Stuff ----------------------
global currentTask
currentTask = None
global currentThread
currentThread = None

def start_task(mode):
    global currentTask
    global currentThread
    stop_task()
    if mode == "train":
        currentTask = BackgroundTrain()
    elif mode == "siren":
        currentTask = BackgroundSiren()
    elif mode == "rainbow":
        currentTask = BackgroundChanging()
    currentThread = Thread(target = currentTask.run)
    currentThread.start()

def stop_task():
    #print "stopping task"
    global currentTask
    global currentThread
    if currentTask != None:
        #print "do have ref"
        currentTask.terminate()
        #print "terminate called"
        while currentTask.is_active():
            time.sleep(0.1)
            #print "not shut down"
        currentTask = None
        currentThread = None
    #print "end terminate"
