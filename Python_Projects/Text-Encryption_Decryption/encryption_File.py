from tkinter import *
from tkinter import messagebox
import base64

screen = Tk()
screen.geometry("620x520")
screen.title("ENCRYPTION-DECRYPTION TECHNIQUE")
screen.configure(bg="gray")

def encrypt():
    password = code.get()
    if password=="1234":
        screen1 = Toplevel(screen)
        screen1.title("Encrypted Messege")
        screen1.geometry("400x250")
        screen1.configure(bg="pink")
        
        #encryption logic
        message = input.get(1.0,END)
        encode_msg = message.encode("ascii")
        pybase64_bytes = base64.b64encode(encode_msg)
        encrypt = pybase64_bytes.decode("ascii")
        
        Label(screen1,text="Your Encrypted Message!!!",font="impack 10 bold").place(x=5,y=7)
        input2 = Text(screen1,font="30",bd=4,wrap=WORD)
        input2.place(x=2,y=30,width=390,height=180)
        input2.insert(END,encrypt)

    elif(password==""):
        messagebox.showerror("Error","Please enter your secret key")
    elif(password!="1234"):
        messagebox.showerror("Oops","Please enter correct secret key")
        
def decrypt():
    password = code.get()
    if password=="1234":
        screen2 = Toplevel(screen)
        screen2.title("Decrypted Messege")
        screen2.geometry("400x250")
        screen2.configure(bg="pink")
        
        #encryption logic
        message = input.get(1.0,END)
        decode_msg = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_msg)
        decrypt = base64_bytes.decode("ascii")
        
        Label(screen2,text="Your Encrypted Message!!!",font="impack 10 bold").place(x=5,y=7)
        input2 = Text(screen2,font="30",bd=4,wrap=WORD)
        input2.place(x=2,y=30,width=390,height=180)
        input2.insert(END,decrypt)

    elif(password==""):
        messagebox.showerror("Error","Please enter your secret key")
    elif(password!="1234"):
        messagebox.showerror("Oops","Please enter correct secret key")

def reset():
    input.delete(1.0,END)
    code.set("")
    
Label(screen,text="Enter Your Message Here For Encryption And Decryption!!!",font="impack 14 bold",bg="blue",fg="white").place(x=50,y=7)
input = Text(screen,font="20")
input.place(x=5,y=45,width=610,height=120)
Label(screen,text="Enter Your Secret Key",font="impack 13 bold").place(x=230,y=185)

code=StringVar()
Entry(textvariable=code,bd=4,font="20",show="*").place(x=225,y=225)

Button(screen,text="ENCRYPT",font="airal 15 bold",bg="green",fg="white",command=encrypt).place(x=120,y=280,width=180)
Button(screen,text="DECRYPT",font="airal 15 bold",bg="orange",fg="white",command=decrypt).place(x=320,y=280,width=180)
Button(screen,text="RESET",font="airal 15 bold",bg="red",fg="white",command=reset).place(x=180,y=350,width=280)

mainloop()