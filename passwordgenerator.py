import tkinter as tk
import random as rd
password=tk.Tk()
password.title("PASSWORD GENERATOR.")

def generate_password():
    c_1=var1.get()
    c_2=var2.get()
    alp_l="abcdefghijklmnopqrstuvwxyz"
    alp_h=alp_l.upper()
    symbols="!@$%*&#"
    total=alp_l+alp_h+symbols
    numbers="1234567890"
    if c_1=="ALPHANUMERIC":
        result_1=""
        for i in range(c_2):
            result_1=result_1+rd.choice((total+numbers))
    elif c_1=="ONLY WITH SPECIAL CHARACTERS":
        result_1=""
        for i in range(c_2):
            result_1=result_1+rd.choice(total)
    result.config(text=f"YOUR PASSWORD:{result_1}")               
select1=tk.Label(password,text="SELECT THE TYPE OF PASSWORD.")
select1.pack()

s1=["ALPHANUMERIC","ONLY WITH SPECIAL CHARACTERS"]
var1=tk.StringVar()
option1=tk.OptionMenu(password,var1,*s1)
option1.pack()

select2=tk.Label(password,text="SELECT THE LENGTH OF PASSWORD.")
select2.pack()

s2=[6,7,8]
var2=tk.IntVar()
option2=tk.OptionMenu(password,var2,*s2)
option2.pack()

result=tk.Label(password,text=" SELECT OPTIONS & CLICK ON DISPLAY PASSWORD.")
result.pack()

result_b=tk.Button(password,text="DISPLAY PASSWORD.",command=generate_password)
result_b.pack()

password.mainloop()