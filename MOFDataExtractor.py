import openai
import re
import PyPDF2
import pandas as pd
import os
from tqdm import tqdm

openai.api_key = "Your api Key"
directory = 'Directory for Literature'

def ask1(system_prompt,user_prompt,engine='gpt-4o-mini'):
    response=openai.ChatCompletion.create(
        model=engine,
        messages=[
            {
                'role': 'system',
                'content': system_prompt
            },
            {
                'role': 'user',
                'content': user_prompt
            }
        ]
    )
    response = response.choices[0].message.content.strip()
    return response

system_prompt="""
            Answer this question as truthfully as possible using the provided context.
            The information should be as short as possible. 
            Use the chemical formula for materials if available. 
            If no data is available or you aren't sure, fill the cells with null.
            Don't fill the cells based on your knowledge, fill it based on the provided context.
            There should be one row of data for each MOF type.
            Summarize the following details in a table with these columns:
            {"MOF Type or MOF Name"|"Secondary building block formation"|"Linker"|"Solvent"|"Reaction Temperature"|"Reaction Time"|"Physical state"|"Metal"|"Oxidation number"|"Pore size or pore diameter"|"pore volume"|"Ligand"|"Multi dentate"|"Synthesis method"|"carboxylate ligands"|"imidazolate"|"Specific Surface Area"|"BET"|"CO2 selectivity amount"|"CO2 selectivity percentage"|"CO2 adsorption amount"|"CO2 adsorption capacity"|"Adsorption temperature"|"Adsorption pressure"}. 
            Write the table in JSON format.
            """
user_prompt="""
input: 
"""

DF_temp = pd.DataFrame()
DF = pd.DataFrame()

try:
    for filename in tqdm(os.listdir(directory)):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory, filename)

            Text = ''
            with open(file_path, 'rb') as file:
                # Create a PDF reader object
                reader = PyPDF2.PdfReader(file)
                num_pages = len(reader.pages)
				
                for page_number in range(num_pages):
                    page = reader.pages[page_number]
                    text = page.extract_text()
                    Text += text

			# Remove references
            references_pattern = r'References\n([\s\S]*)$'
            cleaned_text = re.sub(references_pattern, '', Text, flags=re.DOTALL | re.IGNORECASE).strip()

            # Send GPT prompt
            answer = ask1(system_prompt, cleaned_text)  
            my_string = answer
			
			# Remove unwanted characters
            patterns = ["\\n", "json", "\```"]
            for pattern in patterns:
                my_string = re.sub(pattern, '', my_string)

            my_string = re.sub(r'\n', '', my_string)           
            my_string = re.sub(r'\s+', ' ', my_string).strip()

            # Convert JSON string to DataFrame
            DF_temp = pd.read_json(my_string)
            DF_temp["filename"]=filename
            
        DF=pd.concat([DF,DF_temp])
except Exception as e: 
    print(e)
    

DF.to_csv('GPT_extracted_dataset.csv')

