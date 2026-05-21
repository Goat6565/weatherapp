from tkinter import *
from tkinter import messagebox as mb
import requests
from PIL import Image, ImageTk
from datetime import datetime
import pyttsx3
from threading import Thread

root = Tk()
root.title("WEATHER APPLICATION")
root.geometry("600x400")



def display_and_speak(text):
    print("Text to display:", text)

    # Use a separate thread for speaking to avoid blocking the GUI
    def speak():
        engine = pyttsx3.init()
        engine.say(text)   
        engine.runAndWait()

    speak_thread = Thread(target=speak)
    speak_thread.start()   


def get_weather():
    global city
    city=city_input.get()
    api_key='dfb96d8288ab698da28c1f283e0834ef'
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response=requests.get(url)
    if response.status_code == 200:
        data=response.json()
        temp=data['main']['temp']-273.15
        humidity=data['main']['humidity']
        pressure=data['main']['pressure']
        wind=(data['wind']['speed'])*3.6
        epoch_time=data['dt']
        date_time=datetime.fromtimestamp(epoch_time)
        desc=data['weather'][0]['description']
        cloudy=data['clouds']['all']
       

        timelabel.config(text=str(date_time))
        temp_field.insert(0, '{:.2f}'.format(temp) + "celcius")
        pressure_field.insert(0, str(pressure) + "hPa")
        humid_field.insert(0, str(humidity) + "%")
        wind_field.insert(0, '{:.2f}'.format(wind) + "km/h")
        cloud_field.insert(0, str(cloudy) + "%")
        desc_field.insert(0, str(desc))
        text_to_display_and_speak=(f"Hi i am sudharsan weather reporter. Today {date_time}.  I will tell about weather report for {city}. The temperature is {temp:.2f} celcius. The pressure is {pressure} hectopascals. The humidity is {humidity} percent. The wind speed is {wind:.2f} kilometers per hour. The cloudiness is {cloudy} percent. The sky is {desc}.  Thank you. Have a nice day!")
        display_and_speak(text_to_display_and_speak)
       
    else:
        mb.showerror("Error", "City Not Found.Enter a valid city name")
        city_input.delete(0, END)


     


def reset():
        city_input.delete(0, END)
        temp_field.delete(0, END)
        pressure_field.delete(0, END)
        humid_field.delete(0, END)
        wind_field.delete(0, END)
        cloud_field.delete(0, END)
        desc_field.delete(0, END)
        timelabel.config(text='')


def get_forecast():
     url1='https://wttr.in/{}'.format(city)
     response1=requests.get(url1)
     print(response1.text)
     
               
bg_image = Image.open("C://WEATHER//climate.jpg")  # Specify the path to your image
bg_image = bg_image.resize((600,400))  # Resize the image to fit the window
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to hold the background image
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title = Label(root, text="Weather detection and forecast", fg="black", bg="royal blue1", font=("bold", 15), justify="center")
label1 = Label(root, text="Enter the city name :", font=("bold", 12), bg="palegreen")
city_input = Entry(root, width=24, fg="red2", font=12, relief=GROOVE)
timelabel = Label(root, text="", bg="yellow", font=("bold", 14), fg="navy")

btn_submit = Button(root, text="Get weather", width=10, font=12, bg="salmon", command=get_weather) 
btn_forecast = Button(root, text="Weather forecast", width=14, font=12, bg="salmon", command=get_forecast)
btn_reset = Button(root, text="Reset", font=12, bg="salmon", command=reset)



label2 = Label(root, text="Temperature :", font=("bold", 12), bg="darkorange")
label3 = Label(root, text="Pressure :", font=("bold", 12), bg="greenyellow")
label4 = Label(root, text="Humidity :", font=("bold", 12), bg="pink")
label5 = Label(root, text="Wind :", font=("bold", 12), bg="mediumslateblue")
label6 = Label(root, text="Cloudiness :", font=("bold", 12), bg="cyan")
label7 = Label(root, text="Description :", font=("bold", 12), bg="hotpink")

temp_field = Entry(root, width=24, font=11)
pressure_field = Entry(root, width=24, font=11)
humid_field = Entry(root, width=24, font=11)
wind_field = Entry(root, width=24, font=11)
cloud_field = Entry(root, width=24, font=11)
desc_field = Entry(root, width=24, font=11)

# Update this line to center the title, assuming 3 is the total number of columns used
title.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

label1.grid(row=1, column=0, padx=5, pady=5, sticky="W")
timelabel.grid(row=1, column=2)
btn_submit.grid(row=2, column=1, pady=5)
btn_forecast.grid(row=2, column=2, pady=5)
label2.grid(row=3, column=0, padx=5, pady=5, sticky="W")
label3.grid(row=4, column=0, padx=5, pady=5, sticky="W")
label4.grid(row=5, column=0, padx=5, pady=5, sticky="W")
label5.grid(row=6, column=0, padx=5, pady=5, sticky="W")
label6.grid(row=7, column=0, padx=5, pady=5, sticky="W")
label7.grid(row=8, column=0, padx=5, pady=5, sticky="W")

city_input.grid(row=1, column=1, padx=5, pady=5)
temp_field.grid(row=3, column=1, padx=5, pady=5)
pressure_field.grid(row=4, column=1, padx=5, pady=5)
humid_field.grid(row=5, column=1, padx=5, pady=5)
wind_field.grid(row=6, column=1, padx=5, pady=5)
cloud_field.grid(row=7, column=1, padx=5, pady=5)
desc_field.grid(row=8, column=1, padx=5, pady=5)
btn_reset.grid(row=9, column=1, pady=5)


root.mainloop()