import requests
def sent_and_length(posts):
    pos_list = []
    len_list = []
    for i in range(len(posts)):
        input = posts[i]
        r = requests.get('https://api.uclassify.com/v1/uClassify/Sentiment/classify/?readKey=CXv5qrtonYLk&text=' + input)
        index_pos = r.text.index("\"positive\":")
        if (index_pos>=19):
            end_pos = r.text.index("}")
        else:
            end_pos = r.text.index(",")
        r = (float)(r.text[index_pos+11:end_pos])
        pos_list.append(r)
        l = len(input.split())
        len_list.append(l)
    return (pos_list,len_list)
