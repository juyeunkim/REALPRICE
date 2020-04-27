import json
import pandas as pd
import os
import shutil

DATA_DIR = "../data"
DATA_FILE = os.path.join(DATA_DIR, "testdata.json")

store_columns = (
    "id",
    "srcUrl",
    "address",
    "latitude",
    "longitude",
    "storeName",
    "menu",
    "price",
    "distanceCost",
    "score"
)
def data_to_csv(data_path=DATA_FILE):
    try:
        with open(data_path, encoding="utf-8") as f:
                data = json.loads(f.read())
    except FileNotFoundError as e:
        print(f"`{data_path}` 가 존재하지 않습니다.")
        exit(1)
    stores = []
    for d in data["stores"]:
        stores.append(
            [
                int(d["id"]),
                d["srcUrl"],
                d["address"],
                round(float(d["latitude"]),6),
                round(float(d["longitude"]),6),
                d["storeName"],
                d["menu"],
                int(d["price"]),
                int(d["distanceCost"]),
                round(float(d["score"]),2),
            ]
        )
    storeDF = pd.DataFrame(data=stores, columns=store_columns)
    storeDF.to_csv('./store_test.csv',encoding='utf-8')

if __name__ == "__main__":
    data_to_csv()
    print("Done")