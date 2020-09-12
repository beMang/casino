import tkinter as tk


class Lose(tk.Frame):
    def __init__(self, root: tk.Tk, app):
        tk.Frame.__init__(self, master=root, bg="#A2A2A2")
        self.app = app
        self.init_widgets()

    def init_widgets(self):
        self.title_m = tk.Label(
            self, text="Tu n'as plus d'argent !", font=("Courrier", 12, 'bold'), bg="#A2A2A2")
        self.title_m.grid(row=0, columnspan=2, ipady=7)

        self.new_game_b = tk.Button(
            self, text="Nouvelle partie", command=self.app.new_game, width=20, bg="#1BA1E2")
        self.new_game_b.grid(row=1, column=0, ipady=7)

        self.leave_b = tk.Button(self, text="Quitter",
                                 command=self.app.leave_app, width=20, bg="#A20025")
        self.leave_b.grid(row=1, column=1, ipady=7)

        self.grid_rowconfigure(0, pad=40)
        self.grid_rowconfigure(1, pad=40)
        self.grid_columnconfigure(0, pad=40)
        self.grid_columnconfigure(1, pad=40)
