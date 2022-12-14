import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--country", required=False)
parser.add_argument("--year", type=int, required=False)
parser.add_argument("--medals", required=False)
parser.add_argument("--total", type=int, required=False)
parser.add_argument("--overall", required=False)
parser.add_argument("--interactive", required=False)

args = parser.parse_args()

print(args)
all_years = []
all_countries = []
counter = 1
with open("athletics.tsv", 'r') as file:
    file.readline()
    line = file.readline()
    if args.country != None:
        if args.year != None:
            if args.medals != None:
                bronze = 0
                silver = 0
                gold = 0
                while line != "":
                    line_split = line.split("\t")
                    name = line_split[1]
                    country = line_split[6]
                    NOC = line_split[7]
                    year = line_split[9]
                    sport = line_split[12]
                    medal = (line_split[14])
                    line = file.readline()
                    if args.country == country or args.country == NOC:
                        if int(args.year) == int(year):
                            if medal != "NA\n":
                                if counter <= 10:
                                    print(f"{counter}.{name} - {sport} - {medal}")
                                    counter += 1
                                    if medal == "Bronze\n":
                                        bronze += 1
                                    if medal == "Silver\n":
                                        silver += 1
                                    if medal == "Gold\n":
                                        gold += 1
                                    if counter == 11:
                                        if bronze + silver + gold < 10:
                                            print("This country doesn't have more than 10 medals")
                                            break
                                        else:
                                            print("Gold - " + str(gold) + "Silver - " + str(silver) + " Bronze - " + str(bronze))
                                            break
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
