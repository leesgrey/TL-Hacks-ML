"""
This file calculates various statistics for the website.
"""

FILEPATH = "finalcsv.csv"


def calculate(results):
    abnormal = {
        "Jc": "Jayce",
        "Lil": "Lillia",
        "Syl": "Sylas",
        "Leo": "Leona",
        "Thr": "Thresh",
        "Aph": "Aphelios",
        "Yuu": "Yuumi",
        "Dra": "Draven",
        "Ska": "Skarner",
        "Skar": "Skarner",
        "Ill": "Illaoi",
        "Qiy": "Qiyana",
        "Nee": "Neeko",
        "Kind": "Kindred",
        "Kai": "Kai'sa",
        "Ive": "Ivern",
        "Cam": "Camille",
        "Bardo": "Bard",
        "Zig": "Ziggs",
        "Tali": "Taliyah",
        "Sam": "Samira",
        "Yas": "Yasuo",
        "Kha": "Kha'Zix",
        "Luc": "Lucian",
        "Tk": "Tahm Kench",
        "Syn": "Snydra",
        "K6": "Kha'Zix",
        "Khazix": "Kha'Zix",
        "Liss": "Lissandra",
        "Kaisa": "Kai'Sa",
        "Velkoz": "Vel'Koz",
        "Vel": "Vel'Koz",
        "Rek": "Rek'Sai",
        "Kali": "Kalista",
        "Xay": "Xayah",
        "Naut": "Nautilus",
        "Quin": "Quinn"}

    roles = ["top", "jungle", "mid", "bot", "support"]

    new_abnormal = {}
    for k,v in abnormal.items():
        new_abnormal[k] = v
        new_abnormal[k.lower()] = v
    abnormal = new_abnormal

    # for k,v in abnormal.items():
    #     print(k,v)

    with open(FILEPATH, "r+", encoding="utf-8") as f:
        lines = f.readlines()

        teams = {}

        team_win_rates = {}
        champion_overall_winrates = {}
        champion_role_winrates = {}

        for i, line in enumerate(lines):
            split = line.split(",")

            if len(split[2]) == 0 or len(split[3].split("/")) == 0 or len(split[4].split("/")) == 0 or len(split) != 6 or not split[2].isnumeric():  
                continue
            
            #Parse champions
            champions_split_1 = split[3].split("/")
            champions_split_2 = split[4].split("/")
            
            #Parse teams
            if split[0] not in teams:
                teams[split[0]] = len(teams)
            if split[1] not in teams:
                teams[split[1]] = len(teams)


            if split[2] == "1":
                #Update team winrates
                if split[0] not in team_win_rates:
                    team_win_rates[split[0]] = (1,1)
                else:
                    curr = team_win_rates[split[0]]
                    team_win_rates[split[0]] = (curr[0] + 1, curr[1] + 1)

                if split[1] not in team_win_rates:
                    team_win_rates[split[1]] = (0,1)
                else:
                    curr = team_win_rates[split[1]]
                    team_win_rates[split[1]] = (curr[0], curr[1] + 1)

                #Calculate champion win rates
                for i,c in enumerate(champions_split_1):
                    if len(c) == 0:
                        break

                    if c.lower() in abnormal:
                        c = abnormal[c]

                    if c.lower() not in champion_overall_winrates:
                        champion_overall_winrates[c.lower()] = (1,1)
                    else:
                        curr = champion_overall_winrates[c.lower()]
                        champion_overall_winrates[c.lower()] = (curr[0] + 1, curr[1] + 1)

                    #Calculate per role winrates
                    if c.lower() not in champion_role_winrates:
                        champion_role_winrates[c.lower()] = {k: (0,1) for k in roles}
                        curr = champion_role_winrates[c.lower()][roles[i]] 
                        champion_role_winrates[c.lower()][roles[i]] = (curr[0] + 1, curr[1] + 1)
                    else:
                        curr = champion_role_winrates[c.lower()][roles[i]] 
                        champion_role_winrates[c.lower()][roles[i]] = (curr[0] + 1, curr[1] + 1)

                for i,c in enumerate(champions_split_2):
                    if len(c) == 0:
                        break
                    
                    if c.lower() in abnormal:
                        c = abnormal[c]

                    if c.lower() not in champion_overall_winrates:
                        champion_overall_winrates[c.lower()] = (0,1)
                    else:
                        curr = champion_overall_winrates[c.lower()]
                        champion_overall_winrates[c.lower()] = (curr[0], curr[1] + 1)

                    #Calculate per role winrates
                    if c.lower() not in champion_role_winrates:
                        champion_role_winrates[c.lower()] = {k: (0,1) for k in roles}
                        curr = champion_role_winrates[c.lower()][roles[i]] 
                        champion_role_winrates[c.lower()][roles[i]] = (curr[0], curr[1] + 1)
                    else:
                        curr = champion_role_winrates[c.lower()][roles[i]] 
                        champion_role_winrates[c.lower()][roles[i]] = (curr[0], curr[1] + 1)


            elif split[2] == "2":

                if split[0] not in team_win_rates:
                    team_win_rates[split[0]] = (0,1)
                else:
                    curr = team_win_rates[split[0]]
                    team_win_rates[split[0]] = (curr[0], curr[1] + 1)

                if split[1] not in team_win_rates:
                    team_win_rates[split[1]] = (1,1)
                else:
                    curr = team_win_rates[split[1]]
                    team_win_rates[split[1]] = (curr[0] + 1, curr[1] + 1)

                #Calculate champion win rates
                for i,c in enumerate(champions_split_1):
                    if len(c) == 0:
                        break

                    if c.lower() in abnormal:
                        c = abnormal[c]

                    if c.lower() not in champion_overall_winrates:
                        champion_overall_winrates[c.lower()] = (0,1)
                    else:
                        curr = champion_overall_winrates[c.lower()]
                        champion_overall_winrates[c.lower()] = (curr[0], curr[1] + 1)

                    #Calculate per role winrates
                    if c.lower() not in champion_role_winrates:
                        champion_role_winrates[c.lower()] = {k: (0,1) for k in roles}
                        curr = champion_role_winrates[c.lower()][roles[i]] 
                        champion_role_winrates[c.lower()][roles[i]] = (curr[0], curr[1] + 1)
                    else:
                        curr = champion_role_winrates[c.lower()][roles[i]] 
                        champion_role_winrates[c.lower()][roles[i]] = (curr[0], curr[1] + 1)
                    

                for i,c in enumerate(champions_split_2):
                    if len(c) == 0:
                        break

                    if c.lower() in abnormal:
                        c = abnormal[c]

                    if c.lower() not in champion_overall_winrates:
                        champion_overall_winrates[c.lower()] = (1,1)
                    else:
                        curr = champion_overall_winrates[c.lower()]
                        champion_overall_winrates[c.lower()] = (curr[0] + 1, curr[1] + 1)

                    #Calculate per role winrates
                    if c.lower() not in champion_role_winrates:
                        champion_role_winrates[c.lower()] = {k: (0,1) for k in roles}
                        curr = champion_role_winrates[c.lower()][roles[i]] 
                        champion_role_winrates[c.lower()][roles[i]] = (curr[0] + 1, curr[1] + 1)
                    else:
                        curr = champion_role_winrates[c.lower()][roles[i]] 
                        champion_role_winrates[c.lower()][roles[i]] = (curr[0] + 1, curr[1] + 1)

        sorted_team_winrates = {k: (float(v[0]/v[1])) for k,v in team_win_rates.items()}
        sorted_team_winrates = {k: v for k, v in sorted(sorted_team_winrates.items(), key=lambda item: item[1])}

        sorted_champion_winrates = {k: (float(v[0]/v[1])) for k,v in champion_overall_winrates.items()}
        sorted_champion_winrates = {k: v for k,v in sorted(sorted_champion_winrates.items(), key=lambda item: item[1])}

        with open("champion_winrate_csv.csv", "a+", encoding="utf-8") as f:
            for k,v in sorted_champion_winrates.items():
                f.write (k + "," + str(v) + "," + str(champion_overall_winrates[k][0]) +"," + str(champion_overall_winrates[k][1]) + "\n")

        with open("champion_winrate_role_csv.csv", "a+", encoding="utf-8") as f:
            for k,v in champion_role_winrates.items():
                for role, games in champion_role_winrates[k].items():
                    f.write(k + "," + role + "," + str(float(games[0])/games[1]) + "," + str(games[0]) + "," + str(games[1]) + "\n")

        # for k,v in champion_role_winrates.items():
        #     print(k,v)