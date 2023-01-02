strongRandomPasswordToClipboard
---
Python script to quickly generate a password and send to system clipboard without revealing text on-screen.

Details
---
This script creates a 32 character password containing at least one (to be increased) of each of the following:
 - uppercase letter
 - lowercase letter
 - number
 - special character

The characters are selected using the [Python Random Module](https://docs.python.org/3/library/random.html).

Once a password has been generated, the script checks to make sure that the password contains an upper and lowercase letter, as well as a number and a special character. If the password does not satisfy these requirements, a new password is generated until the requirements are met.

Once a password that meets the requirements is generated, the password is copied to the system clipboard using the [Python Subprocess Module](https://docs.python.org/3/library/subprocess.html). This means that the password is never shown on-screen unless the user pastes it somewhere other than an obfuscated password field, giving the user discretion over whether the password is ever visable on their screen.

Improvements
---
- The generated password can be compared against known password lists.
  - This functionality is available if you store the script in the same directory as a password list and uncomment the `rockyouCheck(password)` condition. However, a much better hash table implementation may actually be worth using especially if the password length is small.
- Improve randomness source
  - physical source like a [HRNG](https://en.wikipedia.org/wiki/Hardware_random_number_generator#:~:text=In%20computing%2C%20a%20hardware%20random,by%20means%20of%20an%20algorithm.)
- Could be integrated into a password manager program
  - manager program oversees encrypted usernames/passwords (could use OpenSSL to perform aes-256 encryption/decryption for example)
  - the encrypted data could be stored locally or in cloud storage (as long as encryption standard is kept up to date)
