"""Generate markov text from text files."""


from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    f = open(file_path)

    text = f.read()

    f.close()

    return text


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - 2):     # changes from -1 to -2

        first, second, third = words[i], words[i+1], words[i+2]     # add third = words[i+2]
        key = (first, second, third)                    # add third to tuple

        if key not in chains:
            chains[key] = []

        try:
            fourth = words[i+3]     # changes from i+2 to i+3
            chains[key].append(fourth)  # changes from third to fourth
        except:
            chains[key].append(None)

    print chains

    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    # WORKING ON CAPITALIZATION

    # upper_chains = {}

    # for key, value in chains.items():
    #     if key[0][0].isupper():
    #         upper_chains[key] = value

    # print upper_chains

    current_key = tuple(choice(chains.keys()))
    words.extend(current_key)

    while True:
        new_link = choice(chains[current_key])
        words.append(new_link)
        current_key = tuple(words[-3:])     # changes from -2 to -3
        if None in chains[current_key]:
            break

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
