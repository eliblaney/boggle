import nltk
from nltk.corpus import words
from pprint import pprint

end = '_end_'
def is_valid(trie, word):
    pos = trie
    for letter in word:
        if letter not in pos:
            return False
        pos = pos[letter]
    return end in pos

def is_prefix(trie, word):
    pos = trie
    for letter in word:
        if letter not in pos:
            return False
        pos = pos[letter]
    # If there's more than just '_end_', then it's a word prefix
    return len(pos) > 1

neighbors = [(-1,-1),(-1,0),(0,-1),(1,0),(0,1),(1,1),(1,-1),(-1,1)]
def get_neighbors(row, col):
    result = []
    for row_offset, col_offset in neighbors:
        r = row + row_offset
        c = col + col_offset
        if(0 <= r < ROW_LENGTH and 0 <= c < COL_LENGTH):
            result.append((r, c))
    return result

valid_words = set()
def dfs(board, row, col, trie, visited_path, curr):
    letter = board[row][col]
    visited_path.append((row, col))
    curr += letter.lower()

    if len(curr) >= 3 and is_valid(trie, curr):
        valid_words.add(curr)

    if not is_prefix(trie, curr):
        return

    curr_neighbors = get_neighbors(row, col)
    for n in curr_neighbors:
        if n not in visited_path:
            dfs(board, n[0], n[1], trie, visited_path.copy(), curr)


print("Reading board...")
# Read board
board = []
with open("board.txt") as f:
    lines = f.readlines()
    for line in lines:
        row = []
        last = ""
        for letter in line:
            letter = letter.upper()
            if letter == 'Q':
                row.append('QU')
            elif letter == 'U' and last == 'Q':
                continue
            elif letter == '\n':
                continue
            else:
                row.append(letter)
            last = letter
        board.append(row)

ROW_LENGTH = len(board)
COL_LENGTH = len(board[0])


pprint(board)

print("Reading dictionary...")
# Get English words according to NLTK
word_list = words.words()

# Generate prefix trie
trie = dict()
for word in word_list:
    pos = trie
    last = ""
    for letter in word:
        # I hate the Qu tile
        if letter == 'u' and last == 'q':
            continue
        if letter == 'q':
            letter = 'qu'
        pos = pos.setdefault(letter, {})
        last = letter
    pos[end] = end

print("Searching board...")
# Perform depth first search on the Boggle board
for row in range(ROW_LENGTH):
    for col in range(COL_LENGTH):
        dfs(board, row, col, trie, [], "")

print("Valid words:")
print(valid_words)
