# Parking Space Detection

# Table of Contents
0. [Purpose](#0-purpose)
1. [Setup](#1-setup)
2. [Personal Project Description](#2-personal-project-description)
3. [Imlpementation status](#3-implementation-status)

## 0 Purpose
The purpose of this library is to setup a remotely accessible camera that scans a static location for available 
parking spots and informs the user about it (i.e., you should be able to trigger a camera via phone/email 
and receive a message/email about whether a given parking area has a free spot available or not)
![plot](./data/Diagram.png)
## 1 Setup
### 1a Conda environment
Install the corresponding conda environment via   
```conda env create -f environment.yml```  
(and don't forget to activate it via `conda activate cam`)

### 1b Testing
- Unit tests  
Run unit tests via  
```python -m unittest```  
Note: if you are using PyCharm, I would recommend to setup the testing environment as is shown [here](https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html#create-test)
- Integration tests  
__TBD__

### 1c Formatting
Run black code formatting from the project root directory via  
```black --line-length 120 .```  
Note: if you are using PyCharm, I would recommend to setup black as is shown [here](https://godatadriven.com/blog/partial-python-code-formatting-with-black-pycharm/) as default code formatter with the additional argument `line-length 120` triggered during every _save_ operation.  
Black version used in the code is 21.12b0.

## 2 Personal Project Description
This Repo is built for the purpose of remote parking space monitoring and based on 2 main parts (and 4 resulting features) 
1. Image acquisition part:
- Feature A > Camera setup: Building a camera setup that allows remote access (e.g., via smartphone)
- Feature B > Server setup: Sending the acquired image to a (remote) server
2. Computer Vision part:
- Feature C > Parking space detection: Detection of free parking space based on acquired image
- Feature D > Information sharing: Sharing of results (e.g., just sharing raw image and/or Yes-No result of CV algorithm - i.e., yes there is a free parking spot)

### Feature A > Camera setup:
Requirements:
- Needs to be accessible remotely (e.g., via smartphone and/or computer) - e.g., send an e-mail to server -> image acquisition is triggered
Initial idea of solution:
- Hook up camera to RaspberryPi which is connected to WiFi
- Triggering TBD
- Image needs to be uploaded to server (can be just simple sharing to Laptop in beginning)

### Feature B > Server setup:
- TBD -> Can be done on local machine in beginning; AWS EC2 instance later

### Feature C > Parking space detection:
- Probably some simple CNN (e.g., from detectron2) - but should be able to fine-tune based on specific scene of interest (which will be static - i.e., always the same)

### Feature D > Information sharing:
- Once results are available, should be shared via e-mail - (can be just sharing of the raw image in beginning)

## 3 Implementation status 
|                             | Level 1                                                                                                                              |                    | Level 2                                                                                |              | Level 3                                                                                   |              |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------|:------------------:|----------------------------------------------------------------------------------------|:------------:|-------------------------------------------------------------------------------------------|:------------:|
| __Feature__                 | __Description__                                                                                                                      |     __Status__     | __Description__                                                                        |  __Status__  | __Description__                                                                           |  __Status__  |
| A > Camera setup            | Trigger laptop/smartphone camera from device in same WiFi (e.g., via SSH)                                                            |         -          | Trigger laptop/smartphone camera from device outside of network (e.g., via VPN & SSH?) |      -       | Standalone camera module connected to Wifi (e.g., RaspberryPi)                            |      -       |
| B > Server setup            | _tbd: will likely do this last and run computations locally first_                                                                   |         -          | -                                                                                      |      -       | -                                                                                         |      -       |
| C > Parking space detection | Yolov4-tiny to infer number of cars in image (and if less than given number -> assume free spot)                                     | :white_check_mark: | __TBD__                                                                                |      -       | Fine-tuned CNN predicting whether free parking spot is available (i.e., yes/no vs n_cars) |      -       |
| D > Information sharing     | Programmatically send plain-text e-mail to specified address                                                                         | :white_check_mark: | Send attachments (e.g., image)                                                         |      -       | n/a                                                                                       |      -       |
| E > Forecasting             | Take multiple images of parking lot over extended period of time and detect patterns (i.e., forecast expected n_cars in parking lot) |         -          | n/a                                                                                    |      -       | n/a                                                                                       |      -       |