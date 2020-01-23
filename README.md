# Plasma: LED Sequencing

Plasma is an LED/Light sequencing suite written to harmonise a variety of LED strand/board types and interfaces into a standard API for write-once-run-anyway lighting code.

Plasma also includes plasmad, a system daemon for sequencing light strips using PNG images to provide animation frames.

[![Build Status](https://travis-ci.com/pimoroni/plasma.svg?branch=master)](https://travis-ci.com/pimoroni/plasma)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/plasma/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/plasma?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/plasmalights.svg)](https://pypi.python.org/pypi/plasmalights)
[![Python Versions](https://img.shields.io/pypi/pyversions/plasmalights.svg)](https://pypi.python.org/pypi/plasmalights)

## Compatible Products

Plasma was originally written to provide an easy way to sequence lights and swap out patterns for the Pimoroni Plasma kit.

- https://shop.pimoroni.com/products/picade-plasma-kit-illuminated-arcade-buttons
- https://shop.pimoroni.com/products/player-x-usb-games-controller-pcb
- https://shop.pimoroni.com/products/blinkt
- https://shop.pimoroni.com/products/unicorn-hat
- https://shop.pimoroni.com/products/unicorn-phat

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

### Using Plasma Daemon

Note: If you're using Picade Player X you should edit daemon/etc/systemd/system/plasma.service and change the output device option from `-o GPIO:14:15` to `-o SERIAL:/dev/ttyACM0`. If you're using Unicorn HAT or pHAT you should use `-o WS281X:WS2812:18:0`.

To install the Plasma daemon you should clone this repository, navigate to the "daemon" directory and run the installer:

```
git clone https://github.com/pimoroni/plasma
cd plasma/daemon
sudo ./install
```

The Plasma daemon installer installs two programs onto your Raspberry Pi. `plasma` itself and a tool called `plasmactl` you can use to install and switch lighting effects. Plasma runs as a service on your system.

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
