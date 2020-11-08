import requests
import json

key = "AV9vu9eX2q758qYj4FjNDseIXiuxTbF885BZ41CMcPWO2kPdsrSXHrk3XShJafUgxzCi49i3BDuDet8Z2AQmLESMDBPqMQSJIEe8D3HAM8Tqldjmp45hCyoZFubSs8Qf"
base_url = "https://api.liquipedia.net/api/v1/game"

if __name__ == "__main__":
    send = {
        "apikey": key,
        "limit": 5000,
        "conditions": "[[date::>2020-06-01]]",
        "wiki": "leagueoflegends"}

    response = requests.post(base_url, data=send)    
    parsed = json.loads(response.text)

    with open("byyear.json", "w+") as f:
        f.write("")

    with open("byyear.json", "a+") as f:
        for x in parsed["result"]:
            if "2020" in x["date"]:
                f.write(json.dumps(x, indent=4))

    print(parsed)

    # with open("out.json", "w+") as f:
    #     f.write(json.dumps(parsed, indent=4))

    # print(json.dumps(parsed, indent=4))