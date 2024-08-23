# m3_super_90_counter_v2
M3 super 90 Airsoft shotgun counter

![](https://github.com/mattabott/m3_super_90_counter_v2/blob/main/img/VideoEditor_20240823_103058.gif)

This project is a custom counter designed for the M3 Super 90 softair shotgun by Tokyo Marui. The counter tracks the number of shots fired and the number of shells used. The project is built using a 3D-printed housing, a Raspberry Pi Pico, an OLED display, a button, and an endstop switch.

# Features
- Shot Counter: Counts the number of shots fired from the M3 Super 90.
- Shell Counter: Tracks the number of shells used.
- OLED Display: Shows the current count of shots and shells.
- Reset Button: Allows resetting the counter when a new shell is loaded.
- Compact Design: The counter is housed in a custom 3D-printed case designed to be mounted on the shotgun.

![](https://github.com/mattabott/m3_super_90_counter_v2/blob/main/img/20240823_165340.jpg)

# Components
- Raspberry Pi Pico: The microcontroller that runs the code and handles the input/output.
- OLED Display (128x64 pixels): Used to display the shot and shell count.
- Endstop Switch: Detects when a shot is fired.
- Reset Button: Resets the counter after loading a new shell.
- Battery pack for 2 AA battery.
- 3D Printed Case: Custom case to house all components securely on the shotgun (find .STL file [here](https://www.thingiverse.com/thing:6741174)).

# Wiring and Connections
Below are the detailed wiring connections between the components and the Raspberry Pi Pico:

![](https://github.com/mattabott/m3_super_90_counter_v2/blob/main/img/20240823_165333.jpg)

- OLED Display:
 
  - SDA (Data Line): Connect to GP0 (Pin 1) on the Raspberry Pi Pico.
  - SCL (Clock Line): Connect to GP1 (Pin 2) on the Raspberry Pi Pico.
  - VCC: Connect to a 3.3V pin on the Raspberry Pi Pico.
  - GND: Connect to a ground (GND) pin on the Raspberry Pi Pico.

- Endstop Switch:

  - Signal Pin: Connect to GP26 (Pin 31) on the Raspberry Pi Pico.
  - GND: Connect to a ground (GND) pin on the Raspberry Pi Pico.

- Reset Button:

  - Signal Pin: Connect to GP22 (Pin 29) on the Raspberry Pi Pico.
  - GND: Connect to a ground (GND) pin on the Raspberry Pi Pico.

- Battery Pack:

 - Signal Pin: connect to 3V Gpio (Pin 40).
 - GND: Connect to a ground (GND) pin on the Raspberry Pi Pico.

# Installation

1. 3D Print the Case: Use the provided STL files from [here](https://www.thingiverse.com/thing:6741174).
2. Wiring: Connect the components to the Raspberry Pi Pico as per the wiring instructions above.
3. Load the Code: Upload the provided Python code onto your Raspberry Pi Pico using Thonny (raccomended).
4. Assembly: Assemble the components into the 3D printed case.
5. Mount: Secure the counter onto your M3 Super 90 softair shotgun with nuts.

# Usage
Power On: Power the Raspberry Pi Pico with 2 AA battery.
Shot Tracking: The OLED display will show the number of shots fired and the current shell count.
Reset: Press the reset button after reloading a new shell to reset the shot counter to 10.
Automatic Shell Increment: When the counter reaches 0, the shell count automatically increments by 1.

# Licence

This project is in CC licence. If you use it, tag me on your social post with @mattabott tag!
