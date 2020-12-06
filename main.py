from commenUtils import get_input_data
import argparse
import logging


parser = argparse.ArgumentParser()
parser.add_argument("--log", default="warning")

options = parser.parse_args()
levels = {'info': logging.INFO, 'debug': logging.DEBUG}

level = levels.get(options.log.lower())

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    level=level)

logger = logging.getLogger(__name__)


def decode(code: str) -> (int, int):
    binary: str = ""
    for char in code[:7]:
        binary += str(int((char == "B")))
    row: int = int(binary, base=2)
    binary = ""
    for char in code[7:]:
        binary += str(int((char == "R")))
    column: int = int(binary, base=2)
    logger.debug(f"Input: {code}, Output: Row {row}, Column {column}")
    return row, column


def input_data_to_seat_id_list(file_name: str) -> list[int]:
    codes: list[str] = get_input_data(file_name)
    seat_ids: list[int] = []
    for code in codes:
        row, column = decode(code)
        seat_ids.append(row * 8 + column)
    return seat_ids


def solution_part_1(file_name: str) -> int:
    seat_ids: list[int] = input_data_to_seat_id_list(file_name)
    seat_ids.sort()
    return seat_ids[-1]


def solution_part_2(file_name: str) -> int:
    seat_ids: list[int] = input_data_to_seat_id_list(file_name)
    seat_ids.sort()
    logger.debug(f"Lowest seat ID: {seat_ids[0]}, Highest seat ID: {seat_ids[-1]}")
    current_index = 0
    current_id = seat_ids[current_index]
    while current_id + 1 == seat_ids[current_index + 1]:
        current_id += 1
        current_index += 1
    logger.debug(f"Neighbor IDS: {seat_ids[current_index-1:current_index+2]}")
    return current_id+1


if __name__ == '__main__':
    logger.info(f"Highest seat ID: {solution_part_1('inputData.txt')}")
    logger.info(f"My seat ID is {solution_part_2('inputData.txt')}")
