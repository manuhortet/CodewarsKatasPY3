def time2int(time):
    hour, min = time.split(':')
    return int(hour) * 60 + int(min)


def get_start_time(schedules, duration):
    merged_schedules = [meeting for schedule in schedules for meeting in schedule]
    merged_schedules.sort(key=lambda meeting: meeting[0])
    open_start = '09:00'
    open_stop = open_start

    for meeting in merged_schedules:
        if meeting[0] > open_stop:
            open_stop = meeting[0]
        if time2int(open_stop) - time2int(open_start) >= duration:
            return open_start
        if meeting[1] > open_start:
            open_start = meeting[1]
    open_stop = '19:00'
    if time2int(open_stop) - time2int(open_start) >= duration:
        return open_start
    return None

'finding an appointment'
schedules = [
    [['09:00', '11:30'], ['13:30', '16:00'],
     ['16:00', '17:30'], ['17:45', '19:00']],
    [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
    [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]]

def timetoint(interval):
    s, e = interval
    sf = float(s.split(':')[0]) + float(s.split(':')[1]) / 60
    ef = float(e.split(':')[0]) + float(e.split(':')[1]) / 60
    return [sf, ef]