import tkinter as tk


class Interface:
    def __init__(self, window_size, info):
        self.info = info
        self.window = tk.Tk()
        self.window.title(info.game_name)
        self.window.geometry(window_size)

    def add_message(self):
        initial_message = tk.Label(self.window, text=self.info.welcome_message(), font=('Arial', 14))
        initial_message.pack(expand=True)

        sign_in_button = tk.Button(self.window, text="Sign In!", command=self.sign_in_page)
        sign_in_button.pack(pady=5)
        register_button = tk.Button(self.window, text="Sign up!", command=self.register_page)
        register_button.pack(pady=5)

        
    def sign_in_page(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        sign_in_message = tk.Label(self.window, text="Please enter your information to sign in!", font=('Arial', 14))
        sign_in_message.pack(pady=10)

        username_label = tk.Label(self.window, text="Username:")
        username_label.pack(pady=2)  
        username_feild = tk.Entry(self.window, width=30)
        username_feild.pack(pady=2)

        password_label = tk.Label(self.window, text="Password: ")
        password_label.pack(pady=2)
        password_feild = tk.Entry(self.window, width=30, show="*")
        password_feild.pack(pady=2)

        sign_in_button = tk.Button(self.window, text="Sign In!", command=self.sign_in_message)
        sign_in_button.pack(pady=5)

    def register_page(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        registration_message = tk.Label(self.window, text=f"Please enter your information for your new {self.info.game_name} account!", font=('Arial', 14))
        registration_message.pack(pady=10)

        username_label = tk.Label(self.window, text="Your new username:")
        username_label.pack(pady=2)  
        username_feild = tk.Entry(self.window, width=30)
        username_feild.pack(pady=2)

        password_label = tk.Label(self.window, text="Your new password: ")
        password_label.pack(pady=2)
        password_feild = tk.Entry(self.window, width=30, show="*")
        password_feild.pack(pady=2)

        sign_in_button = tk.Button(self.window, text="Sign Up!", command=self.sign_in_message)
        sign_in_button.pack(pady=5)

    def sign_in_message(self):
        print("Login button clicked")

    def registration_message(self):
        print("Sign up button clicked.")
        
    def play_game(self):
        self.window.mainloop()