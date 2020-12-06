def get_input_data(input_file_name: str) -> list[str]:
    f = open(input_file_name, "r")
    codes: list[str] = []
    for line in f:
        codes.append(line.strip())
    return codes
