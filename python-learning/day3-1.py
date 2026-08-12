with open("D:\chen2\AI-Journey\python-learning\day2-3database.csv") as file:

    lines = file.readlines()

    found = False


    for line in lines[1:]:
        line = line.strip()
        data = line.split(",")

        weight = float(data[1])

        logP = float(data[2])

        if weight < 500 and logP < 5:

            found = True

            print("药物名称：",data[0])
            print("分子量：",float(data[1]))
            print("logP:",data[2])
            print("作用靶点",data[3])

            print("-----------------")

    if found == False:  #if not found:
        print("没有找到符合条件的候选药物")



