# %% imports
import string

# %% custom functions
def count_words(file):

    def get_words_in_txt(file):
        """Open a text file & return a list of strings."""
        try:
            with open(file) as f:
                words = f.read().translate(str.maketrans("", "", string.punctuation)).split()
            return words
        except FileNotFoundError:
            print(f'{file} not found. Check argument.')
    
    words_count = len(get_words_in_txt(file))
    return words_count

# translate explanation:
# string.punctuation contains all common punctuation characters:
# !"#$%&'()*+,-./:;<=>?@[\]^_{|}~
# str.maketrans("", "", string.punctuation) creates a translation table that
# maps all punctuation to None.
# .translate(...) removes all characters from the text that are in
# string.punctuation.

# %% application
number_words = count_words("The_Zen_of_Python.txt")
print(number_words)
# TODO: do not count punctuation

# %%
