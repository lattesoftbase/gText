from tkinter import *
from tkinter.filedialog import *
import webbrowser

resolution = [1280, 720] # Разрешение основного окна

root = Tk() # Создаем основное окно
root.geometry(f"{resolution[0]}x{resolution[1]}") # Устанавливаем разрешение основного окна
root.resizable(True, True) # Разрешаем изменение разрешения основного окна
root.title("gText BASIC EDITION") # Устанавливаем заголовок основного окна

config = open("config.txt", "r") # Открываем файл конфига

choosed = config.readlines() # Читаем файл конфига

# Создаем текстовое поле
text = Text(root, width=resolution[0], height=resolution[1], font=("Consolas", choosed[5].strip()), bg=choosed[0].strip(), fg=choosed[1].strip())
text.config(insertbackground=choosed[2].strip()) # Настраиваем курсор текстового поля
version = "RELEASE 1.0" # Версия

def about():
    # Создаем окно "О программе"
    about = Tk()
    # Добавляем заголовок к about
    about.title("О программе")
    # Делаем надписи
    about_label = Label(about, text=f"gText version: {version}", font=(choosed[4].strip(), 20)).pack(side="top", pady=20)
    about_label2 = Label(about, text=f"by ПарашаСофт", font=(choosed[4].strip(), 20)).pack(side="top", pady=20)
    # Создаем кнопку закрыть
    close_button = Button(about, text="закрыть", command=about.destroy, font=(choosed[4].strip(), 20), fg="black", activebackground="#999999")
    close_button.pack(side="bottom", pady=20) # Размещаем кнопку закрыть
    about.geometry("480x240") # Задаем разрешение для окна about
    about.resizable(False, False) # Запрещаем изменять разрешение окна about
    about.mainloop() # Цикл окна about

def open_file():
    fname = askopenfilename() # Создаем диалоговое окно выбора файла
    f = open(fname, "r", encoding="utf-8") # Открываем файл
    text.insert("1.0",str(f.read())) # Вставляем текст из файла
    f.close() # Закрываем файл

def new_file():
    text.delete("1.0", END) # Чистим экран
    # Создаем новый файл
    fname = asksaveasfilename(filetypes=(("Text", "*.txt"), ("All files", "*.*")))
    f = open(fname, "w+", encoding="utf-8")

def save_file():
    try:
        # Открываем файл
        fname = asksaveasfilename(filetypes=(("Text", "*.txt"), ("All files", "*.*")))
        f = open(fname, "w")
        f.write(text.get("1.0", END)) # Записываем информацию в файл
        f.close() # Закрываем файл
    except FileNotFoundError or UnboundLocalError:   pass

altmenu = Menu(root) # Создаем ALTMENU
filemenu = Menu(altmenu, tearoff=0) # Делаем контекстное меню для ФАЙЛ
filemenu.add_command(label="Открыть...", command=open_file)
filemenu.add_command(label="Новый", command=new_file)
filemenu.add_command(label="Сохранить...", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=root.quit)

editmenu = Menu(altmenu, tearoff=0) # Делаем контекстное меню для СПРАВКА
editmenu.add_command(label="Копировать", command=lambda : root.clipboard_append(text.selection_get()))
editmenu.add_command(label="Вставить", command=lambda : text.insert("1.0", root.clipboard_get()))

supportmenu = Menu(altmenu, tearoff=0) # Делаем контекстное меню для СПРАВКА
supportmenu.add_command(label="Наш сайт!", command=lambda : webbrowser.open("https://leightsoft.github.io"))
supportmenu.add_command(label="Наш VK!", command=lambda : webbrowser.open("https://vk.com/parashasoftware"))
supportmenu.add_separator()
supportmenu.add_command(label="О программе...", command=about)


# Сочетания клавиш
root.bind(("<Control_L>", "c"), lambda event : root.clipboard_append(text.selection_get()))
root.bind(("<Control_L>", "v"), lambda event : text.insert("1.0", root.clipboard_get()))
root.bind(("<Control_L>", "s"), save_file)

# Заполняем ALTMENU
altmenu.add_cascade(label='Файл', menu=filemenu)
altmenu.add_cascade(label='Правка', menu=editmenu)
altmenu.add_cascade(label='Справка', menu=supportmenu)
text.pack() # Вставляем текстовое поле
root.config(menu=altmenu) # Вставляем ALTMENU
root.update()
root.mainloop() # Главный цикл основного окна
