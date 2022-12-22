import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--country", required=False)
parser.add_argument("--year", type=int, required=False)
parser.add_argument("--medals", required=False)
parser.add_argument("-T", "--total", required=False)
parser.add_argument("--overall", required=False)
parser.add_argument("--interactive", required=False)

args = parser.parse_args()


def gag(current_year, country1):
    counter = 0
    with open("athletics.tsv", 'r') as file:
        file.readline()
        line = file.readline()
        while line != "":
            line_split = line.split("\t")
            country = line_split[6]
            year = line_split[9]
            medal = (line_split[14])
            line = file.readline()
            if country1 == country:
                if current_year == year:
                    if medal != "NA\n":
                        counter += 1
                    else:
                        continue
                else:
                    continue
            else:
                continue
        return counter


def gog(type):
    data = []
    count = []
    with open("athletics.tsv", 'r') as file:
        file.readline()
        line = file.readline()
        while line != "":
            line_split = line.split("\t")
            country = line_split[6]
            year = line_split[9]
            medal = (line_split[14])
            line = file.readline()
            if type == country:
                if medal != "NA\n":
                    current_year = year
                    data.append(year)
                    count.append(gag(current_year, country))
                else:
                    continue
            else:
                continue
        print(len(data))
        n = 0
        while True:
            if max(count) != count[n]:
                n += 1
            else:
                print(type, data[n], count[n])
                break
        return


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


    if args.overall != None:
        type = args.overall.split(" ")
        n = 0
        while n < len(type):
            (gog(type[n]))
            n += 1

def total():
    olymp_year = args.total
    dict = {}
    while True:
        line = file.readline()
        split_line = line.split("\t")
        if not line:
            break
        country = split_line[6]
        medal = split_line[14]
        year = split_line[9]
        if olymp_year == year:
            if medal != "NA" and medal != "NA\n":
                if country not in dict:
                    dict.update({country: [0, 0, 0]})
                if medal == "Gold\n":
                    dict[country][0] += 1
                if medal == "Silver\n":
                    dict[country][1] += 1
                if medal == "Bronze\n":
                    dict[country][2] += 1
    for country in dict:
        print(f"{country} - {dict[country][0]} gold medals, {dict[country][1]} silver medals, {dict[country][2]} bronze medals")


with open("athletics.tsv", 'r') as file:
    file.readline()
    total()

