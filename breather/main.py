import tkinter as tk

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        
        self.label = tk.Label(root, font=('Helvetica', 48), text="")
        self.label.pack(pady=20)
        
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=20)
        
        self.count = 4
        self.update_label()
        
    def update_label(self):
        self.label.config(text=str(self.count))
        self.count -= 1
        if self.count < 0:
            self.count = 4
        self.root.after(1000, self.update_label)

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()