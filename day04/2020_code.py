import os
scriptdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(scriptdir,'2020_input.txt')) as raw:
    data = raw.read().split("\n\n")

import re
requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optionalFields = ['cid']
def serialize(doc):
    return re.split("\n| |:", doc)

def dict_me_down(doc):
    doc = re.split("\n| ", doc)
    return dict(x.split(':') for x in doc)

#quick and dirty
def simple_validate(doc):
    doc = serialize(doc)
    if set(requiredFields).issubset(set(doc)):
        return 1
    else:
        return 0

def year_validator(low, high, value):
    if low <= int(value) <=  high:
        return True
    return False

hgt = re.compile('''(\d*)(\w*)''')
def hgt_validator(value):
    quant, qual = hgt.search(value).group(1,2)
    if qual == 'cm':
        if 150 <= int(quant) <= 193:
            return True
        return False
    if 59 <= int(quant) <= 76:
        return True
    return False

def hcl_validator(value):
    if re.match('''#[a-f0-9]{6}''', value) is None:
        return False
    return True

def ecl_validator(value):
    valid = ['amb','blu','brn','gry','grn','hzl','oth']
    if value in valid:
        return True
    return False

def pid_validator(value):
    if len(value) == 9:
        return True
    return False

def validator(k,v):
    validate_switch={
        'byr': lambda x: year_validator(1920,2002,x),
        'iyr': lambda x: year_validator(2010,2020,x),
        'eyr': lambda x: year_validator(2020,2030,x),
        'hgt': lambda x: hgt_validator(x),
        'hcl': lambda x: hcl_validator(x),
        'ecl': lambda x: ecl_validator(x),
        'pid': lambda x: pid_validator(x),
        'cid': lambda x: True
    }
    return validate_switch[k](v)
    
failureList=set()
def validate(doc):
    doc = dict_me_down(doc)
    if set(requiredFields).issubset(set(doc.keys())) is False:
        return False
    for key in doc:
        if validator(key, doc[key]) is False:
            failureList.add(key)
            return False
    return True


def main(data, val_func):
    count = 0
    for doc in data:
        count += 1 if val_func(doc) else 0
    return count

if __name__ == "__main__":
    print(main(data, simple_validate))
    print(main(data, validate))