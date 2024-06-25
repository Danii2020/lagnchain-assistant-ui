from modules.langchain_assistant import (
    LangChainProductivityAssistant,
    LangChainBrowserAssistant,
    LangChainScientisAssistant,
    LangChainChatAssistant,
    LangChainDocumentAssistant,
    LangchainImageAssistant
)

from modules.menus.role import create_notion_page

productivity_role = LangChainProductivityAssistant()
browser_role = LangChainBrowserAssistant()
scientist_role = LangChainScientisAssistant()
regular_chat_role = LangChainChatAssistant()

def chat(chat_history, user_input, role):
    content = ''
    assistant_response = role.chat(input=user_input)
    if isinstance(role, LangChainChatAssistant):
        content = assistant_response
    else:
        content = assistant_response['content']
        create_notion_page(assistant_response)
    response = ''
    for letter in content:
        response += letter
        yield chat_history + [(user_input, response)]

def productivity_chat(chat_history, user_input):
    responses = chat(
        chat_history=chat_history,
        user_input=user_input,
        role=productivity_role
    )
    for response in responses:
        yield response

def browser_chat(chat_history, user_input):
    responses = chat(
        chat_history=chat_history,
        user_input=user_input,
        role=browser_role
    )
    for response in responses:
        yield response

def scientist_chat(chat_history, user_input):
    responses = chat(
        chat_history=chat_history,
        user_input=user_input,
        role=scientist_chat
    )
    for response in responses:
        yield response

def regular_chat(chat_history, user_input):
    responses = chat(
        chat_history=chat_history,
        user_input=user_input,
        role=regular_chat_role
    )
    for response in responses:
        yield response


def document_chat(chat_history, user_input, document_name):
    document_role = LangChainDocumentAssistant(document_name=document_name)
    assistant_response = document_role.chat(query=user_input)
    response = ''
    for letter in assistant_response:
        response += letter
        yield chat_history + [(user_input, response)]


def image_chat(chat_history, user_input, image_path):
    image_role = LangchainImageAssistant(image_path=image_path)
    assistant_response = image_role.chat(input=user_input)
    content_response = assistant_response["image_description"]
    response = ''
    for letter in content_response:
        response += letter
        yield chat_history + [(user_input, response)]



