import random

# Major keys in C major
notes = ['C(I)', 'Dm(ii)', 'Em(iii)', 'F(IV)', 'G(V)', 'Am(vi)', 'B(vii)']

# Progressions
progressions = [
    ['C(I)', 'G(V)', 'Am(vi)', 'F(IV)'],  # Progression a
    ['C(I)', 'F(IV)', 'G(V)', 'C(I)'],    # Progression b
    ['C(I)', 'Dm(ii)', 'Em(iii)', 'F(IV)']  # Progression c
]

# Welcome message
print("Welcome to the C Major Song Generator!")

# Get the tempo from the user
tempo = int(input("Please enter the tempo for your song (in BPM): "))

# Randomly select a progression
selected_progression = random.choice(progressions)

# Display the result to the user
print("\nYour song is in C major.")
print(f"Tempo: {tempo} BPM")
print("The chosen progression is: ", ' - '.join(selected_progression))
