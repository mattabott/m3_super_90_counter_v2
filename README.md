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

# Components
-Raspberry Pi Pico: The microcontroller that runs the code and handles the input/output.
-OLED Display (128x64 pixels): Used to display the shot and shell count.
-Endstop Switch: Detects when a shot is fired.
-Reset Button: Resets the counter after loading a new shell.
-3D Printed Case: Custom case to house all components securely on the shotgun.

# Wiring and Connections
Below are the detailed wiring connections between the components and the Raspberry Pi Pico:

-OLED Display:
 
  -SDA (Data Line): Connect to GP0 (Pin 1) on the Raspberry Pi Pico.
  -SCL (Clock Line): Connect to GP1 (Pin 2) on the Raspberry Pi Pico.
  -VCC: Connect to a 3.3V pin on the Raspberry Pi Pico.
  -GND: Connect to a ground (GND) pin on the Raspberry Pi Pico.

-Endstop Switch:

  -Signal Pin: Connect to GP26 (Pin 31) on the Raspberry Pi Pico.
  -GND: Connect to a ground (GND) pin on the Raspberry Pi Pico.

-Reset Button:

  -Signal Pin: Connect to GP22 (Pin 29) on the Raspberry Pi Pico.
  -GND: Connect to a ground (GND) pin on the Raspberry Pi Pico.

Installation
3D Print the Case: Use the provided STL files (if available) to 3D print the case that fits the components.
Wiring: Connect the components to the Raspberry Pi Pico as per the wiring instructions above.
Load the Code: Upload the provided Python code onto your Raspberry Pi Pico using a suitable IDE or method.
Assembly: Assemble the components into the 3D printed case.
Mount: Secure the counter onto your M3 Super 90 softair shotgun.
Usage
Power On: Power the Raspberry Pi Pico via a USB connection.
Shot Tracking: The OLED display will show the number of shots fired and the current shell count.
Reset: Press the reset button after reloading a new shell to reset the shot counter to 10.
Automatic Shell Increment: When the counter reaches 0, the shell count automatically increments by 1.
