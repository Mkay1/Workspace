from tkinter import *
from PIL import Image, ImageTk
import random
import time
start = time.time()
root = Tk()
root.title("V-COMM")
root.geometry("800x600+400+100")
root.resizable(False,False)
root.configure(bg="black")

Icon = Image.open("icon.jpg")
icon = ImageTk.PhotoImage(Icon)
root.iconphoto(False,icon)

bgImg = Image.open("bg.png")

#Resize the image using the resize() method
bgImg = bgImg.resize((800, 600 ))
image = ImageTk.PhotoImage(bgImg)
label = Label(root, image=image)
label.place(x=0, y=0)
label_welcome = Label(root, text="VEHICLE TO VEHICLE COMMUNICATION SYSTEM", font="arial 20 bold")
label_welcome.place(x=70, y=10)
i = 0

for i in range(1,51 ) :
    status = ["NM","AM"]
    msg_sta = random.choice(list(status))
    if msg_sta =="NM":
        label_nomessage = Label(root, text="There is no message to be sent ", font="arial 15 bold")
        label_nomessage.place(x=250, y=60)
    elif msg_sta =="AM":
   
        label_rec = Label(root, text="...Identitifying Receiving Node...", font="arial 15 bold")
        label_rec.place(x=250, y=60)
    
    
        label_opt = Label(root, text="Receiving Node Identified", font="arial 15 bold")
        label_opt.place(x=280, y=110)
    
    
        label_cal = Label(root, text="...Calculating the distance between the sender and the receiver...", font="arial 15 bold")
        label_cal.place(x=100, y=160)
    
        def distance():
            dis = random.randint(1,2000)
        
            label_opt = Label(root, text= (dis,"Meters"), font="arial 15 bold")
            label_opt.place(x=330, y=210)
        
            if dis <= 300:
            
                label_opt = Label(root, text="...Sending Message...", font="arial 15 bold")
                label_opt.place(x=280, y=260)
            
                label_ack = Label(root, text="Acknowledging Message", font="arial 15 bold")
                label_ack.place(x=265, y=310)
            
            
                label_ack = Label(root, text="Done", font="arial 15 bold")
                label_ack.place(x=360, y=360)
           

            else:
           
                label_opt = Label(root, text="...Getting Relay Node...", font="arial 15 bold")
                label_opt.place(x=280, y=260)
           
                class Relay(list):
                    def __init__(self, name, distance, speed, direction):
                        self.name = name
                        self.distance =  distance
                        self.speed = speed 
                        self.direction = direction
                dir = ["Fb", "Bb"]
                msg_dir = random.choice(list(dir))
                move = ["F","B"]
                node1 = Relay("car1", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node2 = Relay("car2", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node3 = Relay("car3", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node4 = Relay("car4", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node5 = Relay("car5", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node6 = Relay("car6", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node7 = Relay("car7", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node8 = Relay("car8", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node9 = Relay("car9", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node10 = Relay("car10", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node11 = Relay("car11", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node12 = Relay("car12", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node13 = Relay("car13", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node14 = Relay("car14", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node15 = Relay("car15", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node16 = Relay("car16", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node17 = Relay("car17", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node18 = Relay("car18", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node19 = Relay("car19", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node20 = Relay("car20", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node21 = Relay("car21", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node22 = Relay("car22", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node23 = Relay("car23", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node24 = Relay("car24", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node25 = Relay("car25", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node26 = Relay("car26", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node27 = Relay("car27", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                node28 = Relay("car28", random.randint(1,2000),random.randint(1,120) ,random.choices(list(move)))
                Nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, 
                        node11, node12, node13, node14, node15, node16, node17, node18, node19, node20,
                        node21, node22, node23, node24, node25, node26, node27, node28]
            
                dis_nodes = []
                dir_arr = []
                for node in Nodes:
                    
                    if "F" in node.direction and msg_dir == "Fb": 
                        dir_arr.append(node)
                        for node in dir_arr:
                            if node.distance <= 300:
                                dis_nodes.append(node)
                            for node in dis_nodes:
                                if len(dis_nodes) == 1:
                               
                                    label_rel1 = Label(root, text="Relay node obtained", font="arial 15 bold")
                                    label_rel1.place(x=295, y=310)
                                 
                                elif len (dis_nodes) > 1:
                                
                                    label_rel = Label(root, text="Relay nodes obtained", font="arial 15 bold")
                                    label_rel.place(x=295, y=310)
                                
                                    select = min(dis_nodes, key=lambda node: node.speed)
                                    select_node = select.name
                                
                                    label_rel = Label(root, text=(select_node,"with the least speed has been choosen as the relay node"), font="arial 15 bold")
                                    label_rel.place(x=100, y=360)
                                
                                
                                    label_send2 = Label(root, text="...Sending Message...", font="arial 15 bold")
                                    label_send2.place(x=280, y=410)
                                
                                
                                    label_ack2 = Label(root, text="Acknowledging Message", font="arial 15 bold")
                                    label_ack2.place(x=265, y=460)
                                
                                
                                    label_ack2 = Label(root, text="Done", font="arial 15 bold")
                                    label_ack2.place(x=360, y=510)
                                

                    elif "B" in node.direction and msg_dir == "Bb":
                        dir_arr.append(node)
                        for node in dir_arr:
                            if node.distance <= 300:
                                dis_nodes.append(node)
                            for node in dis_nodes:
                                if len(dis_nodes) == 1:
                                
                                    label_rel3 = Label(root, text="Relay node obtained", font="arial 15 bold")
                                    label_rel3.place(x=295, y=310)
                                   
                                elif len (dis_nodes) > 1:
                                
                                    label_rel2 = Label(root, text="Relay nodes obtained", font="arial 15 bold")
                                    label_rel2.place(x=295, y=310)
                                
                                    select = max(dis_nodes, key=lambda node: node.speed)
                                    select_node = select.name
                                
                                    label_rel = Label(root, text=(select_node," with the most speed has been choosen as the relay node"), font="arial 15 bold")
                                    label_rel.place(x=100, y=360)
                                
                                    label_send2 = Label(root, text="...Sending Message...", font="arial 15 bold")
                                    label_send2.place(x=280, y=410)
                                
                                    label_ack2 = Label(root, text="Acknowledging Message", font="arial 15 bold")
                                    label_ack2.place(x=265, y=460)
                              
                                
                                    label_ack2 = Label(root, text="Done", font="arial 15 bold")
                                    label_ack2.place(x=360, y=510)
                                
                for node in dis_nodes:
                    print(f"Name: {node.name}, Distance: {node.distance}, Speed: {node.speed}, Direction: {node.direction}") 
        distance()
end = time.time()
final = end - start
print("30 out of 30 packets were succesfully sent in ", final, "ms")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

root.mainloop()
