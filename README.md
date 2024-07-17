# DIY TV Bias Lighting
Bias lighting is a technique where lights are placed behind a TV or computer monitor, and shine at the wall. The result is not only a cool effect, but also reduced eye strain and a higher percieved contrast of the screen.
I had the idea to create a custom system using a Raspberry Pi, and RGB light strips. Then, I learned of a service called [If This Then That](https://ifttt.com/) which allowed me to recieve commands from my Google Home via web requests.
The final project used a Flask server, some custom circuitry my brother soldered for me, and a Raspberry Pi Zero W to listen for, and act on Google Home requests to change the colours of the lights.
## The Relay Board
![Relay Board](/docs/relay-board.jpg)

The specific LED strips we used had one +12V pin, and multiple ground pins. To work around this, we used relay switches to allow the Raspberry Pi's +3.3V GPIO pins to control whether or not the grounding pins for each colour were enabled.
The downside to this approach was that we could only turn each light on or off, limiting us to 8 different colours.
## The Mofet Board
`//TODO - Add image of  working board`

In an attempt to solve the limited colours available to us in the original circuitry, we designed and built a second control board using Mofets instead of relays. Theoretically, this would allow the Raspberry Pi to use PWM control to dim the brightness of each lighting channel allowing for significantly more colours.
Unfortunatly, while we were setting up this control board, an electrical short irreperably damaged our Raspberry Pi. Work is still being done on upgrading this new circuit board to work properly with new hardware.


## The System in Action
![The Legend of Zelda: Breath of the Wild](/docs/zelda-green.jpg)
![Celeste](/docs/celeste-purple.jpg)
![The Legend of Zelda: Breath of the Wild](/docs/zelda-blue.jpg)
# DIYLED
