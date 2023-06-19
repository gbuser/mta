# mta
mta subway update using gtfs

files:

gtfs-realtime.proto is the general proto file for mass transit

nyct-subway.proto adds the specific NYC MTA extensions

mta.proto is the concatenation of the two; nyct-subway.proto appended to gtfs-realtime.proto 
(with the first two lines deleted as instructed somewhere, I think they were the INCLUDE statements that would allow you to compile 
straight from nyct-subway.proto


