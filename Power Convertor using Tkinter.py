#T1v9 Power Convertor using Tkinter 


from tkinter import *
root=Tk()
root.geometry("600x250")
root.minsize(100,100)
root.maxsize(600,400)
root.title("T1v9 Power Convertor")


def convertHPtoWATTS():
    if(entry.get()==""):
        result_label.config(text="Error: Horsepower amount cannot be empty")
    elif(entry.get().isalpha()):   
        result_label.config(text="Error : Horsepower amount cannot be non numeric value") 
    elif any(char in set('!@#$%^&*()_+[]{}|;:,.<>?`~') for char in entry.get()):
        result_label.config(text="Error : Horsepower amount cannot be special characters") 
    elif(" " in entry.get()):
        result_label.config(text="Error:Horsepower amount cannot contain spaces")
    elif(int(entry.get())<0):
        result_label.config(text="Error : Horsepower amount cannot be negative value") 
    elif not (0 <= float(entry.get()) <= 1000):
        result_label.config(text="Error: Horsepower amount is not in the min-max range") 
    else:   
        hp = float(entry.get())
        watts = hp * 745.7

        # Updating the labelwith the result
        result_label.config(text=f"{hp} HP = {watts:.2f} Watts")

def convertWATTStoHP():
    if(entry2.get()==""):
        result_label.config(text="Error: Watts amount cannot be empty")
    elif(entry2.get().isalpha()):   
        result_label.config(text="Error : Watts amount cannot be non numeric value") 
    elif any(char in set('!@#$%^&*()_+[]{}|;:,.<>?`~') for char in entry2.get()):
            result_label.config(text="Error : Watts amount cannot be special characters") 
    elif(" " in entry2.get()):
        result_label.config(text="Error:Watts amount cannot contain spaces")  
    elif(int(entry2.get())<0):
        result_label.config(text="Error : Watts amount cannot be negative value") 
    elif not (0 <= float(entry2.get()) <= 1000):
        result_label.config(text="Error:  Watts amount  is not in the min-max range")  
    else:   
        w = float(entry2.get())
        h = w / 745.7

        # Updating the labelwith the result
        result_label.config(text=f"{w} Watts = {h:.2f} HP")


# Creating a label  for horsepower input
Label(root, text="Enter Horsepower:",font=("arial",12,"bold")).grid(row=0,column=0)


# Creating a Entry for horsepower input
entry = Entry(root,width=25,font=("arial",10))
entry.grid(row=1,column=0,pady=20,padx=40)

# Creating a button to make GUI interactive
convert_button=Button(root, text="Convert HP to Watts",bg="pink",fg="red",borderwidth=5, relief=RAISED,font=("arial",10,"bold"),command=convertHPtoWATTS)
convert_button.grid(row=2,column=0)


# Creating a  label  for watts input
Label(root, text="Enter Watts:",font=("arial",12,"bold")).grid(row=0,column=1)
entry2 = Entry(root,width=25,font=("arial",10))
entry2.grid(row=1,column=1,pady=20,padx=40)

# Creating a button to make GUI interactive
convert_button=Button(root, text="Convert Watts to HP",bg="pink",fg="red",borderwidth=5, relief=RAISED,font=("arial",10,"bold"),command=convertWATTStoHP)
convert_button.grid(row=2,column=1)


# Creating a label to show the final result(i.e conversion)
result_label = Label(root,bg="white",fg="black",relief=RAISED,font=("arial",13,"bold"))
result_label.place(anchor = CENTER, relx = .45, rely = .65)





















root.mainloop()

