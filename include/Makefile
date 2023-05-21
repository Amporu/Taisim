
default:
	g++ -shared -c -fPIC sparkverse.cpp -o sparkverse.o
	g++ -shared -Wl,-soname libspark.so -o sparkverse.so sparkverse.o