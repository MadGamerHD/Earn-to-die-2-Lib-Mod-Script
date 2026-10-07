import re

OG = "/storage/emulated/0/Download/libEarnToDie2.so"
DIFF = "/storage/emulated/0/Download/libEarnToDie2.ini"
OUT = "/storage/emulated/0/Download/libEarnToDie2_mod.so"

# Read original file
with open(OG, "rb") as f:
    data = bytearray(f.read())

# Read diff
with open(DIFF, "r", encoding="utf-8") as f:
    text = f.read()

# Find:
# Offset: 0x12345678
# ...
# MOD:  AA BB CC DD
pattern = re.compile(
    r"Offset:\s*0x([0-9A-Fa-f]+).*?"
    r"MOD:\s*([0-9A-Fa-f ]+)",
    re.DOTALL
)

matches = pattern.findall(text)

print("Found", len(matches), "patches")

patched_bytes = 0

for offset_hex, mod_hex in matches:
    offset = int(offset_hex, 16)

    # Remove extra whitespace
    mod_hex = " ".join(mod_hex.split())

    new_bytes = bytes.fromhex(mod_hex)

    # Make sure the patch fits
    if offset + len(new_bytes) > len(data):
        print(f"Skipping 0x{offset:X}: outside file")
        continue

    # Apply MOD bytes
    data[offset:offset + len(new_bytes)] = new_bytes

    patched_bytes += len(new_bytes)

    print(
        f"Patched 0x{offset:08X} "
        f"({len(new_bytes)} bytes)"
    )

# Write new file
with open(OUT, "wb") as f:
    f.write(data)

print()
print("========== DONE ==========")
print("Patches:", len(matches))
print("Bytes changed:", patched_bytes)
print("Created:")
print(OUT)