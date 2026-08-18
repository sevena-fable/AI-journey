def load_drugs():

    drugs = []

    with open("python-learning/day6-project/data/drug_database.csv") as file:

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