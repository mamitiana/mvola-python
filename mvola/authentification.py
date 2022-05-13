from email import header
import requests 
import base64

url = "https://devapi.mvola.mg/token"

def get_access_token( consumer_key="", consumer_secret="") -> str :
    param = {'grant_type':'client_credentials'}
    
    # TO DO : solve base64 encoding

    # key = "{}:{}".format(consumer_key,consumer_secret)
    # key = key.encode("ascii")
    # b64_key = base64.b64encode(key)
    # headers = {'Authorization' : "Basic {}".format(b64_key)}

    headers = {'Authorization': 'Basic aWdXZndxUGM1OGdHeWYyZWY3MGdKd0hjbnd3YTpFcExaWWdMZ1VSV3FPb0Y3VnowcXFmX1Q4Tllh'}
    response = requests.post(url, data = param , headers= headers)
    access_token = response.text
    return access_token

consumer_key = "igWfwqPc58gGyf2ef70gJwHcnwwa"
consumer_secret = "EpLZYgLgURWqOoF7Vz0qqf_T8NYa"

access_token = get_access_token(consumer_key,consumer_secret)
print("access token : {}".format(access_token))
