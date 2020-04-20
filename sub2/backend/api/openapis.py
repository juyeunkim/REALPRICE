from .properties import ClientID, ClientSecret
import requests
import json

headers = {
        'Content-Type': 'application/json; charset=utf-8', 
        "mimetype" : "applications/json",
        "X-NCP-APIGW-API-KEY-ID":ClientID,
        "X-NCP-APIGW-API-KEY":ClientSecret
        }

def geoCoding(area):
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    query = "?query="+str(area)
    response = requests.get(url+query,headers=headers)
    return response
'''    
"latitude": "37.503652",
"longitude": "127.038125"
'''
def reverseGeoCoding(longitude, latitude):
    url = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
    coords = "?coords="+longitude+","+latitude
    orders ="&orders=legalcode,admcode,addr,roadaddr"
    output = "&output=json"
    response = requests.get(url+coords+orders+output,headers=headers)
    return response