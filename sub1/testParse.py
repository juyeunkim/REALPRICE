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

import mysql.connector as mariadb
def insertToDB():
    col_list = [
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
    ]				
    rdata = pd.read_csv('./store_testdata.csv',engine='python',encoding='utf-8',header=None,names=col_list)
    mariadbConnection = mariadb.connect(user='root', password='ssafy', database='realpricedb', host="13.125.68.33")
    cursor = mariadbConnection.cursor()

    for i in range(0,len(rdata)):
        sql =  "UPDATE api_store SET src_url = '"+str(rdata['srcUrl'][i])+"' WHERE id = "+ str(rdata['id'][i])
        cursor.execute(sql)
        cursor.execute("SELECT * FROM api_store WHERE id ="+str(rdata['id'][i]))
        print(cursor.fetchone())

    mariadbConnection.commit()

if __name__ == "__main__":
    # data_to_csv()
    # insertToDB()
    print("Done")