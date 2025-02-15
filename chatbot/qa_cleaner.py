import re
import json


list_of_companies = ['reliance-industries','hdfc','ongc','indian-oil-corporation','adani-group',
                     'hero-motocorp','asian-paints','eicher-motors','itc','tata-steel',
                  'shriram-transport-finance','dr-reddys-laboratories','infosys','sun-pharma','tata-consultancy-services-(tcs)',
                      'maruti-suzuki','hcl-technologies','coal-india','lti-mindtree','hdfc-life',
                      'bajaj-auto','britannia-industries','hindalco-industries','larsen-and-toubro','tata-consumer-products',
                     'wipro','titan','bajaj-finance','jsw-steel','icici-bank',
                      'indusind-bank','bharti-airtel','divis-laboratories','sbi-life-insurance','bajaj-finserv',
                      'cipla','grasim-industries','hindustan-unilever','mahindra-and-mahindra','tata-motors',
                     'apollo-hospitals-enterprises','sbi','kotak-mahindra-bank','power-grid-corporation-of-india','axis-bank',
                     'ntpc','tech-mahindra','adani-ports','ultratech-cement','nestle','bharat-petroleum']



load_dir = r"C:\Users\akshi\data for ie643\qa_pairs"
save_dir = r"C:\Users\akshi\data for ie643\qa_pairs_clean"


fail_count = 0
for company_name in list_of_companies:
    # print(company_name)
    loading_file_name = f"\qa_pairs_{company_name}.json"
    file_loading_path = load_dir + loading_file_name


    '''
     
       This section check that if the json file is valid or not, if it is invalid then if add the required pattern in the end of string to make it avalid json file.

    '''
    #------------------------------------------------------

    with open(file_loading_path, 'r') as f:
        data = json.load(f)

    print(len(data))
    collection = []
    for i in range(len(data)):
        if not data[i].endswith(']'):
            data[i] += '\"\n    }\n]\n'
        data[i] = json.dumps(data[i])
        k = json.loads(data[i])
        collection.append(k)

    with open(file_loading_path, 'w') as f:
        json.dump(collection, f, indent=4)

    #-------------------------------------------------------



    '''
    
    this section extracts only list of dictionary(json) that are enclosed in square brackets(elimination all other characters that are outside the brackets) and then saves them in a separate directory.
    
    '''

    #--------------------------------------------------------

    with open(file_loading_path,'r') as f:
        data = json.load(f)


    list_of_dictionaries = []
    print(len(data))
    for i,element in enumerate(data):
        print(i+1)
        json_text = re.search(r'\[.*?\]', element, re.DOTALL)
        qa_pairs = []
        try:
            if json_text:
                qa_pairs = json.loads(json_text.group(0))
                print("yes")
        except:
            fail_count+=1
            # qa_pairs = []
            print("no")

        list_of_dictionaries.extend(qa_pairs)

    saving_file_name = rf"\qa_pairs_clean_{company_name}.json"
    file_saving_path = save_dir + saving_file_name

    with open(file_saving_path,'w') as f:
        json.dump(list_of_dictionaries,f,indent=4)

print("total no of times loop was failed: ",fail_count)

    #-----------------------------------------------------------



