#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json as js
import sys
import pip
from pandas.io.json import json_normalize
from collections import Counter
from collections import OrderedDict 


# In[4]:


with open("/work/00713/kelly/DATA/JUNE_TWITTER/tweets.log.2020-06-04-08-00", "r") as f:
    tweets = f.readlines()


# In[5]:


# tweets


# In[6]:


get_ipython().system('ls /work/00713/kelly/DATA/JUNE_TWITTER')


# In[7]:


# counter = 0
# all_tweets = []
# First_Tweet = js.loads(tweets[0])
# Second_Tweet = js.loads(tweets[1])
# Third_Tweet = js.loads(tweets[2])
# for tweet in tweets:
#     many_tweets = js.loads(tweets[count])
#     counter += 1
#     all_tweets.append(many_tweets)
  


# In[8]:


# print(many_tweets)
# print(len(many_tweets))


# In[9]:


# print(First_Tweet)


# In[10]:


# print(Second_Tweet)


# In[11]:


# print(Third_Tweet)


# In[12]:


print(len(tweets))


# In[13]:


# pd.set_option('display.max_columns', None)


# In[14]:


# json_normalize(First_Tweet)


# In[15]:


# json_normalize(Second_Tweet)


# In[16]:


# json_normalize(Third_Tweet)


# In[17]:


# url_list = []
# url1 = First_Tweet['entities']['urls']
# if "http" in url1[0]["url"]:
#     url_list.append(url1[0]["url"])
# print(len(url_list))
# print(url1)


# In[18]:


# creation_list = []
# create = Third_Tweet['user']['created_at']
# if "2007" in create:
#     creation_list.append(create)
# print(len(creation_list))
# print(create)


# In[19]:


# default = []
# profile = Second_Tweet['user']['default_profile_image']
# if profile == False:
#     default.append(profile)
# print(len(default))


# In[20]:


# fav = []
# fav_cnt = First_Tweet['user']['favourites_count']
# fav.append(fav_cnt)
# print(fav)


# In[21]:


# follow = []
# followers = First_Tweet['user']['followers_count']
# follow.append(followers)
# print(follow)


# In[22]:


# friends = []
# friend_cnt = First_Tweet['user']['friends_count']
# friends.append(friend_cnt)
# print(friends)


# In[23]:


# geo = []
# geo_enabled = Third_Tweet['user']['geo_enabled']
# if geo_enabled == True:
#     geo.append(Third_Tweet['user']['location'])
# print(geo)


# In[24]:


# list = []
# list_cnt = First_Tweet['user']['listed_count']
# if list_cnt >= 1:
#     list.append(list_cnt)
# print(list)


# In[25]:


# private = []
# protected = First_Tweet['user']['protected']
# if protected == False:
#     private.append(First_Tweet['id'])
# print(private)


# In[26]:


# hashtag = []
# hash_cnt = First_Tweet['entities']['hashtags']
# if hash_cnt != []:
#     hashtag.append(hash_cnt)
# print(len(hashtag))


# In[27]:


# status = []
# status_cnt = First_Tweet['user']['statuses_count']
# status.append(status_cnt)
# print(status)


# In[28]:


# mention = []
# mentions_count = Second_Tweet['entities']['user_mentions']
# if mentions_count != []:
#     mention.append(mentions_count)
# print(mention)
# print(len(mention))


# In[29]:


# verified = []
# bin_cla = First_Tweet['user']['verified']
# if bin_cla == False:
#     verified.append(bin_cla)
# print(len(verified))


# In[ ]:





# In[ ]:





# In[ ]:





# In[39]:


Bot_Flag = []
All_Flag = []
Url_Flag = []
Creation_Flag = []
Default_Flag = []
Favourites_Flag = []
Ratio_Flag = []
Geo_Flag = []
Hashtag_Flag = []
Statuses_Flag = []
Verified_Flag = []
Mentions_Flag = []


# In[31]:


count = 0
All_Tweets = []
for tweet in tweets:
    many_tweets = js.loads(tweets[count])
    count += 1
    All_Tweets.append(many_tweets)


# In[ ]:





# In[40]:



all_url = []
counts = 0
for i in All_Tweets:
    
    try:
        temp = i['entities']
 
        for url in temp['urls']:
            print(url)
          
        if len(temp['urls']) > 1 :
            all_url.append(i)
            Bot_Flag.append(i)
        counts += 1
        
    except:
        All_Tweets.remove(i)


# In[33]:


# Url_Flag = []
# for j in all_url:
#     print(j['id'])
#     Url_Flag.append(j['id'])
#     All_Flag.append(j['id'])


# In[34]:


print(len(All_Tweets))


# In[35]:


print(len(all_url))


# In[36]:


print(len(Url_Flag))


# In[37]:


print(len(All_Flag))


# In[41]:


print(len(Bot_Flag))
Bot


# In[39]:


all_hashtag = []
counts = 0
for i in All_Tweets:
    
    try:
        temp = i['entities']
 
        for url in temp['hashtags']:
            print(url)
          
        if len(temp['hashtags']) > 1 :
            all_hashtag.append(i)
            Bot_Flag.append(i)
        counts += 1
        
    except:
        All_Tweets.remove(i)


# In[40]:


print(len(all_hashtag))


# In[41]:


# Hashtag_Flag = []
# for j in all_hashtag:
#     print(j['id'])
#     Hashtag_Flag.append(j['id'])
#     All_Flag.append(j['id'])


# In[42]:


print(len(Hashtag_Flag))


# In[43]:


print(len(All_Flag))
print(len(All_Tweets))
print(len(Bot_Flag))


# In[44]:


