# filename: stats.py

def get_num_words(text_string):
    return len( text_string.split() )


def get_char_count(text_string):
    text_chars = list(text_string)
    seen_chars = set()
    unique_chars = list()
    counter_dict = dict()

    for char in text_chars:
        char = char.lower()
        if (char not in seen_chars):
            seen_chars.add(char)
            unique_chars.append(char)
            counter_dict[char] = 1
        elif (char in seen_chars):
            counter_dict[char] = counter_dict.get(char) + 1

    return counter_dict

# Print a Report
def sort_dict(char_count):

    # A function that takes a dictionary and returns the value of the "num" key
    # This is how the `.sort()` method knows how to sort the list of dictionaries
    def sort_on(items):
        k = list(items.keys())[0]
        return items[k]

    buff = []
    
    for k,v in char_count.items():
        d = dict({k : v})
        buff.append(d)

    buff.sort(reverse=True, key=sort_on)
    #return buff

    for item in buff[::]:
        for k,v in item.items():
            print(f"{k}: {v}")
#dict({'t': counter_dict.get('t')})
