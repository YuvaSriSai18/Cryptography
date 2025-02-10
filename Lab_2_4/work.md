### Workflow
---
1. Plain Text and the Key of Same length will be given in a list format
    - Here we use token_bytes for generating a secret key and making a list initially
2. Initialize a list with number 0 to 255
3. Here there will be 2 functions 
    - Key Scheduling Algorithm (KSA)
    - Pseudo-Random Generation Algorithm (PRGA)
4. In KSA we initialize the list and will scramble (re-arranging) the list with some formulas
5. The scrambled list will then sent to **PRGA** for key generation ,as it does some calculations like mod or swapping ultimately we will  be returning the **key list** 
6. 