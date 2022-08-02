# Latency Tester
<h4>A simple tester for determining the input delay between button press and on screen update.</h4>

The screen software will flash white when any mouse movement of buttons presses are done inside the window.
The Latency tester arduino setup should have the photosensor taped to the screen over the screen software. The desired button on the controller should
be pressed using the button connected to the arduino. The pressure and speed at which the button should be pressed will be dependant on the sensativity and travel of the controllers buttons.
Idealy, the button connected to the arduino and the controller should be depressed at the same moment. The time between the button being pushed and the photosensor
reacting to the screen software will be output via serial monitor and is the effective latency between the controller and the computer.

<h2> Setup </h2>

Both the photosensor and the button should be placed in their respective 3d printable housing for ease of use.
The photosensor should have one leg wired to the 5v pin of the arduino. The other leg should be wired to both A0 and gnd.
The button should be wired on one side to 3.3v. The otherside should be wired to digital pin 2 and gnd.

<img src="/img/Setup1.jpg" width = 500 height = 500/>
<img src="/img/Setup2.jpg" width = 500 height = 500/>
