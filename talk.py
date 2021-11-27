import requests

def postTalkApi(apikey, query):
	endpoint = "https://api.a3rt.recruit.co.jp/talk/v1/smalltalk"
	params = {'apikey': apikey,
          	 'query': query,
          	 }
	response = requests.post(endpoint, params)
	return response.json()

apikey = "DZZUtDgIX6YByrW9nkWMqJrWYRl33Qeq"

while True:
	text = input("> ")
	res = postTalkApi(apikey, text)
	print(res['results'][0]['reply'])
    