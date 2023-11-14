import tkinter as tk
from tkinter import messagebox
import random

class RandomSelectionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("随机选择程序")

        self.machine_list = ["SpiderPi1", "SpiderPi2", "JetHexe", "Jettank", "JetRover"]
        self.group_list = ["Van", "Genshin", "原神", "老八", "二刺螈"]

        self.selections = {group: None for group in self.group_list}

        self.machine_label = tk.Label(master, text="选择机器:")
        self.machine_label.pack()

        self.group_label = tk.Label(master, text="选择组:")
        self.group_label.pack()

        self.random_button = tk.Button(master, text="随机选择", command=self.random_selection)
        self.random_button.pack()

    def random_selection(self):
        available_groups = [group for group in self.group_list if self.selections[group] is None]

        if not available_groups:
            messagebox.showwarning("警告", "每个组都已经选择了机器！")
            return

        selected_group = random.choice(available_groups)
        selected_machine = random.choice(self.machine_list)

        self.selections[selected_group] = selected_machine
        self.machine_list.remove(selected_machine)

        messagebox.showinfo("随机选择结果", f"{selected_group}组选择了机器{selected_machine}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomSelectionApp(root)
    root.mainloop()
