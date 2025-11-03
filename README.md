# GPT-MOF-Project

In this project we used GPT-4o-mini engine to extract key elements from scientific literature regarding metal-organic frameworks features and their CO2 capture properties.

Using the MOFDataExtractor,py, you can extract MOF key characteristics from literature.
These characteristics include: 
MOF Type, Secondary building block formation, Linker, Solvent, Reaction Temperature, Reaction Time, Physical state, Metal, Oxidation number, Pore diameter, pore volume, Ligand, Multi dentate, Synthesis method, carboxylate ligands, imidazolate, Specific Surface Area, BET, CO2 selectivity, CO2 selectivity percentage, CO2 adsorption amount, CO2 adsorption capacity, Adsorption temperature, and Adsorption pressure.

You can edit the characteristics inside the code by editing the GPT prompt.

In order to run the code:

1-install the requirements

2-insert your OpenAI API key in the outlined section.

3-make a directory with the name "Directory for Literature" and put the literature in PDF format in the folder.

4-rename the documents in numeric format to track the documents for further analysis (optional). 

MOF_database_cleaned.csv contains the csv output of data extracted from 434 articles. The data has been cleaned and is machine-readable.

