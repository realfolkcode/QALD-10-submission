import json
from tqdm.notebook import tqdm


with open('qald_10.json', 'r') as file:
    data = json.load(file)
    
    
questions = []
for question in data['questions']:
    var_list = {}
    for var in question['question']:
        if var['language'] in var_list:
            var_list[var['language']].append(var['string'])
        else:
            var_list[var['language']] = [var['string']]
            
    questions.append(var_list)
    
with open('questions_only.json', 'w') as file:
    json.dump(questions, file)
