import random
def choose():
    words=['apple', 'journey', 'cloud', 'whisper', 'galaxy', 'river', 'umbrella', 'stone', 'breeze', 'spark', 'ladder', 'dream', 'ocean', 'flame', 'shadow', 'bridge', 'forest', 'crystal', 'echo', 'thunder']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1name,p2name,pp1,pp2):
    print(p1name,'Your score is ',pp1)
    print(p2name,'Your score is ',pp2)
    print('Thanks for Playing')
    
def play():
    p1name=input('Player 1, Please enter your name-->')
    p2name=input('Player 2, Please enter your name-->')
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        # player 1
        if turn%2==0:
            print(p1name,'Your turn')
            ans=input('What is in your mind ?')
            if ans==picked_word:
                pp1=pp1+1
                print('Your score is ',pp1)
            else:
                print('Better luck next time. I thought-->',picked_word)
            c=input('Press 1 to Continue and 0 to Quit')
            if c==0:
                thank(p1name, p2name, pp1, pp2)
            #player 2
            else:
                print(p2name,'Your turn')
                ans=input('What is in your mind ?')
                if ans==picked_word:
                    pp2=pp2+1
                    print('Your score is ',pp2)
                else:
                    print('Better luck next time. I thought-->',picked_word)
                c=input('Press 1 to Continue and 0 to Quit')
                if c==0:
                    thank(p1name, p2name, pp1, pp2)
                    break
            turn=turn+1
play()                