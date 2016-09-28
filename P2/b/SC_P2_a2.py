# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:13:15 2015

@author: Karan Hegde
"""
import tweepy
from tweepy import OAuthHandler
from random import randint
import json

mylocation = "#hunt"
myname = "sharaths1993"
my_mode = "Loud"
expected_mode = "Loud"
call_list = ['Anakin', 'Chewbacca', 'Han', 'Jango', 'JarJar', 'Leia', 'Luke', 'Mace', 'ObiWan', 'Padme', 'Yoda']
urgency_list = ['0','1']
response_list = ['Positive','Negative','Neutral']
choice_list = ['Yes','No']

class MyStreamListener(tweepy.StreamListener):
    
    def on_status(self, status):
        screenname = status.user.screen_name
        
        if "checked" in status.text:
            with open('checkedtweets.txt','a') as tf:
                tf.write(status.text)
                tf.write('\n')
            count = 0
            substrindex=[]
            for i in range(0,len(status.text)):
                if status.text[i] == '#' and count<3:
                    substrindex.append(i)
                    count = count + 1
            location = status.text[substrindex[0]:(substrindex[1]-1)]
            if location == mylocation:                
                responseid = status.text[(substrindex[1]+1):(substrindex[2]-1)]
                response_tweet = "@"+screenname+"\nName: "+myname+"\nMY_MODE: "+my_mode+"\nEXPECTED_MODE: "+expected_mode+"\n#"+responseid+" #P2CSC555F15"
                #print "MY RESPONSE TWEET CHECKED"                
                api.update_status(status=response_tweet)               
                #print response_tweet
        
        elif "CALL" in status.text:
            with open('calltweets.txt','a') as tf:
                tf.write(status.text)
                tf.write('\n')
            count = 0
            substrindex=[]
            for i in range(0,len(status.text)-2):
                if status.text[i] == '#' and count < 2:
                    substrindex.append(i)
                    count = count + 1
            responseid = status.text[substrindex[0]:(substrindex[1]-1)]
            rand = randint(0,(len(call_list)-1))
            rand2 = randint(0,(len(urgency_list)-1))
            response_tweet = "@"+screenname+"\nCall from: "+call_list[rand]+"\nURGENCY: "+urgency_list[rand2]+"\n"+responseid+" #P2CSC555F15"
            #print "MY RESPONSE TWEET IN CALL"            
            #print response_tweet            
            api.update_status(status=response_tweet)
        
        elif "ACTION" in status.text:
            with open('actiontweets.txt','a') as tf:
                tf.write(status.text)
                tf.write('\n')
            count = 0
            substrindex = []
            for i in range(0,len(status.text)-2):
                if status.text[i] == '#' and count <2:
                    substrindex.append(i)
                    count = count + 1
            responseid = status.text[substrindex[0]:(substrindex[1]-1)]
            rand = randint(0,(len(response_list)-1))
            response_tweet = "@"+screenname+"\nRESPONSE: "+response_list[rand]+"\n"+responseid+" #P2CSC555F15"
            #print "MY RESPONSE TWEET IN ACTION"            
            #print response_tweet
            api.update_status(status=response_tweet)
            
        elif "@sharaths1993" in status.text:
            with open('callresponsetweets.txt','a') as tf:
                tf.write(status.text)
                tf.write('\n')
            count = 0
            substrindex = []
            for i in range(0,len(status.text)-2):
                if status.text[i] == '#' and count <2:
                    substrindex.append(i)
                    count = count + 1
            responseid = status.text[substrindex[0]:(substrindex[1]-1)]
            rand = randint(0,1)
            response_tweet = "ACTION: "+choice_list[rand]+" "+responseid+" #P2CSC555F15"
            print "MY RESPONSE TWEET URGENCY @sharaths1993"
            print response_tweet
        return True
        
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

ACCESS_TOKEN = '4147000203-REcSr6HMTGTJWvUPdBrigixqphOclTLWl0Dm3fg'
ACCESS_SECRET = 'MEQgIxxJmpoCD0poMJxYxv0M8iAcSVdVH9RkIWdA1WW7p'
CONSUMER_KEY = 'cDrmgM7RVvSqmQAepKZdBEtqm'
CONSUMER_SECRET = '3cmB3lnIdilSZLsNz7SHJK7EcISjh48NfLS8m16JSiKxiznnUj'

authorization = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(authorization)
authorization.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
TwitterStream = tweepy.Stream(authorization, MyStreamListener())
TwitterStream.filter(track=['P2CSC555F15'])