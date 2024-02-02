# Password-Cracker-Challange
This challange consists on the cracking of a password set by the professor for the Data and System Security Course of the Master Degree in Cybersecurity at the University of Pisa. 
In particular, I know the cybertext and the salt used into the algorithm and the unknown informations are the password and the cleartext. The vulnerability consists of an unsafe password: it is a combination of the word "stefano" in lowercase, combined with a number and an uppercase character.

The salt is the following: 
Salt = b'\xd4\x1f\xceg\xe9\xafW\xad\xb7+Y\xc3\xd9t\xe1\xc6'

The ciphertext is the following:
Cypertext = b'gAAAAABgoqMJ17XcgGFW347sJ9q1cXjzd1Cl74v42sZVhmbGGer1_l1NFfZSM-FRCVpCaZ9-JYjy5Ut0Ycy4E1GHyUxCSEgROSw2HFsJjX43qZgk2AyMG1Vzfxx8V212x3WWwszfCV1rR2KWHvUyorQB-0asgI3NLcrZiLVjJSQHg2qOqqKNUyv-TQsR-EIo-GgI4FOnA1kyFymTQv2Vcjxq4zAtUO3-nssuxuVC_n27xefX4eRd_GrnonCvRL_0b_3KYt-pQp4iT_hcbvuEnuM--Ue-F_BjYg=='

The package used is cryptography-3.4.7-cp36-abi3-win_amd64.whl and the encryption script used is contained in the encryption file (with the flag obsfuscated).
