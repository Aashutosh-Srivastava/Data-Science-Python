# infinite loop using while example

story = ''  #empty string
while 'the end' not in story:
    line = input('enter a line:')
    story += line + '\n'
print('yeh rahi kahani')
print(story)
