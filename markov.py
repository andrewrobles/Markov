def create_dictionary(filename):
    # Initialize dictionary to create
    # and sentence start character
    dictionary = {}
    sentence_start = '$'
    dictionary = {sentence_start: []}


    # Read contents from file
    file = open(filename, 'r')
    contents = file.read()
    file.close()

    # Seperate sentences into lists
    sentence_list = contents.split('.')


    # Iterate through every sentence
    for sentence in sentence_list:

        # Seperate words into lists
        word_list = contents.split(' ')

        # Handle first word of sentence
        dictionary[sentence_start].append(word_list[0])

        # Iterate through every word after first sentence
        for i in range(len(word_list)-1):
            # Get current word and word that comes after
            current_word = word_list[i]
            next_word = word_list[i + 1]

            # Add word to list if it exists in dictionary
            # otherwise create a new list
            if current_word not in dictionary:
                dictionary[current_word] = []
            
            dictionary[current_word].append(next_word)        
            
    return dictionary