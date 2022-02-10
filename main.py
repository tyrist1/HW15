import sqlite3  #, #jsonfy
import json
from flask import Flask

app = Flask(__name__)

@app.route('/animals/<itemid>')
def vasya(itemid):

    con = sqlite3.connect("animal.db")
    cur = con.cursor()
    sqlite_query = f"""select * from animals_fin
                        left join outcomes on outcomes.animal_id=animals_fin.animal_id
                        where animals_fin.id = {itemid}"""


    cur.execute(sqlite_query)
    result=cur.fetchall()
    con.close()

    if len(result)==1:
        line=result[0]
        data = {
            "1": line[0],
            "2": line[1],
            "3": line[2],

        }
    else:
        data ={}
    return json.dumps(data)

app.run()




