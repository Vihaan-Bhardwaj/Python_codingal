s1  = input("Enter a word: ")
s2 = input("Enter another word: ")

print("They are anagrams" if sorted(s1) == sorted(s2) else "They are not anagrams")