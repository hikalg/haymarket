import player as p

class Match:
    class Participant():
        player = {
            
        }
        score : int
        
        def __init__(self, player: p.Player) -> None:
            self.player = {
                'object': player,
                'player_name': player.name,
                'rating': player.rating, 
            }
            self.score = 0
             
             

    p1 : p.Player
    p2 : p.Player
    winner : Participant

    def __init__(self, p1 : p.Player, p2 : p.Player) -> None:
            self.p1 = p1
            self.p2 = p2
            
            self.participant_one = self.Participant(self.p1)
            self.participant_two = self.Participant(self.p2)
            
    def score(self, p1, p2) -> int:
        if ((p1 or p2) is not (int or '*')):
              return -21 # returns error 21: scoring error
        p1.score = p1
        p2.score = p2
        return 0