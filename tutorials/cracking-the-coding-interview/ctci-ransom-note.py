def ransom_note(magazine, ransom):
    magazine.sort()
    ransom.sort()
    for w in ransom:
        if w in magazine:
            magazine.remove(w)
        else:
            return False
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    
