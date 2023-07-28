import streamlit as st
import math

st.title("Caesar Cipher")

message = st.text_input("Enter the plaintext: ")
key = math.floor(st.number_input("Enter the secret key: "))

def CaesarCipher(message: str, key: int) -> str:
    if not message:
        return "Please enter a message."

    key %= 26
    val = list(message)

    for x in range(len(val)):
        if val[x].isupper():
            shifted = ord(val[x]) + key
            if shifted > ord('Z'):
                val[x] = chr((shifted - ord('A')) % 26 + ord('A'))
            else:
                val[x] = chr(shifted)
        elif val[x].islower():
            shifted = ord(val[x]) + key
            if shifted > ord('z'):
                val[x] = chr((shifted - ord('a')) % 26 + ord('a'))
            else:
                val[x] = chr(shifted)
    
    return "".join(val)

if st.button("Encode"):
    st.header(f"Cipher Text: {CaesarCipher(message, key)}")