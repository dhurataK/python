import re

def get_matched_word(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    for word in words:
        match = re.search(regex,word)
        if match:
            print 'Found:', match.group(),' in word:', word

# prints all words that contain double v
# get_matched_word(r'v')

# # prints all words that contain double s
# get_matched_word(r'ss')

# prints all words that end with e
# get_matched_word(r'e$')

# All words that contain an b, any character, then another b
# get_matched_word(r'b\w+b')

# All words that contain an b, at least one character, then another b
# get_matched_word(r'b\w?b')

# All words that contain an b, any number of characters (including zero), then another b
# get_matched_word(r'b\w*b')

# All words that include all five vowels in order
# get_matched_word(r'^[^aeiou]*a[^aeiou]*e[^aeiou]*i[^aeiou]*o[^aeiou]*u[^aeiou]*$')

# All words that only use the letters in 'regular expression' (each letter can appear any number of times)
# get_matched_word(r'\w[a-zA-Z]')

# All words that contain a double letter
get_matched_word(r'(.)\1')
