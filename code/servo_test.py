import pyfirmata
import time

# 連接到Arduino
board = pyfirmata.Arduino('COM15')

# 設定伺服馬達的腳位
servo = board.get_pin('2')

# 將伺服馬達旋轉到90度
servo.write(90)

# 等待1秒
time.sleep(1)

# 關閉連接
board.exit()