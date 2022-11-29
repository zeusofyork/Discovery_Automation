import cryptocode

class RunSecretStuff:
    def __init__(self,password) -> None:
        self.password = password
    
    def encrypt_file(self, file_name):   
        with open(file_name, "r") as f:
            file = f.read()
            

        with open(file_name, "wb") as f:
            encoded = cryptocode.encrypt(file, self.password)
            print(encoded)
            f.write(bytes(encoded, encoding="utf-8"))
    
        
    def run_file(self,file):  
        exec(str(file))
    
    
    def decrypt_file(self,file):
        with open(file, "r") as r:
            test = r.read()
            decoded = cryptocode.decrypt(test, self.password)
        return decoded
    
    def save_file(self,str_file,filename):
        with open(filename, "w+") as f:
            f.write(str_file)    
    
if __name__ == "__main__":
    password = "mypassword"
    file = "test.py"
    runner = RunSecretStuff(password)
    
    #to encrypt a file
    runner.encrypt_file(file)
    
    #to decrpyt
    decrypted_file = runner.decrypt_file(file)
    
    # to save file back as unencrpyted
    #runner.save_file(decrypted_file, file)
    
    #to run
    runner.run_file(decrypted_file)