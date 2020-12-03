import os

def expense_product_two(x):
    for num in x:
        candidate_num = 2020 - num
        if candidate_num in x:
            break
    return [num*candidate_num]

def expense_product_three(x):
    done = False
    for num in x:
        for bum in x:
            candidate_num = 2020 - num - bum
            if candidate_num in x:
                done = True
                break
        if done:
            break
    return [num*bum*candidate_num]

def import_data(rel_path):
    abs_file_path = os.path.join(os.getcwd(), rel_path)
    with open(abs_file_path) as records:
        y = [int(x) for x in records]
    return y

if __name__ == '__main__':
    entries = import_data('data/day_1_input.txt')
    two_product = expense_product_two(entries)
    three_product = expense_product_three(entries)
    print('Product of two entries is:' + str(two_product))
    print('Product of three entries is:' + str(three_product))

