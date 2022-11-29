
from cryptography.fernet import Fernet
import re
import ctypes
import time
import os
import sys


class Credentials():
    def __init__ (self):
        self.__username = ''
        self.__key = ''
        self.__password = ''
        self.__key_file = 'key.key'
        
    @property
    def username (self):
        return self. username
    @username.setter
    def username (self, username):
        while (username == ''):

            username = input('Enter username ')
            self._username = username
        
        
    @property
    def password(self):
        return self.__password
    
    
    @password.setter
    def password(self, password):
        self._key = Fernet.generate_key()
        f = Fernet (self._key)
        self._password = f.encrypt (password.encode()).decode()
        del f
        
    def create_cred(self):
        cred_filename = 'CredFile.ini'
        
        with open (cred_filename, 'w') as file_in:
            file_in.write('#Credential file:\nUsername{}\nPassword={}'.format(self.__username, self.__password))
            file_in.write('++' * 20)
            
        #creates or overwrites existing key file
        if (os.path.exists(self.__key_file)):
            os.remove(self.__key_file)

        try:
            os_type = sys.platform
            if (os_type == 'linux'):
                self.__key_file = '.' + self.__key_file
            with open (self.__key_file, 'w') as key_in:
                key_in.write(self.__key.decode())
                
                
            #Hiding the key file
            if (os_type == 'win32'):
                ctypes.windl1.kernel32. SetFileAttributes (self._key_file, 2)
            else:
                pass
            
        except PermissionError:
            os.remove(self.__key_file)
            print("A permission error occured")
            sys.exit()
            
            
        self.__username = ''
        self.__password = ''
        self.__key = ''
        self.__key_file
        
        
def main():
    #Creating object credentials class
    
    creds = Credentials()
    
    #Accepting Creds
    creds.username = input('Enter Username: ')
    creds.password = input('Enter Password: ')
    
    creds.create_cred()
    print('**' * 20)
    print('Credential file created successfully at {}').format(time.ctime())
    print('**' * 20)
    
    if __name__ == '__main__':
        main()
