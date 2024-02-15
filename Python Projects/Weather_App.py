from tkinter import *
from tkinter import ttk
import requests


def get_data():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=766f0d9dfb7b9618f208fe2efb33f550").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    wt_label1.config(text=str(data["main"]["temp"]-273.15))
    wp_label1.config(text=data["main"]["pressure"])




win = Tk()
win.title("Weather App")
win.config(bg='#3e3e3e')
win.geometry("500x570")

name_label = Label(win, text="My Weather App",
                   font=("Time New Roman", 30, "bold"))

name_label.place(x=25, y=50, height=60, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text="My Weather App", values=list_name,
                   font=("Time New Roman", 30, "bold"), textvariable=city_name)

com.place(x=25, y=120, height=60, width=450)


w_label = Label(win, text="Weather Climate",
                font=("Times New Roman", 15, ))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="",
                font=("Times New Roman", 15, ))
w_label1.place(x=250, y=260, height=50, width=210)


wb_label = Label(win, text="Weather Description",
                font=("Times New Roman", 15, ))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label1 = Label(win, text="",
                font=("Times New Roman", 15, ))
wb_label1.place(x=250, y=330, height=50, width=210)


wt_label = Label(win, text="Temprature",
                font=("Times New Roman", 15, ))
wt_label.place(x=25, y=400, height=50, width=210)

wt_label1 = Label(win, text="",
                font=("Times New Roman", 15, ))
wt_label1.place(x=250, y=400, height=50, width=210)


wp_label = Label(win, text="Pressure",
                font=("Times New Roman", 15, ))
wp_label.place(x=25, y=470, height=50, width=210)

wp_label1 = Label(win, text="",
                font=("Times New Roman", 15, ))
wp_label1.place(x=250, y=470, height=50, width=210)


done_button = Button(win, text="Done",
                   font=("Time New Roman", 15, "bold"), command=get_data)

done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()