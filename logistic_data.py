import os
import pandas as pd
from pandasai import SmartDatalake, Agent
from langchain_google_vertexai import ChatVertexAI
from dotenv import load_dotenv

load_dotenv()


class logistics_data:
    def __init__(self, file_name="logistics.xlsx"):

        self.llm = ChatVertexAI(
            model="gemini-1.5-flash-001",
            temperature=0.7,
            # max_tokens=None,
            # max_retries=6,
            # stop=None,
            # other params...
        )


        self.transportation_df = pd.read_excel(file_name, sheet_name="Transportation")
        self.inventory_df = pd.read_excel(file_name, sheet_name="Inventory")
        self.wearhouse_df = pd.read_excel(file_name, sheet_name="Warehousing")
        self.orders_df = pd.read_excel(file_name, sheet_name="Order Processing")

        df = pd.read_excel(file_name, sheet_name=None)
        self.sheets = list(df.keys())
        

        # lake = SmartDatalake([transportation_df, inventory_df, wearhouse_df, orders_df], config={"llm": llm, "verbose": False})
        self.agent = Agent([self.transportation_df, self.inventory_df, self.wearhouse_df, self.orders_df], config={"llm": self.llm, "verbose": True})
        # self.agent.train(docs=["Provide detailed step-by-step explanation in your response "])
        
        

    def chat(self, query):
        ## "What is average Total  transportation cost per km in Ocean and by Air?"
        # response = lake.chat("What is the average distance from Asia to Africa")
        # response = lake.chat("In Which region Product B is available in abundance based on inventory level of weahousing")
        ## What is the storage space required in square feet for Product B?
        ## How many no. of orders have been placed for the product whose sum of total inventory carrying cost is highest?

        # query = f"Please answer in detail for this query: {query}"
        # import re
        # pattern = r"^#+"
        # replacement = ""

        response = self.agent.chat(query)
        detailed_response = self.agent.explain()

        detailed_response += "\nCode Generated:\n"
        # # detailed_response += "|One|Two|Three|\n"

        for item in self.agent.logs:
            if item["source"] == "CodeCleaning":
                # detailed_response += f"#### Source: {item['source']}\n"
                # rep_txt = re.sub(pattern, replacement, )
                detailed_response += f"{item['msg']}\n"

        # print(detailed_response)


        # detailed_response = 
        return response, detailed_response


