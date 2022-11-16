#-------------------------------------------------------------------------------
# LA1.py
# Name: Cayden Taylor
# Python Version: 3.9.1
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Lab session
#-------------------------------------------------------------------------------
# Any notes to grader: fully implemented
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

#define vote_dict function

def vote_dict(filename):
    votes = {}
    with open(filename) as f:
        for line in f:
            key = line.strip()
            if key in votes:
                votes[key] +=1
            else:
                votes[key] = 1
    return votes


#define get_winner function
def get_winner(votes_dict):
    max_vote = 0
    winner = ''
    for k,v in votes_dict.items():
        if v> max_vote:
            max_vote = v
            winner = k
    return max_vote, winner
    



def main():
    votes = vote_dict('LA1_ReadFile.txt')
    print(votes)
    max_vote, winner = get_winner(votes)
    print('Winner of the election is {} with total votes {}'.format(winner, max_vote))
    
if __name__ == "__main__":
    main()
