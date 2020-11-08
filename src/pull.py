import os
import requests
import json
import csv

key = "zIAPhNbTNS1xT5aEvAO0H4oE4aYrGLr04cjgx8LAqrgEj3iWPI27BG02RO09VgSHAuivIptunkuDZMQ8xjGMTKBXzp68v7e1AIbZBoad42I5dcGbyp9CjFg2czt1g3ak"
base_url = "https://api.liquipedia.net/api/v1/game"

if __name__ == "__main__":
    send = {
        "apikey": key,
        "limit": 10000000,
        "conditions": "[[date::>2020-06-01]]",
        "wiki": "leagueoflegends"}

    response = requests.post(base_url, data=send)    
    parsed = json.loads(response.text)

    # print(json.dumps(parsed, indent=4))

    lines = []

    for x in parsed["result"]:
        #Extract champions from each game
        t1_champions = []
        t2_champions = []

        line = []

        line.append(x["opponent1"])
        line.append(x["opponent2"])
        line.append(x["winner"])

        if "extradata" in x:
            t1_champions.append(x["extradata"]["t1c1"])
            t1_champions.append(x["extradata"]["t1c2"])
            t1_champions.append(x["extradata"]["t1c3"])
            t1_champions.append(x["extradata"]["t1c4"])
            t1_champions.append(x["extradata"]["t1c5"])

            t2_champions.append(x["extradata"]["t2c1"])
            t2_champions.append(x["extradata"]["t2c2"])
            t2_champions.append(x["extradata"]["t2c3"])
            t2_champions.append(x["extradata"]["t2c4"])
            t2_champions.append(x["extradata"]["t2c5"])

        t1_champions_string = "/".join(t1_champions)
        t2_champions_string = "/".join(t2_champions)

        line.append(t1_champions_string)
        line.append(t2_champions_string)

        line.append(x["date"])

        lines.append(line)  

        with open("finalcsv.csv", "w+", encoding="utf-8", newline='') as c: 
            csvwriter = csv.writer(c)
            csvwriter.writerows(lines)