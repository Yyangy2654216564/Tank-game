'''
新增功能：
    左上角文字绘制：
    左上角输出的敌方坦克的数量
'''
import pygame
screen_width = 700
screen_height = 500
Bk_color = pygame.Color(0,0,0)
TEXT_COLOR=pygame.Color(255,0,0)

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
            #获取事件
            self.getEvent()
            #绘制文字
            Maingame.window.blit(self.getTextSuface('敌方坦克剩余数量%d'%6),(10,10))
            pygame.display.update()

    #结束游戏
    def  endGame(self):
        print('END GAME '
              '-----------'
              'Reporting Officer'
             'Enemy situation detected 1.1 kilometers ahead'
              '########'
              'keep up with'
        )
        exit()
    #左上角文字的复制
    def getTextSuface(self,text):
        # 初始化字体模块
        pygame.font.init()
        #查看所有的字体
        # print(pygame.font.get_fonts())
        # 获取字体font对象
        font=pygame.font.SysFont('kaiti',18)
        #绘制文字信息
        textSurface = font.render(True,TEXT_COLOR)
        return textSurface
    # 获取事件
    def getEvent(self):
        #获取所有事件
        eventlist = pygame.event.get()
        #遍历事件
        for event in eventlist:
            #判断按下的键是关闭还是键盘按下
            #如果按的是退出，关闭窗口
           if event.type == pygame.QUIT:
              self.endGame()
            # 如果是键盘的按下键
           if event.type == pygame.KEYDOWN:
               #判断键盘按的是上，下，左，右
               if event.key == pygame.K_LEFT:
                   print("按下左键，坦克向左移动")
               elif event.key == pygame.K_RIGHT:
                   print("按下右键，坦克向右移动")
               elif event.key == pygame.K_UP:
                   print("按下上键，坦克向上移动")
               elif event.key == pygame.K_DOWN:
                   print("按下下键，坦克向下移动")

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
    Maingame().getTextSuface()