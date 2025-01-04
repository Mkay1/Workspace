from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("BMI Calculator")
root.geometry("400x700+1000+150")
root.resizable(False,False)
root.configure(bg="black")

Icon = Image.open("bmi1.png")
icon = ImageTk.PhotoImage(Icon)
root.iconphoto(False,icon)

Img = Image.open("nice.jpeg")

def bmi():
    try:
        weight = float(w.get())
        height = float(h.get())
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and Height must be positive numbers.")
            return
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        if bmi < 18.5:
            status = "Under weight"
            rem = (24 * (height**2)) - weight
            ad = "You would need to add %dkg \nto get to the normal weight"%(rem)
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
            ad = "  Keep maintaining a proper \nfeeding route and work \nout regularly"
        elif 25 <= bmi < 29.9:
            status = "Over weight"
            lose = weight - (24 * (height**2))
            ad = "You would need to lose %dkg \nto get to the normal weight"%(lose)
        else:
            status = "Obesity"
            lose = weight - (24 * (height**2))
            ad = "You would need to lose %dkg \nto get to the normal weight"%(lose)
        w.delete(0, END)
        h.delete(0, END)
        l1.config(text=f"Your BMI is: {bmi}")
        l2.config(text=f"Your are: {status}")
        l3.config(text=f"{ad}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")
        
    
#Resize the image using the resize() method
img = Img.resize((400, 250))
image = ImageTk.PhotoImage(img)
label = Label(root, image=image)
label.place(x=0, y=0)
Label(root, text="BMI CALCULATOR", font=("arial", 20, "bold"),bg="black", fg="white").place(x=70, y=260)
Label(root, text="Enter Your Weight (kg)", font=("arial", 15, "bold"),bg="black", fg="white").place(x=25, y=320)
w = Entry(root, justify=CENTER,font=("arial", 15),bg="white", fg="black", width=10)
w.place(x=255, y=320) 
Label(root, text="Enter Your height (m)", font=("arial", 15, "bold"),bg="black", fg="white").place(x=25, y=380)
h = Entry(root, justify=CENTER,font=("arial", 15),bg="white", fg="black", width=10)
h.place(x=255, y=380) 
btn = Button(root,text="Calculate", font=("arial",15, "bold"),bg="white", fg="black", command=bmi )
btn.place(x=150, y=440)
frame = Frame(root, width=300, height=150)
frame.place(x=50, y=500)
l1 = Label(frame, text="", font=("arial", 15, "bold"), fg="black")
l1.place(x=60, y=10)
l2 = Label(frame, text="", font=("arial", 15, "bold"), fg="black")
l2.place(x=35, y=40)
l3 = Label(frame, text="", font=("arial", 15, "bold"), fg="black")
l3.place(x=10, y=70)





#Entry(root, justify=CENTER,font=("arial", 15),bg="white", fg="black", width=10).place(x=255, y=320)













root.mainloop()