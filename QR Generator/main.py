from tkinter import*;
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator | Developed By Niket")
        self.root.resizable(False,False)
        
        title=Label(self.root,text="  QR Code Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        
 #=====Employee Details=====
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_designation=StringVar()
        
        emp_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_frame.place(x=50,y=100,width=500,height=360)
        emp_title=Label(emp_frame,text="Employee Details",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
        
        lbl_emp_code=Label(emp_frame,text="Employee ID",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_emp_name=Label(emp_frame,text="Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_emp_dept=Label(emp_frame,text="Departmant",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_emp_designation=Label(emp_frame,text="Designation",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)
        
        txt_emp_code=Entry(emp_frame,font=("times new roman",15),textvariable=self.var_emp_code,bg='lightyellow').place(x=200,y=60)
        txl_emp_name=Entry(emp_frame,font=("times new roman",15),textvariable=self.var_name,bg='lightyellow').place(x=200,y=100)
        txt_emp_dept=Entry(emp_frame,font=("times new roman",15),textvariable=self.var_dept,bg='lightyellow').place(x=200,y=140)
        txt_emp_designation=Entry(emp_frame,font=("times new roman",15),textvariable=self.var_designation,bg='lightyellow').place(x=200,y=180)
        
        btn_generate=Button(emp_frame,text='Generate QR',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=50,y=260,width=180,height=40)
        btn_clear=Button(emp_frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=250,y=260,width=180,height=40)
        
        self.msg=''
        self.lbl_msg=Label(emp_frame,text=self.msg,font=("times new roman",20),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1)
        
#=====Employee QR Code Generator=====       
        qr_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_frame.place(x=600,y=100,width=250,height=360)
        emp_title=Label(qr_frame,text="Employee QR Code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
        
        self.qr_code=Label(qr_frame,text='No QR Code \navailable',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180) 
        
    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_dept.set('')
        self.var_designation.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')
        

    def generate(self):
        if self.var_designation.get()=='' or self.var_emp_code.get()=='' or self.var_dept.get()=='' or self.var_name.get()=='':
            self.msg='All Fields are Required!!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Employee ID: {self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\nDepartment:{self.var_dept.get()}\nDesignation:{self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Employee QR/Emp_"+str(self.var_emp_code.get())+'.png')
            #====QR code image update======
            self.im=ImageTk.PhotoImage(file="Employee QR/Emp_"+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.im)
            #====Updating notification=====
            self.msg='QR Code Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg,fg='green')
            
        
        
root=Tk()
obj=Qr_Generator(root)
root.mainloop()
