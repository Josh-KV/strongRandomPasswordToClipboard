#!/usr/bin/env python3
import random
import subprocess

def randStringGenerator(length, charSet): # Generate random string of given length from given charSet
  password = ""
  for i in range(length):
    randChar = charSet[random.randrange(len(charSet))]
    password += randChar
  return password

def rockyouCheck(string): # Check if given string is in rockyou.txt
  with open('rockyou.txt', encoding="utf-8", errors="ignore") as rockyou:
    for weakPassLine in rockyou:
      if string in weakPassLine :
        return False
  return True

def charCheck(string, checkChars): # given a string and set of chars, check if string contains any of chars in set
  for char in string:
    if char in checkChars:
      return True
  return False

def writeToClipboard(output): # output sent to system clipboard
  process = subprocess.Popen('pbcopy', stdin=subprocess.PIPE)
  process.communicate(output.encode('utf-8'))

def main():
  ##############
  # Parameters #
  ##############
  length = 32
  lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
  upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numbers = "0123456789"
  specialChars = "!@#$%^&*()[]?"
  charSet = lowerCaseLetters+upperCaseLetters+numbers+specialChars

  #####################################
  # Create and verify strong password #
  #####################################
  password = randStringGenerator(length,charSet)
  strongCheck = False
  while not strongCheck:
    if charCheck(password,lowerCaseLetters) and charCheck(password,upperCaseLetters) and charCheck(password,numbers) and charCheck(password,specialChars): # (Uncomment for common password check) # and not rockyouCheck(password):
      strongCheck = True
    else: # if tests fail, regen password and test again
      password = randStringGenerator(length,charSet)
  writeToClipboard(password)

if __name__ == "__main__":
  main()
