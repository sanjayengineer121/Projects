import random
def choices():
    print("what is your choice? <r> for rock <p> for paper <s>for scissors")
    user=input()
    comptur=random.choice(['r','p','s'])

    if user==comptur:
        return 'Tie'
    if is_win(user,comptur):
        return 'You Won'
    return 'You Lost'

def is_win(player,opponent):
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
print(choices())
