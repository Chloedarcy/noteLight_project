from music21 import converter, note, chord

# Load the MusicXML file
xml_file = "/Users/dhwang25/Downloads/Runaway - Kanye West.xml"  # Replace with your file
score = converter.parse(xml_file)

note_data = []  # Store extracted notes

for part in score.parts:  # Loop through instruments/parts
    for element in part.flat.notes:
        if isinstance(element, note.Note):
            note_name = element.nameWithOctave  # Example: "C4"
            duration = element.quarterLength  # In beats
            note_data.append((note_name, duration))
        elif isinstance(element, chord.Chord):
            chord_notes = [n.nameWithOctave for n in element.notes]  # List of note names
            duration = element.quarterLength
            note_data.append((chord_notes, duration))

# Print extracted notes
for entry in note_data:
    print(entry)
