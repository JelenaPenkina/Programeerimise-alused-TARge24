class Player:
    def __init__(self, name):
        self.name = name
        self.games_played = 0
        self.games_won = 0
        self.games = []  # Loetelu mängudest, kus mängija on osalenud

    def add_game(self, game_name, result):
        """Salvestame mängu mängimise info."""
        self.games_played += 1
        self.games.append((game_name, result))
        if result == "winner":
            self.games_won += 1