import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-country", default=None)
parser.add_argument("-year", type=int, default=None)
parser.add_argument("-medals", default=None)
parser.add_argument("-total", type=int, default=None)
parser.add_argument("-overall", default=None)
parser.add_argument("-interactive", default=None)

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
                    medal = line_split[14]
                    line = file.readline()
                    if args.country == country or args.country == NOC:
                        if int(args.year) == int(year):
                            if medal != "NA\n":
                                if counter <= 10:
                                    print(f"{counter}.{name} - {sport} - {medal}")
                                    counter += 1
                                    print(medal)
                                else:
                                    break

                                if str(medal) == "Bronze":
                                    bronze += 1
                                    print("ff")
                                elif medal == "Silver":
                                    silver += 1
                                elif medal == "Gold":
                                    gold += 1
                                if counter == 10:
                                    print("Gold="+ str(gold) +" Silver="+ str(silver) +" Bronze="+ str(bronze))


                            else:
                                continue
                        else:
                            continue
                    else:
                        continue