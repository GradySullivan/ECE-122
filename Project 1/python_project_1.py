import math

def main():
    # ECE 122
    # Project #1
    # Grady Sullivan

    def my_quad_equation():
        a = float(input("Enter value for a: "))
        b = float(input("Enter value for b: "))
        c = float(input("Enter value for c: "))  # user enters inputs for a,b,and c
        astr = str(a)  # convert float to string
        bstr = str(b)
        cstr = str(c)
        print("\n")
        if a == 1: astr = ''  # if a or b is equal to one (or negative 1), remove the number before x
        if b == 1: bstr = ''
        if a == -1: astr = '-'
        if b == -1: bstr = '-'
        if b >= 0: bstr = '+' + bstr  # the + or minus is based on the user's input
        if c >= 0: cstr = '+' + cstr
        print("Equation is: f(x)=" + astr + "x**2" + bstr + "x" + cstr + "\n")
        return a, b, c

    def evaluate_quad_equation(num1, num2, num3):
        x = float(input("Enter Value for x: "))
        answer = num1 * x ** 2 + num2 * x + num3  # calculate f(x)
        answer = str(answer)
        print("f(" + str(x) + ")=" + answer)
        extremeX = (-1 * num2) / (2 * num1)  # vertex equation
        extremeY = num1 * extremeX ** 2 + num2 * extremeX + num3
        max_min = 2 * num1
        return extremeX, extremeY, max_min

    def compute_discriminant(num1, num2, num3):
        d = (b ** 2) - (4 * a * c)  # calculate discriminant
        sol = 0
        return d, sol

    def factorize_form(num1, num2, num3, num4):
        if sol == 0:
            ff = (str(a) + "*(x" + str(x1_str) + ")**2")
        else:
            ff = (str(a) + "*(x" + str(x1_str) + ")(x" + str(x2_str) + ")")
        return ff

    ###########################################################

    # Task 1

    print("Welcome to Quadratic Solver for f(x)=ax**2+bx+c\n")
    a, b, c = my_quad_equation()
    temp = input("\nPress Enter to continue...")  # wait

    # Task 2

    x, y, max_min = evaluate_quad_equation(a, b, c)  # call function to input x into quadratic
    temp = input("\nPress Enter to continue...")  # wait
    if x == -0.0:  # get rid of -0
        x = 0.0
    # Task 3

    if max_min < 0:  # prints out correct statement depending on if vertex is a max or min
        print("f(x) has a maximum at x0=" + str(x) + " with value f(x0)=" + str(y))
    else:
        print("f(x) has a minimum at x0=" + str(x) + " with value f(x0)=" + str(y))
    temp = input("\nPress Enter to continue...")  # wait

    # Task 4

    print("Solving for f(x)=0")
    d, sol = compute_discriminant(a, b, c)
    if math.isclose(d, 0, abs_tol=1e-9):
        d = 0
    print("Discriminant is " + str(d))

    if d < 0:  # determines which statement to print for solutions
        q1 = -1 * b / (2 * a)
        q2 = abs(math.sqrt(abs(d)) / (2 * a))
        x1_str = (str(q1) + "+" + str(q2) + "j")
        x2_str = (str(q1) + "-" + str(q2) + "j")
        answ_1 = str(q1) + '+'

        if q2 == 1:
            print("Complex solutions are (j) and (-j)")
        elif q1 != 0:
            print("Complex solutions are (" + str(q1) + "+" + str(q2) + "j) and (" + str(q1) + "-" + str(q2) + "j)")
        else:
            print("Complex solutions are (" + str(q2) + "j) and (-" + str(q2) + "j)")
    elif d == 0:
        sol = (-1 * b) / (2 * a)  # calculates when only one solution
        x1 = sol
        x1_str = str(x1)
        print("One real solution: " + str(sol))
        ff = factorize_form(a, x1_str, x2_str, d)  # Task 7
        print("Factorize form is: f(x)=" + ff)
    else:
        sqrt_d = math.sqrt(d)
        x1 = (-1 * b + sqrt_d) / (2 * a)  # calculates both solutions
        x2 = (-1 * b - sqrt_d) / (2 * a)
        if x1 >= 0: x1_str = ("-" + str(abs(x1)))  # adds corresponding sign to value
        if x2 >= 0: x2_str = ("-" + str(abs(x2)))
        if x1 <= 0: x1_str = ("+" + str(abs(x1)))
        if x2 <= 0: x2_str = ("+" + str(abs(x2)))
        sol = print(
            "Two real solutions: " + str((-1 * b + sqrt_d) / (2 * a)) + " and " + str((-1 * b - sqrt_d) / (2 * a)))
        ff = factorize_form(a, x1_str, x2_str, d)  # Task 7
        print("Factorize form is: f(x)=" + ff)

    print("\nThanks for using Quadratic solver!, come back soon")

    # Task 5

    # inside the my_quad_equation function

    # Task 6

    # inside the my_quad_equation function

    # Task 7 (mainly in factorized_form function and lines 90-91)

    # Task 8

main()
