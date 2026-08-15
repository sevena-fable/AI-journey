with open("D:\chen2\AI-Journey\python-learning\day2-3database.csv") as file:
    lines = file.readlines()

    candidates = []

    for line in lines[1:]:
        line = line.strip()

        data = line.split(",")

        drug = {
            "name":data[0],
            "weight":float(data[1]),
            "logP":float(data[2]),
            "target":data[3]
            }

        if drug["weight"] < 500 and drug["logP"] < 5 :
            candidates.append(drug)

    print("-----候选药物-----")

    for drug in candidates:
        print("药物名称",drug["name"])
        print("分子量",drug["weight"])
        print("logP",drug["logP"])
        print("药物靶点",drug["target"])

    print("-----数据统计-----")

    print("候选药物数量：",len(candidates))

    total_weight = 0

    for drug in candidates:
        total_weight += drug["weight"]

    average_weight = total_weight / len(candidates)

    print("平均分子量；",average_weight)