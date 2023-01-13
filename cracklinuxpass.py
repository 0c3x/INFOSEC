#!/usr/bin/python3

import crypt, sys

if ( len(sys.argv) < 2  ):
        print(f"Modo de uso: {sys.argv[0]} wordlist.txt")
        raise SystemExit()

wl = sys.argv[1]
hash = input("Digite o hash completo: ")
salt = input("Digite o salt: ")

with open(wl) as mfile:
        for passw in mfile:
                passw = passw.strip()
                hashcry = crypt.crypt(passw, salt)
                if(hashcry == hash):
                        print(f"[+] Senha encontrada: {passw}")
                        raise SystemExit()
                else:
                        print(f"[+] Try: {passw}")
