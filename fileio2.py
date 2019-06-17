f = open('test.txt', 'rt', encoding='utf-8')
text = f.read()
print(text)
text = f.read()
print('---', text, '---')

# position 단위는 byte
pos = f.tell()
print(pos)

# (offset, from_what)
#        , 0(맨앞에서)
f.seek(16, 0)
text = f.read()
print(text)

# (offset, from_what)
#        , 0(처음에서)
#        , 1(현재위치에서)
#        , 2(맨끝에서)
# text모드에서는 0만 허용
# 예외 : 끝으로 가는거 seek(0, 2)는 허용

# line 단위로 읽기
linenum = 0
f2 = open('fileio2.py', 'rt', encoding='utf-8')
while True:
    line = f2.readline()
    if line == '':
        break
    linenum += 1
    print('{0}:{1}'.format(linenum, line), end='')
f2.close()

f3 = open('fileio2.py', 'rt', encoding='utf-8')
lines = f3.readlines()
f3.close()
print(type(lines))
for linenum, line in enumerate(lines):
    print('{0}:{1}'.format(linenum, line), end='')

# with ~ as
with open('fileio2.py', 'rt', encoding='utf-8') as f2:
    for linenum, line in enumerate(f2.readlines()):
        print('{0}:{1}'.format(linenum, line), end='')

