# 读取药物数据库

def load_drugs():

    drugs = []

    with open("D:\\chen2\\AI-Journey\\python-learning\\day2-3database.csv") as file:

        lines = file.readlines()

        for line in lines[1:]:

            line = line.strip()

            data = line.split(",")

            drug = {
                "name": data[0],
                "weight": float(data[1]),
                "logP": float(data[2]),
                "target": data[3]
            }

            drugs.append(drug)

    return drugs



# 按靶点搜索

def search_by_target(drugs, target):

    results = []

    for drug in drugs:

        if target in drug["target"]:

            results.append(drug)

    return results



# 按分子量筛选

def filter_by_weight(drugs, max_weight):

    results = []

    for drug in drugs:

        if drug["weight"] < max_weight:

            results.append(drug)

    return results



# 输出结果

def show_results(results):

    print("-----搜索结果-----")

    for drug in results:

        print("药物名称：", drug["name"])
        print("分子量：", drug["weight"])
        print("logP：", drug["logP"])
        print("作用靶点：", drug["target"])

        print("----------------")



# 主程序

drugs = load_drugs()


print("请选择功能：")
print("1. 按靶点搜索")
print("2. 按分子量筛选")


choice = input("请输入选项：")


if choice == "1":

    target = input("请输入查询靶点：")

    results = search_by_target(drugs, target)


elif choice == "2":

    max_weight = float(input("请输入最大分子量："))

    results = filter_by_weight(drugs, max_weight)



show_results(results)