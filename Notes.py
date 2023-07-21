import tkinter as tk
import os

def create_note():
    note = note_entry.get()
    with open("Notes.txt", "a") as file:
        file.write(note + "\n" + "-" * 20 + "\n")
    note_entry.delete(0, tk.END)  # Очистить поле ввода после сохранения заметки
    read_notes()  # Обновить список заметок

def read_notes():
    if os.path.exists("Notes.txt"):
        with open("Notes.txt", "r") as file:
            notes = file.read()
            notes_text.config(state=tk.NORMAL)  # Разрешить редактирование текстового поля
            notes_text.delete(1.0, tk.END)  # Очистить текстовое поле перед выводом заметок
            notes_text.insert(tk.END, notes)
            notes_text.config(state=tk.DISABLED)  # Запретить редактирование текстового поля

def create_notes_file():
    if not os.path.exists("Notes.txt"):
        with open("Notes.txt", "w"):
            pass

root = tk.Tk()
root.title("Приложение для заметок")

note_label = tk.Label(root, text="Введите заметку:")
note_label.pack()

note_entry = tk.Entry(root, width=50)
note_entry.pack()

create_button = tk.Button(root, text="Создать заметку", command=create_note)
create_button.pack()

notes_text = tk.Text(root, width=60, height=15, state=tk.DISABLED)
notes_text.pack()

exit_button = tk.Button(root, text="Выход", command=root.quit)
exit_button.pack()

create_notes_file()  # Создать файл для заметок, если его нет
read_notes()  # Первоначальное отображение заметок

root.mainloop()
