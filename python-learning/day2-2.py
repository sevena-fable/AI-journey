def analyze_drug(name,weight,targets):
    print("=====药物分析报告=====")
    print(f"药物名称是{name}")
    print(f"分子量是{weight}")

    if weight < 500:
        print("分析结果：小分子候选药物")
    else :
        print("分析结果：大分子或需要进一步分析")

    for target in targets:
        print("-",target)

analyze_drug("阿司匹林",180.16,["COX-1","COX-2","PTGS"])