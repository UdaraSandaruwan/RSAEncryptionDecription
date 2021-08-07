import mysql.connector
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from flask import Flask
import server
app= Flask(__name__)


db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootpass",
        database="data"
    )
#generate Keys for client
keyPair = RSA.generate(3072)
pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()
privKeyPEM = keyPair.exportKey()


mycursor = db.cursor()
mycursor.execute("INSERT INTO clientKeys (clientPubKeyPEM,clientPrivKeyPEM) VALUES (%s,%s)",(pubKeyPEM, privKeyPEM))
db.commit()

server.generateServerKeys()#call function to generate keys for server
mycursor.execute("SELECT serverPubKeyPEM FROM serverKeys")
for i in mycursor:
    serverPubKey = i
    a = "".join(serverPubKey)
importedServerPubKey = RSA.importKey(a)#convert to ras Key

mycursor.execute("SELECT clientPubKeyPEM FROM clientKeys")
for i in mycursor:
    clientPubKey = i
    cPubKey = "".join(clientPubKey)
importedClientPubKey = RSA.importKey(cPubKey)#convert to ras Key
mycursor.execute("SELECT clientPubKeyPEM FROM clientKeys")
for i in mycursor:
    clientPvtKey = i
    clientPvtKey = "".join(clientPubKey)
encode_message = str(importedClientPubKey)
encryptor = PKCS1_OAEP.new(importedServerPubKey) #encryptor
encrypted = encryptor.encrypt(encode_message.encode())
encryptor1 = str(encryptor)
print("Encrypted:", encrypted)


mycursor = db.cursor()
mycursor.execute("INSERT INTO encriptedKeys (encriptedKey,keyNum) VALUES (%s,%s)", (encrypted, encryptor1))
db.commit()

mycursor = db.cursor()
mycursor.execute("SELECT serverPrivKeyPEM FROM serverKeys")
for i in mycursor:
    serverPvtKey = i
    serverPvtKey = str("".join(serverPvtKey))
mycursor = db.cursor()
mycursor.execute("SELECT encriptedKey FROM encriptedKeys")
for i in mycursor:
    encryptedClientsPubKey = i
importedServerPvtKey = RSA.importKey(serverPvtKey) #convert to ras Key

decryptor1 = PKCS1_OAEP.new(importedServerPvtKey)
decrypted = decryptor1.decrypt((encryptedClientsPubKey[0]))
server.secondEncription(decrypted)

finalPubKeyPEM , finalPrivKeyPEM = server.generateSecondKey()##call function to generate second key set

#api route
@app.route("/endTOEndEncryption")
def endTOEndEncryption():
    return {"endTOEndEncryption":["client public key:",str(clientPubKey),"client private key:",str(clientPvtKey),"server public key:",str(serverPubKey),"server private key:",str(serverPvtKey),"second public key for client :",str(finalPubKeyPEM),"second public key for client :",str(finalPrivKeyPEM)]}

if __name__ == "__main__":
    app.run(debug=True)