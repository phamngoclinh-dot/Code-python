import sys
import re

data = sys.stdin.read()


replace_dict = {'.': '|', '?': '|', '!': '|'}
for k, v in replace_dict.items():
    data = data.replace(k, v)


sentences = data.split('|')

for s in sentences:
    
    s = s.strip()
    
    s = re.sub(r'[.?!]', '', s)
    
    words = s.split()
    if not words:
        continue
    sentence = " ".join(words).lower()
    
    sentence = sentence[0].upper() + sentence[1:]
    print(sentence)
