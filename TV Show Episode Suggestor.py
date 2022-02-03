# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 21:39:21 2021

@author: sidvs
"""

import random
show = int(input("Choose a show:\n1.) F.R.I.E.N.D.S\n2.) How I Met Your Mother\n3.) Modern Family\n4.) The Big Bang Theory\n"))

def friends():
    season = random.randint(1,10)
    
    if season == 10:
        episode = random.randint(1,18)
    elif season == 7:
        episode = random.randint(1,22)
    elif season == 9:
        episode = random.randint(1,23)
    elif season == 1 or season == 2 or season == 4 or season == 5 or season == 8:
        episode = random.randint(1,24)
    else:
        episode = random.randint(1,25)
        
    return season, episode

def himym():
    season = random.randint(1,9)
    
    if season == 1 or season ==2:
        episode = random.randint(1,22)
    elif season == 3:
        episode = random.randint(1,20)
    else:
        episode = random.randint(1,24)
        
    return season, episode

def modern_fam():
    if season == 1 or season == 2 or season == 3 or season == 4 or season == 5 or season == 6:
        episode = random.randint(1,24)
    elif season == 7 or season == 8 or season == 9 or season == 10:
        episode = random.randint(1,22)
    else:
        episode = random.randint(1,17)
        
    return season, episode

def TBBT():
    season = random.randint(1,12)
    
    if season == 1:
        episode = random.randint(1,17)
    elif season == 2 or season == 3:
        episode = random.randint(1,23)
    elif season == 4 or season == 5 or season == 6 or season == 7 or season == 8 or season == 9 or season == 10 or season == 11 or season == 12:
        episode = random.randint(1,24)
    
    return season, episode

if show ==1:
    season,episode=friends()
    print("Hi!! I suggest you watch Season %d: Episode %d of F.R.I.E.N.D.S!! Enjoy!!"%(season,episode))
elif show==2:
    season,episode=himym()
    print("Hi!! I suggest you watch Season %d: Episode %d of How I Met Your Mother!! Enjoy!!"%(season,episode))
elif show == 3:
    season,episode = modern_fam()
    print("Hi!! I suggest you watch Season %d: Episode %d of Modern Family!! Enjoy!!"%(season,episode))
else:
    season,episode = TBBT()
    print("Hi!! I suggest you watch Season %d: Episode %d of The Big Bang Theory!! Enjoy!!"%(season,episode))