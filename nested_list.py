# this is a nested list problem

my_list = [["Mike", 80], ["Joe", 75], ["Susan", 90], ["Tim", 65], ["George", 75]]
student_scores = []
my_list.sort()
print(my_list)

for list in my_list:
    student_scores.append(list[1])

student_scores.sort()

for list in my_list:
    if list[1] == student_scores[1]:
        print(f"the name is {list[0]}")
        print(f"the score is {list[1]}")

print(student_scores[1])

