from functools import cmp_to_key
class Player:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def __repr__(self):
        return {'name':self.name,'score':self.score}
    def comparator(a,b):
        if b.score==a.score:  
            return (a.name > b.name) - (a.name< b.name)
        return b.score-a.score

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)