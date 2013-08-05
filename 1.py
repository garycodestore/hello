import os

def foo(pathtosearch, filename):
	tempfile = os.path.join(pathtosearch, filename)
	if os.path.isfile(tempfile):
		return True
	else:
		return False


print foo(".", "hello")
