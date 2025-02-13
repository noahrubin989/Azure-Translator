# Azure Translator

## Overview
This repository deals with translating text with Azure AI Translator service - a service that can translate more than 100 languages and dialects.

## Azure AI Translator Resource Setup
To use the Azure AI Translator service, you must provision a resource for it in your Azure subscription. You can provision a single-service Azure AI Translator resource, or you can use the Text Analytics API in a multi-service Azure AI Services resource. In this example I use a single-service Azure AI Translator resource.

<img width="606" alt="Resource Setup" src="https://github.com/user-attachments/assets/2be5c79d-b3fe-459b-b8b1-f4a81c4f9dce" />

Next, go to the **Keys and Endpoint** section and extract the **Key 1** value. This will be placed in our `.env` file, alongside the region that the resource exists in (Australia East)

<img width="819" alt="Keys and Endpoint" src="https://github.com/user-attachments/assets/811761c7-779b-41d6-b270-a6473b8d11a4" />

The `.env` file takes on the following form:

```
TRANSLATOR_KEY=your_translator_key
TRANSLATOR_REGION=your_translator_region
```

## Environment Setup

I set up a virtual environment called `translator_project` in the VS Code terminal, then activated it:

```bash
python3 -m venv translator_project
```

```bash
source translator_project/bin/activate
```

## Package Configuration

In the VS Code terminal (with the virtual environment now set up), install the following libraries

```bash
pip install azure-ai-translation-text==1.0.0b1 python-dotenv
```

## Run File

In the VS Code terminal, run the following

```bash
python3 translate_text.py
```

## Resources
* [Exploring the `TextTranslationClient` class](https://learn.microsoft.com/en-us/python/api/azure-ai-translation-text/azure.ai.translation.text.texttranslationclient?view=azure-python)
* [Azure Text Translation client library for Python - version 1.0.1](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-translation-text-readme?view=azure-python)


