from tkinter import *
from BackupManager import *
from Screens import *
from random import randint
from math import ceil


class App:
    def __init__(self):
        self.init_window()
        self.backup_manager = BackupManager("save.txt")
        self.init_screens()

        self.begin_money = 500
        self._actual_money = -1

        self.root.mainloop()

    def init_window(self):
        self.root = Tk()
        self.root.resizable(0, 0)
        self.root.title("Casino : la roulette")
        self.root.config(background="#A2A2A2")
        self.root.iconbitmap('bitmap.ico')

    def init_screens(self):
        self.home_screen = Home(self.root, self)
        self.home_screen.grid()

        self.game_screen = Game(self.root, self)
        self.lose_screen = Lose(self.root, self)

    def new_game(self):
        self.actual_money = self.begin_money

        self.game_screen.reset()
        self.game_screen.show_actual_money()
        self.home_screen.grid_forget()
        self.lose_screen.grid_forget()
        self.game_screen.grid()

    def load_game(self):
        if self.backup_manager.backup_exist() == True:
            self.actual_money = self.backup_manager.get_backup_value()
            self.game_screen.reset()
            self.game_screen.show_actual_money()
            self.home_screen.grid_forget()
            self.game_screen.grid()
        else:
            self.home_screen.show_message(
                "Il n'y pas de sauvegarde enregistrée")

    def lose_game(self):
        self.game_screen.grid_forget()
        self.lose_screen.grid()
        self.backup_manager.delete_backup()

    def go_back_to_home(self):
        self.home_screen.reset()
        self.game_screen.grid_forget()
        self.home_screen.grid()
        return False

    def leave_app(self):
        self.root.destroy()

    def play_game(self):
        if self.get_bet_number() == False:
            self.game_screen.show_info_message(
                "Le nombre parié doit être un entier entre 0 et 49")
            return False
        else:
            self.bet_number = self.get_bet_number()

        if self.get_bet_money() == False:
            self.game_screen.show_info_message(
                "L'argent misé doit être un nombre positif")
            return False
        else:
            if self.get_bet_money() > self.actual_money:
                self.game_screen.show_info_message(
                    "Tu n'as pas assez d'argent pour miser cette somme")
                return False
            else:
                self.bet_money = self.get_bet_money()

        self.win_number = randint(0, 49)
        self.game_screen.show_number_a(self.win_number)
        self.distribute_gains()

        if self.actual_money <= 0:
            self.lose_game()

    def distribute_gains(self):
        if self.win_number == self.bet_number:
            self.add_money(3*self.bet_money)
            self.game_screen.show_actual_money()
            self.game_screen.show_info_message(
                "C'est le bon numéro, vous récupérez 3 fois votre mise !")
        else:
            if self.win_number % 2 == self.bet_number % 2:
                self.add_money(ceil(self.bet_money/2))
                self.game_screen.show_actual_money()
                self.game_screen.show_info_message(
                    "C'est la bonne couleur, vous récupérez la moitié de votre mise !")
            else:
                self.add_money(-self.bet_money)
                self.game_screen.show_actual_money()
                self.game_screen.show_info_message(
                    "Dommage, vous perdez votre mise !")

    def get_bet_number(self):
        try:
            value = int(self.game_screen.bet_number_v.get())
        except ValueError:
            return False
        if value < 0 or value > 49:
            return False
        return value

    def get_bet_money(self):
        try:
            value = int(self.game_screen.bet_money_v.get())
        except ValueError:
            return False
        if value <= 0:
            return False
        return value

    def _get_actual_money(self):
        return self._actual_money

    def _set_actual_money(self, money: int):
        self._actual_money = money
        self.backup_manager.make_backup(
            self.actual_money)  # Sauvegarde automatique

    def add_money(self, value: int):
        self.actual_money += value

    actual_money = property(_get_actual_money, _set_actual_money)
