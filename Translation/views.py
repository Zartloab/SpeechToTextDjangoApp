import os
import re
import json
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
load_dotenv()


@csrf_exempt
@require_http_methods(["GET"])
def root_view(request):    
    # Return healthcheck
    data = {
        'message': 'works fine!!',
    }
    return JsonResponse(data)


@csrf_exempt
@require_http_methods(["POST"])
def translate_message(request):
    try:
        # Parse the JSON body
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    # Extract parameters
    input_language = body.get('input_language')
    output_language = body.get('output_language')
    message = body.get('message')

    # Validation pattern (e.g., must be two-letter language codes followed by a hyphen and two-letter country codes)
    language_pattern = r'^[a-z]{2,}-[A-Za-z]{2,}$'

    # Validate input_language, output_language, and message
    if not input_language or not re.match(language_pattern, input_language):
        return JsonResponse({'error': 'Invalid or missing input_language. Must match the pattern "xx" or "xx-XX"'}, status=400)
    
    if not output_language or not re.match(language_pattern, output_language):
        return JsonResponse({'error': 'Invalid or missing output_language. Must match the pattern "xx" or "xx-XX"'}, status=400)
    
    if not message or not isinstance(message, str):
        return JsonResponse({'error': 'Invalid or missing message text'}, status=400)

    # Print validated languages and message to the console
    print(f"Input Language: {input_language}")
    print(f"Output Language: {output_language}")
    print(f"Message to be translated: {message}")

    # Call Azure Translator API to translate the text
    translation_result = translate_text(message, input_language, output_language)

    if translation_result['status'] == 'error':
        return JsonResponse(translation_result, status=500)
    
    # If everything is valid, return a success response with the translation
    data = {
        'message': 'Translation successful!',
        'input_language': input_language,
        'output_language': output_language,
        'original_text': message,
        'translated_text': translation_result['translated_text']
    }
    return JsonResponse(data)


def translate_text(text, input_language, output_language):
    try:
        # Azure Translator API endpoint
        endpoint = f"https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={input_language}&to={output_language}"
        
        # Add your Azure Translator service credentials
        AZURE_TRANSLATOR_KEY = os.getenv('AZ_TRANSLATOR_SECRET_KEY')
        AZURE_REGION = os.getenv('AZ_TRANSLATOR_REGION')
        
        # Headers for the request
        headers = {
            'Ocp-Apim-Subscription-Key': AZURE_TRANSLATOR_KEY,
            'Ocp-Apim-Subscription-Region': AZURE_REGION,
            'Content-Type': 'application/json'
        }
        
        # Request body
        body = [{
            'Text': text
        }]
        
        # Send the request to the Translator API
        response = requests.post(endpoint, headers=headers, json=body)

        # Check if the request was successful
        if response.status_code != 200:
            return {'status': 'error', 'message': f"Translation failed with status code {response.status_code}"}
        
        # Extract the translated text
        response_json = response.json()
        translated_text = response_json[0]['translations'][0]['text']
        print(f"Translated Text: {translated_text}")
        return {'status': 'success', 'translated_text': translated_text}
    
    except Exception as e:
        print(f"Error during translation: {str(e)}")
        return {'status': 'error', 'message': str(e)}