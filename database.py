import mysql.connector
db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootpass",
        database="data"
)
#create data bases
mycursor = db.cursor()
mycursor.execute("CREATE TABLE serverKeys(keyId int PRIMARY KEY AUTO_INCREMENT, serverPubKeyPEM TEXT, serverPrivKeyPEM TEXT)")
mycursor.execute("CREATE TABLE clientKeys(keyId int PRIMARY KEY AUTO_INCREMENT, clientPubKeyPEM TEXT, clientPrivKeyPEM TEXT)")
mycursor.execute("CREATE TABLE finalKeys(keyId int PRIMARY KEY AUTO_INCREMENT, finalPubKeyPEM TEXT, finalPrivKeyPEM TEXT)")
mycursor.execute("CREATE TABLE encriptedKeys(keyId int PRIMARY KEY AUTO_INCREMENT, encriptedKey BLOB, keyNum TEXT)")
mycursor.execute("CREATE TABLE decryptKeys(keyId int PRIMARY KEY AUTO_INCREMENT, decriptedKey BLOB, keyNum TEXT)")
