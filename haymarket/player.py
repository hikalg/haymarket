from dotenv import load_dotenv
import os

load_dotenv()

base_rating = os.getenv("BASE_RATING")

class Player:
    name : str
    rating = 0
    matches = 0
    wins = 0

    def __init__(self, name) -> None:
        self.name = name
        self.rating = base_rating
        self.matches = 0
        self.wins = 0
        
    def __str__(self) -> str:
        return f"Player ${self.name} has rating of ${self.rating} [${self.wins} Wins / ${self.matches} Matches]"
        
    def set_rating(self, rating) -> int:
        self.rating = rating
        return 0
    
    def adjust_rating(self, rating) -> int:
        self.rating = self.rating + rating
        return 0