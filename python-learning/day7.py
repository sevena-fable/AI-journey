def load_drugs():
    drugs = []

    with open ("D:/chen2/AI-Journey/python-learning/day7-2database.csv") as file:

        lines = file.readlines()

        for line in lines[1:]:

            line = line.strip()
            data = line.split(",")

            try:
                weight = float(data[1])
                logP = float(data[2])

            except ValueError:
                print("发现数据错误，跳过",data[0])
                continue

            else:
                drug = {
                    "name":data[0],
                    "weight":float(data[1]),
                    "logP":float(data[2]),
                    "target":data[3]
                }
                drugs.append(drug)

    return drugs 

drugs = load_drugs()

print("成功读取的药物：")

for drug in drugs:

   print(drug["name"])
                

