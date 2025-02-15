'''Importing necessary libraries and creating a list of companies'''

#--------------------------------------------------------------------------------------------------------------------
import json
from g4f.client import Client
import ast
import os


list_of_companies=['reliance-industries','hdfc','ongc','indian-oil-corporation','adani-group',
                     'hero-motocorp','asian-paints','eicher-motors','itc','tata-steel',
                  'shriram-transport-finance','dr-reddys-laboratories','infosys','sun-pharma','tata-consultancy-services-(tcs)',
                      'maruti-suzuki','hcl-technologies','coal-india','lti-mindtree','hdfc-life',
                      'bajaj-auto','britannia-industries','hindalco-industries','larsen-and-toubro','tata-consumer-products',
                     'wipro','titan','bajaj-finance','jsw-steel','icici-bank',
                      'indusind-bank','bharti-airtel','divis-laboratories','sbi-life-insurance','bajaj-finserv',
                      'cipla','grasim-industries','hindustan-unilever','mahindra-and-mahindra','tata-motors',
                     'apollo-hospitals-enterprises','sbi','kotak-mahindra-bank','power-grid-corporation-of-india','axis-bank',
                     'ntpc','tech-mahindra','adani-ports','ultratech-cement','nestle','bharat-petroleum']

#--------------------------------------------------------------------------------------------------------------------


'''

The objective of the code is to generate high-quality question-answer-context pairs from a given paragraph using an AI language model.

It leverages the g4f client to interact with the gemini-pro model for creating completions based on detailed prompts.

The output is returned as a JSON list of dictionaries, each containing the keys "question", "answer" and "context".

'''

#--------------------------------------------------------------------------------------------------------------------

client = Client()

def qa_pair_generator(paragraph, num_pairs):
    
    prompt_1 = '''generate 8 pairs of question and answer and context in a dictionary format from the given paragraph  \ 
                keep in mind of some points:

               1. Each entry is a dictionary with keys "question" and "answer" and "context". 
               4. dictionary can have maximum of 5000 words
               5. make sure that you context should be descriptive text of minimum 200 words
               6. also while generating question answer pair add the name of the company in that question and answer
               
               The format of you output should be the list of dictionary strictly like this given below:
                   [ 
                        {  "question": "value",
                            "answer": "value" , 
                            "context": "value"
                        }
                    ]
                '''

    prompt_2 = fr''' return a valid json format  \ {paragraph}'''
    response = client.chat.completions.create(
        model='gemini-pro',
        messages=[
            {"role": "system", "content": "you are a financial analyst who can generate quality question answers"},
            {"role": "user", "content": prompt_1+prompt_2}
        ],
        max_tokens=100000,
        temperature=1
    )

    gpt_message = response.choices[0].message.content.strip()
    print(gpt_message)
    return gpt_message

#--------------------------------------------------------------------------------------------------------------------


'''
The objective of this code is to generate and save question-answer-context pairs from cleaned JSON data for multiple company files.

It creates a directory for storing the output if it doesn't already exist and reads each JSON file containing cleaned news paragraphs.

For each paragraph in the file, it calls the qa_pair_generator function to create question-answer-context pairs.

These results are stored in a list, and once all paragraphs are processed, the list is saved as a new JSON file in the designated output directory.

'''


#--------------------------------------------------------------------------------------------------------------------
dir_name = "qa_pairs"
save_dir = r"C:\Users\akshi\data for ie643" + fr"\{dir_name}"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
load_dir = r"C:\Users\akshi\data for ie643\cleaned_news_jsons"

num_pairs = 8
for file in list_of_companies:
    print(file)
    list_of_list = []
    file_name = fr"\clean_{file}.json"
    loading_path = load_dir + file_name
    with open(loading_path,'r') as f:
        data = json.load(f)


    for i,element in enumerate(data):
        paragraph = element
        result = qa_pair_generator(paragraph, num_pairs)
        list_of_list.append(result)
        print(i+1,end=' ')

    print("\n")
    # print(list_of_list)
    saving_path = save_dir + f"\qa_pairs_{file}.json"
    with open(saving_path,'w') as f:
        json.dump(list_of_list,f,indent=4)

#--------------------------------------------------------------------------------------------------------------------


