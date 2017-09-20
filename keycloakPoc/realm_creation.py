import requests, json, time, os

url = "http://keycloakpoc_keycloakserver:" + os.getenv("KEYCLOAK_PORT")
result = None
print('Waiting on Keycloak to be up')
while result is None:
    try:
        time.sleep(5)
        result = requests.get(url)
    except:
        print('Keycloak is not running, attempting again in 5s')
        pass

print('Keycloak is live')

data= {"username": "admin", "password": 'password',"client_id": 'admin-cli', "grant_type": 'password'}
myResponse = requests.post(url+"/auth/realms/master/protocol/openid-connect/token", data=data,headers={"Content-Type": "application/x-www-form-urlencoded"})
token=myResponse.json()['access_token']
realms=requests.get(url+"/auth/admin/realms",headers={"Content-Type": "application/json", "Authorization":"Bearer " + token})
if(len(json.loads(realms.text)) < 2):
    with open('/home/demo_realm.json', 'r') as json_file:
        print('calling realm creation api: ' + url + '/auth/admin/realms' )
        data = json_file.read()
        myResponse = requests.post((url + "/auth/admin/realms"), data=data,headers={"Content-Type": "application/json", "Authorization":"Bearer " + token})
        if(myResponse.ok):
            # myResponse = requests.post((url + "/auth/admin/realms/demo/users"), data={'{username:"testuser"}'},headers={"Content-Type": "application/json", "Authorization":"Bearer " + token})
            print('success')
        else:
            print('fail calling post: ' + myResponse.text)
else:
    print('realm already created')