import hashlib

class Encoder:

    def encode(self, string):
        result = ""
        try:
            encriptado = hashlib.md5(string.encode())
            result = encriptado.hexdigest()
        except Exception as ex:
            print(ex)

        return result


    def decode(self, string, claveMD5):

        if hashlib.md5(string.encode()).hexdigest() == claveMD5:
            return True
        else:
            return False

print(Encoder().encode("1234a#"))