# textmode 가 default: t
f = open('test.txt', 'wt', encoding='utf-8')
writesize = f.write('안녕하세요\n파이썬입니다.')
f.close()
print(writesize)

# binary mode : b
f = open('test2.txt', 'wb')
writesize = f.write(bytes('안녕하세요\n파이썬입니다.', encoding='utf-8'))
f.close()
print(writesize)

# read test
f = open('test.txt', 'rt', encoding='utf-8')
text = f.read()
f.close()
print(text)

# binary read : copy file
fsrc = open('python.jpg', 'rb')
data = fsrc.read()
fsrc.close()

print(type(data))

fdest = open('python2.jpg', 'wb')
fdest.write(data)
fdest.close()
