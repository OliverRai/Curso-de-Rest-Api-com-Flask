from flask_restful import Resource

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas' : 5,
        'diaria': 500,
        'cidade': 'Angatuba'
    },
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas' : 5,
        'diaria': 500,
        'cidade': 'Angatuba'
    },
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas' : 5,
        'diaria': 500,
        'cidade': 'Itape'
    },
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas' : 5,
        'diaria': 500,
        'cidade': 'Sorocaba'
    },
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas' : 5,
        'diaria': 500,
        'cidade': 'Sorocaba'
    },
]

# essa classe vai ser um recurso da nossa api
class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}