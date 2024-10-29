# @Time     : 2024/10/29
# @Author   : Horange
# @File     : main.py

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()


def main():
    web.get("https://jwc.ujs.edu.cn/qtxx/jwxt.htm")
    web.implicitly_wait(2)
    input("过程评价页面打开后回车")

    web.switch_to.window(web.window_handles[-1])
    size = len(web.find_elements(By.CLASS_NAME, "item"))

    for _ in range(size):
        # 要获取两遍，因为页面会刷新。第一遍获取数量，第二遍再获取元素
        web.switch_to.window(web.window_handles[-1])
        div = web.find_elements(By.CLASS_NAME, "item")[
            0
        ]  # 始终获取第一个。因为评价过的会进入“已评价”页面
        div.click()

        inps = web.find_elements(By.NAME, "i_pjf")
        for inp in inps:
            inp.send_keys("100")

        web.find_element(By.CLASS_NAME, "mui-btn-blue").click()
        web.find_element(By.CLASS_NAME, "btn-sm").click()

    print("Finished")
    return 0


if __name__ == "__main__":
    sys.exit(main())
