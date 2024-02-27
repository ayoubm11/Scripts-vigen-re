def vigenere(c, cle):
    indice_cle = 0
    msg_code = ""

    for i in range(0,len(c)):
            if 'A' <= c[i] <= 'Z':
                  msg_code += chr ((((ord(c[i]) - ord('A') + ord(cle[indice_cle]) - ord('A') )) %26) + ord('A'))
                  indice_cle = (indice_cle + 1) % len(cle)

            else:
                  msg_code += c[i]
    return msg_code

def decode_vigenere(c, cle):
    indice_cle = 0
    msg_code = ""

    for i in range(0,len(c)):
            if 'A' <= c[i] <= 'Z':
                  msg_code += chr ((((ord(c[i]) - ord('A') - ord(cle[indice_cle]) - ord('A') )) %26) + ord('A'))
                  indice_cle = (indice_cle + 1) % len(cle)

            else:
                  msg_code += c[i]
    return msg_code
            #BONJOUR MES AMIES EST CE QUE VOUS ALLEZ BIEN
print(vigenere('BONJOUR MES AMIES EST CE QUE VOUS ALLEZ BIEN', 'PYT'))
print(decode_vigenere('QMGYMNG KXH YFXCL TQM RC JJC ODSL PJETX UXCG', 'PYT'))

#QMGYMNG KXH YFXCL TQM RC JJC ODSL PJETX UXCG