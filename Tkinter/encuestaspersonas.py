from cProfile import label
from tkinter import * 
import tkinter as tk
from tkinter import Entry 
from tkinter import ttk
import sqlite3 


class Product:
    # connection dir property
    db_name = 'database.db'

    def __init__(self, win2):
        # Initializations 
        self.wind = win2
        self.wind.title('Encuesta De Personas')

        # Creating a Frame Container 
        frame = LabelFrame(self.wind, text = 'Registro de personas')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Name Input
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # Last name Input
        Label(frame, text = 'Apellidos: ').grid(row = 2, column = 0)
        self.apellido = Entry(frame)
        self.apellido.grid(row = 2, column = 1)
        
        # ID Input
        Label(frame, text = 'Cedula: ').grid(row = 3, column = 0)
        self.cedula = Entry(frame)
        self.cedula.grid(row = 3, column = 1)

        # Sisben Input
        Label(frame, text = 'Tipo de sisben: ').grid(row = 4, column = 0)
        self.sisben = Entry(frame)
        self.sisben.grid(row = 4, column = 1)

        # Edad Input
        Label(frame, text = 'Edad: ').grid(row = 5, column = 0)
        self.edad = Entry(frame)
        self.edad.grid(row = 5, column = 1)
        

        # Button Add Product 
        ttk.Button(frame, text = 'Guardar Encuesta', command = self.add_product).grid(row = 6, columnspan = 2)

        # Output Messages 
        self.message = Label(win2,text = '', fg = 'red')
        self.message.grid(row = 7, column = 0, columnspan = 5)

        # Table
        self.tree = ttk.Treeview(win2,height = 10,  columns = (0,1,2,3,4))
        self.tree.grid(row = 8, column = 0, columnspan = 2)
        # self.tree.heading('#0', text = 'ID',anchor= CENTER)
        
        self.tree.column = ("#0")
        self.tree.column = ("#1")
        self.tree.column = ("#2")
        self.tree.column = ("#3")
        self.tree.column = ("#4")

        self.tree.heading(0 ,text = 'Nombre',anchor= CENTER)
        self.tree.heading(1, text = 'Apellido',anchor= CENTER)
        self.tree.heading(2, text = 'Cedula',anchor= CENTER)
        self.tree.heading(3, text = 'Sisben',anchor= CENTER)
        self.tree.heading(4, text = 'Edad',anchor= CENTER)
        
        # Buttons
        ttk.Button(win2,text = 'Borrar', command = self.delete_product).grid(row = 9, column = 0, sticky = W + E)
        ttk.Button(win2,text = 'Editar', command = self.edit_product).grid(row = 9, column = 1, sticky = W + E)

        # Filling the Rows
        self.get_products()
        

    # Function to Execute Database Querys
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
        

    # Get Products from Database
    def get_products(self):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM product ORDER BY sisben DESC'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert('', 0,text=row[0],values=row[:5:1])

            
        

    # User Input Validation
    def validation(self):
        return len(self.name.get()) != 0 and len(self.apellido.get()) != 0 and len(self.cedula.get()) != 0 and len(self.sisben.get()) != 0 and len(self.edad.get()) != 0 
        

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(?,?,?,?,?)'
            parameters =  (self.name.get(), self.apellido.get(),self.cedula.get(), self.sisben.get(), self.edad.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Product {} added Successfully'.format(self.name.get())
            self.name.delete(0, END)
            self.apellido.delete(0, END)
            self.cedula.delete(0, END)
            self.sisben.delete(0, END)
            self.edad.delete(0, END)
            
        else:
            self.message['text'] = 'Nombre y Apellidos Son Requeridos'
        self.get_products()
        

    def delete_product(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, (name,))
        self.message['text'] = 'Record {} deleted Successfully'.format(name)
        self.get_products()
        
        

    def edit_product(self):
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            return
        old_name = self.tree.item(self.tree.selection())['values']
        old_apellido = self.tree.item(self.tree.selection())['values'][1]
        old_sisben = self.tree.item(self.tree.selection())['values'][2]
        old_cedula = self.tree.item(self.tree.selection())['values'][3]
        old_edad = self.tree.item(self.tree.selection())['values'][4]

        self.edit_wind = Toplevel(win2)
        self.edit_wind.title = 'Edit Product'
        # Old Name
        Label(self.edit_wind, text = 'Viejo Nombre:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_name), state = 'readonly').grid(row = 0, column = 2)
        # New Name
        Label(self.edit_wind, text = 'Nuevo Nombre:').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)


        # Old last name 
        Label(self.edit_wind, text = 'Viejo Apellido:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_apellido), state = 'readonly').grid(row = 2, column = 2)
        # New last name
        Label(self.edit_wind, text = 'Nuevo Apellido:').grid(row = 3, column = 1)
        new_apellido= Entry(self.edit_wind)
        new_apellido.grid(row = 3, column = 2)

        # Old id
        Label(self.edit_wind, text = 'Vieja Cedula:').grid(row = 4, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_cedula), state = 'readonly').grid(row = 4, column = 2)
        # New id
        Label(self.edit_wind, text = 'Nueva Cedula:').grid(row = 5, column = 1)
        new_cedula= Entry(self.edit_wind)
        new_cedula.grid(row = 5, column = 2)

        # Old sisben
        Label(self.edit_wind, text = 'Viejo Sisben:').grid(row = 6, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_sisben), state = 'readonly').grid(row = 6, column = 2)
        # New sisben
        Label(self.edit_wind, text = 'Nuevo Sisben:').grid(row = 7, column = 1)
        new_sisben= Entry(self.edit_wind)
        new_sisben.grid(row = 7, column = 2)

        # Old age
        Label(self.edit_wind, text = 'Vieja Edad:').grid(row = 8, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_edad), state = 'readonly').grid(row = 8, column = 2)
        # New age
        Label(self.edit_wind, text = 'Nueva Edad:').grid(row = 9, column = 1)
        new_edad= Entry(self.edit_wind)
        new_edad.grid(row = 9, column = 2)

        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records(new_name.get(), old_name, new_apellido.get(), old_apellido,new_cedula.get(), old_cedula,new_sisben.get(), old_sisben, new_edad.get(), old_edad)).grid(row = 10, column = 2, sticky = W)
        self.edit_wind.mainloop()
        

    def edit_records(self, new_name, name, new_apellido, old_apellido, new_cedula, old_cedula, new_sisben,old_sisben, new_edad, old_edad):
        query = 'UPDATE product SET name = ?, apellido = ? , Cedula = ? , sisben = ?, edad=? WHERE name = ? AND apellido = ? AND Cedula = ? AND sisben = ? AND  edad = ?'
        parameters = (new_name,new_apellido, new_sisben,new_cedula,new_edad, name,old_apellido, old_cedula, old_sisben, old_edad)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated successfylly'.format(name)
        self.get_products()
        

win2=Tk
win2 = tk.Tk()
win2.iconbitmap("FHsimbolo.ico")
win2.config(bg="#2e3192")
application = Product(win2)
win2.mainloop()



