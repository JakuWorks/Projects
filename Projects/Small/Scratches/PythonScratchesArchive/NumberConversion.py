
"""A simple script I wrote to """

from datetime import datetime
from dateutil.parser import parse
from word2number.w2n import word_to_num
from humanize import intword
from typing import Union
import re

# nps - numbers per second

nps_text: str = input("Please Input Numbers Per Second: ")

nps_digits_pattern_part1: str = r'\d+\.\d+'
nps_digits_pattern_part2: str = r'\.\d+'
nps_digits_pattern_part3: str = r'\d+'
nps_digits_pattern: str = '|'.join([nps_digits_pattern_part1, nps_digits_pattern_part2, nps_digits_pattern_part3])
nps_digits_pattern_compiled = re.compile(nps_digits_pattern)
nps_digits_text: str = re.findall(pattern=nps_digits_pattern_compiled, string=nps_text)[0]
nps_digits: float = float(nps_digits_text)
nps_digits: Union[int, float] = int(nps_digits) if nps_digits == int(nps_digits) else nps_digits

nps_modifier: int = word_to_num(nps_text)

nps_number: float = nps_digits * nps_modifier

print(f"({nps_number:,})\n")

time_text: str = input("Please Input Time: ")
time_datetime: datetime = parse(time_text)
time_seconds: int = (time_datetime.second +
                     time_datetime.minute * 60 +
                     time_datetime.hour * 60 * 60)
print(f"({time_seconds:,} seconds)\n")

sum_number: int = nps_number * time_seconds
sum_number_text: str = intword(sum_number, "%0.3f")

sum_text_line1: str = "===== ===== ===== ====="
sum_text_line2: str = f"It's {sum_number_text}!"
sum_text_line3: str = f"({sum_number:,})"
sum_text: str = '\n'.join([sum_text_line1, sum_text_line2, sum_text_line3])

print(sum_text)

input("\nEnd...")