all_mention = []
counts = 0
for i in All_Tweets:
    
    try:
        temp = i['entities']
 
        for url in temp['user_mentions']:
            print(url)
          
        if len(temp['user_mentions']) > 1 :
            all_mention.append(i)
            Bot_Flag.append(i)
        counts += 1
        
    except:
        All_Tweets.remove(i)


# In[45]:


# Mentions_Flag = []
# for j in all_mention:
#     print(j['id'])
#     Mentions_Flag.append(j['id'])
#     All_Flag.append(j['id'])


# In[46]:


print(len(all_mention))
print(len(Mentions_Flag))
print(len(All_Flag))
print(len(All_Tweets))
print(len(Bot_Flag))


# In[48]:


all_create = []
counts = 0
for i in All_Tweets:
    
    try:
        temp = i['user']
 
        for url in temp['created_at']:
            print(url)
          
        if "2020" in temp['created_at']:
            all_create.append(i)
            Bot_Flag.append(i)
        counts += 1
        
    except:
        All_Tweets.remove(i)


# In[49]:


print(len(all_create))


# In[50]:


print(len(All_Flag))
print(len(All_Tweets))
print(len(Bot_Flag))


# In[51]:


# Creation_Flag = []
# for j in all_create:
#     print(j['id'])
#     Creation_Flag.append(j['id'])
#     All_Flag.append(j['id'])


# In[52]:


print(len(Creation_Flag))
print(len(All_Flag))
print(len(All_Tweets))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[53]:


all_favs = []
counts = 0
for i in All_Tweets:
    
   
    if i['user']['favourites_count'] < 50 or i['user']['favourites_count'] > 50000:
        all_favs.append(i)
        Bot_Flag.append(i)
    counts += 1
        


# In[54]:


print(len(all_favs))
print(len(Bot_Flag))


# In[55]:


# Favourites_Flag = []
# for j in all_favs:
#     print(j['id'])
#     Favourites_Flag.append(j['id'])
#     All_Flag.append(j['id'])


# In[56]:


print(len(Favourites_Flag))
print(len(All_Flag))


# In[57]:


print(len(All_Tweets))


# In[58]:


all_ratio = []
counts = 0
for i in All_Tweets:
    
   
    if i['user']['friends_count'] >= (i['user']['followers_count'] * 50):
        all_ratio.append(i)
        Bot_Flag.append(i)
    counts += 1


# In[59]:


print(len(all_ratio))
print(len(Bot_Flag))


# In[60]:


# Ratio_Flag = []
# for j in all_ratio:
#     print(j['id'])
#     Ratio_Flag.append(j['id'])
#     All_Flag.append(j['id'])


# In[61]:


print(len(Ratio_Flag))
print(len(All_Flag))


# In[62]:


all_status = []
counts = 0
for i in All_Tweets:
    
   
    if i['user']['statuses_count'] < 20 or i['user']['statuses_count'] > 50000:
        all_status.append(i)
        Bot_Flag.append(i)
    counts += 1
        


# In[63]:


print(len(all_status))
print(len(Bot_Flag))


# In[64]:


# Statuses_Flag = []
# for j in all_status:
#     print(j['id'])
#     Statuses_Flag.append(j['id'])
#     All_Flag.append(j['id'])


# In[65]:


print(len(Statuses_Flag))
print(len(All_Flag))


# In[66]:


all_default = []
counts = 0
for i in All_Tweets:
    
   
    if i['user']['default_profile'] == True:
        all_default.append(i)
        Bot_Flag.append(i)
    counts += 1
        


# In[67]:


print(len(all_default))
print(len(Bot_Flag))


# In[68]:


# Default_Flag = []
# for j in all_default:
#     print(j['id'])
#     Default_Flag.append(j['id'])
#     All_Flag.append(j['id'])


# In[69]:


print(len(Default_Flag))
print(len(All_Flag))


# In[70]:


all_geo = []
counts = 0
for i in All_Tweets:
    
   
    if i['user']['geo_enabled'] == False:
        all_geo.append(i)
        Bot_Flag.append(i)
    counts += 1
        


# In[ ]:





# In[71]:


print(len(all_geo))
print(len(Bot_Flag))


# In[72]:


# Geo_Flag = []
# for j in all_geo:
#     print(j['id'])
#     Geo_Flag.append(j['id'])
#     All_Flag.append(j['id'])


# In[73]:


print(len(Geo_Flag))
print(len(All_Flag))


# In[74]:


all_verified = []
counts = 0
for i in All_Tweets:
    
   
    if i['user']['verified'] == False:
        all_verified.append(i)
        Bot_Flag.append(i)
    counts += 1
        


# In[75]:


print(len(all_verified))
print(len(Bot_Flag))


# In[76]:


# Verified_Flag = []
# for j in all_verified:
#     print(j['id'])
#     Verified_Flag.append(j['id'])
#     All_Flag.append(j['id'])


# In[77]:


print (len(Verified_Flag))
print(len(All_Flag))
print(len(All_Tweets))
print(len(Bot_Flag))


# In[82]:


final = Bot_Flag
Sort = Counter(final)


# In[109]:


print(Sort)


# In[110]:


# Sort[1268528665110839297]


# In[111]:


# Sort[1268529035895877635]


# In[112]:


print(len(Sort))


# In[113]:


new_dict = {}
for key, value in Sort.items():
    if value >= 5:
        new_dict[key] = value


# In[114]:


print(new_dict)


# In[115]:


print(len(new_dict))


# In[117]:


def final_bot_id(BOTS):
    return new_dict[BOTS] >= 5
bot_id = list(filter(final_bot_id, new_dict.keys()))
bot_id


# In[118]:


print(len(bot_id))


# In[123]:


bot_tweets = []
counts = 0
for i in All_Tweets:
    
   
    if i['user']['id'] in bot_id:
        bot_tweets.append(i)
    counts += 1


# In[124]:


bot_tweets


# In[ ]:




