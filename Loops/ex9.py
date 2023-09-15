story = ''
while True:
    line = input('>>>')
    if not line:
        break
    story += line + '\n'
print('Here ! you go')
print(story)
    