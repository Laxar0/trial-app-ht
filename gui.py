from tkinter import *

root = Tk()
root.geometry("425x150")
root['bg'] = 'Gray'
root.resizable(height = False, width = False)
root.title('Encoding')

r_var = IntVar()

entry1 = Entry(width = 50)
label1 = Label(text = 'Шифруемый текст: ')
entry2 = Entry(width = 50)
label2 = Label(text = 'Ключ: ')
b = Button(width = 12, height = 1, text = 'Создать шифр')
label = Label(text = 'Пример шифра')
r1 = Radiobutton(text = 'Зашифровать', var = r_var, value = 1)
r2 = Radiobutton(text = 'Расшифровать', var = r_var, value = 2)


label1['bg'] = 'Gray'
label2['bg'] = 'Gray'
label['bg'] = 'Gray'
r1['bg'] = 'Gray'
r2['bg'] = 'Gray'

label1.grid(row = 0, column = 0, columnspan = 2)
entry1.grid(row = 0, column = 2)
label2.grid(row = 1, column = 0, columnspan = 2)
entry2.grid(row = 1, column = 2)
b.grid(row = 3, column = 0, columnspan = 3)
r1.grid(row = 2, column = 1, sticky = N)
r2.grid(row = 2, column = 2)
label.grid(row = 4, column = 0, columnspan = 3)


root.mainloop()