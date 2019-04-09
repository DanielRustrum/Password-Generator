import random, json, hashlib, requests



def hashGen():
    password = ''.join(random.choices(characterList, k=passwordLength))
    sha = hashlib.sha1()
    truePass = (password + secKey).encode('utf-8')
    sha.update(truePass)
    return (sha.hexdigest(), password)

def checkIfSecure(genhash):
    request = requests.get("https://api.pwnedpasswords.com/range/" + genhash[0:5])
    hashList = (request.text).split("\n")
    for hashItem in hashList:
        if str(genhash).upper()[5:] == hashItem.split(":")[0]:
            return False
    return True

if __name__ == "__main__":
    try:
        passpassword = "2"
        havePass = False
        characterList = ""
        passwordLength = 10

        secKey = input("Static Password (Hit Enter to not use a static password): ")

        with open("./config.json") as config:
            jsonConfig = json.load(config)
            characterList = jsonConfig["characters"]
            passwordLength = jsonConfig["length"]

        while not(havePass):
            (shaHash, password) = hashGen()
            if checkIfSecure(shaHash):
                havePass = True
                break
            print("Re-attepmting: {} not valid".format(password))
        print("Found: {}".format(password))
    except:
        print("\n\nsee you later cowboy")