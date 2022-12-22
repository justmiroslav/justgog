import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--country", required=False)
parser.add_argument("--year", type=int, required=False)
parser.add_argument("--medals", required=False)
parser.add_argument("--total", required=False)#"-T",
parser.add_argument("--total", required=False)
parser.add_argument("--overall", required=False)
parser.add_argument("--interactive", required=False)

args = parser.parse_args()


def first():
    with open("athletics.tsv", 'r') as file:
        file.readline()
        line = file.readline()
        counter = 1
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
                                    print("Gold - " + str(gold) + " Silver - " + str(silver) + " Bronze - " + str(bronze))
                                    break
                    else:
                        continue
                else:
                    continue
            else:
                continue


if args.country != None:
    if args.year != None:
        if args.medals != None:
            first()

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
        n = 0
        while True:
            if max(count) != count[n]:
                n += 1
            else:
                print(type, data[n], count[n])
                break
        return


with open("athletics.tsv", 'r') as file:
    if args.overall != None:
        type = args.overall.split(" ")
        n = 0
        while n < len(type):
            (gog(type[n]))
            n += 1


def interactive():
    years = {}
    Gold = 0
    Silver = 0
    Bronze = 0
    with open("athletics.tsv", 'r') as file:
        file.readline()
        line = file.readline()
        while line:
            line_split = line.split("\t")
            country = line_split[6]
            NOC = line_split[7]
            year = line_split[9]
            city = line_split[11]
            medal = line_split[14]
            if inter_country == country or inter_country == NOC:
                if year not in years:
                    years.update({f"{year}": {'Place': city, "Total": 0, "Gold": 0, "Silver": 0, "Bronze": 0}})
                if year in years:
                    if medal != "NA\n":
                        years[year]["Total"] += 1
                    if medal == "Gold\n":
                        years[year]["Gold"] += 1
                    if medal == "Silver\n":
                        years[year]["Silver"] += 1
                    if medal == "Bronze\n":
                        years[year]["Bronze"] += 1
            line = file.readline()
        first_years = []
        for year in years:
            first_years.append(year)
        first_years.sort()
        for year in years:
            Gold += years[year]["Gold"]
            Silver += years[year]["Silver"]
            Bronze += years[year]["Bronze"]
        Average_gold = round(Gold/len(first_years))
        Average_silver = round(Silver/len(first_years))
        Average_bronze = round(Bronze/len(first_years))
        total_medals = {}
        for year in years:
            total_medals.update({f"{year}": years[year]["Total"]})
        max_total = max(total_medals.values())
        min_total = min(total_medals.values())
        for year in total_medals:
            if total_medals[year] == max_total:
                lucky_year = year
            if total_medals[year] == min_total:
                unlucky_year = year
        print(f"The country is - {inter_country}.\n"
              f"It's first olympics were in {first_years[0]} in {years[first_years[0]]['Place']}\n"
              f"The most successful olympics were in {lucky_year}, {inter_country} got there {max_total} medals\n"
              f"The least successful olympics were in {unlucky_year}, {inter_country} got there {min_total} medals\n"
              f"Average amount of medals per year: {Average_gold} golden medals, {Average_silver} silver medals, {Average_bronze} bronze medals")


with open("athletics.tsv", 'r') as file:
    file.readline()
    total()



if args.interactive == "t":
    inter_country = input("Enter the country: ")
    interactive()
