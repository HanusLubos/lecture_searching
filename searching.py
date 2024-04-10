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

def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)

    occurance_of_num = linear_search(unordered_numbers, 9)
    print(occurance_of_num)



if __name__ == '__main__':
    main()