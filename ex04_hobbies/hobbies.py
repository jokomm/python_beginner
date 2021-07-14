"""Hobbies."""
import csv


def create_list_from_file(file):
    """
    Collect lines from given file into list.

    :param file: original file path
    :return: list of lines
    """
    with open(file, encoding='utf-8') as file:  # Opens given file.

        list_from_file = file.read().splitlines()  # Reads all the lines from the file and stores it as a string.Every line comes with its end of line characters (\n\r); this way the characters are removed.

    return list_from_file


def create_dictionary(file):
    """
    Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2].

    :param file: original file path
    :return: dict
    """
    lst = create_list_from_file(file)
    dictionary = {}
    for item in lst:
        (key, value) = item.split(':')
        if key in dictionary.keys():
            if value not in dictionary[key]:
                dictionary[key].append(value)
        else:
            dictionary[key] = [value]
    return dictionary


def find_person_with_most_hobbies(file):
    """
    Find the person (or people) who have more hobbies than others.

    :param file: original file path
    :return: list
    """
    dictionary = create_dictionary(file)
    for value in dictionary:
        dictionary[value] = sorted(dictionary[value])
    most_hobbies = len(max(dictionary.values(), key=len))
    person_most_hobbies = list()
    for key, value in dictionary.items():
        if most_hobbies == len(value):
            person_most_hobbies.append(key)

    return person_most_hobbies


def find_person_with_least_hobbies(file):
    """
    Find the person (or people) who have less hobbies than others.

    :param file: original file path
    :return: list
    """
    dictionary = create_dictionary(file)
    for value in dictionary:
        dictionary[value] = sorted(dictionary[value])
    least_hobbies = len(min(dictionary.values(), key=len))
    person_least_hobbies = list()
    for key, value in dictionary.items():
        if least_hobbies == len(value):
            person_least_hobbies.append(key)

    return person_least_hobbies


def create_dictionary_2(file):
    """
    Create dictionary with  hobbies and names of people who have this hobby as Hobby: [name_1, name_2].

    :param file: original file path
    :return: dict
    """
    lst = create_list_from_file(file)
    dictionary = {}
    for item in lst:
        (value, key) = item.split(':')
        if key in dictionary.keys():
            if value not in dictionary[key]:
                dictionary[key].append(value)
        else:
            dictionary[key] = [value]
    return dictionary


def find_most_popular_hobby(file):
    """
    Find the most popular hobby.

    :param file: original file path
    :return: list
    """
    dictionary = create_dictionary_2(file)
    for value in dictionary:
        dictionary[value] = sorted(dictionary[value])
    most_hobbies = len(max(dictionary.values(), key=len))
    most_popular_hobby = list()
    for key, value in dictionary.items():
        if most_hobbies == len(value):
            most_popular_hobby.append(key)

    return most_popular_hobby


def find_least_popular_hobby(file):
    """
    Find the least popular hobby.

    :param file: original file path
    :return: list
    """
    dictionary = create_dictionary_2(file)
    for value in dictionary:
        dictionary[value] = sorted(dictionary[value])
    least_hobbies = len(min(dictionary.values(), key=len))
    least_popular_hobby = list()
    for key, value in dictionary.items():
        if least_hobbies == len(value):
            least_popular_hobby.append(key)

    return least_popular_hobby


def write_corrected_database(file, file_to_write):
    """
    Write .csv file in a proper way. Use collected and structured data.

    :param file: original file path
    :param file_to_write: file to write result
    """
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
        dictionary = create_dictionary(file)
        for i in sorted(dictionary.keys()):
            name = i
            hobbies = sorted(dictionary[i])
            writer.writerow([name, "-".join(hobbies)])
