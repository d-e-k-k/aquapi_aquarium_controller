# AquaPi Project

AquaPi is an automated aquarium controller that can monitor and manage a variety of aquarium components. Built with a RaspberryPi single board computer and some sensors, the AquaPi framework is extremely customizable and affordable. The frontend was built with React while the backend is handled by Django with a Postgresql DB. Excited….? Checkout the frontend and backend repos or the deployed application links! 

- Deployed frontend https://aquapi.herokuapp.com/
- Deployed backend https://mighty-lake-45709.herokuapp.com/
- https://github.com/d-e-k-k/aquapi_frontend 
- https://github.com/d-e-k-k/aquapi_backend
- https://github.com/d-e-k-k/aquapi_aquarium_controller

## AquaPi RaspberryPi Controller
Currently, a waterproof temperature sensor is attached to the RaspberryPi. Every hour via crontab, a python script is run that sends the current date, time, and probe temperature to the server via http post request. This data is then accessed via React and displayed on a web application.

## Hardware
- RaspberryPi 4 B
- DS18B20 Waterproof Digital Temperature Sensor with adapter
- A variety of jumper wires
- 220 ohm resistor
- LED

## Layout

![image](https://user-images.githubusercontent.com/71715721/103029861-a853ba80-4528-11eb-8a31-4a77a82bfcf1.png)



## Cron Job
```
0 * * * * /usr/bin/python3 /home/pi/python/temp/read_water_temp_then_post.py
```
The cron job above runs the python read temperature and post script every hours.

## How to Contribute 
All contributions are appreciated!
1. Push your most recent development branch up to Github
2. Create a pull request against the branch of interest or our Dev branch.
3. Be descriptive in you pull message!
4. Await merge or revision request!
