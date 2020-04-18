import tkinter as tk

from app.label_tool import CountdownLabel


def click_start():
    label = CountdownLabel(root, int(second.get()))
    label.pack(side=tk.TOP, fill=tk.X)


root = tk.Tk()
root.title("Dropbox Screenshots")
root.geometry("500x300")
root.resizable(False, False)
fm = tk.Frame(root)

text = tk.Label(root, text="Введите секунды:").pack(side=tk.TOP, fill=tk.X)
second = tk.StringVar()
second_input = tk.Entry(root, width=25, textvariable=second, justify='center').pack(side=tk.TOP, fill=tk.X)

button = tk.Button(root, width=15, command=click_start, text='Начать').pack(side=tk.TOP, fill=tk.X)

fm.pack(fill=tk.BOTH, expand=tk.YES)
root.mainloop()
