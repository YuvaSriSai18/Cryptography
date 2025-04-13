from py_ecc.bls import G2ProofOfPossession as bls
from py_ecc.optimized_bls12_381 import curve_order
import os

NUM_CLIENTS = 3

clients = []
for i in range(NUM_CLIENTS):
    sk = int.from_bytes(os.urandom(32), 'big') % curve_order
    pk = bls.SkToPk(sk)
    clients.append({'id': i + 1, 'sk': sk, 'pk': pk})

message = b"Secure message from clients"    
for client in clients:
    client['signature'] = bls.Sign(client['sk'], message)
    print(f"Client {client['id']} Public Key: {client['pk'].hex()}")
    print(f"Client {client['id']} Signature: {client['signature'].hex()}\n")

print("🔍 Verifying individual signatures...")
for client in clients:
    valid = bls.Verify(client['pk'], message, client['signature'])
    print(f"Client {client['id']} Signature Valid? {valid}")

print("\n📦 Aggregating signatures and public keys...")
agg_signature = bls.Aggregate([c['signature'] for c in clients])
agg_pubkeys = [c['pk'] for c in clients]

is_valid_agg = bls.AggregateVerify(agg_pubkeys, [message]*NUM_CLIENTS, agg_signature)
print(f"\n✅ Aggregated Signature Valid? {is_valid_agg}")
