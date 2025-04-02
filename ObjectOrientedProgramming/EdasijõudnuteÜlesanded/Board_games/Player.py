class Player:
    def __init__(self, name):
        self.name = name
        self.games_played = 0
        self.games_won = 0
        self.games = []

    def add_game(self, game_name, result):
        self.games_played += 1
        self.games.append((game_name, result))
        if result == "WIN":
            self.games_won += 1