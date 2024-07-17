import RPi.GPIO as GPIO
import time
from threading import Thread

class RampingNum:
	#Stops the background task of a ramping number which is handling changing values
	def terminate(self):
		self.running = False
	
	#Gets the current value of the number after ramping
	def value(self):
		return self.value
	
	#Sets the target value of the number to be reached over time cycles.
	def set_value(self, target, time):
		self.target = target
		self.cycles_left = time
		self.delta = (self.value-self.target)/self.time
	
	#Entry point for the thread running at 50hz.
	def run(self):
		while self.running:
			if self.cycles_left > 0:
				self.value += self.delta
				self.cycles_left -= 1
				pulse.ChangeDutyCycle(self.value)
			
			if self.value == 0 and self.pulse_running == True:
				pulse.stop()
				self.pulse_running = False
			elif self.pulse_running == False:
				pulse.start(self.value)
				self.pulse_running = True
			time.sleep(0.2)
		#After loop exits
		self.pulse.stop()
			
	#Initializes a ramping number with all values set to 0
	def __init__(self, pwm):
		self.running = True
		self.value = 0
		self.delta = 0
		self.target = 0 #Might not need this
		self.cycles_left = 0
		
		self.pulse = pwm
		self.pulse_running = False
		
		self.thread = Thread(target = self.run)
		self.thread.start()

class Side:
	def config_pwm(self, port):
		GPIO.setup(port, GPIO.OUT)
		return GPIO.PWM(port, 100)
	
	def config_on(self, port):
		GPIO.setup(port, GPIO.OUT)
		
	def __init__(self, r, g, b, w, ww, o):
		self.red = r
		self.red_val = RampingNum(self.config_pwm(r))
		self.green = g
		self.green_val = RampingNum(self.config_pwm(g))
		self.blue = b
		self.blue_val = RampingNum(self.config_pwm(b))
		self.white = w
		self.white_val = RampingNum(self.config_pwm(w))
		self.wwhite = ww
		self.wwhite_val = RampingNum(self.config_pwm(ww))
		self.on = o
		config_on(o)
	
	def set_colour(self, tr, tg, tb, tw, tww, time = 50):
		self.red_val.set_value(tr, time)
		self.green_val.set_value(tr, time)
		self.blue_val.set_value(tr, time)
		self.white_val.set_value(tr, time)
		self.wwhite_val.set_value(tr, time)
		
		if tr == 0 and tg == 0 and tb == 0 and tw == 0 and tww == 0:
			GPIO.output(self.on, GPIO.LOW)
		else:
			GPIO.output(self.on, GPIO.HIGH)
	
	def cleanup(self):
		self.red_val.terminate()
		self.green_val.terminate()
		self.blue_val.terminate()
		self.white_val.terminate()
		self.wwhite_val.terminate()
		GPIO.output(self.on, GPIO.LOW)
		time.sleep(0.21)

global left = None
global right = None

def initialize_gpio():
	global left
	global right
	GPIO.setmode(GPIO.BOARD)
	left = Side(0, 0, 0, 0, 0, 0)
	right = Side(0, 0, 0, 0, 0, 0)

def set_colour_full(r, g, b, w, ww, time):
	global left
	global right
	left.set_colour(r, g, b, w, ww, time)
	right.set_colour(r, g, b, w, ww, time)

def set_colour_rgb(r, g, b):
	set_colour_full(r, g, b, 0, 0, 50)

def set_rgb_fast(r, g, b):
	set_colour_full(r, g, b, 0, 0, 1)

def cleanup():
	left.cleanup()
	right.cleanup()
    GPIO.cleanup()
    print ("comms cleaning up")

#Module initialization stuff
initialize_gpio()
