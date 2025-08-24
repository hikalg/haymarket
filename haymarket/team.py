from dotenv import load_dotenv
import os
import player as p

load_dotenv()

min_team_size = os.getenv('MIN_TEAM_SIZE')
max_team_size = os.getenv('MAX_TEAM_SIZE')

class Team:
    players = []
    player_count = 0
    team_info = {
        
    }
    
    def __init__(self, *players : p.Player) -> None:
        # Checks for amount of parameters
        if len(players) < int(min_team_size or 0) or len(players) > int(max_team_size or 0) :
            pass
            
        # Appends players to list    
        for player in players:
            self.players.append(player)
        
    def add_players(self, *players : p.Player) -> int:
        players_queue = self.players
        
        for player in players:
            players_queue.append(player)

        if len(players_queue) >  int(max_team_size or 0):
            return 108
        else:
            self.players = players_queue
            return 0
        
    def remove_players(self, *players : p.Player | int) -> int:
        players_queue = self.players
        for player in players:
            if player not in players_queue:
                return 180
            
            players_queue.remove(player)
            
        if (len(players_queue) < int(min_team_size or 0) or players == "*"):
            players_queue = []
        
        self.players = players_queue
        return 0
    
    def is_in_team(self, *players : p.Player) -> tuple:
        status = []
        for player in players:
            if player not in self.players:
                status.append(False)
            
            status.append(True)
        
        return tuple(status)
            