try:
    import os
    import getpass
    import secrets
    import sys
except ImportError:
    print('Critical Error: Required Modules Not found!\n')
    x = input('Press any key to continue...')
    sys.exit(1)

A = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'
     , 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
from tkinter import *
import onetimepad

root = Tk()
root.title("CRYPTOGRAPHY")
root.geometry("800x600")

# converts Alphanumeric characters to numbers of base 36    
def f(x):
  store = []
  for s in x:
    count = 0
    for i in range(36):
        if A[i].lower() == s.lower():
          store.append(i)
          count = 1
          break
    if count == 0:
      store.append(' ')
  return tuple(store)                

    
# converts base 36 numbers to alphanumeric charactors.
def rf(x):
  store = []
  q = ''
  for s in x:
    count = 0
    for i in range(36):
        if i == s:
          store.append(A[i])
          count = 1
          break
    if count == 0:
      store.append(' ')
  q = ''.join(store)
  return q

    
# generates a key without keyfile.
def ikey(x):
    seed = list(range(36))
    masterkey = []
    for i in range(len(x)):
        masterkey.append(secrets.choice(seed))
    return tuple(masterkey)


# encrypts a given string and returns ciphertxt and key as a tuple. (no file generated!)
def en(msg):
    ciphertxt = []
    x = f(msg)
    y = ikey(msg)
    for i in range(len(x)):
            if type(x[i]) is int:
                ciphertxt.append(((x[i]+y[i]) % 36))
            else:
                ciphertxt.append(' ')
    ctxt = rf(tuple(ciphertxt))
    shk = rf(y)
    return (ctxt, shk)


# decrypts a given encrypted string and returns a plaintxt as output.
def de(c, k):
    ciphertxt = []
    x = f(c)
    y = f(k)
    if len(x) <= len(y):
        for i in range(len(x)):
            if type(x[i]) is int and type(y[i]) is int:
                ciphertxt.append(((x[i]-y[i]) % 36))
            else:
                ciphertxt.append(' ')
   
    return rf(tuple(ciphertxt))

    
# function for secret splitting interface.
def sprocess():
   table = []
   x = 3
   msg = e1.get()
   table += list(en(msg))
   for i in range(2, x):
        tmp = table[-1]
        table.pop()
        table += list(en(tmp))
  
        e2.insert(0,table[0])
        e5.insert(0,table[1])
        e6.insert(0,table[2])

# function for secret combining interface.
def cprocess():
    tab = []
    x = 3
    tab.append(e3.get())
    tab.append(e7.get())
    tab.append(e8.get())
    for i in range(x-1):
        hook = []
        a, b = tab[-2], tab[-1]
        tab.pop()
        tab.pop()
        hook.append(de(a, b))
        tab += hook
    e4.insert(0,''.join(tab))

        



# creating labels and positioning them on the grid
label1 = Label(root, text ='plain text')			
label1.grid(row = 10, column = 1)
label2 = Label(root, text ='Secret1')
label2.grid(row = 11, column = 1)
label5 = Label(root, text ='Secret2')
label5.grid(row = 12, column = 1)
label6 = Label(root, text ='Secret3')
label6.grid(row = 13, column = 1)
l3 = Label(root, text ="Secret1")
l3.grid(row = 10, column = 10)
l7 = Label(root, text ="Secret2")
l7.grid(row = 11, column = 10)
l8 = Label(root, text ="Secret3")
l8.grid(row = 12, column = 10)
l4 = Label(root, text ="decrypted text")
l4.grid(row = 13, column = 10)

# creating entries and positioning them on the grid
e1 = Entry(root)
e1.grid(row = 10, column = 2)
e2 = Entry(root)
e2.grid(row = 11, column = 2)
e5 = Entry(root)
e5.grid(row = 12, column = 2)
e6 = Entry(root)
e6.grid(row = 13, column = 2)

e3 = Entry(root)
e3.grid(row = 10, column = 11)
e7 = Entry(root)
e7.grid(row = 11, column = 11)
e8 = Entry(root)
e8.grid(row = 12, column = 11)
e4 = Entry(root)
e4.grid(row = 13, column = 11)

# creating encryption button to produce the output
ent = Button(root, text = "encrypt", bg ="red", fg ="white", command = sprocess)
ent.grid(row = 14, column = 2)

# creating decryption button to produce the output
b2 = Button(root, text = "decrypt", bg ="green", fg ="white", command = cprocess)
b2.grid(row = 14, column = 11)


root.mainloop()

