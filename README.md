# Plasma Arcade Lights

[![Build Status](https://travis-ci.com/pimoroni/plasma.svg?branch=master)](https://travis-ci.com/pimoroni/plasma)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/plasma/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/plasma?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/plasmalights.svg)](https://pypi.python.org/pypi/plasmalights)
[![Python Versions](https://img.shields.io/pypi/pyversions/plasmalights.svg)](https://pypi.python.org/pypi/plasmalights)

https://shop.pimoroni.com/products/plasma

Add technicolour brilliance to your Picade or Picade Console with this addressable RGB LED arcade button kit, available in a 6-button kit (console buttons) or 10-button kit (all buttons).

Each Picade Plasma PCB has four tiny, addressable, RGB LEDs (APA102) and a data in and data out JST connector. They're designed to fit neatly inside the recess on the back of our low-profile arcade buttons and shine their light through the clear plastic. The white PCB bounces an spilled light from the LEDs to give them extra GLOW.

## Installing

### Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get your Plasma Arcade Button Lights
up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the command exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
curl https://get.pimoroni.com/plasma | bash
```

If you choose to download examples you'll find them in `/home/pi/Pimoroni/plasma/`.

### Manual install:

#### Library install for Python 3:

on Raspbian:

```bash
sudo apt-get install python3-plasmalights
```

other environments: 

```bash
sudo pip3 install plasmalights
```

#### Library install for Python 2:

on Raspbian:

```bash
sudo apt-get install python-plasmalights
```

other environments: 

```bash
sudo pip2 install plasmalights
```

### Using Plasma

Plasma installs two programs onto your Raspberry Pi. `plasma` itself and a tool called `plasmactl` you can use to install and switch lighting effects. Plasma runs as a service on your system.

`plasmactl` commands:

* `plasmactl 255 0 0` - Set Plasma lights to R, G, B colour. Red in this case.
* `plasmactl <pattern>` - Set Plasma lights to pattern image
* `plasmactl fps <fps>` - Change plasma effect framerate (default is 30, lower FPS = less CPU)
* `plasmactl --list` - List all available patterns
* `sudo plasmactl --install <pattern>` - Install a new pattern, where `<pattern>` is the filename of a 24bit PNG image file

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/plasma
* Function reference - http://docs.pimoroni.com/plasma/
* Get help - http://forums.pimoroni.com/c/support
