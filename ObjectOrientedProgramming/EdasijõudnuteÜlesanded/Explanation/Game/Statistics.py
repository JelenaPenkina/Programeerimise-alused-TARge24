class Statistics:
    def __init__(self, filename):
        self.players = {}  # Sõnastik mängijate objektide hoidmiseks
        self.games = {}    # Sõnastik mängude objektide hoidmiseks
        self.matches = []  # Kõik mängud
        self._load_data(filename)

    def _load_data(self, filename):
        """Loeme tulemused failist ja töötleme need."""
        with open(filename, "r") as file:
            for line in file:
                game_name, players, result_type, results = line.strip().split(";")
                players = players.split(",")
                results = results.split(",")

                # Loome mängu objekti, kui see pole veel olemas
                if game_name not in self.games:
                    self.games[game_name] = Game(game_name)

                game = self.games[game_name]

                for player in players:
                    if player not in self.players:
                        self.players[player] = Player(player)
                    player_obj = self.players[player]
                    game.add_player(player_obj)
                    player_obj.add_game(game_name, result_type)

                match = Match(game_name, players, result_type, results)
                self.matches.append(match)
                game.add_result(result_type, results)

    def get(self, path: str):
        """Vastame päringutele."""
        path_parts = path.split("/")
        if path == "/players":
            return list(self.players.keys())
        elif path == "/games":
            return list(self.games.keys())
        elif path == "/total":
            return len(self.matches)
        elif path.startswith("/total/"):
            result_type = path.split("/")[-1]
            return sum(1 for match in self.matches if match.result_type == result_type)
        elif path.startswith("/player/"):
            player_name = path.split("/")[2]
            if path.endswith("/amount"):
                return self.players[player_name].games_played
            elif path.endswith("/won"):
                return self.players[player_name].games_won
