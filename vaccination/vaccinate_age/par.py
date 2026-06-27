file = open('pars', 'w')

count = 0
for i in range(10):
    file.write('{}\n'.format(i))
    count += 1
print(count)

file.close()
