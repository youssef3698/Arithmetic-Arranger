def arithmetic_arranger(problems, solve=False):
    available = list()
    arranged = dict()

    # Check if more than 5 problems were entered
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        # Setting out list of problems
        for i in range(len(problems)):
            available.append(problems[i])
    # Solving each problem alone
    for i in range(len(available)):
        prob = str.split(available[i])
        # Checking if numbers contain non-digit characters
        try:
            int(prob[0])
            int(prob[2])
        except:
            return "Error: Numbers must only contain digits."
            # Checking if operators other that + and - are used
        if prob[1] == "+":
            answer = int(prob[0]) + int(prob[2])
        elif prob[1] == "-":
            answer = int(prob[0]) - int(prob[2])
        else:
            return "Error: Operator must be '+' or '-'."
        if solve is False:
            answer = ""
        # Checking if numbers are more than 4 digits long
        if len(prob[0]) > 4 or len(prob[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        # Setting out spacing parameters to align numbers
        s1 = max(len(prob[0]), len(prob[2])) + 2 - len(prob[0])
        s2 = max(len(prob[0]), len(prob[2])) + 2 - len(prob[2]) - 1
        s3 = max(len(prob[0]), len(prob[2])) + 2 - len(str(answer))
        d1 = max(len(prob[0]), len(prob[2])) + 2
        spaces1 = ""
        spaces2 = ""
        spaces3 = ""
        dashes = ""
        if s1 < 0:
            s1 = 0
        if s2 < 0:
            s2 = 0
        for s in range(s1):
            spaces1 += " "
        for s in range(s2):
            spaces2 += " "
        for s in range(s3):
            spaces3 += " "
        for d in range(d1):
            dashes += "-"
        # Setting out dictionary of arranged solutions
        k1 = "a" + str(i)
        k2 = "b" + str(i)
        k3 = "c" + str(i)
        k4 = "d" + str(i)
        arr = {k1: spaces1 + prob[0], k2: prob[1] + spaces2 + prob[2], k3: dashes, k4: spaces3 + str(answer)}
        # Compiling full list of arranged solutions
        arranged.update(arr)
    # Arranging solutions horizontally
    va = str()
    vb = str()
    vc = str()
    vd = str()
    for l in range(len(available)):
        ka = "a" + str(l)
        kb = "b" + str(l)
        kc = "c" + str(l)
        kd = "d" + str(l)
        va += arranged.get(ka) + "    "
        vb += arranged.get(kb) + "    "
        vc += arranged.get(kc) + "    "
        vd += arranged.get(kd) + "    "
    va = va[:-4]
    vb = vb[:-4]
    vc = vc[:-4]
    vd = vd[:-4]

    if solve is True:
        arranged_problems = va + "\n" + vb + "\n" + vc + "\n" + vd
    else:
        arranged_problems = va + "\n" + vb + "\n" + vc

    return arranged_problems

# Test inputs
# Test two problems arrangement 1
p0 = ['3801 - 2', '123 + 49']
# Test two problems arrangement 2
p1 = ['1 + 2', '1 - 9380']
# Test four problems arrangement
p2 = ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']
# Test five problems arrangement
p3 = ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']
# Test too many problems
p4 = ['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']
# Test incorrect operator
p5 = ['3 / 855', '3801 - 2', '45 + 43', '123 + 49']
# Test too many digits
p6 = ['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']
# Test only digits
p7 = ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']
# Test two problems with solutions
p8 = ['3 + 855', '988 + 40']
# Test five problems with solutions
p9 = ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']

print(arithmetic_arranger(p5, True))
