import mta_pb2
import requests
url = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l'
auth = 'fTrUKUpBJ35KpNIAuemqe8RjhSZdazDT6qpGUqrP'

r = requests.get(url, headers = {"x-api-key": auth})
messages = mta_pb2.TripUpdate()
messages.ParseFromString(r.content)
