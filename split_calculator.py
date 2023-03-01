#split calculator

print('================================================================')
print('                -+- Average Split Calculator -+-                ')
print('================================================================')

while True:
    def get_pace_400():
        total_seconds = (minutes * 60) + seconds
        lap_time = total_seconds / laps
        if lap_time < 100:
            return round(lap_time, 2)
        else:
            m = 0
            s = round(lap_time)
            while s >= 60:
                m += 1
                s -= 60
            if s < 10:
                s = '0' + str(s)
            lap_time = str(m) + ":" + str(s)
            return lap_time

    def get_pace_1600(minutes, seconds):
        m = minutes / miles
        s = seconds / miles
        ms = m - int(m)
        m = int(m)
        s += (ms * 60)
        while s >= 60:
            m += 1
            s -= 60
        s = round(s)
        if s < 10:
            s = '0' + str(s)
        mile_time = str(m) + ":" + str(s)
        return mile_time

    while True:
        try:
            distance = str(input('\nRace Distance (meters):\t'))
            if distance == 'Done' or distance == 'done' or distance == 'D' or distance == 'd':
                break
            elif distance[-1] == 'm':
                distance = distance.rstrip(distance[-1])
            elif distance[-1] == 'k':
                distance = distance.rstrip(distance[-1])
                distance = int(distance) * 1000
            distance = int(distance)
            if distance >= 0:
                laps = distance / 400
                miles = laps / 4
                break
            else:
                print("\nEntry must be a positive number.\t")
        except ValueError:
            print("\nInvalid number.\n")

    if distance == 'Done' or distance == 'done' or distance == 'D' or distance == 'd':
        print('\nBye!')
        print()
        print('================================================================')
        break
    
    while True:
        try:
            time = str(input('Time (mm:ss):\t\t'))
            if len(time) == 5 and time[2] == ':':
                minutes = int(time[0:2])
                seconds = int(time[3:5])
                pace_400 = get_pace_400()
                pace_1600 = get_pace_1600(minutes, seconds)
                break
            elif len(time) == 4 and time[1] == ':':
                minutes = int(time[0:1])
                seconds = int(time[2:4])        
                pace_400 = get_pace_400()
                pace_1600 = get_pace_1600(minutes, seconds)
                break
            elif len(time) == 2:
                minutes = 0
                seconds = int(time)        
                pace_400 = get_pace_400()
                pace_1600 = get_pace_1600(minutes, seconds)
                break
            elif len(time) == 5 and time[2] == '.':
                minutes = 0
                seconds = float(time)        
                pace_400 = get_pace_400()
                pace_1600 = get_pace_1600(minutes, seconds)
                break
            elif len(time) == 4 and time[2] == '.':
                minutes = 0
                seconds = float(time)        
                pace_400 = get_pace_400()
                pace_1600 = get_pace_1600(minutes, seconds)
                break
            elif len(time) == 7 and time[1] == ':' and time[4] == ':':
                minutes = int(time[2:4]) + 60 * int(time[0:1])
                seconds = int(time[5:7])        
                pace_400 = get_pace_400()
                pace_1600 = get_pace_1600(minutes, seconds)
                break
            else:
                print("\nEntry invalid.\n")
        except ValueError:
            print("\nEntry invalid.\n")


    print()
    print('----------------------------------------------------------------')
    print()
    print(f'Average 400 Split:\t{pace_400}')
    print(f'Average Mile Pace:\t{pace_1600}')
    print()
    print('================================================================')
