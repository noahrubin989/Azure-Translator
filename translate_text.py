import os
from typing import List

# To load key, endpoint and region information
from dotenv import load_dotenv

# Azure imports
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem, TranslatedTextItem

def get_input_text_info() -> List[InputTextItem]:
    """
    Generates a list of text items to be used as input for translation.

    Returns:
        List[InputTextItem]: A list containing the input text items to translate.
    """
    return [InputTextItem(text="Azure is the cloud computing platform developed by Microsoft")]
 

def setup_client() -> TextTranslationClient:
    """
    Initialises and returns a TextTranslationClient using credentials stored in environment variables.

    The function loads the environment variables from a `.env` file, retrieves the
    Azure Translator key, endpoint, and region. Then, it constructs the TranslatorCredential
    and uses it to create a TextTranslationClient instance.

    Returns:
        TextTranslationClient: A configured TextTranslationClient for making translation requests.
    """
    load_dotenv()
    key = os.getenv('TRANSLATOR_KEY')
    endpoint = os.getenv('TRANSLATOR_ENDPOINT')
    region = os.getenv('TRANSLATOR_REGION')
    credential = TranslatorCredential(key, region)
    text_translator_client = TextTranslationClient(endpoint=endpoint, credential=credential)
    return text_translator_client


def translate_text(
        text_translator_client: TextTranslationClient,
        source_language: str="en-AU",
        target_languages: List[str]=["es", "it", "fr"]
    ) -> TranslatedTextItem:
    """
    Translates the text items obtained from `get_input_text_info` into multiple target languages.

    Args:
        text_translator_client (TextTranslationClient): 
            A configured TextTranslationClient instance used for performing text translations.

    Returns:
        TranslatedTextItem: 
            The first item from the translation response, containing details such as the 
            target language and translated text. If the response is empty, returns None.
    """
    source_language = source_language
    target_languages = target_languages

    response = text_translator_client.translate(
        content=get_input_text_info(), 
        to=target_languages, 
        from_parameter=source_language
    )

    translation_info = response[0] if response else None
    return translation_info


def print_transltion_info(translation_info):
    if translation_info:
        print("Original Text:")
        print(f"{get_input_text_info()[0].text}\n")
        print('Translations are:')
        for translated_text in translation_info.translations:
            print(f"{translated_text.to.upper()}: {translated_text.text}:")


def main():
    text_translator_client = setup_client()
    translation_info = translate_text(text_translator_client, "en-AU", ['es', 'it', 'fr'])
    print_transltion_info(translation_info)


if __name__ == '__main__':
    main()