

saldo = 100.0
debito = 50.0
credito = 1200.0

print(f"Saldo atual: R$ {saldo}")

saldo = saldo - debito + credito

print(f"Saldo atual: R$ {saldo}")

if saldo <0:
    print("Conta estourada!")
    print(f"Saldo atak: R$ {saldo}")

else:
    print("Conta OK!")