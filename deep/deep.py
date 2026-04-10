# get the user answer for the following question
ans = input('What is the answer to the Great Question of Life, ' \
'the Universe and Everything? ')

#check if the user's answer is equal to 42 that accept different version
if ans == "42" or ans == "forty two" or ans == "forty-two" :
    print("Yes")

else:
    print("No")
