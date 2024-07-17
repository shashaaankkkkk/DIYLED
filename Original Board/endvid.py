import time
import comms

if __name__ == "__main__":
	print("start")
	comms.pins_only(["red"])
	time.sleep(0.5)
	comms.pins_only(["green"])
	time.sleep(0.5)
	comms.pins_only(["blue"])
	time.sleep(0.5)
	comms.pins_only(["red", "green"])
	time.sleep(0.5)
	comms.pins_only(["red", "blue"])
	time.sleep(0.5)
	comms.pins_only(["green", "blue"])
	time.sleep(0.5)
	comms.pins_only(["red", "green", "blue"])
	time.sleep(0.5)
	comms.pins_only(["white"])
	time.sleep(0.5)
	comms.pins_only(["wwhite"])
	time.sleep(0.5)
	comms.pins_only([])
	print("done")
	comms.cleanup()

