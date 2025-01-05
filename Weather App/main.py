from tkinter import *
from geopy.geocoders import Photon
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


def getWeather():
    try:
        city = textentry.get()
        geolocator = Photon(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat= location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weathercc252560eeb02426d2fc20cfc4f76a3e
        api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cc252560eeb02426d2fc20cfc4f76a3e"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data ['main']["temp"]-273.15)
        pressure = json_data ['main']["pressure"]
        humidity = json_data ['main']["humidity"]
        wind = json_data ['wind']["speed"]

        t.config(text=(temp ,"°"))
        c.config(text=(condition, "|", "FEELS", "LIKES",temp, "°" ))

        w.config(text= wind)
        h.config(text= humidity)
        d.config(text= description)
        p.config(text= pressure)
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Location Entry")
Icon = Image.open("logo.jpeg")
icon = ImageTk.PhotoImage(Icon)
root.iconphoto(False,icon)

#Search box
search_image = PhotoImage(file="Copy of search.png")
myimage = Label(image= search_image)
myimage.place(x=20, y=20)

textentry = Entry(root, justify="center", width=17, font=("poppins",25, "bold"), bg="#404040", border=0, fg="white")
textentry.place(x=50, y=40)
textentry.focus()

search_icon = PhotoImage(file="Copy of search_icon.png")
myimage_icon = Button(image= search_icon,borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

#Logo
Logo_image = PhotoImage(file="logo2.png")
logo = Label(image= Logo_image)
logo.place(x=150, y=100)

#Bottom box
Frame_image = PhotoImage(file="Copy of box.png")
frame_myimage = Label(image= Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

#time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 15))
clock.place(x=30, y=130)
#label
label1 = Label (root, text="WIND", font=("Helvetica",15, "bold"), bg="#1ab5ef", fg="white")
label1.place(x=120, y=400)

label2 = Label (root, text="HUMIDITY", font=("Helvetica",15, "bold"), bg="#1ab5ef", fg="white")
label2.place(x=250, y=400)

label3 = Label (root, text="DESCRIPTION", font=("Helvetica",15, "bold"), bg="#1ab5ef", fg="white")
label3.place(x=430, y=400)

label4 = Label (root, text="PRESSURE", font=("Helvetica",15, "bold"), bg="#1ab5ef", fg="white")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="",font=("arial", 15, "bold"), bg="#1ab5ef")
w.place(x=125, y=430)
h = Label(text="",font=("arial", 15, "bold"), bg="#1ab5ef")
h.place(x=285, y=430)
d = Label(text="",font=("arial", 15, "bold"), bg="#1ab5ef")
d.place(x=430, y=430)
p = Label(text="",font=("arial", 15, "bold"), bg="#1ab5ef")
p.place(x=685, y=430)


root.mainloop()
#
#cc252560eeb02426d2fc20cfc4f76a3e