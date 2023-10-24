from music21 import stream, chord, duration, key, roman

# Define the available keys
keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Define chord progressions for each key (you can customize these)
progressions = {
    "C": ["I", "IV", "V", "I"],
    "D": ["I", "IV", "V", "I"],
    "E": ["I", "IV", "V", "I"],
    # Add progressions for other keys here
}

# Function to create chord progression
def generate_chord_progression(key_name, progression):
    chord_stream = stream.Stream()
    key_signature = key.Key(key_name)

    for chord_symbol in progression:
        if chord_symbol.startswith("V7/") and len(chord_symbol) > 3:
            secondary_dominant = True
            tonicized_chord = chord_symbol.split("/")[1]
        else:
            secondary_dominant = False
            tonicized_chord = None

        if secondary_dominant:
            roman_numeral = roman.RomanNumeral(tonicized_chord, key_signature)
        else:
            roman_numeral = roman.RomanNumeral(chord_symbol, key_signature)

        chord_obj = chord.Chord(roman_numeral.pitches)  # Use pitches instead of chord_obj
        duration_obj = duration.Duration(4.0)  # Create a duration object
        chord_stream.append(chord_obj)
        chord_stream[-1].duration = duration_obj  # Set the duration for the last added chord

        if secondary_dominant:
            tonicized_key = key.Key(tonicized_chord)
            trans_interval = tonicized_key.tonic.transpose(-key_signature.tonic)
            chord_stream[-1].chordTranspose(trans_interval)  # Transpose the last chord in the stream

    return chord_stream

# Generate and print chord progressions for all keys
for key_name, progression in progressions.items():
    print(f"Chord Progression in {key_name} Major:")
    chord_progression = generate_chord_progression(key_name, progression)
    # Use show('text') to avoid launching an external application
    chord_progression.show('text')
    print("\n")
