# SatSale needs to connect to your bitcoin/lnd node,
# with the correct RPC port(s) as set in this config.

# Connecting through local host (see below if connecting to remote node):
host = "127.0.0.1"
rpcport = "8332"

# From ~/.bitcoin/bitcoin.conf
username = "bitcoinrpc"
password = "rpcpassword"

# Wallet (empty "" if your node has a single wallet, OR wallet name/path as shown in `biitcoin-cli listwallets`)
wallet = ""

# File in which API key will be stored
api_key_path = "SatSale_API_key"


#### Connect To Remote Node ####
# Can use SSH or TOR
# to tunnel/relay ports required to talk to the node via RPC (gRPC for lightning)

# SSH tunnel to node
# Make sure this command works `ssh HOST@IP -q -N -L 8332:localhost:8332`
# Use host = "127.0.0.1" and you will be able to see your node on 8332
tunnel_host = None  # "HOST@IP"

# or tor hidden service for RPC (see docs for how to set up), need onion:
tor_bitcoinrpc_host = None # e.g. "http://if...dwr.onion"
# and a tor proxy, default 127.0.0.1:9050 (for Tor Browser use "127.0.0.1:9150")
tor_proxy = None

#### Payment method ####
pay_method = "bitcoind"

#### Lightning ####
# Switch payment_method to lnd if you want to use lightning payments instead. And uncomment lnd_dir.
#pay_method = "lnd"

# To find (or copy from remote nodes) the macaroon and TLS certs
#lnd_dir = "~/.lnd/"

# lnd RPC port and lnd macaroon (uncomment)
#lnd_rpcport = "10009"
#lnd_macaroon = "admin.macaroon"


# Check for payment every xx seconds
pollrate = 15

# Payment expires after xx seconds
payment_timeout = 60*60

# Required confirmations for a payment
required_confirmations = 2

# Global connection attempts
connection_attempts = 3

# Generic redirect url after payment
redirect = "https://github.com/nickfarrow/satsale"

# Lightning Address
lightning_address = None

# DO NOT CHANGE THIS TO TRUE UNLESS YOU WANT ALL PAYMENTS TO AUTOMATICALLY
# BE CONSIDERED AS PAID.
free_mode = False
