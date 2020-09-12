import tkinter as tk


class Home(tk.Frame):
    def __init__(self, root: tk.Tk, app):
        tk.Frame.__init__(self, master=root, bg="#A2A2A2")
        self.app = app
        self.init_widgets()

    def init_widgets(self):
        self.title = tk.Label(
            self, text="Casino : La roulette", width=60, bg="#A2A2A2", font=("Courrier", 12, 'bold'))
        self.title.grid(row=0, columnspan=3, ipady=7)

        self.load_b = tk.Button(
            self, text="Charger la partie", width=20, bg="#60A917", command=self.app.load_game)
        self.load_b.grid(row=1, column=0, ipady=7)
        self.new_b = tk.Button(
            self, text="Nouvelle partie", width=20, bg="#1BA1E2", command=self.app.new_game)
        self.new_b.grid(row=1, column=1, ipady=7)
        self.leave_b = tk.Button(
            self, text="Quitter", width=20, bg="#A20025", command=self.app.leave_app)
        self.leave_b.grid(row=1, column=2, ipady=7)

        self.message = tk.Label(self, text="", bg="#A2A2A2", width=60)
        self.message.grid(row=2, columnspan=3, ipady=7)

        self.grid_rowconfigure(0, pad=25)
        self.grid_rowconfigure(1, pad=25)
        self.grid_rowconfigure(2, pad=25)
        self.grid_columnconfigure(0, pad=25)
        self.grid_columnconfigure(1, pad=25)
        self.grid_columnconfigure(2, pad=25)

    def show_message(self, message: str):
        self.message["text"] = message

    def reset(self):
        self.show_message("")
