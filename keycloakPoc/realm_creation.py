import requests, json

result = None
while result is None:
    try:
        result = requests.get("http://localhost:8080")
    except:
        pass

url = "http://localhost:8080"

data= {"username": "admin", "password": 'password',"client_id": 'admin-cli', "grant_type": 'password'}
myResponse = requests.post(url+"/auth/realms/master/protocol/openid-connect/token", data=data,headers={"Content-Type": "application/x-www-form-urlencoded"})
token=myResponse.json()['access_token']
realms=requests.get(url+"/auth/admin/realms",headers={"Content-Type": "application/json", "Authorization":"Bearer " + token})
if(len(json.loads(realms.text)) < 2):
    with open('demo_realm.json', 'r') as json_file:
        print('calling realm creation api: ' + url + '/auth/admin/realms' )
        data = json_file.read()
        myResponse = requests.post((url + "/auth/admin/realms"), data=data,headers={"Content-Type": "application/json", "Authorization":"Bearer " + token})
        if(myResponse.ok):
            print('success')
        else:
            print('fail calling post: ' + myResponse.text)
else:
    print('realm already created')