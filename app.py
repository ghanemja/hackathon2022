from flask import Flask, render_template, request, make_response
import sys
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/',methods = ['POST', 'GET'] )
def index():
    if request.method == 'GET':
        company_id = request.args.get('companyId')
        if company_id:
            investors_file = "investors.csv"
            peers_file = "peers.csv"
            try:
                with open(investors_file) as invest:
                    with open(peers_file) as peer:
                        return render_template("index.html", investors=invest, peers=peer, company_id=company_id)
            except:
                return render_template("index.html", company_id=company_id)
        else: 
            return render_template("index.html")
    return render_template("index.html")



if __name__ == "__main__":
    app.run()
