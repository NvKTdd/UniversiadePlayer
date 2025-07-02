print('''
 _____      __   ___            ___  ___      ___   ____________        ___           ___   
|     \    |  |  \  \          /  /  |  |    /  /  |____    ____|      |   |         |   |
|  |\  \   |  |   \  \        /  /   |  |   /  /        |  |           |   |         |   |
|  | \  \  |  |    \  \      /  /    |  |__/  /         |  |           |   |         |   |
|  |  \  \ |  |     \  \    /  /     |  |__  |          |  |      ____/    |    ____/    |
|  |   \  \|  |      \  \  /  /      |  |  \  \         |  |     /   ___   |   /   ___   |  
|  |    \  \  |       \  \/  /       |  |   \  \        |  |    |   |___|  |  |   |___|  |
|__|     \____|        \____/        |__|    \__\       |__|     \ _______/    \ _______/
      ''')
import time
import pygame
import os
import time
import cv2
from ffpyplayer.player import MediaPlayer
time.sleep(0.8)
print("欢迎使用大运播放器！")

def play_video(file_path):
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print("Error: 文件不存在:", file_path)
        return
    
    # 使用ffpyplayer打开视频文件
    player = MediaPlayer(file_path)
    
    while True:
        # 获取音频帧
        audio_frame, val = player.get_frame()
        if val == 'eof':
            break
        elif audio_frame is not None:
            if val == 'audio':
                audio = audio_frame[0]
                # 处理音频帧（此处可以留空或根据需要处理）
                
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# 使用原始字符串
play_video(r'C:\Users\Administrator\Downloads\30660889659-1-192.mp4')


