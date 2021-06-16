"""
2021.06.16
"""


import pywinmacro as pw
import time


location1 = (1080, 574)  # 그림선택
location2 = (1557, 100)  # 창닫기
location3 = (638, 42)   # 바탕화면


# 배경바꾸기 실행 함수
def run():
    pw.key_press_once("window")
    pw.key_press_once("d")
    time.sleep(1)
    pw.right_click(location3)
    time.sleep(1)
    for i in range(12):
        pw.key_press_once("down_arrow")
        time.sleep(0.5)
    pw.key_press_once("enter")
    time.sleep(1)
    pw.key_press_once("tab")
    time.sleep(1)
    pw.key_press_once("enter")
    time.sleep(1)
    pw.click(location1)
    time.sleep(1)
    pw.click(location2)


# 배경바꾸기 함수 실행행
run()