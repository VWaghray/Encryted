from tkinter import *
root = Tk()
root.title("Ascii")
root.geometry("400x400")
root.configure(bg="PaleGreen1")

name = Entry(root)
name.place(relx=0.5, rely=0.4, anchor=CENTER)
label=Label(root, text="Name in ASCII: ", bg="dark green", fg="goldenrod3")
label.place(relx=0.5, rely=0.6, anchor=CENTER)
label1=Label(root, text="Name in Encrypted Value: ", bg="dark green", fg="goldenrod3")
label1.place(relx=0.5, rely=0.7, anchor=CENTER)

def ascii():
    word = name.get()
    for letter in word:
        label["text"] += str(ord(letter)) + " "
        
    Ascii = int(ord(letter))
    encrypte = Ascii - 1 
    for letter in Ascii:
        label1["text"] += str(chr(encrypte))


btn=Button(root, text="Show name in ASCII and Encrypted Value", command=ascii, bg="DarkSeaGreen4", fg="alice blue")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()