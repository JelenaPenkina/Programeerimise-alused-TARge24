import Player
import Game
import Match

class Statistics:
    def __init__(self, filename):
        self.players = {}
        self.games = {}
        self.matches = []
        self._load_data(filename)

    def _load_data(self, filename):
        with open(filename, "r") as file:
            for line in file:
                game_name, players, result_type, results = line.strip().split(";")
                players = players.split(",")
                results = results.split(",")

                # Create game and player objects
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
            elif path.endswith("/favourite"):
                # Favourite game is the game the player has played most frequently
                game_counts = {}
                for game, _ in self.players[player_name].games:
                    if game not in game_counts:
                        game_counts[game] = 0
                    game_counts[game] += 1
                return max(game_counts, key=game_counts.get)
            elif path.endswith("/won"):
                return self.players[player_name].games_won
        elif path.startswith("/game/"):
            game_name = path.split("/")[2]
            game = self.games[game_name]
            if path.endswith("/amount"):
                return len(game.results)
            elif path.endswith("/player-amount"):
                # Count the most frequent number of players
                player_count = {}
                for match in game.results:
                    player_count[len(match[1])] = player_count.get(len(match[1]), 0) + 1
                return max(player_count, key=player_count.get)
            elif path.endswith("/most-wins"):
                # Get the player with most wins in this game
                win_count = {}
                for match in game.results:
                    for i, result in enumerate(match[1]):
                        if result == "winner":
                            win_count[game.players[i]] = win_count.get(game.players[i], 0) + 1
                return max(win_count, key=win_count.get)
            elif path.endswith("/most-frequent-winner"):
                # Calculate player with most frequent wins
                pass  # Similar approach as for most-wins
