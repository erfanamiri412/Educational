s = 'A bullet that is fired, never returns to gun.'
words = s.split()
for i in range(len(words)):
    if words[i]=='gun':
        words[i]='g*n'
s = ' '.join(words)
print(s)

# answer = A bullet that is fired, never returns to g*n.