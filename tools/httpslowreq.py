import requests
l=input('input url>')
n=1
while True:
    requests.get(l)
    print('request %1.0f sent'%n)
    n+=1
