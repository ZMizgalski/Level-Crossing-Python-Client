# Level-Crossing-Python-Client
> The level crossing clinet app made with Angular and Flask for competition: "OLIMPIADA INNOWACJI TECHNICZNYCH I WYNALAZCZOŚCI" [Link](https://www.pzswir.pl/olimpiada)

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)
* [License](#license)

## General Information
- This project was made for school competition and also to improve railroads in whole country. It uses AI to detect objects and decide to open crossing barriers when someone is blocked. To work properly it needs to be connected to a network. Client app is controlling servos connected to the Raspberry Pi

## Technologies Used
- OpenCv
- Socket
- Python
- Raspberry Pi
- Adafruit PCB

## Features
List the ready features here:
- Control of servos
- Socket connection

## Screenshots
![IMG](https://github.com/ZMizgalski/Level-Crossing-Python-Client/blob/master/imgs/logo.png)
![IMG](https://github.com/ZMizgalski/Level-Crossing-Python-Client/blob/master/imgs/1.png)
![IMG](https://github.com/ZMizgalski/Level-Crossing-Python-Client/blob/master/imgs/2.jpg)
![IMG](https://github.com/ZMizgalski/Level-Crossing-Python-Client/blob/master/imgs/3.png)
![IMG](https://github.com/ZMizgalski/Level-Crossing-Python-Client/blob/master/imgs/4.png)


## Setup
- Python 3.6+
- configured pip
- More requirements found in [requirements.txt](https://github.com/ZMizgalski/Level-Crossing-Python-Client/blob/master/requirements.txt)

## Usage

IMPORTANT PARTS!
1. Raspberry Pi 4B at least https://www.raspberrypi.org/ and also multiple modifications
2. Raspberry Pi camera
3. Adafruit PCA9685 16-channel servo driver
4. Raspberry Pi power supply
5. 5V simple power supply (for PCA9685)
6. SD Card
7. 4 x 180 degree servo

ClIENT + [SERVER](https://github.com/ZMizgalski/Level-Crossing-Python-Server) 
1. Create a folder named you like.
2. Inside your folder, open console and paste: `git clone https://github.com/ZMizgalski/Level-Crossing-Python-Client.git`
3. Install OS on Raspberry Pi with easy Imager https://www.raspberrypi.com/software/
4. Enable SSH and pi-camera on Raspberry Pi
5. Then you need to transfer this program to Raspberry Pi with ssh best option
6. Install python from the official website. [Download here](https://www.python.org/downloads/)
7. Install pip then install all requirements from [requirements.txt](https://github.com/ZMizgalski/Level-Crossing-Python-Client/blob/master/requirements.txt)
7. Then you are ready to go just open console and run `Main.py`

## Project Status
Project is:  _complete_ .

## Room for Improvement
- Security
- Improve socket connection
- create cloud database with last connected crossings
- create cloud for selected areas

## Contact
Created by [@zmizgalski](https://zmizgalski.github.io/) - feel free to contact me!

## License
This project is open source and available under the [... License](https://github.com/ZMizgalski/Level-Crossing-Python-Client/blob/master/LICENSE).
