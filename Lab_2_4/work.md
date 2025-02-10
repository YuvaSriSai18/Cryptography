### **Simple Workflow of RC4 Cipher**  
---

- **Input the Plain Text and Key**  
   - We provide a **plain text message** (the text we want to encrypt).  
   - We generate a **random key** using `token_bytes`, ensuring it has the same length as needed.  

- **Initialize a List**  
   - We create a list of numbers **from 0 to 255**. This list will be **scrambled** using the key.  

- **Use Two Functions for Encryption**  
   - **Key Scheduling Algorithm (KSA)** → Scrambles the list using the key.  
   - **Pseudo-Random Generation Algorithm (PRGA)** → Generates a key stream to encrypt the message.  

- **Key Scheduling Algorithm (KSA)**  
   - We mix (shuffle) the list using the key.  
   - This ensures that the encryption is different each time.  

- **Generate Keystream Using PRGA**  
   - The scrambled list is used to generate a **random keystream** (a sequence of numbers).  
   - These numbers are used to encrypt the plain text.  

- **Encrypt the Plain Text**  
   - Each letter in the plain text is **XORed** (mathematically combined) with the corresponding keystream value.  
   - This produces the **cipher text** (encrypted text).  

- **Decrypt Using the Same Process**  
   - Since XOR is **reversible**, running the process again **decrypts** the text back to its original form.  
