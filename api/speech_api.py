#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
"""
Speech recognition samples for the Microsoft Cognitive Services Speech SDK
"""

import time
import wave
import api.constants as key
import os, requests, uuid, json

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


# Set up the subscription info for the Speech Service:
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = key.Const.SPEECH_SUBSCRIPTION_KEY, key.Const.SPEECH_SERVICE_REGION


# https://docs.microsoft.com/mt-mt/azure/cognitive-services/speech-service/language-support#speech-to-text
def speech_recognize_once_with_auto_language_detection_from_mic(ui_callback):
    """performs one-shot speech recognition from the default microphone with auto language detection"""
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # create the auto detection language configuration with the potential source language candidates
    auto_detect_source_language_config = \
        speechsdk.languageconfig.AutoDetectSourceLanguageConfig(languages=["ja-JP", "en-US", "en-IN"])
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, auto_detect_source_language_config=auto_detect_source_language_config)
    result = speech_recognizer.recognize_once()

    # add kim
    ui_callback()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        auto_detect_source_language_result = speechsdk.AutoDetectSourceLanguageResult(result)
        print("Recognized: {} in language {}".format(result.text, auto_detect_source_language_result.language))
        return result.text, auto_detect_source_language_result.language
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
        return "No speech could be recognized", ""
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        return "Speech Recognition canceled", cancellation_details.reason


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
        # 'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': source_text
    }]

    try:
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()
        print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))

        return result_from_translate_response(response)
    except requests.exceptions.RequestException as e:
        return "The Connection is failed: {}", e
    except Exception as e:
        return e


def result_from_translate_response(response):
    response_dict = response[0]
    if 'translations' in response_dict:
        response_results = response_dict['translations']
        return response_results[0]['text']
    else:
        raise Exception("The response is incorrect.")
