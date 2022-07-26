dict = {1: "AEIOULNSTR", 2: "DG"}
score = 0
word = input("Insert word: ").upper()
for k, v in dict.items():
    for i in word:
        if i in v:
            score += k

print(score)