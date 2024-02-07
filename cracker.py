#The used approach is a bruteforce. It is tested each combination of the string
#"stefano", an uppercase character and a number.

def TestaPassword(password, cyphertext, number, salt):
    import base64
    import os
    import sys
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    try:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key)
        print(f.decrypt(cyphertext))
        print("Found Password: \n")
        print(b"passwd : " + password)
        exit()
    except:
        print(b"password " + password + b" not correct")






import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
salt = b'\xd4\x1f\xceg\xe9\xafW\xad\xb7+Y\xc3\xd9t\xe1\xc6'
cifre = [b"1", b"2", b"3", b"4", b"5", b"6", b"7", b"8", b"9"]
listaCaratteri = [b"A", b"B", b"C", b"D", b"E", b"F", b"G", b"H", b"I", b"J", b"K", b"L", b"M", b"N", b"O", b"P", b"Q", b"R", b"S", b"T", b"U", b"V", b"W", b"X", b"Y", b"Z"]
number = 0
cyphertext = b'gAAAAABgoqMJ17XcgGFW347sJ9q1cXjzd1Cl74v42sZVhmbGGer1_l1NFfZSM-FRCVpCaZ9-JYjy5Ut0Ycy4E1GHyUxCSEgROSw2HFsJjX43qZgk2AyMG1Vzfxx8V212x3WWwszfCV1rR2KWHvUyorQB-0asgI3NLcrZiLVjJSQHg2qOqqKNUyv-TQsR-EIo-GgI4FOnA1kyFymTQv2Vcjxq4zAtUO3-nssuxuVC_n27xefX4eRd_GrnonCvRL_0b_3KYt-pQp4iT_hcbvuEnuM--Ue-F_BjYg=='


#code about assignments of password (with loop)

for listaNumeri in cifre:
    for carattere in listaCaratteri:
        password = carattere+listaNumeri+b"stefano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = listaNumeri+carattere+b"stefano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = listaNumeri+b"s"+carattere+b"tefano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = listaNumeri+b"st"+carattere+b"efano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = listaNumeri+b"ste"+carattere+b"fano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = listaNumeri+b"stef"+carattere+b"ano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = listaNumeri+b"stefa"+carattere+b"no"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = listaNumeri+b"stefan"+carattere+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = listaNumeri+b"stefano"+carattere
        TestaPassword(password, cyphertext, number, salt)
        number+=1

        #parte 2
        password = carattere+b"s"+listaNumeri+b"tefano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+carattere+listaNumeri+b"tefano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+listaNumeri+carattere+b"tefano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+listaNumeri+b"t"+carattere+b"efano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+listaNumeri+b"te"+carattere+b"fano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+listaNumeri+b"tef"+carattere+b"ano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+listaNumeri+b"tefa"+carattere+b"no"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+listaNumeri+b"tefan"+carattere+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+listaNumeri+b"tefano"+carattere
        TestaPassword(password, cyphertext, number, salt)
        number+=1

        #parte 3
        password = carattere+b"st"+listaNumeri+b"efano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+carattere+b"t"+listaNumeri+b"efano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"st"+carattere+listaNumeri+b"efano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"st"+listaNumeri+carattere+b"efano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"st"+listaNumeri+b"e"+carattere+b"fano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"st"+listaNumeri+b"ef"+carattere+b"ano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"st"+listaNumeri+b"efa"+carattere+b"no"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"st"+listaNumeri+b"efan"+carattere+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+listaNumeri+b"tefan"+carattere+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"st"+listaNumeri+b"efano"+carattere
        TestaPassword(password, cyphertext, number, salt)
        number+=1

        #parte 4
        password = carattere+b"ste"+listaNumeri+b"fano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+carattere+b"te"+listaNumeri+b"fano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"st"+carattere+b"e"+listaNumeri+b"fano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"ste"+carattere+listaNumeri+b"fano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"ste"+listaNumeri+carattere+b"fano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"ste"+listaNumeri+b"f"+carattere+b"ano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"ste"+listaNumeri+b"fa"+carattere+b"no"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"ste"+listaNumeri+b"fan"+carattere+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"ste"+listaNumeri+b"fano"+carattere
        TestaPassword(password, cyphertext, number, salt)
        number+=1

        #parte 5
        password = carattere+b"stef"+listaNumeri+b"ano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+carattere+b"tef"+listaNumeri+b"ano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"st"+carattere+b"ef"+listaNumeri+b"ano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"ste"+carattere+b"f"+listaNumeri+b"ano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stef"+carattere+listaNumeri+b"ano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stef"+listaNumeri+carattere+b"ano"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stef"+listaNumeri+b"a"+carattere+b"no"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stef"+listaNumeri+b"an"+carattere+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stef"+listaNumeri+b"ano"+carattere
        TestaPassword(password, cyphertext, number, salt)
        number+=1

        #parte 6
        password = carattere+b"stefa"+listaNumeri+b"no"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+carattere+b"tefa"+listaNumeri+b"no"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"st"+carattere+b"efa"+listaNumeri+b"no"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"ste"+carattere+b"fa"+listaNumeri+b"no"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stef"+carattere+b"a"+listaNumeri+b"no"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stefa"+carattere+listaNumeri+b"no"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stefa"+listaNumeri+carattere+b"no"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stefa"+listaNumeri+b"n"+carattere+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stefa"+listaNumeri+b"no"+carattere
        TestaPassword(password, cyphertext, number, salt)
        number+=1

        #parte 7
        password = carattere+b"stefan"+listaNumeri+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+carattere+b"tefan"+listaNumeri+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"st"+carattere+b"efan"+listaNumeri+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"ste"+carattere+b"fan"+listaNumeri+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stef"+carattere+b"an"+listaNumeri+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stefa"+carattere+b"n"+listaNumeri+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stefan"+carattere+listaNumeri+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stefan"+listaNumeri+carattere+b"o"
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stefan"+listaNumeri+b"o"+carattere
        TestaPassword(password, cyphertext, number, salt)
        number+=1

        #parte 8
        password = carattere+b"stefano"+listaNumeri
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"s"+carattere+b"tefano"+listaNumeri
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"st"+carattere+b"efano"+listaNumeri
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"ste"+carattere+b"fano"+listaNumeri
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stef"+carattere+b"ano"+listaNumeri
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stefa"+carattere+b"no"+listaNumeri
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stefan"+carattere+b"o"+listaNumeri
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stefano"+carattere+listaNumeri
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        password = b"stefano"+listaNumeri+carattere
        TestaPassword(password, cyphertext, number, salt)
        number+=1
        
        
        
        





