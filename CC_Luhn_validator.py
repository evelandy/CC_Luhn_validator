def main():
    cc_num = input("Enter a 16 digit card number to check if it is valid: ")
    return luhn(cc_num)


def luhn(cc_num):
    if not cc_num.isdigit():
        return 'not valid'
    if len(cc_num) > 16 or len(cc_num) < 16:
        return 'not valid'
    rev = reverse(cc_num)
    double = mult_by_2(rev)
    sub_9 = subtract_9(double)
    total_num = add_all(sub_9)
    return check_to_0(total_num)


def reverse(cc_num):
    reved = cc_num[::-1]
    return reved


def mult_by_2(rev):
    cc_lst = []
    doubled_cc = []
    for num in rev:
        cc_lst.append(num)
    for num in range(1, len(cc_lst) + 1):
        if num % 2 == 0:
            doub = int(cc_lst[num-1])
            doubled_cc.append(doub * 2)
        else:
            sing = int(cc_lst[num-1])
            doubled_cc.append(sing)
    return doubled_cc


def subtract_9(double):
    sub_9 = []
    for num in double:
        if num <= 9:
            sub_9.append(num)
        else:
            sub_9.append(num - 9)
    return sub_9


def add_all(sub_9):
    total_num = sum(sub_9)
    return total_num


def check_to_0(total_num):
    if total_num % 10 == 0:
        return 'valid'
    else:
        return 'not valid'


print(main())
