import tkinter as tk

root=tk.Tk()
root.geometry('2000x900')
root.title("MY APPLICATION")
root.config(bg='violet')


m1=tk.Label(root,text="welcome to my new application",font=("algerian", 20 ,"bold"),bg='light green')
m1.place(x=500,y=50)


m2=tk.Label(root,text="login page",font=("algerian", 16),bg='light green')
m2.place(x=700,y=100)


m3=tk.Label(root,text="user name",font=("algerian", 16),bg='light green')
m3.place(x=500,y=200)


e1=tk.Entry(root,font=("arial", 16))
e1.place(x=700,y=200)


m4=tk.Label(root,text="password",font=("algerian", 16),bg='light green')
m4.place(x=500,y=300)


e2=tk.Entry(root,font=("arial", 16))
e2.place(x=700,y=300)


b1=tk.Button(root,text="login",font=("italic", 16),bg='red')
b1.place(x=600,y=400)


b2=tk.Button(root,text="sign in",font=("italic", 16),bg='red')
b2.place(x=700,y=400)



root.mainloop()
