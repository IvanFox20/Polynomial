from Polynomial import Polynomial

dictionary_pol = Polynomial({0: 5, 1: 6, 4: 7, 5: 0, 6: 0})
set_pol = Polynomial(1, 2, 3, 0, 0, 0)
list_pol = Polynomial([4, 5, 6, 0, 0, 0])
another_pol_pol = Polynomial(Polynomial(10, 11, 12))

print("dictionary_pol ", dictionary_pol)
print("set_pol ", set_pol)
print("list_pol ", list_pol)
print("another_pol_pol ", another_pol_pol)
print("repr of set_pol", repr(set_pol))
print("repr of dictionary_pol", repr(dictionary_pol))

add_pol1 = Polynomial(1, 2, 3)
add_pol2 = Polynomial(1, 1, 1)
print("Pol1 + Pol2 = ", add_pol1 + add_pol2)
sub_pol1 = Polynomial(1, 2, 3)
sub_pol2 = Polynomial(2, 1, 4)
print("Pol1 - Pol2 = ", sub_pol1 - sub_pol2)
