from Polynomial import Polynomial

# invalid_pol = Polynomial() # this will throw an exception
zero_pol = Polynomial(0)
dictionary_pol = Polynomial({0: 5, 1: 6, 4: 7, 5: 0, 6: 0})
set_pol = Polynomial(1, 2, 3, 0, 0, 0)
list_pol = Polynomial([4, 5, 6, 0, 0, 0])
another_pol_pol = Polynomial(Polynomial(10, 11, 12))

print("zero_pol = ", zero_pol)
print("dictionary_pol = ", dictionary_pol)
print("set_pol = ", set_pol)
print("list_pol = ", list_pol)
print("another_pol_pol = ", another_pol_pol)
print("repr of set_pol = ", repr(set_pol))
print("repr of dictionary_pol = ", repr(dictionary_pol))

add_pol1 = Polynomial(1, 2, 3)
add_pol2 = Polynomial(1, 1, 1)

print("Pol1 + Pol2 = ", add_pol1 + add_pol2)

sub_pol1 = Polynomial(1, 2, 3)
sub_pol2 = Polynomial(2, 1, 4)

print("Pol1 - Pol2 = ", sub_pol1 - sub_pol2)

eq_pol1 = Polynomial(1, 2, 3)
eq_pol2 = Polynomial(1, 2, 3, 4)
eq_pol3 = Polynomial(1)

print("eq_pol1 == eq_pol2") if eq_pol1 == eq_pol2 else print("eq_pol1 != eq_pol2")
print("eq_pol1 == Polynomial(1, 2, 3)") if eq_pol1 == Polynomial(1, 2, 3) else print("eq_pol1 != Polynomial(1, 2, 3)")
print("eq_pol3 == 1") if eq_pol3 == 1 else print("eq_pol3 != 1")


unary_pol = Polynomial(1, 2, 3)
print(f"-unary_pol = ", -unary_pol)

degree_pol = Polynomial(0, 1, 2, 3)
print("degree of degree_pol1 = ", degree_pol.degree())

der_pol = Polynomial(1, 2, 3, 4)

print("der_pol 1st degree derivative = ", der_pol.der())
print("der_pol 2nd degree derivative = ", der_pol.der(2))
print("der_pol 3rd degree derivative = ", der_pol.der(3))
# print("der_pol 4th degree derivative = ", der_pol.der(4)) # this will throw an exception

func_pol = Polynomial(1, 2, 3)

print("Polynomial value at point 0 = ", func_pol(0))
print("Polynomial value at point 1 = ", func_pol(1))
print("Polynomial value at point 2 = ", func_pol(2))


mul_pol1 = Polynomial(1, 2, 3)
mul_pol2 = Polynomial(1, 1, 1)
mul_pol3 = Polynomial(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
mul_pol4 = Polynomial(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("mul_pol1 * mul_pol2 = ", mul_pol1 * mul_pol2)
print("mul_pol3 * mul_pol4 = ", mul_pol3 * mul_pol4)

iter_pol1 = Polynomial(1, 2, 3, 4, 5, 6, 7)

print("First iteration of iter_pol1:")
for res in iter_pol1:
    print(res)

print("Second iteration of iter_pol1:")
for res in iter_pol1:
    print(res)
