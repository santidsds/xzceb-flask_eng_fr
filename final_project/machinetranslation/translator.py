"""Module for translating text between English and French using IBM Watson Language Translator"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    """Translate English text to French"""
    response = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    french_text = response['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Translate French text to English"""
    response = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    english_text = response['translations'][0]['translation']
    return english_text
