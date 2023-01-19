"""
Module to create an instance of the Watson Language translator.
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

# set up the static variables we need for the service
APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION = '2023-01-18'
AUTHENTICATOR = IAMAuthenticator(APIKEY)

# Create an instance of the language translator
watson_translator = LanguageTranslatorV3(version=VERSION,authenticator=AUTHENTICATOR)
watson_translator.set_service_url(URL)

def english_to_french(english_text = ''):
    """
    method uses IBM watson language translator to translate
    a single string of English words into French. If a list
    of strings is passed in, it will return only the first
    element of that list
    """
    # make sure we have a valid string to translate
    if len(english_text) == 0:
        return "The supplied string is empty"

    translation = watson_translator.translate( text = english_text,
        model_id = 'en-fr' ).get_result()

    # Unpack the translated string from the result
    # Could be a loop if we wanted to fully parse
    # lists of strings
    french_text = translation["translations"][0]["translation"]

    return french_text

def french_to_english(french_text = ''):
    """
    method uses IBM watson language translator to translate
    a single string of French words into English. If a list
    of strings is passed in, it will return only the first
    element of that list
    """
    # make sure we have a valid string to translate
    if len(french_text) == 0:
        return "The supplied string is empty"

    translation = watson_translator.translate( text = french_text,
        model_id = 'fr-en' ).get_result()

    # Unpack the translated string from the result
    # Could be a loop if we wanted to fully parse
    # lists of strings
    english_text = translation["translations"][0]["translation"]

    return english_text
