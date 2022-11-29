from cryptography.fernet import Fernet


def get_creds():
    #Getting login
    cred_filename = 'CredFile.ini'
    key_file = "key.key"
    key = ''
    
    
    with open (key_file, 'r') as key_in:
        key = key_in.read().encode()
    f = Fernet (key)
    with open (cred_filename, 'r') as cred_in:
        lines = cred_in.readlines()
        config = {}
        for line in lines:
            tuples = line.rstrip('\n').split('=',1)
            if tuples[0] in ('Username', 'Password') :
                config [tuples[0]] = tuples [1]
        passwd = f.decrypt(config['Password'].encode()) .decode()
        return passwd


get_creds()