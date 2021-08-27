from flask import Flask, json, request, Response

api = Flask(__name__)

@api.route('/api/v1/data', methods=['POST'])
def datapost():
    print('#' * 24 + ' Received Post ' + '#' * 24)
    print(request.json)
    print('#' * 24 + '     End       ' + '#' * 24)
    return Response(status=200)

@api.route('/api/v1/version', methods=['GET'])
def version():
    return json.dumps({"version": "0.1"}), {'content-type': 'application/json'}

@api.route('/api/v1/data/<string:id>', methods=['GET'])
def orders(id):
    try:
        data = json.load(open('./data{}.json'.format(id),))
        return json.dumps(data), {'content-type': 'application/json'}
    except:
        return api.response_class(response=json.dumps({'message': 'data does not exist for Id ' + id}), status=500, mimetype="application/json")

if __name__ == '__main__':
    api.run(port=5001)
