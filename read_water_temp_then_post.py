
from gpiozero import LED
from datetime import datetime
import glob
import os
import requests

#Probe Location
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28-01145d8e73ba')[0]
device_file = device_folder + '/w1_slave'


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    if lines[0].strip()[-3:] != 'YES':
        print('Cannot access probe')
        exit()
    equals_pos = lines[1].find('t=')
    temp_string = lines[1][equals_pos+2:]
    temp_c = float(temp_string)/1000
    temp_f = temp_c * 1.8 + 32
    return temp_f


now = datetime.now()
current_formatted_date = now.strftime("%d-%m-%Y")
current_formatted_time = now.strftime("%H:%M:%S")

TOKEN = os.environ['TOKEN']
headers = {"Authorization": TOKEN}
url = "https://mighty-lake-45709.herokuapp.com/temperatures/"

f_temp = (read_temp())

r = requests.post(url, headers=headers, data={
    "temperature": f_temp,
    "date": current_formatted_date,
    "time": current_formatted_time
})
print(r.status_code)
print(r.content)
