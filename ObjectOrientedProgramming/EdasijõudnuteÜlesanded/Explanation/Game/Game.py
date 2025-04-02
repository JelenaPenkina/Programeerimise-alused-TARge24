class Game:
    def __init__(self, name):
        self.name = name
        self.players = []  # Mängus osalenud mängijad
        self.results = []  # Mängu tulemused

    def add_player(self, player):
        """Lisame mängijad mängu."""
        self.players.append(player)

    def add_result(self, result_type, results):
        """Salvestame mängu tulemused."""
        self.results.append((result_type, results))
