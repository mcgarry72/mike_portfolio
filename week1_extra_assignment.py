# test problem

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(len(verse))
print(verse.index("and"))

print(verse[verse.index("and"):verse.rindex("and")])

print(verse[13].isupper())

print(verse.rindex("and"))
print(verse.count("you"))
print(verse.count("mike"))
