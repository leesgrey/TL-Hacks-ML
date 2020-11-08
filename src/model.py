from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.model_selection import cross_val_score

import numpy as np

FILEPATH = "finalcsv.csv"
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
    "Ill": "Illaoi",
    "Qiy": "Qiyana",
    "Nee": "Neeko",
    "Kind": "Kindred",
    "Kai": "Kai'sa",
    "Ive": "Ivern",
    "Cam": "Camille",
    "Bardo": "Bard",
    "Zig": "Ziggs",
    "Quin": "Quinn"}

def prepare_data():
    

    with open(FILEPATH, "r+", encoding="utf-8") as f:
        lines = f.readlines()

        X = np.empty((len(lines), 12))
        y = np.empty((len(lines), ))

        teams = {}
        champions = {}

        for i, line in enumerate(lines):
            split = line.split(",")

            if len(split[2]) == 0 or len(split[3].split("/")) == 0 or len(split[4].split("/")) == 0: 
                continue

            #Parse teams
            if split[0] not in teams:
                teams[split[0]] = len(teams)
            if split[1] not in teams:
                teams[split[1]] = len(teams)
            
            #Parse champions
            champions_split_1 = split[3].split("/")
            champions_split_2 = split[4].split("/")

            sample = [teams[split[0]], teams[split[1]]]

            for c in champions_split_1:
                if len(c) > 0:
                    if c not in champions:
                        if c in abnormal:
                            c = abnormal[c]

                        champions[c] = len(champions)
                    sample.append(champions[c])

            for c in champions_split_2:
                if len(c) > 0:
                    if c not in champions and len(c) > 0:
                        if c in abnormal:
                            c = abnormal[c]

                        champions[c] = len(champions)
                    sample.append(champions[c])

            if len(sample) < 12:
                continue

            X[i] = np.asarray([np.float(x) for x in sample], dtype=np.float)
            # y[i] = int(split[2])
            y[i] = np.asarray(split[2], dtype=np.int)


    return X, y

if __name__ == "__main__":
    # X, y = make_classification(n_samples=10000, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)
    X, y = prepare_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=1000, max_depth=50, random_state=0, n_jobs=16, verbose=2)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    print(score)