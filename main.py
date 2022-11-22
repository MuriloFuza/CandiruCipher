from candiruCipher import CandiruCipher

candiruCipher = CandiruCipher()
messageEncrypted = candiruCipher.encrypt(message='texto qualquer', key='4,3,1,2')

print(messageEncrypted)

messageDecrypted = candiruCipher.decrypt(messageEncrypted=messageEncrypted, key='4,3,1,2')

print(messageDecrypted)
