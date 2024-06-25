import gradio as gr
from modules.utils.chat_utils import (
    productivity_chat,
    browser_chat,
    scientist_chat,
    regular_chat, document_chat,
    image_chat
)

BUTTON_TEXT = "Enviar"
PLACEHOLDER = "Escribe lo que necesites"


with gr.Blocks() as assistant:
    gr.Markdown("# Asistente Virtual Web Version")
    with gr.Tab("Chat de productividad"):
        chatbot = gr.Chatbot()
        text_input = gr.Textbox(placeholder=PLACEHOLDER)
        text_button = gr.Button(BUTTON_TEXT)
        text_button.click(productivity_chat, [chatbot, text_input], chatbot)
    with gr.Tab("Chat de búsqueda web"):
        chatbot = gr.Chatbot()
        text_input = gr.Textbox(placeholder=PLACEHOLDER)
        text_button = gr.Button(BUTTON_TEXT)
        text_button.click(browser_chat, [chatbot, text_input], chatbot)
    with gr.Tab("Chat científico"):
        chatbot = gr.Chatbot()
        text_input = gr.Textbox(placeholder=PLACEHOLDER)
        text_button = gr.Button(BUTTON_TEXT)
        text_button.click(scientist_chat, [chatbot, text_input], chatbot)
    with gr.Tab("Chat regular"):
        chatbot = gr.Chatbot()
        text_input = gr.Textbox(placeholder=PLACEHOLDER)
        text_button = gr.Button(BUTTON_TEXT)
        text_button.click(regular_chat, [chatbot, text_input], chatbot)
    with gr.Tab("Chat PDF"):
        chatbot = gr.Chatbot()
        text_input = gr.Textbox(placeholder=PLACEHOLDER)
        text_button = gr.Button(BUTTON_TEXT)
        uploaded_document = gr.UploadButton("Sube un archivo PDF", file_types=[".pdf"])
        text_button.click(document_chat, [chatbot, text_input, uploaded_document], chatbot)
    with gr.Tab("Image chat"):
        chatbot = gr.Chatbot()
        text_input = gr.Textbox(placeholder=PLACEHOLDER)
        text_button = gr.Button(BUTTON_TEXT)
        uploaded_image = gr.UploadButton("Sube una imagen", file_types=[".jpg", ".jpeg", ".png"])
        text_button.click(image_chat, [chatbot, text_input, uploaded_image], chatbot)