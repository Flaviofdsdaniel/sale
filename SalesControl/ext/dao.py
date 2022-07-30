import json

from flask import Response, request

from SalesControl.ext.config import db

class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50))
    monthyPrice = db.Column(db.String(50))
    setupPrice = db.Column(db.String(50))
    currency = db.Column(db.String(50))

    def to_json(self):
        return {"id": self.id, "value": self.value, "monthyPrice": self.monthyPrice, "setupPrice": self.setupPrice,
                "currency": self.currency}


def init_app(app):

    @app.route("/sales/<int:page_num>&&<int:per_num>", methods=["GET"])
    def sale(page_num, per_num):
        select = Sales.query.paginate(per_page=per_num, page=page_num, error_out=True)
        select.page
        sales_json = [selects.to_json()for selects in select.items]

        return response(200, "Vendas", sales_json)

    @app.route("/sale/<id>", methods=["GET"])
    def select_sale(id):
        select = Sales.query.filter_by(id=id).first()
        sale_json = select.to_json()

        return response(200, "Vendas", sale_json)

    @app.route("/sale", methods=["POST"])
    def create():
        body = request.get_json()

        try:
            sale = Sales(value=body["value"], monthyPrice=body["monthyPrice"], setupPrice=body["setupPrice"], currency=body["currency"])
            db.session.add(sale)
            db.session.commit()
            return response(201, "sale", sale.to_json(), "Venda cadastrada com sucesso")
        except Exception as e:
            print('Error', e)
            return response(400, "sale", {}, "Erro ao cadastrar venda")

    @app.route("/sale/<id>", methods=["PUT"])
    def update(id):
        select = Sales.query.filter_by(id=id).first()
        body = request.get_json()

        try:
            if('value' in body):
                select.value = body['value']
            if('monthyPrice' in body):
                select.monthyPrice = body['monthyPrice']
            if('setupPrice' in body):
                select.setuPrice = body['setupPrice']
            if('currency' in body):
                select.currency = body['currency']

            db.session.add(select)
            db.session.commit()
            return response(200, "sale", select.to_json(), "Venda atualizada com sucesso")
        except Exception as e:
            print('Error', e)
            return response(400, "sale", {}, "Erro ao atualizar venda")  

    @app.route("/sale/<id>", methods=["DELETE"])
    def delete(id):
        select = Sales.query.filter_by(id=id).first()

        try:
            db.session.delete(select)
            db.session.commit()
            return response(200, "sale", select.to_json(), "Venda apagar com sucesso")
        except Exception as e:
            print('Error', e)
            return response(400, "sale", {}, "Erro ao apagar venda")

    def response(status, name_content, content, message=False):
        body = {}
        body[name_content] = content

        if(message):
            body["message"] = message

        return Response(json.dumps(body), status=status, mimetype="application/json")
