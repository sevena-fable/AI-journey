from drug import load_drugs
from analysis import search_by_target



drugs = load_drugs()

target = input("请输入靶点：")

results = search_by_target(drugs, target)

print(results)

