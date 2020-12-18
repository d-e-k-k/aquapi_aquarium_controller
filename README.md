# Aquapi Aquarium Controller

AquaPi is an automated aquarium controller that can monitor and manage a variety of aquarium components. Built with a RaspberryPi single board computer and some sensors, the AquaPi framework is extremely customizable and affordable. Excited….? Checkout the frontend and backend repo or the deployed frontend here! 
- Deployed frontend https://aquapi.herokuapp.com/
- https://github.com/d-e-k-k/aquapi_frontend 
- https://github.com/d-e-k-k/aquapi_backend

# Hardware
- RaspberryPi 4 B
- DS18B20 Waterproof Digital Temperature Sensor with adapter
- A variety of jumper wires
- 220 ohm resistor
- LED

# Schematic 

![image](https://user-images.githubusercontent.com/71715721/102635483-5f16fb80-4121-11eb-888f-959c1590be39.png)


# Cron Job
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
