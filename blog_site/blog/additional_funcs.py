def get_substring_before_separator(input_string, separator):
    separator_index = input_string.find(separator)

    if separator_index == -1:
        return input_string

    return input_string[:separator_index]