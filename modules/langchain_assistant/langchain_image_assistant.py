import base64
import dotenv
from langchain.chains import TransformChain
from langchain_openai import ChatOpenAI
from modules.parsers.image_response_parser import parser

from langchain_core.messages import HumanMessage

dotenv.load_dotenv()

llm = ChatOpenAI(temperature=0.5, model="gpt-4o", max_tokens=1024)

class LangchainImageAssistant:
    def __init__(self, image_path):
        self.image_path = image_path
        image_chain = self.get_load_image_chain()
        self.vision_chain = image_chain | self.image_model | parser

    def load_image(self, inputs):
        image_path = inputs["image_path"]

        def encode_image(image_path):
            with open(image_path, 'rb') as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        image_base64 = encode_image(image_path=image_path)
        return {"image":image_base64}
    
    def get_load_image_chain(self):
        return TransformChain(
            input_variables=["image_path"],
            output_variables=["image"],
            transform=self.load_image
        )
    
    def image_model(self, inputs):
        content = [
                HumanMessage(content=[
                    {
                        "type": "text",
                        "text": inputs["prompt"]
                    },
                    {
                        "type": "text",
                        "text": parser.get_format_instructions()
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{inputs['image']}"
                        }
                    }
                ])
            ]
        message_response = llm.invoke(
            content
        )
        return message_response.content
    
    def chat(self, input):
        return self.vision_chain.invoke({
            "image_path": self.image_path,
            "prompt": input
        })

