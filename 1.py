import os

def foo(pathtosearch, filename):
	tempfile = os.path.join(pathtosearch, filename)
	if os.path.isfile(tempfile):
		return True
	else:
		return False

def foo2(pathname):
	dirlist = os.listdir(pathname)
	return dirlist
print foo2(".")
