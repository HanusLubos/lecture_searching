import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)

    return data[field]


def linear_search(nums, target_num):
    positions = []
    count = 0
    for idx in range(len(nums)):
        if nums[idx] == target_num:
            positions.append(idx)
            count += 1

    my_dict = {"positions": positions, "count": count}
    return my_dict

def pattern_search(sequence, vzor):
    idxs = set()
    vzor_delka = len(vzor)
    for idx in range(len(sequence)):
        tesovaci_str = sequence[idx:idx + vzor_delka]
        if tesovaci_str == vzor:
            idx = idx + int(vzor_delka/2)
            idxs.add(idx)
    return idxs


def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    # print(unordered_numbers)

    letter_sequence = read_data("sequential.json", "dna_sequence")

    occurance_let_seq = pattern_search(letter_sequence, "GTA")
    print(occurance_let_seq)

    occurance_of_num = linear_search(unordered_numbers, 9)
    # print(occurance_of_num)





if __name__ == '__main__':
    main()