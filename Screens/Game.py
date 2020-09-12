import tkinter as tk


class Game(tk.Frame):
    def __init__(self, root: tk.Tk, app):
        tk.Frame.__init__(self, master=root, bg="#A2A2A2")
        self.app = app
        self.init_widgets()

    def init_widgets(self):
        # En-tête
        self.header = tk.Frame(self, width=60, bg="#A2A2A2")
        self.header.grid(row=0, columnspan=3)

        self.back = tk.Button(self.header, text="Retour",
                              width=7, command=self.app.go_back_to_home, bg="#1BA1E2")
        self.back.grid(row=0, column=0, ipady=5)
        self.message = tk.Label(self.header, width=40)
        self.message.grid(row=0, column=1, ipady=5)
        self.money = tk.Label(self.header, text="", width=10)
        self.money.grid(row=0, column=2, ipady=5)

        # corps
        self.info_number_f = tk.Label(
            self, width=10, text="Nombre parié:", bg="#A2A2A2")
        self.info_number_f.grid(row=1, column=0, ipady=7)

        self.info_money_f = tk.Label(
            self, width=10, text="Mise(€) :", bg="#A2A2A2")
        self.info_money_f.grid(row=2, column=0, ipady=7, sticky='w')

        self.bet_number_v = tk.StringVar()
        self.bet_number_f = tk.Entry(
            self, textvariable=self.bet_number_v)
        self.bet_number_f.grid(row=1, column=1, ipady=7)

        self.bet_money_v = tk.StringVar()
        self.bet_money_f = tk.Entry(self, textvariable=self.bet_money_v)
        self.bet_money_f.grid(row=2, column=1, ipady=7)

        self.message_number = tk.Label(
            self, width=30)
        self.message_number.grid(row=1, column=2, ipady=7)

        self.play_b = tk.Button(self, text="Jouer !",
                                command=self.app.play_game, bg="#60A917", width=30)
        self.play_b.grid(row=2, column=2, ipady=7)

        # Marges
        self.grid_rowconfigure(0, pad=25)
        self.grid_rowconfigure(1, pad=25)
        self.grid_rowconfigure(2, pad=25)

        self.grid_columnconfigure(0, pad=20)
        self.grid_columnconfigure(1, pad=20)
        self.grid_columnconfigure(2, pad=20)

        self.header.grid_columnconfigure(0, pad=20)
        self.header.grid_columnconfigure(1, pad=20)
        self.header.grid_columnconfigure(2, pad=20)

    def show_info_message(self, message: str):
        self.message["text"] = message

    def show_number_a(self, number: int):
        # TODO : processus d'animation
        if number % 2 == 0:
            self.message_number["bg"] = "black"
            self.message_number["fg"] = "white"
        else:
            self.message_number["bg"] = "red"
            self.message_number["fg"] = "black"
        self.message_number["text"] = "La roulette est sur le numéro {}".format(
            str(number))

        def show_number(self, number: int):
            self.message_number["text"] = "La roulette est sur le numéro {}".format(
                str(number))

    def show_actual_money(self):
        self.money["text"] = str(self.app.actual_money) + " €"

    def reset(self):
        self.money["text"] = "\€"
        self.message_number["text"] = "La roulette n'a pas encore tournée !"
        self.message_number["bg"] = "white"
        self.message_number["fg"] = "black"
        self.message["text"] = "Combien allez-vous misez ?"
        self.clear_bet_money()
        self.clear_bet_number()

    def clear_bet_number(self):
        self.bet_number_f.delete(0, len(self.bet_number_v.get()))

    def clear_bet_money(self):
        self.bet_money_f.delete(0, len(self.bet_money_v.get()))
