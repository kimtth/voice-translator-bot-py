#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
"""
Speech recognition samples for the Microsoft Cognitive Services Speech SDK
"""
import logging

import requests
import uuid

import api.constants as key

try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-python for
    installation instructions.
    """)
    import sys
    sys.exit(1)

logger = logging.getLogger('voice_translator')
# Set up the subscription info for the Speech Service:
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = key.Const.SPEECH_SUBSCRIPTION_KEY, key.Const.SPEECH_SERVICE_REGION


# https://docs.microsoft.com/mt-mt/azure/cognitive-services/speech-service/language-support#speech-to-text
def speech_recognize_once_with_auto_language_detection_from_mic(speech_recognizer, ui_callback):
    """performs one-shot speech recognition from the default microphone with auto language detection"""
    result = speech_recognizer.recognize_once()

    # Turn to button as the inactive state.
    ui_callback()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        auto_detect_source_language_result = speechsdk.AutoDetectSourceLanguageResult(result)
        logger.info("Recognized: {} in language {}".format(result.text, auto_detect_source_language_result.language))
        return result.text, auto_detect_source_language_result.language
    else:
        logger.info("Error Log: ", result.reason)
        return str(result.reason), ""


def translation_once_from_text(source_text, source_lang):
    subscription_key = key.Const.TRANSLATOR_TEXT_SUBSCRIPTION_KEY
    if not subscription_key:
        raise Exception('Please set/export the environment variable: {}'.format(subscription_key))

    endpoint = key.Const.TRANSLATOR_TEXT_ENDPOINT
    if not endpoint:
        raise Exception('Please set/export the environment variable: {}'.format(endpoint))

    target_lang = 'ja'
    if 'ja' in source_lang:
        target_lang = 'en'

    path = '/translate?api-version=3.0'
    params = '&from=' + source_lang + '&to=' + target_lang
    constructed_url = endpoint + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': key.Const.TRANSLATOR_TEXT_REGION_AKA_LOCATION,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': source_text
    }]

    try:
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()
        # logger.info(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))

        return result_from_translate_response(response)
    except requests.exceptions.RequestException as e:
        logger.info("The Connection is failed: {}", e)
        return "The Connection is failed: {}", e
    except Exception as e:
        logger.info(e)
        return e


def result_from_translate_response(response):
    if len(response) > 0:
        response_dict = response[0]
        if 'translations' in response_dict:
            response_results = response_dict['translations']
            return response_results[0]['text']
        else:
            raise Exception("The response is incorrect.")
    else:
        raise Exception("The response is incorrect.")