def main():
    # Starting part of the sentence
    SENTENCE_START = 'Code in place is fun. I learned to program and used python to make '

    # Prompt the user for an adjective, noun, and verb
    adjective = input('Please type an adjective and press enter: ')
    noun = input('Please type a noun and press enter: ')
    verb = input('Please type a verb and press enter: ')

    # Create the full sentence
    sentence = f'{SENTENCE_START} {adjective} {noun} {verb}'

    # Print the final sentence
    print(sentence)

# Ensure the script runs only when executed directly
if __name__ == '__main__':
    main()
