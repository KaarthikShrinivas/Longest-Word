def longestWord(text):
    words = []
    s=''
    for i in text:
        if not (i.lower()).isalpha():
            if s!='':
                words.append(s)
                s=''
        else:
            s+=i
    if s!='':
        if s[-1].isalpha():
            words.append(s)
    max_length = 0
    max_word = ''
    for i in words:
        if len(i)>max_length:
            max_length=len(i)
            max_word=i
    return max_word
