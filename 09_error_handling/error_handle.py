# METHOD-1
file = open('youtube.txt', 'w')

try:
    file.write('Chai Aur Code')
finally:
    file.close()

# METHOD-2
with open('youtube_1.txt', 'w') as file:
    file.write('Chai Aur Code...')