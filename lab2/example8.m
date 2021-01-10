x = 2;
y = 3.5;
z = "foo";
t = [1, 2, 3];
v = [2, 3, 4];
u = [4, 6, 7, 8];
a = [[1, 1], [2, 2]];
b = [[3, 3], [4, 4]];
c = [[1, 2, 3], [4, 5, 6]];

# Arithmetic operations with two integers:
e = x + x;
e = x - x;
e = x * x;
e = x / x;

#Arithmetic operations with two floats
f = y + y;
f = y - y;
f = y * y;
f = y / y;

# Arithmetic operations with integer and float:
d = x + y;
d = y - x;
d = x * y;
d = y / x;

# Arithmetic operations with two strings:
g = z + z;
g = z - z;
g = z * z; 
g = z / z;

# Arithmetic operations with string and some other type:
h = z + x;
h = z - y;
h = z * x;
h = z / y;

# Arithmetic operations for two vectors/arrays:
i = t + v;
i = t .+ v;
i = a + b;
i = a .+ b;

# Arithmetic operations with two vectors/arrays with bad dimensions:
j = a .+ c;
j = t .+ u;


