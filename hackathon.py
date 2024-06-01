def check_weight_status(sensor_reading, registered_weight):
    # 압전소자를 사용하여 측정된 압력을 기준으로 몸무게의 상태를 확인하는 함수
    
    # 몸무게의 임계값 계수 설정
    threshold_factor_high = 1.5
    threshold_factor_low = 0.7
    
    # 몸무게의 임계값 계산
    weight_threshold_high = registered_weight * threshold_factor_high
    weight_threshold_low = registered_weight * threshold_factor_low
    
    # 압전소자에서 측정된 압력과 임계값 비교
    if sensor_reading >= weight_threshold_high:
        return "high"
    elif sensor_reading <= weight_threshold_low:
        return "low"
    else:
        return "normal"

def calculate_penalty(start_time, current_time):
    # 경고음이 울린 후부터 현재까지의 시간을 기반으로 벌금을 계산하는 함수
    
    # 경과 시간 계산 (초 단위)
    elapsed_time = current_time - start_time
    
    # 경과 시간이 10초 이하이면 벌금 없음
    if elapsed_time <= 10:
        penalty = 0
    else:
        # 경과 시간이 10초를 초과한 경우 벌금 계산
        penalty = (elapsed_time - 10) * 500
    
    return penalty

# 전동킥보드 앱에 등록된 사용자의 몸무게
registered_weight = float(input("전동킥보드 앱에 등록된 사용자의 몸무게를 입력하세요 (kg): "))

# 압전소자에서 측정된 압력 입력 받기 (임의로 설정)
sensor_reading = float(input("압전소자에서 측정된 압력을 입력하세요: "))

# 몸무게 상태 확인 함수 호출
weight_status = check_weight_status(sensor_reading, registered_weight)

# 경고음이 울렸는지 여부 확인
if weight_status == "high" or weight_status == "low":
    print("주의: 몸무게가 정상 범위를 벗어났습니다. 경고음이 울립니다!")
    
    # 경고음이 울린 시간 기록
    start_time = float(input("경고음이 울린 시간을 입력하세요 (초): "))
    # 현재 시간 입력 받기
    current_time = float(input("현재 시간을 입력하세요 (초): "))
    # 경과 시간 계산
    elapsed_time = current_time - start_time
    
    # 경과 시간이 10초 이상인 경우 추가 조치 필요
    if elapsed_time > 10:
        print("경고음이 10초 이상 울렸습니다. 추가 조치가 필요합니다.")
        
        # 벌금 계산 함수 호출
        penalty_amount = calculate_penalty(start_time, current_time)
        print("10초 후부터 1초당 벌금:", penalty_amount, "원")
else:
    print("안전: 몸무게가 정상 범위 내에 있습니다.")