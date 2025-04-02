class Player:
    def __init__(self, name):  # Konstruktor, mis käivitatakse objekti loomisel
        self.name = name        # Salvestame mängija nime
        self.games_played = 0   # Mängude arv
        self.games_won = 0      # Võitude arv

    def play_game(self, won: bool):  # Meetod mängu mängimiseks
        self.games_played += 1       # Suurendame mängude arvu
        if won:
            self.games_won += 1      # Kui võidab, suurendame võitude arvu

# Loome objekti "Mati" klassist Player
mati = Player("Mati")
mati.play_game(True)  # Mati võitis ühe mängu
mati.play_game(False) # Mati kaotas ühe mängu

print(mati.name)  # -> Mati
print(mati.games_played)  # -> 2
print(mati.games_won)  # -> 1