import numpy as np
str_formula = "y = ax + b"
data_name = "data.txt"


def get_data(f_name):
    resource = open(f_name, "r")
    data = []
    x = 0

    while x<100:
        data.append(resource.readlines(999))
        if data[x] == []:
            break
        x+=1

    data.remove([])
    data = data[0]

    for i in range(len(data)):
        data[i] = data[i].split("   ")
        temp = []
        for j in data[i]:
            j.replace('\n', '')
            temp.append(float(j))
        data[i] = temp

    return data

def fcost(a, b, data):
    length = len(data)
    temp = 0
    
    for trial in data:
        x = trial[0]
        y = trial[1]
        temp = temp + (a * x + b - y)*(a * x + b - y)

    cost = (0.5/length)*temp
    # print(f"cost = {cost}")
    return cost

def d_fcost_a(a, b, data):
    length = len(data)
    temp = 0
    
    for trial in data:
        x = trial[0]
        y = trial[1]
        temp = temp + ((a * x + b - y)*x)

    d_cost_a = (1/length)*temp
    # print(f"d_cost_a = {d_cost_a}")
    return d_cost_a

def d_fcost_b(a, b, data):
    length = len(data)
    temp = 0
    
    for trial in data:
        x = trial[0]
        y = trial[1]
        temp = temp + (a * x + b - y)

    d_cost_b = (1/length)*temp
    # print(f"d_cost_b = {d_cost_b}")
    return d_cost_b

def GD(data_name, str_formula):
    support_3D = np.zeros([1, 3])
    zero3 = np.zeros([1, 3]) # 这两个是后面3D绘图用的

    data = get_data(data_name)
    
    formula = list(str_formula)
    for x in formula:
        if x == ' ':
            formula.remove(' ')
    if "".join(formula) != "y=ax+b":
        print("\nOnly linear relationships avaliable,\nplease try: y = ax + b")

    a = 0.0
    b = 0.0

    while True:
        cost = fcost(a, b, data)
        
        if support_3D.all() == zero3.all():
            support_3D = np.array([[round(a, 5), round(b, 5), round(cost, 5)]])
            # print(support_3D)
        elif round(cost, 5) == 0:
            data_3D = support_3D
        else:
            temp = np.array([[round(a, 5), round(b, 5), round(cost, 5)]])
            support_3D = np.concatenate((support_3D, temp))
            # print(support_3D)

        temp_a = a - 0.1*d_fcost_a(a, b, data)
        temp_b = b - 0.1*d_fcost_b(a, b, data)
        a = temp_a
        b = temp_b
        if cost == fcost(a, b, data):
            break
        
    ab = [a, b]
    return ab, data_3D


if __name__ == '__main__':
    str_formula = input("Please input the formula. (Press inter to use 'y = ax + b')")
    if str_formula == '':
        str_formula = "y = ax + b"
        print(str_formula)
    data_name = input("Please input the name of your data. Your data should be in txt. (Press inter to use 'data.txt')")
    if data_name == '':
        data_name = "data.txt"
    ab, support_3D = GD(data_name, str_formula)

    pformula = "y = " + str(round(ab[0], 5)) +"x + " + str(round(ab[1], 5))
    print(pformula)
    # print(ab)
    # print(support_3D)
    # print(np.prod(support_3D.shape))