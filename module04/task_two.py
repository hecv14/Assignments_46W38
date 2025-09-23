# %% custom functions
def count_words(file):

    def get_words_in_txt(file):
        """Open a text file & return a list of strings."""
        try:
            with open(file) as text_read:
                words = text_read.read().split()
            return words
        except FileNotFoundError:
            print(f'{file} not found. Check argument.')

    words_count = len(get_words_in_txt(file))
    return words_count


# %% application
number_words = count_words("The_Zen_of_Python.txt")
print(number_words)
# TODO: do not count punctuation
