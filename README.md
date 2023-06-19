# mta
mta subway update using gtfs

files:

gtfs-realtime.proto is the general proto file for mass transit

nyct-subway.proto is the specific NYC MTA extensions

mta.proto is the concatenation of the two; nyct-subway.proto appended to gtfs-realtime.proto 
(with the first two lines deleted as instructed somewhere, I think they were the INCLUDE statements that would allow you to compile 
straight from nyct-subway.proto)

mta_pb2.py is the result of running mta.proto through an online protoc compiler.  I have a suspicion that later errors might come from here

mta.py is my python code. Note that the URL for L train data and my auth code are hard coded for now. all i want  is to be able to request data and convert it into text. I can easily then parse out what I want later. 
So far, I can retrieve a hunk of binary as a requests.get() object  (r = requests.get(url, headers = {"x-api-key": authkey})
r.content is 37k bytes of binary data

r.text I think is the same, but now a string object.

The messages I want are   "TripUpdates"
so messages = mta_pb2.TripUpdate()

then messages.ParseFromString(r.content) *should* give me the parsed text.
But instead, it fails with an error message that utf-8 cant decode 0xca in position 32

my theories are:
1) online compiler gave me corrupted pb2.py file. Fix would be to compile myself, yech.
2) I'm doing something wrong with the ParseFronString. no idea how to fix




