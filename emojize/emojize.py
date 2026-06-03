"""
Prompt the user for str in english.
Output the emojize version of that str ,converting any codes(or aliases) therein
to their corresponding emoji. 
"""
import emoji

def main():
    str = input('Input: ')
    print(emoji.emojize(str,language='alias'))

main()