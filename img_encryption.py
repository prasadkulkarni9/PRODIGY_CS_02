from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("500x300")
root.title("Image Encryptor/Decryptor")

def enc_img():
    file1 = filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg')])
    if file1 is not NONE:
        file_name = file1.name
       # print(file_name) 
    key = entry_file.get(1.0,END)
    print(file_name,key)
    fi = open(file_name,'rb')
    img = fi.read()
    fi.close()
    img = bytearray(img)
    for index,values in enumerate(img):
        img[index] = values^int(key)
    fi1 = open(file_name, 'wb')
    fi1.write(img)    
    fi1.close()
l1 = Label(root,height=2,width=20,text="Enter The Key")
l1.place(x=170,y=80)
b1 = Button(root,height=2, text="Encrypt/Decrypt Image", command=enc_img)
b1.place(x=185,y=30)
entry_file = Text(root,height=2,width=20) 
entry_file.place(x=170,y=120)
root.mainloop()
