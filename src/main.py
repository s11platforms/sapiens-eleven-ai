from flask import Flask, request, jsonify
from src.LargeLanguageModelServices.OpenAI.OpenAIChatCompletionsService import OpenAIService
from src.LargeLanguageModelServices.LargeLanguageModelService import PROMPT

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_response():
    """

    :return:
    """
    if request.method == 'POST':
        payload = request.json

        #TODO: payload validations
        if not payload.get(PROMPT):
            return jsonify({"error": "No prompt provided"}), 400

        try:
            model_service = OpenAIService()
            return model_service.getSimpleResponse(payload)

        except:

            return "Sorry, we were unable to get an answer", 500

if __name__ == '__main__':
    app.run(debug=True)
