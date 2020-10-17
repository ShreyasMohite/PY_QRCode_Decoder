from tkinter import *
from PIL import Image
from tkinter.filedialog import asksaveasfile 
from tkinter import filedialog
from pyzbar.pyzbar import decode
import tkinter.messagebox

class Decode:
    def __init__(self,root):
        self.root=root
        self.root.title("DECODE QR CODE")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo428.ico")
        self.root.resizable(0,0)


        paths=StringVar()

        #=========================================================#
        def on_enter1(e):
            but_select['background']="black"
            but_select['foreground']="cyan"  
        def on_leave1(e):
            but_select['background']="SystemButtonFace"
            but_select['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter3(e):
            but_genarate['background']="black"
            but_genarate['foreground']="cyan"  
        def on_leave3(e):
            but_genarate['background']="SystemButtonFace"
            but_genarate['foreground']="SystemButtonText"

        #=========================command=========================#
        def clear():
            text.delete("1.0","end")
            lab_select.config(text="Select Only QR Image")

        def browse():
            global filename
            file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("png files","*.png"),("all files","*.*"))) 
            filename = file_path
            if file_path:
                lab_select.config(text="Images is Selected")

        def Decode():
            try:
                d=decode(Image.open(filename))
                x=d[0].data.decode('ascii')
                text.insert("end",x)            
            except:
                tkinter.messagebox.showerror("Error","No path is selected/Not a QR Code")

        #=========================frame===========================#
        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=493,height=300,relief="ridge",bd=3)
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=493,height=93,relief="ridge",bd=3,bg="#495057")
        secondframe.place(x=0,y=300)

        #===========================firstframe=================================#

        topframe=Frame(firstframe,width=486,height=150,relief="ridge",bd=3,bg="#a100f2")
        topframe.place(x=0,y=0)

        bottomframe=Frame(firstframe,width=486,height=143,relief="ridge",bd=3)
        bottomframe.place(x=0,y=150)

        #======================================================================#
        
        but_select=Button(topframe,text="Browse QR Image",width=20,font=('times new roman',12,'bold'),cursor="hand2",command=browse)
        but_select.place(x=140,y=30)
        but_select.bind("<Enter>",on_enter1)
        but_select.bind("<Leave>",on_leave1)

        lab_select=Label(topframe,text="Select Only QR Image",font=('times new roman',12),bg="#a100f2")
        lab_select.place(x=160,y=80)

        lab_message=Label(topframe,text="Decode Message",font=('times new roman',12,'bold'),bg="#a100f2",fg="white")
        lab_message.place(x=170,y=110)

        #======================================================================#

        scol=Scrollbar(bottomframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(bottomframe,height=7,width=57,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)
        



        #===========================secondframe=================================#

        but_clear=Button(secondframe,text="Clear",width=20,font=('times new roman',12,'bold'),cursor="hand2",command=clear)
        but_clear.place(x=40,y=30)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


        but_genarate=Button(secondframe,text="Decode QR Code",width=20,font=('times new roman',12,'bold'),cursor="hand2",command=Decode)
        but_genarate.place(x=250,y=30)
        but_genarate.bind("<Enter>",on_enter3)
        but_genarate.bind("<Leave>",on_leave3)
         




if __name__ == "__main__":
    root=Tk()
    app=Decode(root)
    root.mainloop()