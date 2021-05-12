# This file is used calculate your sgpa for 3rd sem to 8th sem of vtu 2018 scheme students of any branch.

def sgpa_cal(sem, lt):
    tot = sum([i * (int(input("Enter the marks of each subject "))//10 + 1) for i in lt])
    return tot/sum(lt)


def cgpa_cal(lt, till):
    numerator = sum([ float(input("Enter the each sgpa till {} sem ".format(till))) * sum(lt[i]) for i in range(till-2)])
    denominator = sum([j for i in lt[:till-2] for j in i])
    return numerator/denominator


lt = [[3, 4, 3, 3, 3, 3, 2, 2, 1], [3, 4, 3, 3, 3, 3, 2, 2, 1], [3, 4, 4, 3, 3, 3, 2, 2, 1], [4, 4, 4, 3, 3, 3, 2, 2], [3, 3, 3, 3, 3, 2, 2], [3, 3]]
choice = str(input("Enter what you want to calculate, cgpa or sgpa? "))

if choice.lower() == 'sgpa':
    sem = int(input("Which sem you want to calculate "))
    result = sgpa_cal(sem, lt[sem-3])
    print("Your sgpa of {} sem is ".format(sem), round(result, 2))

elif choice.lower() == 'cgpa':
    till = int(input("Till which sem you want to calculate your cgpa (Note: we can calculate only from 3rd sem to 8th sem) "))
    result = cgpa_cal(lt, till)
    print("Your cgpa till {} sem is".format(till), round(result, 2))

else:
    print("Enter proper input ie cgpa or sgpa")



