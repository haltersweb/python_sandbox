fileobj = open('../python_sandbox/files/basic_text.txt')
contents = fileobj.read()
print(contents[:10])
fileobj.close()