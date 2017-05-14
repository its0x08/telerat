def gftp_decrypt_passwd(encrypted):
    try:

        if '$' not in encrypted:
            exit()
        bit = map(ord, encrypted)
        decrypted = []
        for i in range(1, len(bit), 2):
            if ((bit[i] & 0xc3) != 0x41 or (bit[i+1] & 0xc3) != 0x41):
                return encrypted
            decrypted.append(chr(((bit[i] & 0x3c) << 2) + ((bit[i+1] & 0x3c) >> 2)))
        return "".join(decrypted)
    except Exception:
        print str(Exception)
if __name__ == "__main__":
    print"passwd: %s\n" % (gftp_decrypt_passwd(raw_input("hash: ")))
   
