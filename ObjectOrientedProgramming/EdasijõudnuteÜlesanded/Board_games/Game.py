class Game:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.results = []

    def add_player(self, player):
        self.players.append(player)

    def add_result(self, result_type, results):
        self.results.append((result_type, results))