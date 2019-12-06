from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask


languages = [{'id': 1 ,'blood_group' : 'O+ve','number_of_blood_availaible(525ml)' : '10'}, {'id' : 2 , 'blood_group' : 'O-ve','number_of_blood_availaible(525ml)' : '8'},{'id' : 3 , 'blood_group' : ' A+ve','number_of_blood_availaible(525ml)' : '11'},{'id' : 4 , 'blood_group' : ' B+ve','number_of_blood_availaible(525ml)' : '12'},{'id' : 5 , 'blood_group': ' AB+ve','number_of_blood_availaible(525ml)' : '13'}]


@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})


@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages})


@app.route('/lang/<string:id>', methods=['GET'])
def returnOne(id):
	langs = [language for language in languages if language['id'] == int(id)]
	return jsonify({'language' : langs[0]})


@app.route('/lang', methods=['POST'])
def addOne():
	print(request.json)
	language = {'id': request.json['id'], 'blood_group' : request.json['blood_group'],'number_of_blood_availaible(525ml)' : request.json['number_of_blood_availaible(525ml)']}

	languages.append(language)
	return jsonify({'msg': 'Blood Group has been added.!'})


@app.route('/lang/<string:id>', methods=['PUT'])
def editOne(id):
	langs = [language for language in languages if language['id'] == int(id)]
	langs[0]['blood_group'] = request.json['blood_group']
	langs[0]['number_of_blood_availaible(525ml)'] = request.json['number_of_blood_availaible(525ml)']
	return jsonify({'language' : langs[0]})


@app.route('/lang/<string:id>', methods=['DELETE'])
def removeOne(id):
	lang = [language for language in languages if language['id'] == int(id)]
	languages.remove(lang[0])
	return jsonify({'languages' : languages})

if __name__ == '__main__':
	app.run(debug=True, port=8777) #run app on port 8777 in debug mode
