class Roll():

    def __init__(self, name):
        self.name = name

    def read_rolls():
        import csv
        output_list = []
        output_list_dict = []
        with open('battle-table.csv') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                output_list.append(row['Attacker'])
                del row['Attacker']
                output_list_dict.append(dict(row))
            output_dict = {key:value for key, value in zip(output_list, output_list_dict)}
        return output_dict

    def can_defeat(self, p2_roll):
        return Roll.read_rolls()[self.name][p2_roll.name]


class Player():

    def __init__(self, name, score=0):
        self.name = name
        self.score = score


