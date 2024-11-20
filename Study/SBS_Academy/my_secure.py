def secure_name(name):
    return name[0] + '***'

def secure_no(no):
    return no[0:8] + '******'

def secure_phone(phone):
    return phone.replace(phone[4:8], '****')