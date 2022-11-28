import tweepy
import time
from text_similarity import *
tweets_id=None

PUBLIC_API_KEY = '7GEAlwqaHsCdBMOm7oKgb4oHt'
SECRET_API_KEY = '8l1hYYSqtKZKftWRPhsolqjtZbmpDOD8T6jr1VR9tiaSm7qoEq'

ACCESS_TOKEN_PUBLIC = '1503512551014862850-tu7NtTBXgkszFcelEawQryoVL65RQq'
ACCESS_TOKEN_SECRET = 'CyEoYYq287nS9gbZg5edkJjsNSbASUmLSfS5vOiGkRMdK'

SLEEP_TIME = 30
STARTING_COUNT = 10

LIST_NAME = 'Oops'
LIST_PRIVATE = True     #Set to False if you want the list public
LIST_DESCRIPTION = 'List of users I was following'
SKIP_UNFOLLOWING_PRIVATE_ACCOUNTS = False # Set to true to skip unfollowing private/locked accounts


print('Running Twitter Following to List Migration Script...\n')

#Setup authentication
auth = tweepy.OAuthHandler(PUBLIC_API_KEY, SECRET_API_KEY)
auth.set_access_token(ACCESS_TOKEN_PUBLIC, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#Set list mode to correct value
list_mode = 'private' if LIST_PRIVATE else 'public'

#if list already exists add to it, otherwise create new list
list_already_exists = False
for current_list in api.get_lists():
    if current_list.name == LIST_NAME:
        our_list = current_list
        list_already_exists = True

#Create new list if it doesn't exist already
if not list_already_exists:
    our_list = api.create_list(LIST_NAME, mode=list_mode, description=LIST_DESCRIPTION)

#Get total count of those we are following
following_count = len(api.get_friend_ids())

num_added_to_list = 0
#Iterate through friends adding them to list
for friend_id in api.get_friend_ids():
    print(f"adding {friend_id} to list")
    api.add_list_member(list_id=our_list.id, user_id=friend_id, owner_id=api.verify_credentials().id)
    num_added_to_list += 1
    
    friend = api.get_user(user_id=friend_id)
    ''' The stuff below this is for unfollowing people after 
    if friend.protected:
        if not SKIP_UNFOLLOWING_PRIVATE_ACCOUNTS:
            api.destroy_friendship(user_id=friend_id)
            print(f"unfollowing {friend_id}")
    else:
        api.destroy_friendship(user_id=friend_id)
        print(f"unfollowing {friend_id}")
    '''
#Memory for all tweets in list 
Daily_memory = [""]
Starting_index = 1
Similarity_memory = [{}]

while True:
    if tweets_id is None:
        recent_tweets = api.list_timeline(list_id = our_list.id, include_rts=True, count=STARTING_COUNT)
    else: 
        recent_tweets = api.list_timeline(list_id = our_list.id, include_rts=True, since_id=tweets_id)

    tweets_id = (recent_tweets[0].id)
    for i in (recent_tweets):
        Daily_memory.append(i)
    

    output_list = similarity_run(Daily_memory, Starting_index)
    print(output_list[1])
    print(Daily_memory[1].text)
    print(Daily_memory[3].text)
    

    #Scan 1: 
    layer_1_list = []
    for i in range(len(output_list)-1):
        i+=1
        for b in range(len(Daily_memory)-2):
            if(output_list[i]["similarities"][b]) >= 0.75 and (output_list[i]["similarities"][b]) <= 0.999:
                if(b<=len(output_list)):
                    layer_1_list.append(Daily_memory[i].text)
                else: 
                    layer_1_list.append(Daily_memory[i].text)
                    layer_1_list.append(Daily_memory[b].text)
    print((layer_1_list))

    layer_2_list = []
    layer_output_list = layered_run(layer_1_list)
    for i in range(len(layer_output_list)):
        for b in range(len(layer_output_list)):
            if layer_output_list[i]["similarities"][b] >= 0.75 and  layer_output_list[i]["similarities"][b] <= 0.999:
                layer_2_list.append(layer_1_list[i])

    print(layer_2_list)




    '''for i in range(len(output_list)-1):
        i+=1
        for b in range(len(Daily_memory)-2):
            if(output_list[i]["similarities"][b]) >= 0.75:#Change to more like 0.85
                Similarity_memory.append({
                    "# Of Matches": 1,
                    "Similarity Scores": output_list[i]["similarities"][b],
                    "Tweet_Text_1": Daily_memory[i].text,
                    "Tweet_Text_2": Daily_memory[b].text
                })
    print(Similarity_memory[1])


    print(output_list[1]["similarities"])'''
  











    time.sleep(SLEEP_TIME)






