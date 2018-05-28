#! /usr/bin/python3
#retrieved from:
#https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
from collections import defaultdict

class Trie:
	"""
	Implement a trie with insert, search, and startsWith methods.
	"""
	def __init__(self):
		self.root = defaultdict()

	# @param {string} word
	# @return {void}
	# Inserts a word into the trie.
	def insert(self, word):
		current = self.root
		for letter in word:
			current = current.setdefault(letter, {})
		current.setdefault("_end")

	# @param {string} word
	# @return {boolean}
	# Returns if the word is in the trie.
	def search(self, word):
		current = self.root
		for letter in word:
			if letter not in current:
				return False
			current = current[letter]
		if "_end" in current:
			return True
		return False

	# @param {string} prefix
	# @return {boolean}
	# Returns if there is any word in the trie
	# that starts with the given prefix.
	def startsWith(self, prefix):
		current = self.root
		for letter in prefix:
			if letter not in current:
				return False
			current = current[letter]
		return True


# Now test the class
"""
test = Trie()
test.insert('helloworld')
test.insert('ilikeapple')
test.insert('helloz')

print(test.search('hell'))
print(test.startsWith('hello'))
print(test.search('ilikeapple'))
"""