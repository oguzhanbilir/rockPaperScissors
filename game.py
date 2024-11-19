import tkinter as tk
from tkinter import ttk, messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Taş Kağıt Makas")
        self.root.geometry("400x500")
        self.root.configure(bg='#f0f0f0')

        # Skor
        self.player_score = 0
        self.computer_score = 0

        # Stil ayarları
        style = ttk.Style()
        style.configure('Game.TButton', font=('Arial', 12, 'bold'), padding=10)
        style.configure('Score.TLabel', font=('Arial', 14, 'bold'), background='#f0f0f0')
        style.configure('Choice.TLabel', font=('Arial', 12), background='#f0f0f0')

        # Başlık
        self.title_label = ttk.Label(
            root,
            text="Taş Kağıt Makas",
            font=('Arial', 20, 'bold'),
            style='Score.TLabel'
        )
        self.title_label.pack(pady=20)

        # Skor göstergesi
        self.score_label = ttk.Label(
            root,
            text=f"Skor: Siz {self.player_score} - {self.computer_score} Bilgisayar",
            style='Score.TLabel'
        )
        self.score_label.pack(pady=10)

        # Seçimler
        self.player_choice_label = ttk.Label(
            root,
            text="Sizin seçiminiz: -",
            style='Choice.TLabel'
        )
        self.player_choice_label.pack(pady=5)

        self.computer_choice_label = ttk.Label(
            root,
            text="Bilgisayarın seçimi: -",
            style='Choice.TLabel'
        )
        self.computer_choice_label.pack(pady=5)

        # Sonuç
        self.result_label = ttk.Label(
            root,
            text="",
            style='Choice.TLabel'
        )
        self.result_label.pack(pady=10)

        # Butonlar için frame
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=20)

        # Oyun butonları
        self.create_buttons()

        # Yeni oyun butonu
        self.new_game_button = ttk.Button(
            root,
            text="Yeni Oyun",
            style='Game.TButton',
            command=self.new_game
        )
        self.new_game_button.pack(pady=20)

    def create_buttons(self):
        choices = [("Taş", "🗿"), ("Kağıt", "📄"), ("Makas", "✂️")]
        
        for choice, emoji in choices:
            btn = ttk.Button(
                self.button_frame,
                text=f"{choice} {emoji}",
                style='Game.TButton',
                command=lambda c=choice: self.play(c)
            )
            btn.pack(side=tk.LEFT, padx=5)

    def play(self, player_choice):
        choices = ["Taş", "Kağıt", "Makas"]
        computer_choice = random.choice(choices)

        self.player_choice_label.config(text=f"Sizin seçiminiz: {player_choice}")
        self.computer_choice_label.config(text=f"Bilgisayarın seçimi: {computer_choice}")

        # Kazananı belirle
        if player_choice == computer_choice:
            result = "Berabere!"
        elif (
            (player_choice == "Taş" and computer_choice == "Makas") or
            (player_choice == "Kağıt" and computer_choice == "Taş") or
            (player_choice == "Makas" and computer_choice == "Kağıt")
        ):
            result = "Kazandınız!"
            self.player_score += 1
        else:
            result = "Bilgisayar kazandı!"
            self.computer_score += 1

        # Sonuçları güncelle
        self.result_label.config(text=result)
        self.score_label.config(text=f"Skor: Siz {self.player_score} - {self.computer_score} Bilgisayar")

        # Oyun sonu kontrolü
        if self.player_score == 5 or self.computer_score == 5:
            winner = "Siz" if self.player_score == 5 else "Bilgisayar"
            messagebox.showinfo("Oyun Bitti!", f"Oyun bitti! {winner} kazandı!")
            self.new_game()

    def new_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.player_choice_label.config(text="Sizin seçiminiz: -")
        self.computer_choice_label.config(text="Bilgisayarın seçimi: -")
        self.result_label.config(text="")
        self.score_label.config(text=f"Skor: Siz {self.player_score} - {self.computer_score} Bilgisayar")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
