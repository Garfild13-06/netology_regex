from pprint import pprint
import csv
import re

with open(file="phonebook_raw.csv", encoding="utf8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_contacts_list = []
new_contacts_list.append(('lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email'))


def format_rec(rec):
    new_rec = {'lastname': '',
               'firstname': '',
               'surname': '',
               'organization': '',
               'position': '',
               'phone': '',
               'email': ''}

    lastname = rec[0].split(sep=' ')
    firstname = rec[1].split(sep=' ')
    new_rec['surname'] = rec[2].split(sep=' ')[0]
    new_rec['organization'] = rec[3]
    new_rec['position'] = rec[4]
    phone = rec[5]
    new_rec['email'] = rec[6]
    if len(lastname) == 1:
        new_rec['lastname'] = lastname[0]
    elif len(lastname) == 2:
        new_rec['lastname'] = lastname[0]
        new_rec['firstname'] = lastname[1]
    elif len(lastname) == 3:
        new_rec['lastname'] = lastname[0]
        new_rec['firstname'] = lastname[1]
        new_rec['surname'] = lastname[2]

    if new_rec['firstname'] == '':
        if len(firstname) == 1:
            new_rec['firstname'] = firstname[0]
        elif len(firstname) == 2:
            new_rec['firstname'] = firstname[0]
            new_rec['surname'] = firstname[1]

    phone_pattern = r"(\+7|8)\s?\(?(\d{,3})[\)|\-]?\s?(\d{,3})[-|\s]?(\d{,2})[-|\s]?(\d+)\s?\(?(доб.\s?\d+)?\)?"
    pattern_rel = r"+7(\2)\3-\4-\5 \6"
    new_phone = re.sub(phone_pattern, pattern_rel, phone)
    new_rec['phone'] = new_phone

    result = [
        new_rec['lastname'],
        new_rec['firstname'],
        new_rec['surname'],
        new_rec['organization'],
        new_rec['position'],
        new_rec['phone'],
        new_rec['email']]
    return result


def dublicates_remove(contact_list):
    for i, contact in enumerate(contact_list):
        for y, _ in enumerate(contact_list[i + 1:]):
            n = y + i + 1
            if contact[0] == _[0] and contact[1] == _[1]:
                for x, field in enumerate(contact_list[i]):
                    if field == '':
                        contact_list[i][x] = contact_list[n][x]
                contact_list.pop(n)
            pass
    pass


for person in contacts_list[1:]:
    new_contacts_list.append(format_rec(person))

result_contacts_list = dublicates_remove(new_contacts_list)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
