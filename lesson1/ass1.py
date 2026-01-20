#After Refactoring

def find_machine_epsilon():
    epsilon = 1.0
    while (1.0 + (epsilon / 2.0)) > 1.0:
        epsilon = epsilon / 2.0
    return epsilon


def calculate_numerical_expression():
    result = abs(3.0 * (4.0 / 3.0 - 1) - 1)
    return result


def is_numerically_zero(value, tolerance):
    return value < tolerance


def main():
    m_epsilon = find_machine_epsilon()
    print(f"1. Calculated Machine Epsilon: {m_epsilon}")

    calc_result = calculate_numerical_expression()
    print(f"2. Raw Calculation Result: {calc_result}")

    if is_numerically_zero(calc_result, m_epsilon):
        print("Status: SUCCESS")
        print("The result is 'Numerically Sound' and treated as 0.")
    else:
        print("Status: FAILURE")
        print("The error exceeds machine precision.")


if __name__ == "__main__":
    main()