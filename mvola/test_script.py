from authentification import get_access_token
import configparser

# test get_access funciton from authentification
# it will be useful for making a requests to mvole andpoint
config = configparser.ConfigParser()
config.read('../config.ini')
consumer_key = config["KEYS"]["consumer_key"]
consumer_secret = config["KEYS"]["consumer_secret"]

access_token = get_access_token(consumer_key,consumer_secret)
print("access token : {}".format(access_token))