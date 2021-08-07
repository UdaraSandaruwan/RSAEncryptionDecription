import mysql.connector
from Crypto.PublicKey import RSA


"""
*
****************************** Generate and write rsa keys for server ***********************
*

"""
db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootpass",
        database="data"
)
mycursor = db.cursor()
def generateServerKeys():
    keyPair = RSA.generate(3072)
    serverPubKey = keyPair.publickey()
    serverPubKeyPEM = serverPubKey.exportKey()
    serverPrivKeyPEM = keyPair.exportKey()

    mycursor = db.cursor()
    mycursor.execute("INSERT INTO serverKeys (serverPubKeyPEM,serverPrivKeyPEM) VALUES (%s,%s)",
                     (serverPubKeyPEM, serverPrivKeyPEM))
    db.commit()
    mycursor.execute("SELECT * FROM serverKeys")
    for i in mycursor:
        pass


"""
*
********************************* decrypt clients public key generate the second public key***********************
*
"""


def secondEncription(decrypted):
    mycursor = db.cursor()
    print('Decrypted:', decrypted)

    mycursor.execute("INSERT INTO decryptKeys (decriptedKey,keyNum) VALUES (%s,%s)", (decrypted, "aaa"))
    db.commit()


def generateSecondKey():
    keyPair = RSA.generate(3072)
    serverPubKey = keyPair.publickey()
    serverPubKeyPEM = serverPubKey.exportKey()
    serverPrivKeyPEM = keyPair.exportKey()

    mycursor = db.cursor()
    mycursor.execute("INSERT INTO finalKeys (finalPubKeyPEM,finalPrivKeyPEM) VALUES (%s,%s)",
                     (serverPubKeyPEM, serverPrivKeyPEM))
    db.commit()
    mycursor.execute("SELECT finalPubKeyPEM FROM finalKeys")
    for i in mycursor:
        finalPubKeyPEM = i
    mycursor.execute("SELECT finalPrivKeyPEM FROM finalKeys")
    for i in mycursor:
        finalPrivKeyPEM = i
    return finalPubKeyPEM,finalPrivKeyPEM






