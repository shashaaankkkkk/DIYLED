import RPi.GPIO as GPIO

##Constants
right = {
    "red": 22,
    "green": 26,
    "blue": 24,
    "wwhite": 32,
    "white": 36
    }
left = {
    "red": 18,
    "green": 12,
    "blue": 16,
    "wwhite": 8,
    "white": 10
    }

threshold = 100
closeness = 35
##End Constants

##Init
print ("comms init")

GPIO.setmode(GPIO.BOARD)
for pin in left:
    #print "pin is", left[pin]
    GPIO.setup(left[pin], GPIO.OUT)
    GPIO.output(left[pin], GPIO.LOW)
for pin in right:
    #print "pin is", right[pin]
    GPIO.setup(right[pin], GPIO.OUT)
    GPIO.output(right[pin], GPIO.LOW)
##End Init

def output(lr, lg, lb, lw, lww, rr, rg, rb, rw, rww):
    apply_pin(left["red"], lr)
    apply_pin(left["green"], lg)
    apply_pin(left["blue"], lb)
    apply_pin(left["white"], lw)
    apply_pin(left["wwhite"], lww)
    apply_pin(right["red"], rr)
    apply_pin(right["green"], rg)
    apply_pin(right["blue"], rb)
    apply_pin(right["white"], rw)
    apply_pin(right["wwhite"], rww)

def set_right(r, g, b):
    set_channel(right, r, g, b)

def set_left(r, g, b):
    set_channel(left, r, g, b)

def set_channel(ch, r, g, b):
    if in_range(r, g, 7) and in_range(g, b, 7):
        if r > b + 15:
            pin_only(ch, "wwhite") #warm white
            return
        else:
            pin_only(ch, "white") #cool white
            return
    else:
        if r > g and r > b:
            pin_only(ch, "red")
            if in_range(r, g, closeness):
                apply_pin(ch["green"], True)
            elif in_range(r, b, closeness):
                apply_pin(ch["blue"], True)
        elif g > r and g > b:
            pin_only(ch, "green")
            if in_range(r, g, closeness):
                apply_pin(ch["red"], True)
            elif in_range(g, b, closeness):
                apply_pin(ch["blue"], True)
        elif b > g and b > r:
            pin_only(ch, "blue")
            if in_range(b, g, closeness):
                apply_pin(ch["green"], True)
            elif in_range(r, b, closeness):
                apply_pin(ch["red"], True)
    return

def in_range(valA, valB, threshold):
    return valA < valB+threshold and valA > valB-threshold

def pins_only(on):
    for key in left:
        if key in on:
            apply_pin(left[key], True)
        else:
            apply_pin(left[key], False)
    for key in right:
        if key in on:
            apply_pin(right[key], True)
        else:
            apply_pin(right[key], False)

def pin_only(ch, on):
    for key in ch:
        if key == on:
            apply_pin(ch[key], True)
        else:
            apply_pin(ch[key], False)

def apply_pin(pin, en):
    GPIO.output(pin, state(en))

def state(en):
    if en == True:
        return GPIO.HIGH
    else:
        return GPIO.LOW

def cleanup():
    GPIO.cleanup()
    print ("comms cleaning up")
