"""Here we are doing various computations on Androsense data."""
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def read_excel():
    """Read_Excel() function is defined for reading excel data."""
    xlsx_data = pd.read_excel("androdata.xlsx")
    df_ = pd.DataFrame(xlsx_data)
    print(df_)
    return df_
def max_light_lux(df_):
    """The max_light_lux(): function is defined for calculating max lux level"""
    max_lightinlux = max(df_.LIGHTinLux)
    print("\n The max Light level in lux is:", str(max_lightinlux)+ " lux")
    return max_lightinlux
def min_sound(df_):
    """The min_sound(): function is defined for finding minimum sound level"""
    min_sounddb = min(df_.SOUND)
    print("\n The minimum sound level is:", str(min_sounddb)+ " db")
def data_above_soundlevel(df_):
    """Here we are printing the data above specific sound level by using interrupt"""
    sound = float(input("Enter the sound level above which the data is needed:"))
    print(df_[df_.SOUND > sound])
def sort_by_lux_level(df_):
    """Here we are sorting the data by Light level measured in lux"""
    luxlevel = df_.sort_values('LIGHTinLux')
    print("\n sorted data by Light Level: \n", luxlevel)
    return luxlevel
def avg_acc(df_):
    """ Here we are calculateing the average acceleration of X, Y, Z axis."""
    avgacc = []
    clm = ['AVERAGE_ACCELERATION']
    for i in range(len(df_)):
        avg = 0
        avg = df_.loc[i, 'ACCELEROMETER_X']+df_.loc[i, 'ACCELEROMETER_Y']\
        +df_.loc[i, 'ACCELEROMETER_Z']
        avgacc.append(avg/3)
    avacc = pd.DataFrame(avgacc, columns=clm)
    df_ = df_.join(avacc)
    print(df_)
    return df_
def sound_vs_time(df_):
    """sound_vs_time(DATA_FRAME)"""
    y_axis = df_.SOUND
    x_axis = df_.time_start
    plt.scatter(x_axis, y_axis, label='Sound VS Time')
    plt.legend()
    plt.show()
def graph_acceleration(df_):
    """ 3D graph for acceleration"""
    x_acc = df_.ACCELEROMETER_X
    y_acc = df_.ACCELEROMETER_Y
    z_acc = df_.ACCELEROMETER_Z
    threedee = plt.figure().gca(projection='3d')
    threedee.scatter(x_acc, y_acc, z_acc, label='3D Acceleration plot')
    plt.legend()
    plt.show()
def write_excel(df_):
    """we are creating new output file """
    df_.to_excel("output.xlsx")
