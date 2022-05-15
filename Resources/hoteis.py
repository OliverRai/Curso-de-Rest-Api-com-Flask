from flask_restful import Resource, reqparse

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas' : 5,
        'diaria': 500,
        'cidade': 'Angatuba'
    },
    {
        'hotel_id': 'alpha2',
        'nome': 'Alpha Hotel',
        'estrelas' : 5,
        'diaria': 500,
        'cidade': 'Angatuba'
    },
    {
        'hotel_id': 'alpha3',
        'nome': 'Alpha Hotel',
        'estrelas' : 5,
        'diaria': 500,
        'cidade': 'Itape'
    },
    {
        'hotel_id': 'alpha4',
        'nome': 'Alpha Hotel',
        'estrelas' : 5,
        'diaria': 500,
        'cidade': 'Sorocaba'
    },
    {
        'hotel_id': 'alpha5',
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

class Hotel(Resource):
    argumetos = reqparse.RequestParser()
    argumetos.add_argument('nome')
    argumetos.add_argument('estrelas')    
    argumetos.add_argument('diaria')
    argumetos.add_argument('cidade')

    def busca_hotel(self, hotel_id):
        if hotel_id:
            for hotel in hoteis:
                if hotel['hotel_id'] == hotel_id:
                    return hotel
            return None

    def get(self, hotel_id):
        hotel = Hotel.busca_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message':'Hotel not found'}, 404

    def post(self, hotel_id):
        try:        
            dados = Hotel.argumetos.parse_args()
            novo_hotel = {
                'hotel_id': hotel_id,
                'nome': dados['nome'],
                'estrelas': dados['estrelas'],
                'cidade': dados['cidade']
            }
            hoteis.append(novo_hotel)
            return novo_hotel, 200
        except:
            return {'message':'Erro ao adicionar novo hotel'}, 500

    def put(self, hotel_id):
        dados = Hotel.argumetos.parse_args()
        novo_hotel = {'hotel_id':hotel_id, **dados}
        hotel = self.busca_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200 #ok
        hoteis.append(novo_hotel)
        return novo_hotel, 201 #created

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_if'] != hotel_id]
        return {'message':'Hotel delete'}