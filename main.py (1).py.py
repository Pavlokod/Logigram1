from customtkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.label=None
        self.entry=None
        self.menu_frame = CTkFrame(self, width=50, height=500)
        self.menu_frame.pack_propagate(False)
        self.menu_frame.place(x=0,y=0)
        self.is_show_menu = False
        self.speed_animation_menu = -5
        self.btn = CTkButton(self, text="➡", width=50)
        self.btn.place(x=0,y=0)
        self.scroll = CTkScrollableFrame(self)
        self.scroll.place(x=0,y=0)
        self.entry = CTkEntry(self, placeholder_text="Введіть повідомлення:", height=40)
        self.entry.place(x=0,y=0)
        self.send_btn = CTkButton(self, text=">", width=50, height=40)
        self.send_btn.place(x=0,y=0)
        self.

    def show_menu(self):
        self.menu_frame.configure(width=self.menu_frame.winfo_width() + self.speed_animation_menu)
        if not self.menu_frame.winfo_width() >= 200 and self.is_show_menu:
            self.after(10, self.show_menu())
        elif self.menu_frame.winfo_width()>=40 and not self.is_show_menu:
            self.after(10, self.show_menu())
        if self.label and self.entry:
            self.label.destroy()
            self.entry.destroy()

    def adaptive_ui(self):
        self.menu_frame.configure(height=self.winfo_height())
        self.chat_field.place(x=self.winfo_width() - self.menu - frame.winfo_width())
        self.chat_field.configure(width=self.winfo_width - self.menu_frame.winfo_width()) - self.menu_frame.winfo_width(), height = self.winfo_height())
        self.send_button.place(x=self.winfo_width() - 50,y = self.winfo_height() - 40)
        self.message_entry.place(x=self.menu_frame.winfo_width(), y=self.send_button.winfo_y())
        self.message_entry.configure(width=self.winfo_width - self.menu_frame.winfo_width() - 50)
        self.after(50, self.adaptive_ui)

    def toggle_show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.speed_animation_menu *= -1
            self.btn.configurate(text = "➡")
            self.show_menu()
        else:
            self.is_show_menu = True
            self.speed_animation_menu *= -1
            self.btn.configure(text="⬅️")
            self.label = CTkLabel(self.menu_frame, text="Ім'я")
            self.label.pack(paddy = 30)
            self.entry = CTkEntry(self.menu_frame)
            self.entry.pack()

win = MainWindow()
win.mainloop()
