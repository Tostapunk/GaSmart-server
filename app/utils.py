import datetime


def get_time():
    current_time = datetime.datetime.now().strftime("%d-%m-%Y, %H")
    current_time = current_time.split(", ")
    current_time = {"date": current_time[0], "hour": current_time[1]}
    return current_time
