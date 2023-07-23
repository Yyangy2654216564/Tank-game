'''
新增功能：
    加载主窗口
    pygame官方网址：www.pygame.org
'''
import pygame
screen_width = 700
screen_height = 500
Bk_color = pygame.Color(0,0,0)

class Maingame():
    window = None
    def __init__(self):
        pass
    #开始游戏
    def starGame(self):
        #加载主窗口
        #-初始化窗口
        pygame.display.init()
        #设置窗口的大小及显示
        Maingame.window = pygame.display.set_mode([screen_width,screen_height])
        #设置窗口的标题
        pygame.display.set_caption('坦克大战1.0')
        #一直显示
        while True:
            #给窗口设置填充色
            Maingame.window.fill(Bk_color)
            pygame.display.update()

    #结束游戏
    def  endGame(self):
        pass

class Tank():
    def __init__(self):
        pass
    #移动
    def move(self):
        pass

    #射击
    def shot(self):
        pass
    #展示坦克的方法
    def displayTank(self):
        pass
# 我方坦克
class MyTank(Tank):
    def __init__(self):
        pass

# 敌方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass
#子弹类
class Bullet():
    def __init__(self):
        pass
    #移动
    def move(self):
        pass
    #展示子弹的方法
    def displayBullet(self):
        pass
class Wall():
    def __init__(self):
        pass
    #展示墙壁的方法
    def displayWall(self):
        pass
class Explode():
    def __init__(self):
        pass

    def displayExplode(self):
        pass
class Music():
    def __init__(self):
        pass
    #播放音乐
    def play(self):
        pass
if __name__ =='__main__':
    Maingame().starGame()
