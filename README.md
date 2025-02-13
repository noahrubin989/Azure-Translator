# Azure Translator

## Overview
This repository deals with translating text with Azure AI Translator service - a service that can translate more than 100 languages and dialects.

## Provisioning an Azure AI Translator resource
To use the Azure AI Translator service, you must provision a resource for it in your Azure subscription. You can provision a single-service Azure AI Translator resource, or you can use the Text Analytics API in a multi-service Azure AI Services resource. In this example I use a single-service Azure AI Translator resource.

<img width="606" alt="Resource Setup" src="https://github.com/user-attachments/assets/2be5c79d-b3fe-459b-b8b1-f4a81c4f9dce" />

## Environment Setup

I set up a virtual envirnment called `translator_project` in the VS Code terminal, then activated it

```bash
python3 -m venv translator_project
```

```bash
source translator_project/bin/activate
```

Next, go to the **Keys and Endpoint** section, and extract the **Key 1**
<img width="819" alt="Keys and Endpoint" src="https://github.com/user-attachments/assets/811761c7-779b-41d6-b270-a6473b8d11a4" />
