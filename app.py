from flask import Flask, render_template, request, make_response
import sys
import csv
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app)

@app.route('/',methods = ['POST', 'GET'] )
def index():
    if request.method == 'GET':
        company_name = request.args.get('company-id')
        if company_name:
            company_name = ''.join(company_name.split()).lower()
        selected = request.args.get('selected_cypher')
        if company_name:
            investors_file = "investors.csv"
            peers_file = "peers.csv"
            industry_file = "company_industry.csv"
            score_file = "prediction_percentile.csv"
            try:
                with open(investors_file) as invest:
                    with open(peers_file) as peer:
                        reader = csv.reader(peer)
                        next(reader, None) # skip headers
                        name_id_map = dict((''.join(rows[1].split()).lower(), rows[0]) for rows in reader)
                        peer.seek(0) # back to top of file
                        id_name_map = dict((rows[0], rows[1]) for rows in reader)
                        peer.seek(0)
                        with open(industry_file) as industries:
                            reader = csv.reader(industries)
                            next(reader, None) # skip headers
                            industry_map = dict((rows[0],rows[2]) for rows in reader)
                            with open(score_file) as scores:
                                reader = csv.reader(scores)
                                next(reader, None) # skip headers
                                score_map = dict((rows[0],round(float(rows[2]),3)) for rows in reader)
                                company_id = name_id_map[company_name]
                                _company_name = id_name_map[company_id]
                                
                                return render_template("index.html", investors=invest, peers=peer, company_id=company_id, company_name=_company_name, selected=selected, industries=industry_map, score=score_map)
            except Exception as e:
                traceback.print_exc()
                return render_template("index.html")
        else:
            return render_template("index.html")
    return render_template("index.html")



if __name__ == "__main__":
    app.run()
