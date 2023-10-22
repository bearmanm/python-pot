
def get_sentence_with_word(sentences, target_word):
    matching_sentences = [sentence for sentence in sentences if target_word in sentence]
    return matching_sentences

# Define a list of sentences
sentences = [
    "link to dwag: bcam.broadcast.bskyb.com/dwag.",
    "what is the link to dwag: bcam.broadcast.bskyb.com/dwag.",
    "help me find dwag: bcam.broadcast.bskyb.com/dwag.",
    "tell me the link to dwag",
    "tell me the link for dwag",
    "tell me where to find dwag: bcam.broadcast.bskyb.com/dwag.",
    "return the link to dwag."
]

# Get user input for the target word
target_word = input("Enter the word you want to search for: ")

# Find sentences containing the target word
matching_sentences = get_sentence_with_word(sentences, target_word)

# Print the matching sentences
if matching_sentences:
    print(f"The following sentences contain the word '{target_word}':")
    for sentence in matching_sentences:
        print("bcam.broadcast.bskyb.com/dwag")
        #print(sentence)
else:
    print(f"No sentences contain the word '{target_word}'.")

