from music21 import stream, chord, duration, key

# Define a list of chords
chords = ["Cmaj", "Dmin", "Emin", "Fmaj", "Gmaj", "Amin", "Bdim"]

# Create a Stream to store the chords
chord_stream = stream.Stream()

# Define a key for the chord progression (e.g., C major)
key_signature = key.Key("C")

# Generate a chord progression
for chord_name in chords:
    chord_obj = chord.Chord(chord_name)
    chord_obj.duration = duration.Duration(4.0)  # Set the duration for each chord (4 beats)
    chord_obj.transpose(key_signature.tonic)  # Transpose to the key
    chord_stream.append(chord_obj)

# Print the chord progression
chord_stream.show()