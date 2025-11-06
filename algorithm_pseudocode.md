Set a directory for articles
create empty dataframe
for each file in directory:
__if file format is pdf:
____store file path
____open PDF file
____get total number of pages
____create empty text variable
____for each page in pdf:
______extract text from each page
______append text to text variable
____remove references section from text
____send text to GPT
____ask GPT question about text
######################################################################################
    GPT prompt:
    •	Answer this question as truthfully as possible using the provided context.
    •	The information should be as short as possible. 
    •	Use the chemical formula for materials if available. 
    •	If no data is available or you aren't sure, fill the cells with null.
    •	Don't fill the cells based on your knowledge, fill it based on the provided context.
    •	There should be one row of data for each MOF type.
    •	Summarize the following details in a table with these columns:
    {"MOf Type"|"Secondary building block formation"|"Linker"|"Solvent"|"Reaction Temperature"|"Reaction Time"|"Physical state"|"Metal"|"Oxidation number"|"Ligand"|"Multi dentate"|"Synthesis method"|"solvothermal"|"ball milling"|"sonochemical"|"microwave-assisted"|"carboxylate ligands"|"imidazolate"|"MOF post-synthetic modification"|"Specific Surface Area"|"BET"|"CO2 selectivity amount"|"CO2 adsorption amount"|"CO2 adsorption capacity"|"Adsorption Temperature"|"Adsorption Pressure"}. 
    •	Write the table in JSON format.
######################################################################################
____store GPT answer in JSON format
____remove unwanted characters
____convert JSON to dataframe
____append dataframe to dataframe
  
