def search_by_target(drugs, target):

    results = []

    for drug in drugs:

        if target in drug["target"]:

            results.append(drug)

    return results



