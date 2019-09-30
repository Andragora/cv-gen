from pathlib import Path
from ruamel.yaml import YAML

path = Path('data_str.yaml')
opath = Path('ur_data.yaml')

yaml = YAML()
yaml.indent(sequence=4, offset=2)
code = yaml.load(path)
code['name'] = input('Write your full name ');
code['contact']= [dict(address=input('Full address '), phone=int(input('Phone number ')), email=input('email '), birth_date=input('birth date '))]
print('Education');
code['education']=[dict(degree=input('degree '),direction=input('field of study '),university=input('school name '),data=input('start-end date '))]
print('Experience');
code['experience']=[dict(company=input('company name '),city=input('city '),data=input('start-end date '),title=input('job title '),description=input('short description of the job '))]
print('Skills');
code['skills']=[dict(category=input('category '),list=input('list '))]
print('Languages');
code['languages']=[dict(language=input('language '),level=input('level of the language '))]
print('Others');
code['others']=input('list of hobbies ')

while True:
    a=input("Enter yes/no to add more education");
    if(a=="yes"):
        code['education'].append(dict(degree=input('degree '),direction=input('field of study '), university=input('school name '), data=input('start-end date ')));
    elif(a=="no"):
        break;
    else: print("Enter yes/no");
while True:
    a=input("Enter yes/no to add more exp");
    if(a=="yes"):
        code['experience'].append(dict(company=input('comapny name '), city=input('city '), data=input('start-end date '),title=input('job title '),description=input('short description of the job ')));
    elif(a=="no"):
        break;
    else: print("Enter yes/no");
while True:
    a=input("Enter yes/no to add more skills");
    if(a=="yes"):
        code['skills'].append(dict(category=input('category '), list=input('list of skills ')));
    elif(a=="no"):
        break;
    else: print("Enter yes/no");
while True:
    a=input("Enter yes/no to add more languages");
    if(a=="yes"):
        code['languages'].append(dict(language=input('language '),level=input('level of the language ')));
    elif(a=="no"):
        break;
    else: print("Enter yes/no");
yaml.dump(code, opath)