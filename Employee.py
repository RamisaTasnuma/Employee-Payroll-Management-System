
from tkinter import *
class EmployeeSystem:
      def __init__(self,root): 
        self.root=root
        self.root.title('EmPloyee Payroll Management System | Developed by Ramisa')
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Employee Payroll Management System",  font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        
        #----------Frame1----------------
        #------variables------
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_experience=StringVar()
        self.var_proof_id=StringVar()#----National ID-----
        self.var_contact=StringVar()
        self.var_status=StringVar()



        Frame1=Frame(self.root,bd=3,relief=RIDGE, bg="white")
        Frame1.place(x=10,y=70, width=750, height=710)
        title2=Label(Frame1,text="Employee Details",  font=("times new roman",15,"bold"),bg="red4",fg="ivory2",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        lbl_code=Label(Frame1,text="Employee Code",  font=("times new roman",15),bg="white",fg="black").place(x=10,y=60)
        
        
        txt_code=Entry(Frame1, font=("times new roman",12),textvariable=self.var_emp_code,bg="lightyellow",fg="black").place(x=150,y=65, width=200)
        btn_search=Button(Frame1,text="Search",  font=("times new roman",13, "bold"),bg="red4",fg="white").place(x=380,y=65,  height=30)
        
        
        #_________row1_________
        lbl_designation=Label(Frame1,text="Designation",  font=("times new roman",15),bg="white",fg="black").place(x=10,y=110)
        txt_designation=Entry(Frame1, font=("times new roman",12),textvariable=self.var_designation,bg="lightyellow",fg="black").place(x=150,y=110, width=200)
        lbl_dob=Label(Frame1,text="D.O.B",  font=("times new roman",15),bg="white",fg="black").place(x=380,y=110)
        txt_dob=Entry(Frame1, font=("times new roman",12),textvariable=self.var_dob,bg="lightyellow",fg="black").place(x=490,y=110)
        #---------row2_________________
        lbl_name=Label(Frame1,text="Name",  font=("times new roman",15),bg="white",fg="black").place(x=10,y=170)
        txt_name=Entry(Frame1, font=("times new roman",12),textvariable=self.var_name,bg="lightyellow",fg="black").place(x=150,y=170, width=200)
        lbl_doj=Label(Frame1,text="D.O.J",  font=("times new roman",15),bg="white",fg="black").place(x=380,y=170)
        txt_doj=Entry(Frame1, font=("times new roman",12),textvariable=self.var_doj,bg="lightyellow",fg="black").place(x=490,y=170)

        #---------row3_________________
        lbl_age=Label(Frame1,text="Age",  font=("times new roman",15),bg="white",fg="black").place(x=10,y=220)
        txt_age=Entry(Frame1, font=("times new roman",12),textvariable=self.var_age,bg="lightyellow",fg="black").place(x=150,y=220, width=200)
        lbl_experience=Label(Frame1,text="Experience",  font=("times new roman",15),bg="white",fg="black").place(x=380,y=220)
        txt_experience=Entry(Frame1, font=("times new roman",12),textvariable=self.var_experience,bg="lightyellow",fg="black").place(x=490,y=220)

        #---------row4_________________
        lbl_gender=Label(Frame1,text="Gender",  font=("times new roman",15),bg="white",fg="black").place(x=10,y=270)
        txt_gender=Entry(Frame1, font=("times new roman",12),textvariable=self.var_gender,bg="lightyellow",fg="black").place(x=150,y=270, width=200)
        lbl_proof=Label(Frame1,text="Proof of ID",  font=("times new roman",15),bg="white",fg="black").place(x=380,y=270)
        txt_proof=Entry(Frame1, font=("times new roman",12),textvariable=self.var_proof_id,bg="lightyellow",fg="black").place(x=490,y=270)

        #---------row5_________________
        lbl_email=Label(Frame1,text="Email",  font=("times new roman",15),bg="white",fg="black").place(x=10,y=320)
        txt_email=Entry(Frame1, font=("times new roman",12),textvariable=self.var_email,bg="lightyellow",fg="black").place(x=150,y=320, width=200)
        lbl_contact=Label(Frame1,text="Contact",  font=("times new roman",15),bg="white",fg="black").place(x=380,y=320)
        txt_contact=Entry(Frame1, font=("times new roman",12),textvariable=self.var_contact,bg="lightyellow",fg="black").place(x=490,y=320)


        #---------row6_________________
        lbl_hired=Label(Frame1,text="Hired Location",  font=("times new roman",13),bg="white",fg="black").place(x=10,y=372)
        txt_hired=Entry(Frame1, font=("times new roman",12),textvariable=self.var_hr_location,bg="lightyellow",fg="black").place(x=150,y=370, width=200)
        lbl_status=Label(Frame1,text="Status",  font=("times new roman",15),bg="white",fg="black").place(x=380,y=370)
        txt_status=Entry(Frame1, font=("times new roman",12),textvariable=self.var_status,bg="lightyellow",fg="black").place(x=490,y=370)

         #---------row7_________________
        lbl_address=Label(Frame1,text="Address",  font=("times new roman",13),bg="white",fg="black").place(x=10,y=432)
        self.txt_address=Text(Frame1, font=("times new roman",12),bg="lightyellow",fg="black")
        self.txt_address.place(x=150,y=420, width=500, height=220)
       

        #----------Frame2----------------
        #------variables------
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_t_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()






        Frame2=Frame(self.root,bd=3,relief=RIDGE, bg="white")
        Frame2.place(x=770,y=70, width=680, height=350)
        title3=Label(Frame1,text="Employee Salary Details",  font=("times new roman",15,"bold"),bg="red4",fg="ivory2",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        lbl_month=Label(Frame2,text="Month",  font=("times new roman",15),bg="white",fg="black").place(x=10,y=50)
        txt_month=Entry(Frame2, font=("times new roman",12),textvariable=self.var_month,bg="lightyellow",fg="black").place(x=90,y=52, width=100)
        
        lbl_year=Label(Frame2,text="Year",  font=("times new roman",15),bg="white",fg="black").place(x=210,y=50)
        txt_year=Entry(Frame2, font=("times new roman",12),textvariable=self.var_year,bg="lightyellow",fg="black").place(x=270,y=52, width=100)
        
        lbl_salary=Label(Frame2,text="B.Salary",  font=("times new roman",15),bg="white",fg="black").place(x=380,y=50)
        txt_salary=Entry(Frame2, font=("times new roman",12),textvariable=self.var_salary,bg="lightyellow",fg="black").place(x=490,y=52, width=100)
        
        
        
        #btn_search=Button(Frame2,text="Search",  font=("times new roman",13, "bold"),bg="red4",fg="white").place(x=380,y=65,  height=30)
        
        
        #_________row1_________
        lbl_days=Label(Frame2,text="Total Days",  font=("times new roman",15),bg="white",fg="black").place(x=10,y=110)
        txt_days=Entry(Frame2, font=("times new roman",12),textvariable=self.var_t_days,bg="lightyellow",fg="black").place(x=150,y=110, width=100)
        lbl_absent=Label(Frame2,text="Absents",  font=("times new roman",15),bg="white",fg="black").place(x=300,y=110)
        txt_absent=Entry(Frame2, font=("times new roman",12),textvariable=self.var_absent,bg="lightyellow",fg="black").place(x=410,y=110, width=120)
       
        #_________row2_________
        lbl_medical=Label(Frame2,text="Medical",  font=("times new roman",15),bg="white",fg="black").place(x=10,y=140)
        txt_medical=Entry(Frame2, font=("times new roman",12),textvariable=self.var_medical,bg="lightyellow",fg="black").place(x=150,y=140, width=100)
        lbl_pf=Label(Frame2,text="P.Fund",  font=("times new roman",15),bg="white",fg="black").place(x=300,y=140)
        txt_pf=Entry(Frame2, font=("times new roman",12),textvariable=self.var_pf,bg="lightyellow",fg="black").place(x=410,y=140, width=120)
       
        #_________row3_________
        lbl_convence=Label(Frame2,text="Convence",  font=("times new roman",15),bg="white",fg="black").place(x=10,y=170)
        txt_convence=Entry(Frame2, font=("times new roman",12),textvariable=self.var_convence,bg="lightyellow",fg="black").place(x=150,y=170, width=100)
        lbl_netsalary=Label(Frame2,text="Net Salary",  font=("times new roman",15),bg="white",fg="black").place(x=300,y=170)
        txt_netsalary=Entry(Frame2, font=("times new roman",12),textvariable=self.var_net_salary,bg="lightyellow",fg="black").place(x=410,y=170, width=120)
       
        btn_calculate=Button(Frame2,text="Calculate", command=self.calculate, font=("times new roman",13, "bold"),bg="red4",fg="white").place(x=150,y=250, height=30, width=120)
        btn_save=Button(Frame2,text="Save",  font=("times new roman",13, "bold"),bg="red4",fg="white").place(x=300,y=250, height=30, width=120)
        btn_clear=Button(Frame2,text="Clear",  font=("times new roman",13, "bold"),bg="red4",fg="white").place(x=450,y=250, height=30, width=120)
        


        #----------Frame3----------------
        Frame3=Frame(self.root,bd=3,relief=RIDGE, bg="white")
        Frame3.place(x=770,y=430, width=680, height=350)
        #-------Calculate-----------------
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator + str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''





        Cal_frame=Frame(Frame3,bg="white", bd=2, relief=RIDGE)
        Cal_frame.place(x=2,y=2, width=247, height= 305)
        txt_result=Entry(Cal_frame, bg="lightyellow", textvariable=self.var_txt ,font=("times new roman", 20, "bold"),justify=RIGHT).place(x=0, y=0,relwidth=1, height=50)
        
        
        #-------row1-----------------
        btn_7=Button(Cal_frame, text='7', command=lambda:btn_click(7), font=("times new roman", 12, "bold")).place(x=0, y= 52, width=60, height=60)
        btn_8=Button(Cal_frame, text='8',command=lambda:btn_click(8),font=("times new roman", 12, "bold")).place(x=61, y= 52, width=60, height=60)
        btn_9=Button(Cal_frame, text='9',command=lambda:btn_click(9),font=("times new roman", 12, "bold")).place(x=122, y= 52, width=60, height=60)
        btn_div=Button(Cal_frame, text='/',command=lambda:btn_click('/'),font=("times new roman", 12, "bold")).place(x=183, y= 52, width=60, height=60)

        #-------row2-----------------
        btn_4=Button(Cal_frame, text='4', command=lambda:btn_click(4), font=("times new roman", 12, "bold")).place(x=0, y= 112, width=60, height=60)
        btn_5=Button(Cal_frame, text='5', command=lambda:btn_click(5),font=("times new roman", 12, "bold")).place(x=61, y= 112, width=60, height=60)
        btn_6=Button(Cal_frame, text='6' , command=lambda:btn_click(6),font=("times new roman", 12, "bold")).place(x=122, y= 112, width=60, height=60)
        btn_mul=Button(Cal_frame, text='*', command=lambda:btn_click('*'),font=("times new roman", 12, "bold")).place(x=183, y= 112, width=60, height=60)


        #-------row3-----------------
        btn_1=Button(Cal_frame, text='1',command=lambda:btn_click(1), font=("times new roman", 12, "bold")).place(x=0, y= 172, width=60, height=60)
        btn_2=Button(Cal_frame, text='2',command=lambda:btn_click(2),font=("times new roman", 12, "bold")).place(x=61, y= 172, width=60, height=60)
        btn_3=Button(Cal_frame, text='3',command=lambda:btn_click(3),font=("times new roman", 12, "bold")).place(x=122, y= 172, width=60, height=60)
        btn_min=Button(Cal_frame, text='-',command=lambda:btn_click('-'),font=("times new roman", 12, "bold")).place(x=183, y= 172, width=60, height=60)


        #-------row4-----------------
        btn_0=Button(Cal_frame, text='0', command=lambda:btn_click(1),font=("times new roman", 12, "bold")).place(x=0, y= 233, width=60, height=60)
        btn_dot=Button(Cal_frame, text='C',command=clear_cal,font=("times new roman", 12, "bold")).place(x=61, y= 233, width=60, height=60)
        btn_sum=Button(Cal_frame, text='+',command=lambda:btn_click('+'),font=("times new roman", 12, "bold")).place(x=122, y= 233, width=60, height=60)
        btn_equal=Button(Cal_frame, text='=',command=result,font=("times new roman", 12, "bold")).place(x=183, y= 233, width=60, height=60)
         #-------salary____
        sal_frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_frame.place(x=260,y=2, width=390, height= 300)
        title_sal2=Label(sal_frame,text="Salary Receipt",  font=("times new roman",15,"bold"),bg="red4",fg="ivory2",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        #lbl_code=Label(Frame1,text="Employee Code",  font=("times new roman",15),bg="white",fg="black").place(x=10,y=60)
        
        sal_frame2=Frame(sal_frame,bg="white",bd=2,relief=RIDGE)
        sal_frame2.place(x=0,y=30, relwidth=1,height=230)

        scroll_y=Scrollbar(sal_frame2,orient="vertical")
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_recipt=Text(sal_frame2,font=("times new roman",18),bg="lightyellow", yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)

        btn_print=Button(sal_frame,text="Print",  font=("times new roman",13, "bold"),bg="black",fg="white").place(x=265,y=262, height=30, width=120)
  
  
      def calculate(self): 
          #-----frame1variables
          print(self.var_emp_code.get(),
          self.var_designation.get(),
          self.var_name.get(),
          self.var_age.get(),
          self.var_gender.get(),
          self.var_email.get(),
          self.var_hr_location.get(),
          self.var_dob.get(),
          self.var_doj.get(),
          self.var_experience.get(),
          self.var_proof_id.get(),#----National ID-----
          self.var_contact.get(),
          self.var_status.get())

          #---Frame2Variables
          self.var_month.get(),
          self.var_year.get(),
          self.var_salary.get(),
          self.var_t_days.get(),
          self.var_absent.get(),
          self.var_medical.get(),
          self.var_pf.get(),
          self.var_convence.get(),
          self.var_net_salary.get(),
          self.txt_address.get('1.0',END),





root=Tk()
obj=EmployeeSystem(root)
root.mainloop()