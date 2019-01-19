"""
A simple program written in python that translates words to pig latin!
"""

endFix = 'ay'   # Ending prefix

original = input('Enter a word:')   # User input

# if/else statement that translates program to pig latin
if len(original) > 0 and original.isalpha():
  word = original.lower() 				                 # sets original to lowercase
  firstLetter = word[0]   							          # takes first letter
  new_word = word + firstLetter + endFix	       # translates to pig latin
  new_word = new_word[1:len(new_word)]
  print (new_word)		 # outputs pig latin

else:		# else if input is empty
  print ('empty')
