# Vigenere Decoder/Encoder
This is the simple Python application for encoding/decoding text using the Vigener cipher.

Main trait is universality. Use `settings.json` or CMD to set direction (encode / decode), alphabet, ciphering iterations etc. (See [How to use](#how-to-use))

## How to use
You can use json-file with settings or set them using only CMD args

**To run program with json use flag `-j(--json) <path/to/json>`**

### Fields and flags
- `alphabet` (CMD: `-a` or `--alphabet`) - **ORDERED** string with **ALL** alphabet's chars 
- `key` (CMD: `-k` or `--key`) - value is string
- Data can be defined by 2 ways (**NOT BOTH**):
  - `data` (CMD: `-d` or `--data`) - string with data that we want to encode/decode
  - `dataPath` (CMD: `-dp` or `--dataPath`) - path to file with data
- Cryptographer direction:
  - json - `direction`:
    - `1` - encode
    - `-1` - decode
  - CMD:
    - `-ec` or `--encode`
    - `-dc` or `--decode`
- `iterations` (CMD: `-i` or `--iterations`) - number that defines iterations' count which algorithm must be repeated on one data