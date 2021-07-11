import sys

def move_disk(disk_num, start_peg, end_peg):
    print(f'{start_peg} {end_peg}')

def hanoi(num_disks, start_peg, end_peg):
    # base case: 옮길 원판이 없으면 부분 문제를 나누지 않고 함수 종료
    if num_disks == 0:
        return
    else:
        mid_peg = 6 - start_peg - end_peg

        # 1. 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 mid_peg로 이동
        hanoi(num_disks - 1, start_peg, mid_peg)

        # 2. 가장 큰 원판을 start_peg에서 end_peg로 이동
        move_disk(num_disks, start_peg, end_peg)

        # 3. 나머지 원판들을 mid_peg에서 end_peg로 이동
        hanoi(num_disks - 1, mid_peg, end_peg)

# 테스트
N = int(sys.stdin.readline("원판의 개수 입력"))
print(f'{2 ** N - 1}')  # print(f'{(1 << N) - 1}')
hanoi(N, 1, 3)
