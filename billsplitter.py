import random

n = int(input("Enter number of friends joining (including you): \n"))

if n == 0 or n < 0:
    print("No one is joining for the party")
    exit()


print("Enter the name of every friends (including you), each on a new line: ")
count = 1
people_dict = {}
lucky_people = []
while count <= n:
    name = input()
    names = people_dict.update({name: 0})
    count += 1

print("Enter the total bill value: ")
total_bill = int(input())
result = round(total_bill / n, 2)
for i in people_dict.keys():
    people_dict.update({i: result})
    lucky_people.append(i)


lucky_game = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
if lucky_game in ['yes', 'Yes', 'YEs', 'YES', 'yES']:
    name_lucky = random.choice(lucky_people)
    n = n - 1
    print(name_lucky, "is the lucky one!")
    if name_lucky in people_dict.keys():
        people_dict.update({name_lucky: 0})
        for i in people_dict.keys():
            result = round(total_bill / n, 2)
            if name_lucky == i:
                continue
            else:
                people_dict.update({i: result})
    print(people_dict)
elif lucky_game in ['no', 'No', 'NO', 'nO']:
    print("No one is going to be lucky")
    print(people_dict)
