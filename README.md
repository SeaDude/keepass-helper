## KeePass (or any desktop pw manager?) Helper

### WARNING:

**This script will generate password files in plain text. ITS NOT SECURE.**

I needed help remembering my full KeePass Master Password. I could remember parts of it and which keys were likely used. So I built these scripts to help out!

**AND IT WORKED!!**

## Prerequisites

This is not a "password cracker"! You must know the beginning of the password **and** a set of characters that the remaining password could entail.

## How to use

0. Install `requirements.txt` using `pip install -r requirements.txt`.

1. Open `permutations.py` and enter the beginning portion of the password you remember as the `rem_pw` variable.

2. Enter a separate set of characters for the **`first` through nth positions**. 
- All possible permutations of these characters will be concatenated with `rem_pw` and written to a file to be used by the `pw_prog.py` program.

**Example:**
If you think the `first` position after the `rem_pw` portion was either a 1, 2, 3 or 4, set the `first` array as the strings shown below. 

Perform the same for each additional set.

**NOTE:** The longer the set and the more sets you have will increase the numbers of permutations. 

```python

first = ['1', '2', '3', '4']
second = ['!', '@', '#', '$']
third = ['1', '2', '3', '4']
fourth = ['!', '@', '#', '$']
fifth = ['1', '2', '3', '4']
sixth = ['!', '@', '#', '$']

```

3. Execute the `permutations.py` Python script
- A `output.txt` file with all permutations will be generated in the same folder.

4. Open the `pw_prog.py` and enter values for `keepass_app` (the actual KeePass `.exe`) and `keepass_db` (the KeePass database you want open).
a. **OPTIONAL:** Enter any keywords to ignore. Of use only if you have some header, etc.

5. Run `pw_prog.py`!
- **NOTE:** You cannot work on the computer while the program is running. This is where the `counter` variable comes into play. 