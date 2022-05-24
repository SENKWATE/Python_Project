import os
from itertools import islice
from tkinter import filedialog, messagebox
from tkinter import *



def clearToTextInput():
   txtarea.delete("1.0","end")
   input_path.delete(0,END)
   output_path.delete(0,END)


def splitFile():
    lines_per_channel = 120003
    file_path = input_path.get()
    folder_path = output_path.get()
    with open(file_path) as file:
        channel_No = 1
        while True:
            try:
                checker = next(file)
                with open(f"{folder_path}/channel_{channel_No}.txt", 'w') as output_channel_file:
                    output_channel_file.write(checker)
                    for line in islice(file, lines_per_channel-1):
                        output_channel_file.write(line)
            except StopIteration:
                messagebox.showinfo("Information","Channel file(s) has been split successsfully")
                txtarea.delete("1.0","end")
                input_path.delete(0,END)
                output_path.delete(0,END)
                break
        
            channel_No += 1

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="./", 
        title="Open Text file", 
        filetypes=(("Text Files", ["*.asc","*.txt"]),)
        )
    input_path.insert(END, tf)
    if(tf):
        tf = open(tf, 'r')
        data = tf.read()
        txtarea.insert(END, data)
        tf.close()


def outputFile():
    tf = filedialog.askdirectory(
        initialdir="./", 
        title="Open Text file", 
        )
    output_path.insert(END, tf)



app = Tk()
app.title("Create a seperate file for each channel")
app_width = 520
app_height = 600
app.geometry(f"{app_width}x{app_height}")
app.eval('tk::PlaceWindow . center')

# get the screen size of your computer [width and height using the root object as foolows]
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
# Get the window position from the top dynamically as well as position from left or right as follows
position_top = int(screen_height/2 -app_height/2)
position_right = int(screen_width / 2 - app_width/2)
# this is the line that will center your window
app.geometry(f'{app_width}x{app_height}+{position_right}+{position_top}')



txtarea = Text(app, width=60, height=30)
txtarea.pack(pady=20)

input_path = Entry(app,width=30)
input_path.place(x=20,y=450)

Button(app, text="Clear", height=1,width=5,command=clearToTextInput).place(x=310,y=447)
Button(app, text="Import File", command=openFile).place(x=400,y=447)


output_path = Entry(app,width=40)
output_path.place(x=20,y=500)
Button(app, text="Output File", command=outputFile).place(x=400,y=500)

Button(app, text="Split File", command=splitFile,width=8).place(x=200,y=550)

# input_path.pack(side=LEFT, padx=20)
# Button(app, text="Clear", height=1,width=5,command=clearToTextInput).pack(side=LEFT,expand=True)
# Button(app, text="Open File", command=openFile).pack(side=RIGHT, expand=True, fill=X, padx=20)

# out_path = Entry(app)
# out_path.pack(side=LEFT, expand=True, fill=X, padx=30)
# Button(app, text="Open File", command=openFile).pack(side=RIGHT, expand=True, fill=X, padx=20)


app.mainloop()

