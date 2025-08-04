
def get_dict(lang):
    dictionary = {}
    if lang == 1:    # PL - ENG
        file = 'pl-eng.txt'
    elif lang == 2:  # ENG - SP
        file = 'eng-sp.txt'
    else:
        print("Invalid language choice!")

    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                if '=' in line:
                    word1, word2 = line.strip().split('=', 1)  # line strip: cleans the spaces in line beginning-end, split('=', 1) splits by = 1 time
                    word1, word2 = word1.strip(), word2.strip()  # word strip: same thing at the words
                    dictionary[word1] = word2
                    dictionary[word2] = word1
    except FileNotFoundError:
        print(f"File {file} not found")
    return dictionary, file


def delete(item, dictionary, file):
    if item in dictionary:
        match = dictionary[item]

        dictionary.pop(item)
        dictionary.pop(match, None)

        try:
            with open(file, 'w', encoding='utf-8') as f:
                for key, value in dictionary.items():
                    f.write(f"{key} = {value}\n")
            return f"{item} and {match} deleted from file"
        except Exception as e:
            return f"Error updating file: {e}"

    return f"{item} not found"

def search(item, dictionary):
    for key, value in dictionary.items():
        if item in key or item in value:
            return  f"{item} is in the dictionary: {key} = {value}"
    return "No match found"


def main():
    while True:
        menu = input('Choose an operation\nT: Translation\nD: Delete\nS: Search\nQ: Quit\n').strip().lower()

        if menu == 'q':
            print('Goodbye')
            break

        try:
            lang = int(input('Which language dictionary do you want to use? (1: PL - ENG, 2: ENG - SP)\n'))
        except ValueError:
            print('Invalid input')
            continue

        dictionary, file = get_dict(lang)

        if not dictionary:
            print('No dictionary found')
            continue

        if menu == 't':
            while True:
                word = input('Enter a word to translate - 0 - menu\n').strip().lower()
                if word == '0':
                    break
                result = dictionary.get(word)

                if result:
                    print(f"Translation: {result}")
                else:
                    print("Word not in dictionary")

        elif menu == 'd':
            element_to_del = input(f'Enter a word to delete from chosen dictionary - 0 - menu\n').strip().lower()
            if element_to_del  == '0':
                continue
            print(delete(element_to_del, dictionary, file))

        elif menu == 's':
            element_to_search = input(f'Enter a word to search from chosen dictionary - 0 - menu\n').strip().lower()
            if element_to_search  == '0':
                continue
            print(search(element_to_search, dictionary))

        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()





