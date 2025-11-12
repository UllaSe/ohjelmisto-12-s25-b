from flask import Flask, request, Response, jsonify, render_template
import json
import alkulukulaskuri
app = Flask(__name__)

@app.route('/')
def moikka():
    return 'Terve maailma!'

# http://127.0.0.1:3000/alkuluku/31
@app.route('/alkuluku/<alkuluku>')
def alkuluku(alkuluku):
    try:
        luku = int(alkuluku)
        # laske tässä alkuluku TAI kutsu funktiota toisesta tiedostosta
        alkuluku = alkulukulaskuri.laske(luku)

        tilakoodi = 200

        vastaus = {
            "Number": luku,
            "isPrime": alkuluku
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen luku alkulukua ei voida laskea"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

# http://127.0.0.1:3000/summa?luku1=13&luku2=28
# tämä on route eli reitti
@app.route('/laske')
def laske():
    print(request.args)
    args = request.args
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa = luku1 + luku2

    # itse tehty JSON vastaus
    vastaus = {
        "luku1": luku1,
        "luku2": luku2,
        "summa": summa
    }

    return vastaus

# # http://127.0.0.1:3000/kaiku/huhuuuuuu
@app.route('/kaiku/<teksti>/<kertaa>')
def kaiku(teksti, kertaa):
    print(teksti, kertaa)
    tulos = ""
    for i in range(int(kertaa)):
        tulos += teksti + ' '

    vastaus = {
        "kaiku": tulos
    }
    return vastaus

@app.route('/summa/<luku1>/<luku2>')
def summa(luku1, luku2):
    try:
        luku1 = float(luku1)
        luku2 = float(luku2)
        summa = luku1 + luku2

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "luku1": luku1,
            "luku2": luku2,
            "summa": summa
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    # json_vastaus = json.dumps(vastaus)
    # return Response(response=json_vastaus, status=tilakoodi, mimetype="application/json")
    return jsonify(vastaus), tilakoodi

@app.errorhandler(404)
def page_not_found(virhe):
    #print(f"Virhe: {virhe}") # debug-tulostus konsoliin
    vastaus = {
        "status": virhe.code,
        "teksti": virhe.description
    }
    # versio 1
    # jsonvast = json.dumps(vastaus)
    # return Response(response=jsonvast, status=404, mimetype="application/json")

    # versio 2
    # return jsonify(vastaus), virhe.code

    # huvin vuoksi versio 3
    return render_template('404.html'), 404


# käynnistää serverin, joten alimmaisena ja KERRAN!
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)