# You can use a midi sequencer to generate the MIDI file of the notes you play in muted .io and this program can convert it into numerical file by reading each byte and converting it to binary
# header  ,track ID , BPM all are already inside the file 
# 


from google.colab import files    #Colab-ൽ File Upload Library Import ചെയ്യുന്നു

# Upload MIDI file
uploaded = files.upload()

filename = next(iter(uploaded))    #Dictionary-യിലെ keys iterate ചെയ്യാൻ ഉപയോഗിക്കുന്നു.

with open(filename, "rb") as f:
    data = f.read()              #File-ലെ എല്ലാ bytes-ഉം വായിക്കുന്നു.

array_name = filename.split(".")[0]   #Array Name ഉണ്ടാക്കുന്നു

print(f"\nflash unsigned char {array_name}[{len(data)}] = {{")

for i, byte in enumerate(data):
    if i % 16 == 0:
        print("    ", end="")              #ഓരോ 16 Byte കഴിഞ്ഞ് Indentation കൊടുക്കുന്നു

    print(byte, end="")

    if i != len(data) - 1:
        print(",", end="")

    if (i + 1) % 16 == 0:
        print()

print("\n};")
