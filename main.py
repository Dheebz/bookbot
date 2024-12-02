

path_to_file = "books/frankenstein.txt"
with open(path_to_file) as f:
    file_content = f.read()



def get_word_count(file_content):
    words = file_content.split()
    return len(words)

def count_characters(file_content):
    lowered_string = file_content.lower()
    #generate a map of unique characters(a-z)
    char_map = {}
    for char in lowered_string:
        if char.isalpha():
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
    return char_map


print(f'--- BEGIN REPORT of {path_to_file} ---')

print(f"{get_word_count(file_content)} words in this book")

char_maps = count_characters(file_content)
print('')

# order charmap by count
sorted_char_map = sorted(char_maps.items(), key=lambda x: x[1], reverse=True)
for char, count in sorted_char_map:
    print(f"{char}: {count}")
print('---- End Report ----')

#End

