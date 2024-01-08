#import nyct_subway_pb2
import gtfs_realtime_pb2
import requests
import datetime

url = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l'
auth = #see mta_unredated_auth.py in local repo
currentTime = int((datetime.datetime.now()).timestamp()) #current time in integer of epochal format
r = requests.get(url, headers = {"x-api-key": auth})
feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(r.content)
trains = []

for entity in feed.entity:
  if ('S' in entity.trip_update.trip.trip_id): #Manhattan bound train IDs end in "S"
    trains.append(entity)

for train in trains:
  for stopTime in train.trip_update.stop_time_update:
    if (stopTime.stop_id == "L11S"): #Graham st station is known as "L11S" to MTA
      print ("Train", train.trip_update.trip.trip_id,
             "arrives at stop", 
             stopTime.stop_id, "(Graham Street) in ",
             stopTime.arrival.time - currentTime, "seconds")
  
  
