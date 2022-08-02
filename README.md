# Latency Tester
<h4>A simple tester for determining the input delay between button press and on screen update.</h4>

The screen software will flash white when any mouse movement of buttons presses are done inside the window.
The Latency tester arduino setup should have the photosensor taped to the screen over the screen software. The desired button on the controller should
be pressed using the button connected to the arduino. The pressure and speed at which the button should be pressed will be dependant on the sensativity and travel of the controllers buttons.
Idealy, the button connected to the arduino and the controller should be depressed at the same moment. The time between the button being pushed and the photosensor
reacting to the screen software will be output via serial monitor and is the effective latency between the controller and the computer.

