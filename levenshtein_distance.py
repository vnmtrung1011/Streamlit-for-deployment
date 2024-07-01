import streamlit as st

def levenshtein_distance(s1, s2):
    # Initialize the matrix
    len_s1, len_s2 = len(s1), len(s2)
    matrix = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    # Initialize the first row and column
    for i in range(len_s1 + 1):
        matrix[i][0] = i
    for j in range(len_s2 + 1):
        matrix[0][j] = j

    # Fill the matrix
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,       # Deletion
                               matrix[i][j - 1] + 1,       # Insertion
                               matrix[i - 1][j - 1] + cost) # Substitution

    # The Levenshtein distance is the value in the bottom right corner of the matrix
    return matrix[len_s1][len_s2]

def load(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set(line.strip().lower() for line in lines))
    return words

vocabs = load('./data/vocab.txt')

def main():
    st.title('Word Correction using Levenshtein Distance')
    word = st.text_input('Word input')
    
    if st.button('Compute'):
        leven_distances = dict ()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)
        sorted_distences = dict(sorted( leven_distances.items() , key = lambda item : item[1]) )


        correct_word =   list(sorted_distences.keys())[0]  
        st.write('Correct word : ', correct_word )
        
        col1, col2 = st.columns(2)
        col1.write('Vocabulary')
        col1.write(vocabs)

        col2.write('Distances :')
        col2.write(sorted_distences)


if __name__ == "__main__":
    main ()
           
  




