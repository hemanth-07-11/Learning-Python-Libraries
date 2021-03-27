def armstrong_number(n: int) -> bool:

    if not isinstance(n, int) or n < 1:
        return False

    sum = 0
    number_of_digits = 0
    temp = n

    while temp > 0:
        number_of_digits += 1
        temp //= 10

    temp = n
    while temp > 0:
        rem = temp % 10
        sum += rem ** number_of_digits
        temp //= 10
    return n == sum

def narcissistic_number(n: int) -> bool:

    expo = len(str(n)) 
   
    temp = [(int(i) ** expo) for i in str(n)]
    return n == sum(temp)

def main():
   
    num = int(input("Enter an integer to see if it is an Armstrong number: ").strip())
    print(f"{num} is {'' if armstrong_number(num) else 'not '}an Armstrong number.")
    print(f"{num} is {'' if narcissistic_number(num) else 'not '}an Armstrong number.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
