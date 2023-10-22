# testing sentence searching targeting specific words.. 

def get_sentence_with_word(sentences, target_word):
    matching_sentences = [sentence for sentence in sentences if target_word in sentence]
    return matching_sentences

# Define a list of sentences
sentences = [
    "link to dwag",
    "what is the link to dwag",
    "where can i find dwag",
    "help me find dwag",
    "tell me dwag",
    "tell me the link to dwag",
    "tell me the link for dwag",
    "tell me where to find dwag",
    "return the link to dwag."
]

# Get user input for the target word
target_word = input("Enter the word you want to search for: ")

# Find sentences containing the target word
matching_sentences = get_sentence_with_word(sentences, target_word)

# Print the matching URL once
if matching_sentences:
    print(f"The following sentences contain the word '{target_word}':")
    print("bcam.broadcast.bskyb.com/dwag")
else:
    print(f"sorry please refine your search '{target_word}'.")




