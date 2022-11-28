'''Pricing is getting reall complicated, but for now let's just work with fake numbers 
Should I use comments or only posts. I think that comments might be valuable too. 
First, I should decide what data goes in for decision making (INPUT)

1. Post/comment (The contents of the post made taken)
2. Likes
3. # of Comments, 
4. Average likes (Taken from all, or maybe a small sample size. No garuntee I can do it with pricing in mind)
5. Time 

OPTIONS: 
1. selected topic 
2. selected keyword
3. range in predicted popularity 
4. range and/or intensity of sentiment 

I sorta forgot to do #3 in a range. Maybe I can have 2 modes, with 1 for getting engagement vs one for education 
Don't forget about the idea of having a startup wizard thing that asks a few questions and makes a default setup. 
'''

from Functions.sentiment_n_length import *
from Functions.scoring import *
#Starting point variable exambles: 

posts_in = ["We live in a society, you know right?", "I am not a Crook!"]
likes_in = [52,603]
comment_number_in = [1,6]
avg_likes_in = [100,1200]
time_in = ["Mon Nov 20 13:08:45 +0000 2022", "Mon Nov 20 13:09:45 +0000 2022"]

#There could be 3  kinds of User_pref, where one uses topic modelling to automatically find what to follow, Another uses a premade topic analzer,  third can look for specific words 
#User settings example: 
user_preference_param = 0
topics_param = [0.04, 0.02, 0.354, 0.26, .62]
keywords_param_regular  = ["analytics", "Pivot", "Pivot Analytics", "Social Media Analytics", "Society"]
matches = 5 #How many tweets need to match the alert before it goes off 
#Should I always lowercase, or maybe ask which words should only be uppercased?
keywords_param = [] 
for i in range(len(keywords_param_regular)):
    keywords_param.append(keywords_param_regular[i].lower())

predicted_likes_param = True 
sentiment_param = 0.8
intensity_param = 0.3 #(Ranges from 0-1, where 1 is most intense, false for not included)
length_param = False

#Finds the sentiment and length of each post and saves them in seperate lists 
sentiment_list, length_list = sent_and_length(posts_in)
#Converts sentiment, length and # of likes into a score, saved in seperate lists (doesn't check length on this one)
length_scores, sentiment_scores, like_scores = sentiment_likes_intensity_scorer(posts_in, sentiment_param, sentiment_list, avg_likes_in, likes_in,intensity_param)

#Keyword scoring: 
keyword_scores = []
for i in range (len(posts_in)):
    keyword_scores.append(0)
    posts_in_lower = posts_in[i].lower()
    for b in range (len(keywords_param)):
        if((keywords_param[b]) in posts_in_lower):
            keyword_scores[i] += 1

'''The final score should probably be handled by an AI, but I need a way to train it :(
 One consideration though is that predicted_likes stuff should be added later unless feedback is after a while of posting a response 

I have 2 options to train my AI: 
1. Start out with a beta group, then use their selections saved as data for training 
2. Do it myself

1. is more accurate and doesn't require a ton of work from me, but could be much more expensive and take longer in days 
2. easier to do but takes much longer in time and is less accurate 
'''











