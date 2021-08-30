''''
the users can get to the top of the leaderboard by earning XP (experience points) in different modes. The leaderboard is sorted by players XP in descending order, and in case of a tie - by their ids in ascending order.

Your task is to implement an algorithm that will return the state of the weekly leaderboard given a list of users.

Example

For

users = [["warrior", "1", "1050"],
         ["Ninja!",  "21", "995"],
         ["recruit", "3", "995"]]
the output should be
sortUsers(users) = ["warrior", "recruit", "Ninja!"].

'''
def sortUsers(users):
    res = [User(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))

class User(object):
    def __init__(self, name, userid, xp):
        self.name = name
        self.userid = int(userid)
        self.xp = int(xp)
        
    def __str__(self):
        return self.name
    
    def __lt__(self, other):
        return (self.xp, -self.userid) < (other.xp, -other.userid)