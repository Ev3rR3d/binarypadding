def pad_shellcode(shellcode, block_size=16):
    padding_len = block_size - (len(shellcode) % block_size)
    padding = bytes([padding_len] * padding_len)
    return shellcode + padding

user_input = input("Digite o shellcode em formato hexadecimal (com espaços entre bytes): ")

shellcode = bytes.fromhex(user_input.replace(" ", ""))

padding_len = 16 - (len(shellcode) % 16)

padding = bytes([padding_len] * padding_len)

padded_shellcode = shellcode + padding

formatted_output = ", ".join(f"0x{byte:02X}" for byte in padded_shellcode)

print("Shellcode com padding:", formatted_output)
