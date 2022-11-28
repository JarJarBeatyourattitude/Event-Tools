#Likes scores is a wip, it needs to be fixed with real data on time 
def sentiment_likes_intensity_scorer(posts_in, sentiment_param, sentiment_list, avg_likes_in, likes_in, intensity_param):
    length_scores = []
    sentiment_scores = []
    like_scores = []
    for i in range(len(posts_in)):
        sentiment_scores.append(1-(abs(sentiment_param-sentiment_list[i])))
        intensity_scores = (abs(0.5-intensity_param)*2)
        like_scores.append(1-(abs(avg_likes_in[i]-likes_in[i]))/avg_likes_in[i])
    return length_scores, sentiment_scores, like_scores

def length_sentiment_likes_scorer(posts_in, length_avg, length, sentiment_param, sentiment_list, avg_likes_in, likes_in):
    length_scores = []
    sentiment_scores = []
    like_scores = []
    for i in range(len(posts_in)):
        sentiment_scores.append(1-(abs(sentiment_param-sentiment_list[i])))

        if (length_avg>length):
            length_score = 1-(abs(length_avg-length))/length_avg
        else: 
            length_score = 1-(abs(length_avg-length))/length
            

        like_scores.append(1-(abs(avg_likes_in[i]-likes_in[i]))/avg_likes_in[i])
    return length_scores, sentiment_scores, like_scores
