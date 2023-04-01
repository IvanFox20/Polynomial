class Polynomial:
    coefs_count = None

    def __init__(self, *coefficients):
        self.coefs_dict = {}
        self.coefs_count = 1
        if coefficients.__len__() > 0:
            if isinstance(coefficients[0], int):
                degree = 0
                for coef_value in coefficients:
                    self.coefs_dict[degree] = coef_value
                    degree += 1
                self.__coefs_count__()
                self.__insignificant_remove__()
            elif isinstance(coefficients[0], list):
                degree = 0
                for coef_value in coefficients[0]:
                    self.coefs_dict[degree] = coef_value
                    degree += 1
                self.__coefs_count__()
                self.__insignificant_remove__()
            elif isinstance(coefficients[0], dict):
                self.coefs_dict = coefficients[0]
                self.__coefs_count__()
                self.__filling_missings__()
                self.__sort__()
                self.__insignificant_remove__()
            elif isinstance(coefficients[0], Polynomial):
                self.coefs_dict = coefficients[0].coefs_dict
                self.__coefs_count__()
                self.__insignificant_remove__()
        else:
            raise Exception("Invalid coefficients in Polynom")

    def degree(self):
        return self.coefs_count - 1

    def der(self, d=1):
        if d < 0:
            raise Exception("Degree can`t be less than 0")
        temp_pol = Polynomial(0)
        if d > 0:
            temp_pol.coefs_dict[d - 1] = self.coefs_dict[d] * d
        temp_pol.__temp_fix__()
        return temp_pol

    # Combining Polynomial Repair Methods
    def __temp_fix__(self):
        self.__coefs_count__()
        self.__sort__()
        self.__insignificant_remove__()
        self.__filling_missings__()
        self.__coefs_count__()

    def __sort__(self):
        self.coefs_dict = {coef_degree: coef_value for coef_degree, coef_value in sorted(self.coefs_dict.items())}

    def __coefs_count__(self):
        self.coefs_count = self.coefs_dict.__len__()

    # removal of insignificant coefficients
    def __insignificant_remove__(self):
        curr_coefs_size = self.coefs_count
        most_significant_degree = 0
        it = 0
        for coef_degree, coef_value in self.coefs_dict.items():
            if coef_value != 0:
                most_significant_degree = coef_degree
        most_significant_degree += 1
        while most_significant_degree < curr_coefs_size:
            del self.coefs_dict[most_significant_degree]
            most_significant_degree += 1
        self.__coefs_count__()

    # filling in the missing degree coefficients if argument is dictionary
    def __filling_missings__(self):
        curr_coefs_size = self.coefs_count
        curr_degree = 0
        while curr_coefs_size != 0:
            if curr_degree in self.coefs_dict:
                curr_coefs_size -= 1
                curr_degree += 1
            else:
                self.coefs_dict[curr_degree] = 0
                curr_degree += 1
        self.__coefs_count__()

    def __str__(self):
        answer = ""
        curr_degree = self.coefs_count - 1
        curr_coef = self.coefs_dict[curr_degree]
        if curr_degree == 0 and curr_coef == 0:
            answer += "0"
        if curr_coef != 0:
            sign = "-" if curr_coef < 0 else " "
            if abs(curr_coef) != 1:
                if curr_degree > 1:
                    answer += f" {sign}{abs(curr_coef)}x^{curr_degree}"
                elif curr_degree == 1:
                    answer += f" {sign}{abs(curr_coef)}x"
                else:
                    answer += f" {sign}{abs(curr_coef)}"
            else:
                if curr_degree > 1:
                    answer += f" {sign}x^{curr_degree}"
                elif curr_degree == 1:
                    answer += f" {sign}x"
                else:
                    answer += f" {sign}{abs(curr_coef)}"
        curr_degree -= 1
        while curr_degree >= 0:
            curr_coef = self.coefs_dict[curr_degree]
            if curr_coef != 0:
                sign = "-" if curr_coef < 0 else "+"
                if abs(curr_coef) != 1:
                    if curr_degree > 1:
                        answer += f" {sign} {abs(curr_coef)}x^{curr_degree}"
                    elif curr_degree == 1:
                        answer += f" {sign} {abs(curr_coef)}x"
                    else:
                        answer += f" {sign} {abs(curr_coef)}"
                else:
                    if curr_degree > 1:
                        answer += f" {sign} x^{curr_degree}"
                    elif curr_degree == 1:
                        answer += f" {sign} x"
                    else:
                        answer += f" {sign} {abs(curr_coef)}"

            curr_degree -= 1
        return answer

    def __repr__(self):
        answer = "Polynomial ["
        curr_degree = self.coefs_count - 1
        curr_coef = self.coefs_dict[curr_degree]
        answer += f"{curr_coef}"
        curr_degree -= 1
        while curr_degree >= 0:
            curr_coef = self.coefs_dict[curr_degree]
            answer += f", {curr_coef}"
            curr_degree -= 1
        answer += "]"
        return answer

    def __add__(self, other):
        temp_pol = Polynomial(self)
        if isinstance(other, Polynomial):
            for coef_degree, coef_value in other.coefs_dict.items():
                if coef_degree in self.coefs_dict:
                    temp_pol.coefs_dict[coef_degree] = self.coefs_dict[coef_degree] + coef_value
                else:
                    temp_pol.coefs_dict[coef_degree] = coef_value
        elif isinstance(other, int):
            if 0 in self.coefs_dict:
                temp_pol.coefs_dict[0] = self.coefs_dict[0] + other
            else:
                temp_pol.coefs_dict[0] = other
        temp_pol.__coefs_count__()
        temp_pol.__sort__()
        return temp_pol

    def __sub__(self, other):
        temp_pol = Polynomial(0)
        if isinstance(other, Polynomial):
            for coef_degree, coef_value in other.coefs_dict.items():
                if coef_degree in self.coefs_dict:
                    temp_pol.coefs_dict[coef_degree] = self.coefs_dict[coef_degree] - coef_value
                else:
                    temp_pol.coefs_dict[coef_degree] = coef_value
        elif isinstance(other, int):
            if 0 in self.coefs_dict:
                temp_pol.coefs_dict[0] = self.coefs_dict[0] - other
            else:
                temp_pol.coefs_dict[0] = other
        temp_pol.__temp_fix__()
        return temp_pol

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            for coef_degree, coef_value in other.coefs_dict.items():
                if coef_degree in self.coefs_dict:
                    if self.coefs_dict[coef_degree] != coef_value:
                        return False
                else:
                    return False
        elif isinstance(other, int):
            if not (0 in self.coefs_dict):
                return False
            elif self.coefs_count != 1:
                return False
            elif self.coefs_dict[0] != other:
                return False
        return True

    def __neg__(self):
        temp_pol = Polynomial(0)
        for coef_degree, coef_value in self.coefs_dict.items():
            temp_pol.coefs_dict[coef_degree] = -coef_value
        temp_pol.__temp_fix__()
        return temp_pol

    def __mul__(self, other):
        temp_pol = Polynomial(0)
        if isinstance(other, Polynomial):
            for other_coef_degree, other_coef_value in other.coefs_dict.items():
                for coef_degree, coef_value in self.coefs_dict.items():
                    if other_coef_value and coef_value:
                        multiplied_degree = other_coef_degree + coef_degree
                        multiplied_value = other_coef_value * coef_value
                        temp_pol += Polynomial({multiplied_degree: multiplied_value})
        elif isinstance(other, int):
            if 0 in self.coefs_dict:
                temp_pol.coefs_dict[0] = self.coefs_dict[0] * other
        temp_pol.__temp_fix__()
        return temp_pol

    def __call__(self, x):
        result = 0
        for coef_degree, coef_value in self.coefs_dict.items():
            result += coef_value * x ** coef_degree
        return result

    def __iter__(self):
        self.current_num = 0
        return self

    def __next__(self):
        if self.current_num <= self.degree():
            result = f"({self.current_num}, {self.coefs_dict[self.current_num]})"
            self.current_num += 1
            return result
        else:
            raise StopIteration

    pass
