'''
新增功能：
    1.我方坦克切换方向
    2.我方坦克移动
'''
import pygame
screen_width = 700
screen_height = 500
Bk_color = pygame.Color(0,0,0)
TEXT_COLOR=pygame.Color(255,0,0)

class Maingame():
    window = None
    my_tank = None
    def __init__(self):
        pass
    #开始游戏
    def starGame(self):
        #加载主窗口
        #-初始化窗口
        pygame.display.init()
        #设置窗口的大小及显示
        Maingame.window = pygame.display.set_mode([screen_width,screen_height])
        #初始化我方坦克
        Maingame.my_tank=Tank(400,350)
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
            #调用坦克显示的方法
            Maingame.my_tank.displayTank()
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
    #左上角文字的绘制
    def getTextSuface(self,text):
        # 初始化字体模块
        pygame.font.init()
        #查看所有的字体
        # print(pygame.font.get_fonts())
        # 获取字体font对象
        font=pygame.font.SysFont('kaiti',18)
        #绘制文字信息
        textSurface = font.render(text,True,TEXT_COLOR)
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
                   #切换方向
                   Maingame.my_tank.direction='L'
                   Maingame.my_tank.move()
                   print("按下左键，坦克向左移动")
               elif event.key == pygame.K_RIGHT:
                   Maingame.my_tank.direction='R'
                   Maingame.my_tank.move()
                   print("按下右键，坦克向右移动")
               elif event.key == pygame.K_UP:
                   Maingame.my_tank.direction='U'
                   Maingame.my_tank.move()
                   print("按下上键，坦克向上移动")
               elif event.key == pygame.K_DOWN:
                   Maingame.my_tank.direction='D'
                   Maingame.my_tank.move()
                   print("按下下键，坦克向下移动")

class Tank():
    #添加距离左边left 距离上边top
    def __init__(self,left,top):
        #保存加载的图片
        self.images={
            'U':pygame.image.load('../img/p1tankU.gif'),
            'D':pygame.image.load('../img/p1tankD.gif'),
            'L':pygame.image.load('../img/p1tankL.gif'),
            'R':pygame.image.load('../img/p1tankR.gif'),

        }
        #方向
        self.direction='L'
        #根据当前图片的方向获取图片 surface
        self.image = self.images[self.direction]
        #根据图片获取区域
        self.rect = self.image.get_rect()
        #设置区域的left 和top
        self.rect.left = left
        self.rect.top = top

        #速度 决定移动的快慢
        self.speed = 10
    #移动
    def move(self):
        #判断坦克的方向进行移动
        if self.direction == 'L':
            self.rect.left -= self.speed
        elif self.direction == 'U':
            self.rect.top -= self.speed
        elif self.direction == 'R':
            self.rect.left += self.speed
        elif self.direction  == 'D':
            self.rect.top += self.speed

    #射击
    def shot(self):
        pass
    #展示坦克的方法
    def displayTank(self):
        #获取展示的对象
        self.imge = self.images[self.direction]
        #调用bllit方法展示3
        Maingame.window.blit(self.imge,self.rect)
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
    # Maingame().getTextSuface()