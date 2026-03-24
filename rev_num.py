def reverse_num(num):
    if len(num) < 1:
        return num
    else:
        rev_num = []
        sample_num = num
        for i in sample_num[::-1]:
            rev_num.append(i)

        return tuple(rev_num)


do = reverse_num((1,2,3,4,5))
print(do)
