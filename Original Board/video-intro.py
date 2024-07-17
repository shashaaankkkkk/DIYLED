import comms
import time

if __name__ == '__main__':
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(0.5)
    print("0.5")
    time.sleep(0.5)
    print("0")
    comms.pins_only(["green"]) #Opening Forest is green
    time.sleep(4.36)
    comms.pins_only(["green", "blue"]) # Turqoise Ocean 4:22
    time.sleep(5.52) # 5:31
    comms.pins_only(["blue"]) # Blue Spaceship 9:53
    time.sleep(6.2) # 6:12
    comms.pins_only(["red"]) # Red Nether 16:05
    time.sleep(4.66) # 4:40
    comms.pins_only(["red", "blue"]) # Purple Movent 20:45
    time.sleep(3.25) # 3:15
    comms.pins_only(["blue"]) # Blue Spaceship 24:00
    time.sleep(5.6) # 7:10
    comms.pins_only(["wwhite"]) # White Sun 27:55
    time.sleep(1.75) # 2:45
    comms.pins_only([]) # End 30:50
    comms.cleanup()
