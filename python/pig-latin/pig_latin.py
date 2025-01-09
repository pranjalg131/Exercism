def starts_with(text, starts):
    
    for start in starts:
        if text.startswith(start): 
            return True
    
    return False

def add_suffix(text):
    return text + 'ay'

def find_first_vowel_idx(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for i in range(len(text)):
        if(text[i] in vowels):
            return i;
    
    return len(text) - 1

def translate_word(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if starts_with(text, vowels) or starts_with(text, ['xr', 'yt']):
        return add_suffix(text)
    else:
        vowel_idx = find_first_vowel_idx(text) 
        
        consonant_part = text[:vowel_idx]
        
        if consonant_part and text[vowel_idx] == 'u' and consonant_part[-1] == 'q':
            word = text[vowel_idx + 1:] + consonant_part[:-1] + 'qu'
            return add_suffix(word)
        
        y_idx = consonant_part.find('y')
        
        if y_idx > 0:
            word = text[y_idx:] + text[:y_idx]
            return add_suffix(word)
        
        word = text[vowel_idx:] + consonant_part
        
        return add_suffix(word)

def translate(text):
    
    words = text.split();
    results = []
    for word in words:
        results.append( translate_word(word) )
    
    return ' '.join(results)
    
