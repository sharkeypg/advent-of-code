import os
import pandas as pd

def import_data(rel_path):
    abs_file_path = os.path.join(os.getcwd(), rel_path)
    y = pd.read_csv(abs_file_path, sep=' ', header=None)
    y = y.rename(columns = {0: 'limits', 1: 'letter', 2: 'password'})
    return y

def calc_valid_entries(df, method):
    df[['lower_lim', 'upper_lim']] = df.limits.str.split(pat='-', expand=True).astype('int32')
    df.letter = df.letter.str.strip(':')
    valid = 0
    if method == 'first':
        for index, row in df.iterrows():
            letter_count = row['password'].count(row['letter'])
            if row['lower_lim'] <= letter_count <= row['upper_lim']:
                valid += 1
    elif method == 'second':
        for index, row in df.iterrows():
            letter_matches = int(row['password'][row['lower_lim'] - 1] == row['letter']) + int(row['password'][row['upper_lim'] - 1] == row['letter'])
            if letter_matches == 1:
                valid += 1
    return valid

if __name__ == '__main__':
    pwd_df = import_data('data/day_2_input.txt')
    num_valid_one = calc_valid_entries(pwd_df, method='first')
    num_valid_two = calc_valid_entries(pwd_df, method='second')
    print('The number of valid passwords using the first method is ' + str(num_valid_one))
    print('The number of valud passwords using the second method is ' + str(num_valid_two))

