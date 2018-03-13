#!/usr/bin/python
# encoding: utf-8


import os
from multiprocessing import Pool

from pydub import AudioSegment
from PIL import Image, ImageDraw
import numpy as np

PROCESSING_COUNT = 10

BARS = 500
BAR_HEIGHT = 60
LINE_WIDTH = 5

src = './bangbangbangbang.mp3'

audio = AudioSegment.from_file(src)
data = np.fromstring(audio._data, np.int16)
fs = audio.frame_rate


length = len(data)
RATIO = length/BARS


def get_bars(data):
    """# get_bars: docstring
    args:
        data:    ---    arg
    returns:
        0    ---    
    """
    count = 0
    maximum_item = 0
    max_array = []
    highest_bar = 0

    # 将整个数据按照总长度跟规定长度的比分段
    # 取出每段的最大值，加入到结果数组中
    for d in data:
        if count < RATIO:
            count = count +1

            if abs(d) > abs(maximum_item):
                maximum_item = d

        else:
            max_array.append(maximum_item)

            if maximum_item > highest_bar:
                highest_bar = maximum_item

            maximum_item = 0
            count = 1
    return highest_bar, max_array

all_data = []
start_pointer = 0
end_pointer = 0
step_length = len(data)/PROCESSING_COUNT
for i in range(PROCESSING_COUNT):
    start_pointer = end_pointer
    end_pointer = np.int32(step_length * (i+1))
    all_data.append(data[start_pointer:end_pointer])
if end_pointer < len(data):
    all_data.append(data[end_pointer:-1])


result_0 = []
#for i in all_data:
#    result_0.append(get_bars(i))

pool = Pool(PROCESSING_COUNT)
result_0 = pool.map(get_bars, all_data)

highest_bar = 0
result = []
for i in result_0:
    result.extend(i[1])
    if i[0] > highest_bar:
        highest_bar = i[0]
    
bar_ratio = highest_bar/BAR_HEIGHT

im = Image.new("RGBA", (BARS * LINE_WIDTH, BAR_HEIGHT), (255, 255, 255, 1))
draw = ImageDraw.Draw(im)

current_x = 1
for item in result:
    item_height = item/bar_ratio

    current_y = (BAR_HEIGHT - item_height)/2
    draw.line((current_x, current_y, current_x, current_y+item_height), fill=(169, 171, 172), width=4)

    current_x = current_x + LINE_WIDTH

#im.show()
im.save('out.bmp')


