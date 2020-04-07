"""
Created on Mon Feb 17 15:47:27 2020

@author: vishalk23
"""
import andro as sense
DATA_FRAME = sense.read_excel()
sense.max_light_lux(DATA_FRAME)
sense.min_sound(DATA_FRAME)
sense.data_above_soundlevel(DATA_FRAME)
DATA = sense.sort_by_lux_level(DATA_FRAME)
NEW_DATA = sense.avg_acc(DATA)
sense.sound_vs_time(NEW_DATA)
sense.graph_acceleration(NEW_DATA)
sense.write_excel(NEW_DATA)
sense.open_text()
