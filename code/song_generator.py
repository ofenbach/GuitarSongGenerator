import sys
import random

# Chords
d_chords = ['D', 'Dm']
e_chord = ['E', 'Em']
a_chords = ['A', 'Am']
f_chords = ['F', 'Fm']
g_chords = ['G', 'Gm']
chords = [d_chords, e_chord, a_chords, f_chords, g_chords]

def generate_chords(amount):
	""" Generates basic chords.
	    param: amount of chords (int) """
	final_chords = []

	for i in range(amount):	# TODO fix double chords
		final_chords.append(chords[random.randint(0,4)][random.randint(0,1)])

	return final_chords

def main():

  # setup
  arg_list = sys.argv[1:]
  intro_chord_list = []
  bridge_chord_list = []
  refrain_chord_list = []

  # generate chords TODO: if (arg_list[0] == "-chords"):
  intro_chord_list = generate_chords(4)
  bridge_chord_list = generate_chords(2)
  refrain_chord_list = generate_chords(4)

  # display chords
  print("Intro Chords: " + str(intro_chord_list))
  print("Bridge Chords: " + str(bridge_chord_list))
  print("Refrain Chords: " + str(refrain_chord_list))

main()
