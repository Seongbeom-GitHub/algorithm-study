def map_value(input_value, input_value_max, output_power_max):
    # 음수 체크
    is_negative = input_value < 0

    # 절대값으로 변환
    absolute_input = abs(input_value)

    # 입력 값을 0 ~ output_power_max 범위로 변환
    normalized_input = absolute_input / input_value_max

    # 변환된 입력 값을 사용하여 출력 값을 보간
    output = output_power_max * normalized_input

    # 음수의 경우 음수값으로 반환
    return -output if is_negative else output

print(map_value(-100, 200, 10))