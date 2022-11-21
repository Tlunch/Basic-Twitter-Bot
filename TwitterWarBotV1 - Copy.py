# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:32:51 2020

@author: demon
"""
import tweepy
import secrets as r
import time as t

#Add your credentials here
twitter_keys = {
        'consumer_key':        ,
        'consumer_secret':     ,
        'access_token_key':    ,
        'access_token_secret': 
    }

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)

Players = ["Calum","Chris","Soctt Edler","Robbie","Rory","Keelan","Sophy","Jas","Lewis","Fast Eddie","Andrew"]
Weapons = ["a knife","the wooden hand of god","the visual bible","a Wee Mexico","Sophies nonce classes","some moldy dishes","a horrific dish towlel","a pair of flip flops","a dissapointed parent","steepies","the large suculent","the ceramic goose","the visual bible","a cheap chinese bike frame","the frozen orange","the frozen VK", "the frozen burger","the C1"]
Adjectives = ["horrifically","creatively","grusomely","slowly","by beating them","by flaying them","horrifically","creatively","grusomely","slowly","by beating them","by flaying them","rectally"]

def procedure():
    if len(Players) == 1:
        api.update_status("Congratulations {} you have won the tournament.".format(Players[0]))
        return
    else:
        A = r.choice(Players)
        while True:
            B = r.choice(Players)
            if A == B:
                continue
            else:
                break
        api.update_status("{} killed {} {} with {}.".format(A,B,r.choice(Adjectives),r.choice(Weapons)))
        Players.remove(B)
        if len(Players)==1:
            procedure()
        api.update_status("{} players remain. May the odds be ever in your favor.".format(len(Players)))
        t.sleep(120)
        procedure()
procedure()

