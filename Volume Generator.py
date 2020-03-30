import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class VolumeGenerator(tk.Tk):

    ''' The Labels '''
  
    def Label(self,t,r,c):
        a = tk.Label(
            text = t,
            font = ("Calibri",16)
        )
        a.grid(row = r, column = c)

    ''' The OTHER Labels '''
        
    def miscLabels(self,t,x,y):
        a = tk.Label(
            text = t,
            font = ("Calibri",14)
        )
        a.place(x = x , y = y)    

    ''' The text boxes '''
    def validation(self):
        
        layout =tk.StringVar()
        length =tk.StringVar()
        width  =tk.StringVar()
        height =tk.StringVar()
        radius =tk.StringVar()
        output =tk.StringVar()
        
        self.shape = ttk.Combobox(
            width = 10,
            font = ("Calibri",14),
            textvariable = layout,
            state = "readonly"
        )
        self.shape['values'] = ("Cube" , "Cuboid" , "Cylinder" , "Cone" , "Sphere" , "Hemisphere")
        self.shape.place(x = 175, y = 2)     
        
        self.length = tk.Entry(
            width = 9,
            font = ("Calibri",16),
            textvariable = length
        )
        self.length.place(x = 195,y = 33)
        
        self.width = tk.Entry(
            width = 9,
            font = ("Calibri",16),
            textvariable = width
        )
        self.width.place(x = 195, y = 63)
        
        self.height = tk.Entry(
            width = 9,
            font = ("Calibri",16),
            textvariable = height
        )
        self.height.place(x = 195,y = 93)
        
        self.radius = tk.Entry(
            width = 9,
            font = ("Calibri",16),
            textvariable = radius
        )
        self.radius.place(x = 195,y = 123)  
        
        self.volume = tk.Entry(
            width = 10,
            font = ("Calibri",28),
            textvariable = output,
            state = "readonly"
            )
        self.volume.place(x = 10,y = 210)
        
        ''' The commands for the buttons '''
        
        def result():
            s = (layout.get())
            l = (length.get())
            w = (width.get())
            h = (height.get())
            r = (radius.get())

            pi = 22 / 7
            
            if (s == "Cube") and (l.isdigit()):
                l = int(l)
                
                v = l ** 3
                v = round(v,2)
                output.set(v)
                                
            elif (s == "Cuboid") and (l.isdigit() and w.isdigit() and h.isdigit()):
                l = int(l)
                w = int(w)
                h = int(h)
                
                v = l * w * h
                v = round(v,2)
                output.set(v)
            
            elif (s == "Cylinder") and (h.isdigit() and r.isdigit()):
                h = int(h)
                r = int(r)
                
                v = pi * ( r ** 2 ) * h
                output.set(v)

            elif (s == "Cone") and (h.isdigit() and r.isdigit()):
                h = int(h)
                r = int(r)
                
                v = 1 / 3 * ( pi * ( r ** 2 ) * h )
                v = round(v,2)
                output.set(v)
                                
            elif (s == "Sphere") and (r.isdigit()):
                r = int(r)
                v = 4 / 3 * ( pi * r ** 3 )
                v = round(v,2)
                output.set(v)
                                
            elif (s == "Hemisphere") and (r.isdigit()):
                r = int(r)
                v = 2 / 3 * ( pi * r ** 3)
                v = round(v,2)
                output .set(v)
                                    
            else:
                tk.messagebox.showwarning(" Invalid Input!", "Please fill in only with integers and the other fields.") 
                    
        def clear():
            layout.set("")
            length.set("")
            width.set("")
            height.set("")
            radius.set("")
            output.set("") 
              
        ''' The Buttons '''
             
        self.BtnResult = tk.Button(
            text = "Find Volume",
            font = ("Calibri",16),
            command = result
        )
        self.BtnResult.place(x = 10 , y = 350)
        
        self.BtnClear = tk.Button(
            text = "Clear",
            font = ("Calibri",16),
            command = clear
        )
        self.BtnClear.place(x = 220 , y = 350)

''' The important loop '''

if __name__ == "__main__":
        root = VolumeGenerator()
        root.title("Volume Generator")
        root.geometry("300x445+10+10")
        root.resizable(0,0)
        
        root.Label("3D Shape",0,1)
        root.Label("Length",3,1)
        root.Label("Width",6,1)
        root.Label("Height",9,1)
        root.Label("Radius",12,1)
        
        root.Label("Volume:",18,1)
        
        root.miscLabels("cc.units",210,220)
        
        root.validation()
              
        root.mainloop()
