class Polynomial:
    coefs_count = None

    def __init__(self, *coefficients):
        self.coefs_dict = {}
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

    def __sort__(self):
        self.coefs_dict = {coef_degree: coef_value for coef_degree, coef_value in sorted(self.coefs_dict.items())}

    def __coefs_count__(self):
        self.coefs_count = self.coefs_dict.__len__()

    # removal of insignificant coefficients
    def __insignificant_remove__(self):
        curr_coefs_size = self.coefs_count
        most_significant_degree = 0
        it = 0
        while it < curr_coefs_size:
            if self.coefs_dict[it] > 0:
                most_significant_degree = max(most_significant_degree, it)
            it += 1
        it = most_significant_degree + 1
        while it < curr_coefs_size:
            del self.coefs_dict[it]
            it += 1
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

    def __full_cleaning__(self):
        self.__coefs_count__()
        self.__filling_missings__()
        self.__sort__()
        self.__insignificant_remove__()

    def __str__(self):
        answer = ""
        curr_degree = self.coefs_count - 1
        curr_coef = self.coefs_dict[curr_degree]
        if curr_coef != 0:
            sign = "-" if curr_coef < 0 else " "
            if curr_degree > 1:
                answer += f" {sign} {abs(curr_coef)}x^{curr_degree}"
            elif curr_degree == 1:
                answer += f" {sign} {abs(curr_coef)}x"
            else:
                answer += f" {sign} {abs(curr_coef)}"
        curr_degree -= 1
        while curr_degree >= 0:
            curr_coef = self.coefs_dict[curr_degree]
            if curr_coef != 0:
                sign = "-" if curr_coef < 0 else "+"
                if curr_degree > 1:
                    answer += f" {sign} {abs(curr_coef)}x^{curr_degree}"
                elif curr_degree == 1:
                    answer += f" {sign} {abs(curr_coef)}x"
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
        temp_pol = Polynomial(0)
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

#  Не работает, добавить full cleaning
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
        temp_pol.__coefs_count__()
        temp_pol.__sort__()
        return temp_pol

    pass
