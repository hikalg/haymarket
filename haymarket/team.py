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
       pass