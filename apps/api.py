# -*- coding: utf-8 -*-

from flask_restful import Api, Resource

# Criamos a classe que estende de Resource
class Index(Resource):

    # Definimos a operação GET
    def get(self):

        # Retornamos um json pelo Flask
        return {'hello': 'world by apps'}


# Instânciamos a API do FlaskRestful
api = Api()


def configure_api(app):
    api.add_resource(Index, '/')

    api.init_app(app)

