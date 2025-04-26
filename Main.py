from binance.client import Client

# Inserisci qui le tue API Key e Secret
api_key = 'G9YPk5NuUDaDBs1VnqsFiwBBQpmlJKzPQqN2fwgVi1iOUpG7mqiON4m1H5caFUJA'
api_secret = 'Qqtq5ihtsvBk97j4MkorZD2G7wFMPoxuFrkoGC3GbpS25Xr1P8KnxdSCK4upL2IC'

# Connessione a Binance
client = Client(G9YPk5NuUDaDBs1VnqsFiwBBQpmlJKzPQqN2fwgVi1iOUpG7mqiON4m1H5caFUJA, Qqtq5ihtsvBk97j4MkorZD2G7wFMPoxuFrkoGC3GbpS25Xr1P8KnxdSCK4upL2IC)

# Controlliamo il saldo dell'account
account_info = client.get_account()
print("Saldo disponibile:")
for balance in account_info['balances']:
    if float(balance['free']) > 0:
        print(f"{balance['asset']}: {balance['free']}")
