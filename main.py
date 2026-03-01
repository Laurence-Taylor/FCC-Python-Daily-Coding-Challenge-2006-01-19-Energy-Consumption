def compare_energy(calories_burned, watt_hours_used):
    # define conversion factor variables
    conv_factor_cal_to_joules = 4184
    conv_factor_watt_to_joules = 3600
    # check conditions and return value
    if (conv_factor_cal_to_joules*calories_burned)>(conv_factor_watt_to_joules*watt_hours_used): return "Workout"
    elif (conv_factor_cal_to_joules*calories_burned)<(conv_factor_watt_to_joules*watt_hours_used): return "Devices"
    else: return "Equal"

    return calories_burned

if __name__ == '__main__':
    print(compare_energy(250, 50))
    print('=========')
    print(compare_energy(100, 200))
    print('=========')
    print(compare_energy(450, 523))
    print('=========')
    print(compare_energy(300, 75))
    print('=========')
    print(compare_energy(200, 250))
    print('=========')
    print(compare_energy(900, 1046))