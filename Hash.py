import hashlib
frase = ('Aqui deve ser inserida a sua frase')
sha256 = ("valor sha256 da frase")
MD5 = ("valor MD5 da frase")
hash_sha256 = hashlib.sha256(frase.encode()).hexdigest()
hash_md5 = hashlib.md5(frase.encode()).hexdigest()
if hash_sha256 == sha256 and hash_md5 == MD5 :
    print("Para a seguinte frase: {}". format(frase))
    print("SHA256 e MD5 corretos")

if hash_sha256 == sha256 and hash_md5 != MD5 :
    print("Para a seguinte frase: {}". format(frase))
    print("Somente SHA256 correto")

if hash_sha256 != sha256 and hash_md5 == MD5 :
    print("Para a seguinte frase: {}". format(frase))
    print("Somente MD5 correto")

if hash_sha256 != sha256 and hash_md5 != MD5 :
    print("Para a seguinte frase: {}". format(frase))
    print("Nenhum dos dois corretos")