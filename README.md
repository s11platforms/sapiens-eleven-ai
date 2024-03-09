# Chatbot Implementation API Design

This design outlines the process for a client or UI to post requests and receive responses from a LargeLanguageModel provider. The workflow is simple and intended for further iteration.

## Workflow Overview

1. **User/Customer Prompts**
   - The starting point where user or customer inputs are gathered.

2. **UI/UX/Client Interaction**
   - Sends POST request to `/generate` endpoint.

3. **Python Server Processing**
   - Intercepts the request for `generate_response()`.
     1. **Instantiate LargeLanguageModelService Object**
        - Based on the payload's `PROVIDER`.
     2. **Call getResponse()**
        - Fetches the response from the Large Language Model service.
     3. **Return Large Language Model Response**
        - The response is prepared to be sent back to the UI/UX/Client.

4. **Response Delivery**
   - The Large Language Model response is returned back to the UI/UX/Client.

## Detailed Process

### Instantiation of LargeLanguageModelService

- Based on the payload's `PROVIDER`.
  1. **Validate Payload**
     - Ensures the payload is correct and all necessary information is included.
  2. **Return LargeLanguageModelService Object**
     - The configured service object is returned for further action.

#### Payload Validation

- Ensures that:
  1. The prompt isn't empty or missing.
  2. Access credentials are not empty or missing.
  3. The access value is valid.
  4. The API key isn't empty or missing.
  5. The API key value is valid.

### LargeLanguageModelService.getResponse()

- Processes the request to get a response.
  1. **Determine Expert**
     - Figures out which expert to prompt based on the context.
  2. **RAG**
     - Performs Retrieval-Augmented Generation, if applicable.
  3. **Execute Chat Completions API Request**
     - Calls the necessary API to get the completion.
  4. **Return Response**
     - Returns the final response from the model.

#### Expert Determination

- Specific steps to determine the expert to prompt, such as calling a specific API.

##### API Execution for Simple Call

- Calls `execute_chat_completions_api_request()` specifically for the Sapiens 11 expert.
  1. **Build Headers Payload**
     - Prepares the headers required for the API request.
  2. **Build JSON Payload**
     - Constructs the JSON payload for the API call.
  3. **Return Executed Response**
     - Returns the response obtained from OpenAI's API after execution.

##### API Execution for Simple Call

###### Building Headers Payload

- Process to build the headers:
  1. Retrieve the API key using `getAPIKey()`.
  2. Return headers payload containing the OpenAI API key.

###### Building JSON Payload

- Steps to construct the JSON payload for the API request:
  1. Call `getContext()` to retrieve the context.
  2. Call `getPrompt()` to fetch the prompt.
  3. Call `getModel()` to specify the model.
  4. Return the complete OpenAI API request payload.

###### RAG