from flask import Flask , request ,jsonify,make_response
import json

app = Flask(__name__)

Animes =[
    {
        "id": 1,
        "titulo": "Gintama: The final",
        "poster": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx114129-RLgSuh6YbeYx.jpg",
        "categoria": ["action","comedy","drama","sci-fi"],
        "rating": 9.1,
        "reviews": 235,
        "season": "Winter 2021",
        "tipo": "movie"
    },
    {
        "id": 2,
        "titulo": "Death Note",
        "poster": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx114129-RLgSuh6YbeYx.jpg",
        "categoria": ["Action","Comedy","Drama","Sci-fi"],
        "rating": 9.0,
        "reviews": 227,
        "season": "spring 2015",
        "tipo": "Serie Tv"
    },
    {
        "id": 3,
        "titulo": "Fruits Basket: The Final",
        "poster": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx124194-pWfBqp3GgjOx.jpg",
        "categoria": ["Comedy","Drama","Psychological","Romance","Slice of Life","Supernatural"],
        "rating": 9.0,
        "reviews": 181,
        "season": "Spring 2021",
        "tipo": "Serie Tv"
    }
]

@app.route('/')
def Inicio():
    return "!Hola mundo! estos son mis primeros pasos realizando una Api"

'''
def cargar_archivo():
    with open('Animes.json','r+') as archivo:
        Animes= json.load(archivo)
        return Animes
'''

@app.route('/anime',methods=['GET'])
def listAnimes():
   
    #Animes = cargar_archivo()
        #m = json.dump(datos,listado,indent=4)

    return jsonify(Animes)


#ANIME por id metodo get
@app.route('/anime/<int:id>',methods=['GET'])
def Anime_Por_Id(id):
    #Animes = cargar_archivo()
    for anime in Animes:
        if anime["id"] == id:
            return jsonify(anime)
    return jsonify({"message": "no se puedo encontrar el anime"},Animes)


@app.route('/anime',methods=['POST'])
def agregarNuevoAnime():
    new_anime = request.json
    for anime in Animes:
        if anime["id"] == new_anime["id"]:
            return jsonify({"mensaje":"El anime ya existe.no se puede agregar"})
    Animes.append(new_anime)
    return jsonify({"mensaje":"El anime se agrego existosamente"},Animes)


#anime por id metodo delete
@app.route('/anime/<int:id>',methods=['DELETE'])
def eliminar_anime(id):
    #Animes = cargar_archivo()
    for anime in Animes:
        if anime["id"] == id:
            Animes.remove(anime)
            return jsonify({"mensaje":"se elemino el anime correctamente"},Animes)
    return make_response(jsonify({"Mensaje":"Anime no encontrado"}),404)

# metodo PUT actualizar anime por id
@app.route('/anime/<int:id>',methods=['PUT']) 
def update_anime(id):
    anime_actualizado =request.get_json()
    for anime in Animes:
        if anime["id"] == id:
            anime.update(anime_actualizado)
            return jsonify({"Mensaje":"Actualización realizada"},Animes)
    return make_response(jsonify({"Mensaje":"Anime no encontrado"}),404)


# metodo patch
@app.route('/anime/<int:id>',methods=['PATCH'])
def update_parcial_anime(id):
        actualización_parcial = request.get_json()
        for anime in Animes:
            if anime["id"] == id:
                 anime.update(actualización_parcial)
                 return jsonify({"Mensaje":"Actualización parcial realizada"},Animes)
        return make_response(jsonify({"Mensaje":"Anime no encontrado"}),404)


#@app.route('/',methods=['PATCH'])

  
if __name__ == '__main__':
    app.run(debug=True)
    #m = imprimir(2)
    #print(m)

