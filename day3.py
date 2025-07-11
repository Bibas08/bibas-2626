def encode_secret_word(word):
   
    vowels = 'aeiouAEIOU'
    replaced = ''.join(['*' if char in vowels else char for char in word])

 # Step 2: Reverse the string
    reversed_str = replaced[::-1]

    
    encoded = ''
    for char in reversed_str:
        if char.isalpha():
           
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + 2) % 26 + base)
            encoded += shifted
        else:
            encoded += char

   
    return encoded


secret_word = "hello"
print("Encoded word:", encode_secret_word(secret_word))




