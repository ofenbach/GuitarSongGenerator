import sys
import random

chords = ['D', 'Dm', 'E','Em','A','Am','F','G']	# TODO add every basic chord

def play_chord(id):
	""" Doesn't work (yet)! """
 	system.play(chords[id])

def generate_chords(amount):
	""" Generates basic chords.
	    param: amount of chords (int) """
	final_chords = []

	for i in range(amount):	# TODO fix double chords AND not sounding good combinations (e.g. D, Dm):
		final_chords.append(chords[random.randint(0,amount)])

	return final_chords

def main():

	# setup
	arg_list = sys.argv[1:]
	intro_chord_list = []
	bridge_chord_list = []

	# generate chords
	intro_chord_list = generate_chords(4)	#TODO fix: if (arg_list[0] == "chords"):
	bridge_chord_list = generate_chords(2)

	# display chords
	print "Intro Chords: " + str(intro_chord_list) + "\n"
	print "Bridge Chords " +  str(bridge_chord_list) + "\n"

main()
