from typing_samples import typing_sample_data
from manipulator import SpeedCalc
from ts_ui import TypingSpeedUI

sample_data = []
for paragraph in typing_sample_data:
    sample_paragraph = paragraph["text"]
    sample_data.append(sample_paragraph)
    random_sample_data = sample_data
    new_paragraph = random_sample_data

speed_calc = SpeedCalc(new_paragraph)
ts_ui = TypingSpeedUI(speed_calc)




# print(new_paragraph)












