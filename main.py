def wordcounter():
    print("Copy text here. End with '!--!'")
    lines = []
    line = ''
    while line != '!--!':
        line = input()
        if line != '!--!':
            lines.append(line)

    lines.remove('')
    text = '\n'.join(lines)
    words = text.split()
    return len(words)

print(wordcounter())