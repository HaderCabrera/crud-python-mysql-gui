import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class FormatTask:

    def __init__(self):
        # Conexión a la base de datos
        ##MODIFICAR
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="root7800",  
            database="tareasCopower"
        )
        self.cursor = self.conn.cursor()

    def task(self):
        try:
            base = Tk()  # Template
            base.geometry("500x600")
            base.title("Formulario Tareas")

            # Encabezado
            label = Label(base, text="Gestor de tareas", font=("Arial", 14))
            label.pack(pady=10)

            # Listbox para mostrar las tareas
            self.task_list = Listbox(base, width=50, height=10)
            self.task_list.pack(pady=10)

            # Campo de entrada para tareas
            Label(base, text="Descripción de la tarea:").pack()
            self.task_entry = Entry(base, width=40)
            self.task_entry.pack(pady=10)

            # Scrollbar departamentos
            Label(base, text="Seleccionar Departamento:").pack()
            self.department_combobox = ttk.Combobox(base, width=37, state="readonly")
            self.department_combobox.pack(pady=5)
            self.load_departments()

            # Scrollbar trabajadores
            Label(base, text="Seleccionar Trabajador:").pack()
            self.worker_combobox = ttk.Combobox(base, width=37, state="readonly")
            self.worker_combobox.pack(pady=5)
            self.load_workers()

            # Estilo para los botones
            button_style = {
                'bg': '#333333',   
                'fg': '#ffffff',  
                'font': ('Helvetica', 10),
                'bd': 0,     
                'relief': 'flat',
                'width': 10,
                'height': 2, 
                'activebackground': '#555555',
                'activeforeground': '#ffffff'
            }

            # Botones para acciones CRUD
            create_button = Button(base, text="Crear", command=self.create_task, **button_style)
            create_button.pack(pady=5)

            read_button = Button(base, text="Leer", command=self.read_tasks, **button_style)
            read_button.pack(pady=5)

            update_button = Button(base, text="Actualizar", command=self.update_task, **button_style)
            update_button.pack(pady=5)

            delete_button = Button(base, text="Borrar", command=self.delete_task, **button_style)
            delete_button.pack(pady=5)

            base.mainloop()  # Inicia la interfaz gráficaa

        except ValueError as error:
            print("Error al mostrar interfaz: {}".format(error))

    # Cargar departamentos
    def load_departments(self):
        try:
            self.cursor.execute("SELECT id, nombre FROM departamento")
            departments = self.cursor.fetchall()
            self.department_combobox['values'] = [f"{d[0]} - {d[1]}" for d in departments]
        except mysql.connector.Error as error:
            print(f"Error al cargar departamentos: {error}")

    # Cargar trabajadores
    def load_workers(self):
        try:
            self.cursor.execute("SELECT id, nombre FROM trabajador")
            workers = self.cursor.fetchall()
            self.worker_combobox['values'] = [f"{w[0]} - {w[1]}" for w in workers]
        except mysql.connector.Error as error:
            print(f"Error al cargar trabajadores: {error}")

    # Crear tarea
    def create_task(self):
        task = self.task_entry.get()
        department = self.department_combobox.get()
        worker = self.worker_combobox.get()

        if task and department and worker:
            try:
                department_id = department.split(" - ")[0]
                worker_id = worker.split(" - ")[0]
                query = "INSERT INTO tarea (descripcion, id_trabajador) VALUES (%s, %s)"
                self.cursor.execute(query, (task, worker_id))
                self.conn.commit()
                self.task_list.insert(END, f"Tarea creada: {task} (Trabajador ID: {worker_id})")
                self.task_entry.delete(0, END)
                print(f"Tarea creada: {task}")
            except mysql.connector.Error as error:
                print(f"Error al crear la tarea: {error}")
        else:
            print("Todos los campos son obligatorios.")

    # Leer tareas
    def read_tasks(self):
        try:
            self.task_list.delete(0, END)
            query = """
            SELECT t.id, t.descripcion, d.nombre AS departamento, w.nombre AS trabajador
            FROM tarea t
            LEFT JOIN trabajador w ON t.id_trabajador = w.id
            LEFT JOIN departamento d ON w.id_departamento = d.id
            """
            self.cursor.execute(query)
            tasks = self.cursor.fetchall()
            for task in tasks:
                self.task_list.insert(END, f"{task[0]} - {task[1]} (Dept: {task[2]}, Trabajador: {task[3]})")
            print("Tareas cargadas correctamente.")
        except mysql.connector.Error as error:
            print(f"Error al leer las tareas: {error}")

    # Actualizar tarea
    def update_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            new_task = self.task_entry.get().strip()
            if new_task:
                try:
                    selected_task = self.task_list.get(selected_task_index[0])
                    task_id = selected_task.split(" - ")[0]
                    query = "UPDATE tarea SET descripcion = %s WHERE id = %s"
                    self.cursor.execute(query, (new_task, task_id))
                    self.conn.commit()
                    self.read_tasks()  # Recargar la lista de tareas
                    self.task_entry.delete(0, END)
                    print(f"Tarea actualizada: ID {task_id} -> {new_task}")
                except mysql.connector.Error as error:
                    print(f"Error al actualizar la tarea: {error}")
            else:
                print("El campo de tarea está vacío. Por favor, escribe una descripción.")
        else:
            print("No se ha seleccionado ninguna tarea para actualizar.")

    # Borrar tarea
    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            try:
                selected_task = self.task_list.get(selected_task_index[0])
                task_id = selected_task.split(" - ")[0]
                query = "DELETE FROM tarea WHERE id = %s"
                self.cursor.execute(query, (task_id,))
                self.conn.commit()
                self.read_tasks()  # Recargar la lista de tareas
                print(f"Tarea borrada: ID {task_id}")
            except mysql.connector.Error as error:
                print(f"Error al borrar la tarea: {error}")
        else:
            print("No se ha seleccionado ninguna tarea para borrar.")

# Instanciar la clase y ejecutar el programa
if __name__ == "__main__":
    app = FormatTask()
    app.task()
