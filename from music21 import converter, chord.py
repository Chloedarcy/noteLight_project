from music21 import converter, chord

# Load your MusicXML file
xml_file = "/Users/dhwang25/Downloads/Beethoven7th_chorus_only.mxl"  # Make sure it's in the same folder as this script
score = converter.parse(xml_file)

# Scan for chords
chords_found = False
for part in score.parts:
    for element in part.flat.notes:
        if isinstance(element, chord.Chord):
            chords_found = True
            print("Chord detected:", [n.nameWithOctave for n in element.notes])

if not chords_found:
    print("No chords found in this MusicXML file.")
