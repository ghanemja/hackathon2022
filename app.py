from flask import Flask, render_template, request, make_response
import sys
import csv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/',methods = ['POST', 'GET'] )
def index():
    if request.method == 'GET':
        company_id = request.args.get('company-id')
        selected = request.args.get('selected_cypher')
        if company_id:
            investors_file = "investors.csv"
            peers_file = "peers.csv"
            industry_file = "company_industry.csv"
            try:
                with open(investors_file) as invest:
                    with open(peers_file) as peer:
                        with open(industry_file) as industries:
                            reader = csv.reader(industries)
                            next(reader, None) # skip headers
                            industry_map = dict((rows[0],rows[2]) for rows in reader)
                            return render_template("index.html", investors=invest, peers=peer, company_id=company_id, selected=selected, industries=industry_map)
            except:
                return render_template("index.html", company_id=company_id)
        else:
            return render_template("index.html")
    return render_template("index.html")



if __name__ == "__main__":
    app.run()
