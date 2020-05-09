# Boggle

This program solves Boggle boards for all possible words. Uses the NLTK dictionary.

# Requirements

Python3, nltk

    pip install nltk

# Usage

Edit `board.txt` to contain the letters in the Boggle board, and then execute `boggle.py`

    nano board.txt
	python3 boggle.py

# Strategy

The script makes a prefix tree ("trie") from each of the words in the dictionary, so each letter of a word is represented as a node that contains the next letter of every possible word starting with that letter. The trie is recursive and allows for quick verification of words as the script uses a depth-first search of possible words on the board.
