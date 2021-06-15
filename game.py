import random
def rolldice():
    x = random.randint(1, 7)
    return x
p1=0
p2=0

def danger(p) :
    thisdict = {
        19: 9,
        25: 16,
        46: 32,
        74: 63,
        95: 83,
        99: 10
    }
    danger_numbers = [19, 25, 46, 74, 95, 99]
    for i in danger_numbers:
        if p == i:
            p = thisdict[i]
            print('srry the snake has taken u down')
        else:
            return p
def good(l):
    thisdicto = {
        14: 28,
        22: 31,
        36: 49,
        38: 85,
        48: 69,
        54: 72,
        71: 88
    }
    good_numbers = [14, 22, 36, 38, 71, 54, 48]
    for w in good_numbers:
        if l == w:
            l = thisdicto[w]
            print('hey u got a ladder')
        else:
            return l
danger_numbers=[5,19,25,46,74,95,99]
number_of_players=input("Enter go  ")
if number_of_players=="go":

    while True:
        rollit=input('click r to roll for p1 ')
        if rollit=='r' :
            number=rolldice()
            p1 = p1 + number
            p1=danger(p1)
            p2=good(p1)
            print( p1 )
            if p1>=100:
                print('p1 won congratulations')
                break


        rollit2=input('click r to roll for p2  ')
        if rollit2=="r":
            number2=rolldice()
            p2=p2+number2
            p2=danger(p2)
            p2=good(p2)
            print(  p2)
            if p2==100:
                print('p2 won congratulations')
                break
print('thank you for playing')








