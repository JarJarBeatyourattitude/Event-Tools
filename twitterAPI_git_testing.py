from TwitterAPI import TwitterAPI

SEARCH_TERM = 'pizza'

api = TwitterAPI('7GEAlwqaHsCdBMOm7oKgb4oHt', 
                 '8l1hYYSqtKZKftWRPhsolqjtZbmpDOD8T6jr1VR9tiaSm7qoEq',
                 auth_type='oAuth2')

r = api.request('search/tweets', {'q':SEARCH_TERM})
for item in r: 
    print(item['text'] + "\n")

print(r.get_quota())
