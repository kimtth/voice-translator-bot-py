'''
Signals & Slots
Signals and slots are used for communication between objects. The signals and slots mechanism is a central feature of Qt.
https://doc.qt.io/qt-5/signalsandslots.html
'''
import logging

from PySide2 import QtCore

import api.constants as key

logger = logging.getLogger('voice_translator')

try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print('''
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-python for
    installation instructions.
    ''')
    import sys

    sys.exit(1)


class SpeechContinuousWorker(QtCore.QObject):
    # Signal for dict
    text_result_lang = QtCore.Signal(object)
    speech_key, service_region = key.Const.SPEECH_SUBSCRIPTION_KEY, key.Const.SPEECH_SERVICE_REGION

    def speech_recognize_generator_auto_detect(self):
        speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.service_region)
        auto_detect_source_language_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(
            languages=['ja-JP', 'en-US', 'en-IN', 'en-GB'])

        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
                                                       auto_detect_source_language_config=auto_detect_source_language_config)

        return speech_recognizer

    def speech_recognize_generator_source_language_config(self, source_lang):
        speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.service_region)
        source_language_config = speechsdk.languageconfig.SourceLanguageConfig(source_lang)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
                                                       source_language_config=source_language_config)

        return speech_recognizer

    def speech_recognize_generator_japanese_detect(self):
        speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.service_region)
        # source_language_config = speechsdk.languageconfig.SourceLanguageConfig('ja-JP')
        # speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
        #                                               source_language_config=source_language_config)

        auto_detect_source_language_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(
            languages=['ja-JP'])
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
                                                       auto_detect_source_language_config=auto_detect_source_language_config)

        return speech_recognizer

    def speech_recognize_generator_english_detect(self):
        speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.service_region)
        auto_detect_source_language_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(
            languages=['en-US', 'en-IN', 'en-GB'])

        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
                                                       auto_detect_source_language_config=auto_detect_source_language_config)

        return speech_recognizer

    def speech_recognize_continual_from_mic(self, speech_recognizer, ui_callback):
        # Connect callbacks to the events fired by the speech recognizer
        speech_recognizer.recognized.connect(lambda evt: self.yield_string_to_gui(evt.result))
        speech_recognizer.session_stopped.connect(ui_callback)
        speech_recognizer.canceled.connect(ui_callback)

        # Start continuous speech recognition
        speech_recognizer.start_continuous_recognition()

    def yield_string_to_gui(self, result):
        recognized_text = result.text
        auto_detect_source_language_result = speechsdk.AutoDetectSourceLanguageResult(result)
        lang = auto_detect_source_language_result.language

        logger.info('Recognized: {} in language {}'.format(recognized_text, lang))
        print('Recognized: {} in language {}'.format(recognized_text, lang))

        # PyQT slot and signal
        if recognized_text:
            result = {'text': recognized_text, 'lang': lang}
            self.text_result_lang.emit(result)  # Emit Signal
