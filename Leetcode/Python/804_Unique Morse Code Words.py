class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':
        import string
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = string.ascii_lowercase
        morse_map = {}
        for i in range(26):
            morse_map[alphabet[i]] = morse[i]
        encoded_set = set()
        for word in words:
            encoded = ''
            for letter in word:
                encoded += morse_map[letter]
            encoded_set.add(encoded)
        return len(encoded_set)
