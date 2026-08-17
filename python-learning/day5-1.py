def load_drugs():
    drugs = []
    with open ("D:\chen2\AI-Journey\python-learning\day2-3database.csv")as files:
        lines = files.readlines()

        for line in lines[1:]:

            line = line.strip()
            data = line.split(",")

            drug = {
                "name":data[0],
                "weight":float(data[1]),
                "logP":float(data[2]),
                "target":data[3]
            }

            drugs.append(drug)

    return drugs

def search_drugs(drugs,target):
    results = []

    for drug in drugs:

        if target in drug["target"]:
            results.append(drug)

    return results

def show_results(results):

    print("-----搜索结果------")

    for drug in results:
        print("药物名称是",drug["name"])
        print("分子量是",drug["weight"])
        print("logP:",drug["logP"])
        print("药物靶点是",drug["target"])

        print("------------------")

drugs = load_drugs()

target = input("请输入你想查询的靶点：")

results = search_drugs(drugs,target)

show_results(results)




