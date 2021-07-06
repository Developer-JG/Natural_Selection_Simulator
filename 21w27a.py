# 시스템 정의 함수
import random
import pygame
from pygame.locals import *


# 전역 변수 (게임 설정)
initial_passive_objects = 50 # 초기 피식자 개체수
initial_hostile_objects = 1 # 포식자 개체수
division_count = 4 # 분열 개체수 (최대 4)
division_time = 300 # 분열 주기 (초)
division_percent = 70 # 분열 확률 (%)
max_passive = 500 # 최대 피식자 개체수


# 기본 설정값
ver = "21w27a"
python_ver  = "3.7"

# 파이게임 초기화
pygame.init()

# 색 정의 (RGB)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 화면 정의
screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# 폰트 정의
font_input_1 = pygame.font.Font("BinggraeTaom-Bold.ttf", 29)
font_input_2 = pygame.font.Font("BinggraeTaom-Bold.ttf", 13)

# 프로그램 이름
pygame.display.set_caption("Natural_Selection_Simulator")


clock = pygame.time.Clock()


def main():
    # 피식자 [[x좌표, y좌표], [x크기, y크기], 활동성, 속도, 이전에 움직인 방향]
    passive_mobs_list = []

    # 피식자 소환
    count = 0
    while count != initial_passive_objects:
        count += 1
        passive_mobs_list.append([[random.randint(20, 1430), random.randint(80, 930)], [50, 50], 5, 7, 0])


    # 포식자
    hostile_mobs_list = []

    # 포식자 소환
    count = 0
    while count != initial_hostile_objects:
        count += 1
        hostile_mobs_list.append([[random.randint(20, 1430), random.randint(80, 930)], [100, 100], 1, 20, 0])


    fps = 60

    gen = 1
    gen_time = 1

    while True:
        if len(passive_mobs_list) == 0:
            return

        # 화면 전환 주기 (진행 속도)
        clock.tick(fps)

        for event in pygame.event.get():

            # 화면 갱신 주기 설정
            if event.type == KEYDOWN:
                if event.key == ord('1'):
                    fps = 1
                elif event.key == ord('2'):
                    fps = 5
                elif event.key == ord('3'):
                    fps = 10
                elif event.key == ord('4'):
                    fps = 30
                elif event.key == ord('5'):
                    fps = 50
                elif event.key == ord('6'):
                    fps = 60
                elif event.key == ord('7'):
                    fps = 80
                elif event.key == ord('8'):
                    fps = 120
                elif event.key == ord('9'):
                    fps = 140
                elif event.key == ord('0'):
                    fps = 0
            elif event.type == QUIT:
                return

        # 화면 채우기
        screen.fill(white)

        # 도형 출력
        pygame.draw.line(screen, black, [0, 50], [screen_width, 50], 1)

        # 글자 출력
        text_1 = font_input_1.render(str(fps) + "FPS / " + str(gen) + "Generation", True, black)
        rect_text_1 = text_1.get_rect()
        rect_text_1.topleft = (5, 5)
        screen.blit(text_1, rect_text_1)

        text_2 = font_input_1.render("Object count : " + str(len(passive_mobs_list)), True, black)
        rect_text_2 = text_2.get_rect()
        rect_text_2.midtop = (screen_width // 2, 5)
        screen.blit(text_2, rect_text_2)

        text_3_1 = font_input_2.render("ver." + ver, True, black)
        rect_text_3_1 = text_3_1.get_rect()
        rect_text_3_1.topright = (screen_width - 5, 5)
        screen.blit(text_3_1, rect_text_3_1)

        text_3_2 = font_input_2.render("POWERED BY PYTHON" + python_ver + " | MADE BY JG IN SEOUL", True, black)
        rect_text_3_2 = text_3_2.get_rect()
        rect_text_3_2.bottomright = (screen_width - 5, 44)
        screen.blit(text_3_2, rect_text_3_2)




        # 게임이 멈춤 상태가 아닐때
        if fps != 0:
            # 몹 위치 변경
            # [[x좌표, y좌표], [x크기, y크기], 활동성, 속도, 이전에 움직인 방향]
            for i in range(0, len(passive_mobs_list)):
                move = random.randint(1,10)

                if move >= passive_mobs_list[i][2]:
                    before_direction = random.randint(1, 10)

                    if before_direction == 1:
                        direction = random.randint(1, 4)
                        if direction == 1: # 동
                            passive_mobs_list[i][0][0] = passive_mobs_list[i][0][0] + passive_mobs_list[i][3]
                            passive_mobs_list[i][4] = 1
                            direction_plus = random.randint(1,2)
                            if direction_plus == 1:
                                passive_mobs_list[i][0][1] = passive_mobs_list[i][0][1] + passive_mobs_list[i][3]
                                passive_mobs_list[i][4] = 5

                        elif direction == 2: # 서
                            passive_mobs_list[i][0][0] = passive_mobs_list[i][0][0] - passive_mobs_list[i][3]
                            passive_mobs_list[i][4] = 2
                            direction_plus = random.randint(1, 2)
                            if direction_plus == 1:
                                passive_mobs_list[i][0][1] = passive_mobs_list[i][0][1] - passive_mobs_list[i][3]
                                passive_mobs_list[i][4] = 6

                        elif direction == 3: # 남
                            passive_mobs_list[i][0][1] = passive_mobs_list[i][0][1] + passive_mobs_list[i][3]
                            passive_mobs_list[i][4] = 3
                            direction_plus = random.randint(1, 2)
                            if direction_plus == 1:
                                passive_mobs_list[i][0][1] = passive_mobs_list[i][0][1] + passive_mobs_list[i][3]
                                passive_mobs_list[i][4] = 7

                        elif direction == 4: # 북
                            passive_mobs_list[i][0][1] = passive_mobs_list[i][0][1] - passive_mobs_list[i][3]
                            passive_mobs_list[i][4] = 4
                            direction_plus = random.randint(1, 2)
                            if direction_plus == 1:
                                passive_mobs_list[i][0][1] = passive_mobs_list[i][0][1] - passive_mobs_list[i][3]
                                passive_mobs_list[i][4] = 8

                    else: # 같은 방향
                        if passive_mobs_list[i][4] == 1 or passive_mobs_list[i][4] == 3 or \
                                passive_mobs_list[i][4] == 5 or passive_mobs_list[i][4] == 7:
                            passive_mobs_list[i][0][0] = passive_mobs_list[i][0][0] + passive_mobs_list[i][3]

                        elif passive_mobs_list[i][4] == 2 or passive_mobs_list[i][4] == 4 or \
                                passive_mobs_list[i][4] == 6 or passive_mobs_list[i][4] == 8:
                            passive_mobs_list[i][0][0] = passive_mobs_list[i][0][0] - passive_mobs_list[i][3]

                        if passive_mobs_list[i][4] == 5 or passive_mobs_list[i][4] == 7:
                            passive_mobs_list[i][0][0] = passive_mobs_list[i][0][0] + passive_mobs_list[i][3]

                        elif passive_mobs_list[i][4] == 6 or passive_mobs_list[i][4] == 8:
                            passive_mobs_list[i][0][1] = passive_mobs_list[i][0][1] - passive_mobs_list[i][3]
                        

                    if 0 >= passive_mobs_list[i][0][0]:
                        passive_mobs_list[i][0][0] = 1500 - passive_mobs_list[i][1][0]
                    elif 1500 - passive_mobs_list[i][1][0] <= passive_mobs_list[i][0][0]:
                        passive_mobs_list[i][0][0] = 0

                    if 60 >= passive_mobs_list[i][0][1]:
                        passive_mobs_list[i][0][1] = 1000 - passive_mobs_list[i][1][1]
                    elif 1000 - passive_mobs_list[i][1][1] <= passive_mobs_list[i][0][1]:
                        passive_mobs_list[i][0][1] = 60


            for i in range(0, len(hostile_mobs_list)):
                move = random.randint(1,10)

                if move >= hostile_mobs_list[i][2]:
                    before_direction = random.randint(1, 10)

                    if before_direction == 1:
                        direction = random.randint(1, 4)
                        if direction == 1: # 동
                            hostile_mobs_list[i][0][0] = hostile_mobs_list[i][0][0] + hostile_mobs_list[i][3]
                            hostile_mobs_list[i][4] = 1
                            direction_plus = random.randint(1,2)
                            if direction_plus == 1:
                                hostile_mobs_list[i][0][1] = hostile_mobs_list[i][0][1] + hostile_mobs_list[i][3]
                                hostile_mobs_list[i][4] = 5

                        elif direction == 2: # 서
                            hostile_mobs_list[i][0][0] = hostile_mobs_list[i][0][0] - hostile_mobs_list[i][3]
                            hostile_mobs_list[i][4] = 2
                            direction_plus = random.randint(1, 2)
                            if direction_plus == 1:
                                hostile_mobs_list[i][0][1] = hostile_mobs_list[i][0][1] - hostile_mobs_list[i][3]
                                hostile_mobs_list[i][4] = 6

                        elif direction == 3: # 남
                            hostile_mobs_list[i][0][1] = hostile_mobs_list[i][0][1] + hostile_mobs_list[i][3]
                            hostile_mobs_list[i][4] = 3
                            direction_plus = random.randint(1, 2)
                            if direction_plus == 1:
                                hostile_mobs_list[i][0][1] = hostile_mobs_list[i][0][1] + hostile_mobs_list[i][3]
                                hostile_mobs_list[i][4] = 7

                        elif direction == 4: # 북
                            hostile_mobs_list[i][0][1] = hostile_mobs_list[i][0][1] - hostile_mobs_list[i][3]
                            hostile_mobs_list[i][4] = 4
                            direction_plus = random.randint(1, 2)
                            if direction_plus == 1:
                                hostile_mobs_list[i][0][1] = hostile_mobs_list[i][0][1] - hostile_mobs_list[i][3]
                                hostile_mobs_list[i][4] = 8

                    else: # 같은 방향
                        if hostile_mobs_list[i][4] == 1 or hostile_mobs_list[i][4] == 3 or \
                                hostile_mobs_list[i][4] == 5 or hostile_mobs_list[i][4] == 7:
                            hostile_mobs_list[i][0][0] = hostile_mobs_list[i][0][0] + hostile_mobs_list[i][3]

                        elif hostile_mobs_list[i][4] == 2 or hostile_mobs_list[i][4] == 4 or \
                                hostile_mobs_list[i][4] == 6 or hostile_mobs_list[i][4] == 8:
                            hostile_mobs_list[i][0][0] = hostile_mobs_list[i][0][0] - hostile_mobs_list[i][3]

                        if hostile_mobs_list[i][4] == 5 or hostile_mobs_list[i][4] == 7:
                            hostile_mobs_list[i][0][0] = hostile_mobs_list[i][0][0] + hostile_mobs_list[i][3]

                        elif hostile_mobs_list[i][4] == 6 or hostile_mobs_list[i][4] == 8:
                            hostile_mobs_list[i][0][1] = hostile_mobs_list[i][0][1] - hostile_mobs_list[i][3]

                    if 0 >= hostile_mobs_list[i][0][0]:
                        hostile_mobs_list[i][0][0] = 1500 - hostile_mobs_list[i][1][0]
                    elif 1500 - hostile_mobs_list[i][1][0] <= hostile_mobs_list[i][0][0]:
                        hostile_mobs_list[i][0][0] = 0

                    if 60 >= hostile_mobs_list[i][0][1]:
                        hostile_mobs_list[i][0][1] = 1000 - hostile_mobs_list[i][1][1]
                    elif 1000 - hostile_mobs_list[i][1][1] <= hostile_mobs_list[i][0][1]:
                        hostile_mobs_list[i][0][1] = 60

            # 충돌 체크
            try:
                for i in range(0, len(passive_mobs_list)):
                    passive = pygame.Rect((passive_mobs_list[i][0][0], passive_mobs_list[i][0][1]), (passive_mobs_list[i][1][0], passive_mobs_list[i][1][1]))

                    for j in range(0, len(hostile_mobs_list)):
                        hostile = pygame.Rect((hostile_mobs_list[j][0][0], hostile_mobs_list[j][0][1]), (hostile_mobs_list[j][1][0], hostile_mobs_list[j][1][1]))

                        if passive.colliderect(hostile):
                            del passive_mobs_list[i]
            except:
                pass

            # 몹 출력
            for i in range(0, len(passive_mobs_list)):
                pygame.draw.rect(screen, black, [passive_mobs_list[i][0][0], passive_mobs_list[i][0][1],
                                                 passive_mobs_list[i][1][0], passive_mobs_list[i][1][1]], 0)

            for i in range(0, len(hostile_mobs_list)):
                pygame.draw.rect(screen, red, [hostile_mobs_list[i][0][0], hostile_mobs_list[i][0][1],
                                                 hostile_mobs_list[i][1][0], hostile_mobs_list[i][1][1]], 0)


            # 화면 갱신
            pygame.display.update()

            # 세대 연산
            if gen_time == division_time:
                gen += 1

                # 몹 분열
                # [[x좌표, y좌표], [x크기, y크기], 활동성, 속도, 이전에 움직인 방향]
                # 피식자 [[x좌표 (0~1500), y좌표 (60~1000)], [x크기 (30~70), y크기 (30~70)], 활동성 (1~9), 속도 (2~12), 이전에 움직인 방향]
                plus_passive_mobs_list = []
                for i in range(0, len(passive_mobs_list)):
                    for j in range(1, division_count + 1):
                        percent = random.randint(1,100)
                        if percent <= division_percent:
                            # 위치
                            point = random.randint(1,4)
                            if point == 1:
                                x_point = passive_mobs_list[i][0][0] + passive_mobs_list[i][1][0] + random.randint(5,10)
                                y_point = passive_mobs_list[i][0][1]
                            elif point == 2:
                                x_point = passive_mobs_list[i][0][0]
                                y_point = passive_mobs_list[i][0][1] + passive_mobs_list[i][1][1] + random.randint(5,10)
                            elif point == 3:
                                x_point = passive_mobs_list[i][0][0] - passive_mobs_list[i][1][0] - random.randint(5,10)
                                y_point = passive_mobs_list[i][0][1]
                            elif point == 4:
                                x_point = passive_mobs_list[i][0][0]
                                y_point = passive_mobs_list[i][0][1] - passive_mobs_list[i][1][1] - random.randint(5,10)

                            # 크기
                            x_size = random.randint(passive_mobs_list[i][1][0] - 2, passive_mobs_list[i][1][0] + 2)
                            y_size = random.randint(passive_mobs_list[i][1][1] - 2, passive_mobs_list[i][1][1] + 2)

                            # 크기 재조정
                            if 5 >= x_size:
                                x_size = 5
                            elif 100 <= x_size:
                                x_size = 100

                            if 5 >= y_size:
                                y_size = 5
                            elif 100 <= y_size:
                                y_size = 100

                            # 위치 재조정
                            if 0 >= x_point:
                                x_point = 1500 - x_size
                            elif 1500 - x_size <= x_point:
                                x_point = 0

                            if 60 >= y_point:
                                y_point = 1000 - y_size
                            elif 1000 - y_size <= y_point:
                                y_point = 60

                            # 활동성
                            activity = random.randint(passive_mobs_list[i][2] - 1, passive_mobs_list[i][2] + 1)
                            if 1 >= activity:
                                activity = 1
                            elif 9 <= activity:
                                activity = 9

                            # 속도
                            speed = random.randint(passive_mobs_list[i][3] - 1, passive_mobs_list[i][3] + 1)
                            if 2 >= speed:
                                speed = 2
                            elif 12 <= speed:
                                speed = 12

                            direction = random.randint(1,8)

                            if max_passive >= len(passive_mobs_list) + len(plus_passive_mobs_list):
                                plus_passive_mobs_list.append([[x_point, y_point], [x_size, y_size], activity, speed, direction])


                passive_mobs_list += plus_passive_mobs_list

                gen_time = 0

            gen_time += 1


if __name__ == "__main__":
    main()