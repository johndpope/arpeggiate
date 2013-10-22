import midi
import sys

try:
    midifilename = sys.argv[1]
    delta = int(sys.argv[2])
except:
    raise Exception("Usage: python arpeggiate.py <midi file path> <number of ticks separation>.")

midifile = midi.read_midifile(midifilename)

events = [sorted(track,key=lambda x: x.msdelay) for track in midifile]


for track in events:
    i = 0
    prev = -1
    while i<len(track):
        if track[i].type == 'NoteOnEvent':
            if prev > -1 and track[i].tick-track[prev].tick < delta:
                track[i].tick=track[prev].tick+delta
            prev = i
        i+=1
           




X=midi.EventStream()
X.resolution=480

for track in range(len(midifile)):
    X.add_track()
    for e in events[track]:
        X.add_event(e)



midi.write_midifile(X,midifilename[:-3]+'-arpeggiated.mid')



