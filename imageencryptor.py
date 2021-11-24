from Crypto.Cipher import AES
import imghdr
import os
import hashlib

class ImageEncryptor :
    def __init__(self,key,file_path) :
        self.key = key 
        self.iv = '4377777172699a75'.encode()
        self.file_path = file_path

    def key_generate (self,obj) :
        return hashlib.md5( hashlib.sha256( (obj).encode() ).hexdigest().encode() ).hexdigest().encode()

    def check_file (self) :
        if imghdr.what('1'+self.file_path) == None : 
            os.remove('1'+self.file_path)
            return False #Invalid Key
        else :
            os.remove('1'+self.file_path)
            return True #Valid Key
             
    def encrypt (self) :
        while True :
            try:
                file = open(self.file_path,'rb')
                image = file.read() #reading image
                file.close()
                break 
            except :
                print('Please Check File Path')
                return 0
        
        obj = AES.new(self.key_generate(self.key), AES.MODE_CBC, self.iv)
        
        length = 16 - (len(image) % 16)
        image += bytes([length]) * length
        image = obj.encrypt(image)   #encrypting
        
        fin = open(self.file_path, 'wb')
        fin.write(image)
        fin.close()    
        return True     
        
    def decrypt (self) :
        file = open(self.file_path, 'rb')
        image = file.read() #reading image
        file.close()
        
        obj2 = AES.new(self.key_generate(self.key), AES.MODE_CBC, self.iv)
        
        obj=obj2.decrypt(image) #decrypt
        
        length = 16 - (len(obj) % 16)
        obj += bytes([length]) * length    
        
        fin = open('1'+self.file_path, 'wb') 
        #saving temporary because if saves normally and key is invalid , we cant reach image again
        fin.write(obj)
        fin.close()  
        
        if self.check_file() : #if image opens , its save normally , else deletes the temporary image
            fin = open(self.file_path, 'wb')
            fin.write(obj)
            fin.close()   
            return True            
        
        else :
            return False
    