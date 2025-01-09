from tkinter import *
from PIL import Image, ImageTk
import os
import shutil

def run():
    where = w.get()
    directory = os.path.join(os.path.expanduser("~"), where)

    extensions = {
        ".doc" : "Documents",
        ".docx" : "Documents",
        ".xls" : "Documents",
        ".xlsx" : "Documents",
        ".wpd" : "Documents",
        ".txt" : "Documents",
        ".pdf" : "Documents",
        ".jpg" : "Images", 
        ".jpeg" : "Images",
        ".png" : "Images",
        ".gif" : "Images",
        ".bmp" : "Images", 
        ".eps" : "Images",
        ".svg" : "Images", 
        ".webp" : "Images",
        ".tiff" : "Images", 
        ".psd" : "Images",
        ".mp3" : "Music",
        ".wav" : "Music",
        ".mpc" : "Music",
        ".msv" : "Music",
        ".mp4" : "Videos",
        ".mov" : "Videos",
        ".webm" : "Videos",
        ".flv" : "Videos"
    }
    for filename in os. listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            extension = os.path.splitext (filename) [1]. lower ()
            if extension in extensions:
                folder_name = extensions [extension]
                folder_path = os. path. join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                destination_path = os. path. join(folder_path, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved (filename' to {folder_name} folder.")
            else:
                print(f"Skipped {filename}. Unknown file extension.")
        else:
            print(f"Skipped {filename}. It is a directory.")

    print("File organization completed.")

root = Tk()
root.title("File Organizer App")
root.geometry("350x250+1000+150")
root.resizable(False,False)

root.configure(bg="black")
vartype = StringVar
Icon = Image.open("file.jpg")
icon = ImageTk.PhotoImage(Icon)
root.iconphoto(False,icon)

Label(root, text="FILE ORGANIZER APP", font=("arial", 17, "bold"),bg="black", fg="white").pack(pady=10)
Label(root, text="Which folder would you like to organize ?", font=("arial", 12, "bold"),bg="black", fg="white").pack(pady=20)
w = Entry(root, justify=CENTER,font=("arial", 15),textvariable= vartype,bg="white", fg="black", width=15)
w.pack(pady=10) 
btn = Button(root,text="Run", font=("arial",15, "bold"),bg="white", fg="black", command=run )
btn.pack(pady=20)
Label(root, text="", font=("arial", 12, "bold"),bg="black", fg="white").pack(pady=5)

root.mainloop() 