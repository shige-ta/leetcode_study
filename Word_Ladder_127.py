from collections import deque

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    
    wordList = set(wordList)
    queue = deque([(beginWord, 1)])  # (current_word, current_length)
    
    while queue:
        current_word, current_length = queue.popleft()
        
        if current_word == endWord:
            return current_length
        
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append((next_word, current_length + 1))
    
    return 0

# 例1
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladderLength(beginWord, endWord, wordList))  # 出力: 5

# 例2
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
print(ladderLength(beginWord, endWord, wordList))  # 出力: 0
