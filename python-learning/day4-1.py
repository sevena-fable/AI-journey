drugs = [
    {
        "name": "Aspirin",
        "weight": 180.16,
        "logP": 1.2,
        "target": "COX",
        "approved": True
    },
    {
        "name": "Ibuprofen",
        "weight": 206.28,
        "logP": 3.5,
        "target": "COX",
        "approved": True
    },
    {
        "name": "Gefitinib",
        "weight": 446.90,
        "logP": 3.2,
        "target": "EGFR",
        "approved": True
    }
]


# 1. 数据库中药物数量
print("药物数量：", len(drugs))


# 2. 计算平均分子量
total_weight = 0

for drug in drugs:
    total_weight += drug["weight"]

average_weight = total_weight / len(drugs)

print("平均分子量：", average_weight)


# 3. 找到分子量最大的药物
max_weight = 0
max_drug = None

for drug in drugs:

    if drug["weight"] > max_weight:
        max_weight = drug["weight"]
        max_drug = drug

print("分子量最大的药物：", max_drug["name"])
print("分子量：", max_drug["weight"])


# 4. 筛选 logP < 3 的药物
print("logP < 3 的药物：")

for drug in drugs:

    if drug["logP"] < 3:
        print(drug["name"])