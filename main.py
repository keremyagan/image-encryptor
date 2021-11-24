from imageencryptor import ImageEncryptor

while True :
    while True :
        try:
            option = int(input('1-Encryption\n2-Decryption\n3-Exit\nYour Choice:'))
            if option>0 and option<4 :
                break
            else :
                print('Please Choose An Option.')
        
        except:
            print('Please Enter An Integer.')

    if option == 1 : #Encryption
        key = input('Please Enter Key:')
        filepath = input('Please Enter File Path:')
        
        imageEncryptor = ImageEncryptor(key,filepath)
        result = imageEncryptor.encrypt()   
        
        if result:
            print('Image Encrypted.')    
    
    elif option == 2 : #Decryption
        key = input('Please Enter Key:')
        filepath = input('Please Enter File Path:')
        
        imageEncryptor = ImageEncryptor(key,filepath)
        result = imageEncryptor.decrypt()        
        
        if result : #success
            print('Decryption Success.')
        
        else :
            print('Please Check Key.')
              
    else : #exit
        break  
    

