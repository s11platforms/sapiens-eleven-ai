from flask import Flask, request
from S11LargeLanguageModelServices.S11LargeLanguageModelService import S11LargeLanguageModelService


app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_response():
    """

    :return:
    """
    if request.method == 'POST':
        payload = request.json

        try:
            model_service = S11LargeLanguageModelService(payload)
            return model_service.get_response()

        except Exception as e:
            # TODO: improve error handling
            return "Sorry, we were unable to get an answer", 500

if __name__ == '__main__':
    app.run(debug=True)
