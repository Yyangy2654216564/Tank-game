'''
新增功能：
    1.完善音效类
    2.添加开场音效
    3.我方坦克发射子弹音效
'''
from pygame.sprite import Sprite


import pygame, time, random

screen_width = 700
screen_height = 500
Bk_color = pygame.Color(200, 155, 0)
TEXT_COLOR = pygame.Color(111, 0, 110)
#定义一个基类
class BaseItem(Sprite):
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

class Maingame():
    window = None
    my_tank = None
    Wall = None
    # 存储敌方坦克的列表
    enemyTanklist = []
    # 定义敌方坦克的数量
    enemyTankCount = 5
    # 存储我方子弹的列表
    myBulletlist = []
    #存储敌方子弹的列表
    enemyBulletlist = []
     #存储爆炸效果的列表
    explodelist = []
    #存储墙壁的列表
    walllist = []
    def __init__(self):
        pass

    # 开始游戏
    def starGame(self):
        # 加载主窗口
        # -初始化窗口
        pygame.display.init()
        # 设置窗口的大小及显示
        Maingame.window = pygame.display.set_mode([screen_width, screen_height])
        # 初始化我方坦克
        self.createMytank()
        # 初始化敌方坦克，并添加到列表中
        self.createEnemyTank()
        #初始化墙壁
        self.createWall()
        # 设置窗口的标题
        pygame.display.set_caption('坦克大战1.0')
        # 一直显示
        while True:
            # 使用坦克移动的速度慢一点
            time.sleep(0.02)
            # 给窗口设置填充色
            Maingame.window.fill(Bk_color)
            # 获取事件
            self.getEvent()
            # 绘制文字
            Maingame.window.blit(self.getTextSuface('敌方坦克剩余数量%d' % len(Maingame.enemyTanklist)), (10, 10))
            # 调用坦克显示的方法
            #判断我方坦克是否存活
            if Maingame.my_tank and Maingame.my_tank.live:
                Maingame.my_tank.displayTank()
            else:
                #删除我方坦克
                del Maingame.my_tank
                Maingame.my_tank = None
            # 循环遍历敌方坦克列表，展示敌方坦克
            self.blitEnemyTank()
            # 循环遍历显示我方坦克的子弹
            self.blitMyBullet()
            # 循环遍历敌方子弹列表，显示敌方子弹
            self.blitenemyBullet()
            # 循环遍历爆炸列表，展示爆炸效果
            self.blitExplode()
            #循环遍历墙壁列表来展示
            self.blitWall()
            # 调用移动方法
            # 如果坦克的开关是开启，才可以移动
            if Maingame.my_tank and Maingame.my_tank.live:
                if not Maingame.my_tank.stop:
                    Maingame.my_tank.move()
                    #检测我方坦克是否与墙壁发生碰撞
                    Maingame.my_tank.hitWall()
                    # 检测我方坦克是否与敌方坦克发生碰撞
                    Maingame.my_tank.myTank_hit_enemyTank()

            pygame.display.update()
    #循环遍历墙壁列表来展示
    def blitWall(self):
        for wall in Maingame.walllist:
            #判断墙壁是否存活
            if wall.live:
                #调用墙壁的显示方法
                wall.displayWall()
            else:
                #从墙壁列表移除
                Maingame.walllist.remove(wall)
            #调用墙壁的显示方法
            wall.displayWall()
    #初始化墙壁
    def createWall(self):
        for i in range(6):
           #初始化墙壁
          wall = Wall (i *150,220)
           #将墙壁添加到列表中
          Maingame.walllist.append(wall)
    #创建我方坦克的方法
    def createMytank(self):
        Maingame.my_tank = MyTank(350,300)
        #创建music对象
        music = Music('../img/start.wav')
        #播放音乐
        music.play()
    # 初始化敌方坦克，并添加到列表中
    def createEnemyTank(self):
        top = 100
        # 循环生成敌方坦克
        for i in range(Maingame.enemyTankCount):
            left = random.randint(100,200)
            speed = random.randint(1, 3)
            enemy = EnemyTank(left, top, speed)
            Maingame.enemyTanklist.append(enemy)
    #循环展示爆炸效果
    def blitExplode(self):
        for explode in Maingame.explodelist:
            #判断是否活着
            if explode.live:
                #展示
                explode.displayExplode()
            else:
                #在爆炸列表中移除
               Maingame.explodelist.remove(explode)
    # 循环遍历敌方坦克列表，展示敌方坦克
    def blitEnemyTank(self):
        for enemyTank in Maingame.enemyTanklist:
             #判断当前敌方坦克是否活着
         if enemyTank.live:
            enemyTank.displayTank()
            enemyTank.randMove()
            #调用检测是否与墙壁碰撞
            enemyTank.hitWall()
            #检测敌方坦克是否与我方坦克发生碰撞
            if Maingame.my_tank and Maingame.my_tank.live:
               enemyTank.enemyTank_hit_myTank()
            #发射子弹
            enemyBullet = enemyTank.shot()
            # 判断敌方子弹是否是None,如果不是None则加入敌方子弹列表中
            if enemyBullet:
            #将敌方子弹存储到敌方列表中
                Maingame.enemyBulletlist.append(enemyBullet)
         else:#不活着，从敌方坦克列表中移除
            Maingame.enemyTanklist.remove(enemyTank)

    # 循环遍历我方子弹存储列表
    def blitMyBullet(self):
        for myBullet in Maingame.myBulletlist:
            # 判断当前的子弹是否是活着的状态，如果是则进行显示及移动
            if myBullet.live:
                myBullet.displayBullet()
                # 调用子弹的移动方法
                myBullet.move()
                #调用检测我方子弹是否与敌方坦克发生碰撞!!!
                myBullet.myBullet_hit_enemyTank()
                # 检测我方子弹是否与墙壁碰撞
                myBullet.hitWall()
            # 否则在列表
            else:
                Maingame.myBulletlist.remove(myBullet)
    # 循环遍历敌方子弹列表，展示敌方子弹
    def blitenemyBullet(self):
        for enemyBullet in Maingame.enemyBulletlist:
            if enemyBullet.live: # 判断地方子弹是否存活
                enemyBullet.displayBullet()
                # 调用子弹的移动方法
                enemyBullet.move()
                #调用地方子弹与我方坦克碰撞的方法
                enemyBullet.enemyBullet_hit_myTank()
                #检测我方子弹是否与墙壁碰撞
                enemyBullet.hitWall()
            #否则在列表中删除
            else:
                Maingame.enemyBulletlist.remove(enemyBullet)
                # 结束游戏
    def endGame(self):
        print('END GAME '
              '-----------'
              'Reporting Officer'
              'Enemy situation detected 1.1 kilometers ahead'
              '########'
              'keep up with'
              )
        exit()

    # 左上角文字的绘制
    def getTextSuface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 查看所有的字体
        # print(pygame.font.get_fonts())
        # 获取字体font对象
        font = pygame.font.SysFont('kaiti', 18)
        # 绘制文字信息
        textSurface = font.render(text, True, TEXT_COLOR)
        return textSurface

    # 获取事件
    def getEvent(self):
        # 获取所有事件
        eventlist = pygame.event.get()
        # 遍历事件
        for event in eventlist:
            # 判断按下的键是关闭还是键盘按下
            # 如果按的是退出，关闭窗口
            if event.type == pygame.QUIT:
                self.endGame()
            # 如果是键盘的按下键
            if event.type == pygame.KEYDOWN:
                #当坦克不存在或者死亡
                if not Maingame.my_tank:
                   #判断按下的是Esc键，让坦克重生
                  if event.key == pygame.K_ESCAPE:
                      # 我方坦克重生及调用创建坦克的方法
                      self.createMytank()
                if Maingame.my_tank and Maingame.my_tank.live:
                    if event.type == pygame.KEYDOWN:
                        # 判断键盘按的是上，下，左，右
                        if event.key == pygame.K_LEFT:
                            # 切换方向
                            Maingame.my_tank.direction = 'L'
                            # 修改坦克的开关状态
                            Maingame.my_tank.stop = False
                            # Maingame.my_tank.move()
                            print("按下左键，坦克向左移动")
                        elif event.key == pygame.K_RIGHT:
                            Maingame.my_tank.direction = 'R'
                            Maingame.my_tank.stop = False
                            # Maingame.my_tank.move()
                            print("按下右键，坦克向右移动")
                        elif event.key == pygame.K_UP:
                            Maingame.my_tank.direction = 'U'
                            Maingame.my_tank.stop = False
                            # Maingame.my_tank.move()
                            print("按下上键，坦克向上移动")
                        elif event.key == pygame.K_DOWN:
                            Maingame.my_tank.direction = 'D'
                            Maingame.my_tank.stop = False
                            # Maingame.my_tank.move()
                            print("按下下键，坦克向下移动")

                        elif event.key == pygame.K_SPACE:
                            print('发射子弹')
                            # 如果当前我方子弹列表的大小，小于等于3时候才可以创建
                            if len(Maingame.myBulletlist) < 1:
                                # 创建我方坦克发射的子弹
                                myBullet = Bullet(Maingame.my_tank)
                                Maingame.myBulletlist.append(myBullet)
                                #我方坦克发射子弹添加音效
                                music = Music('../img/hit.wav')
                                music.play()

            # 松开方向键，坦克停止移动，修改坦克的开关状态
            if event.type == pygame.KEYUP:
                # 判断松开的键是上，下，左，右时才停止坦克的移动
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN \
                        or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    if Maingame.my_tank and Maingame.my_tank.live:
                       Maingame.my_tank.stop = True


class Tank(BaseItem):
    # 添加距离左边left 距离上边top
    def __init__(self, left, top):
        # 保存加载的图片
        self.images = {
            'U': pygame.image.load('../img/p1tankU.gif'),
            'D': pygame.image.load('../img/p1tankD.gif'),
            'L': pygame.image.load('../img/p1tankL.gif'),
            'R': pygame.image.load('../img/p1tankR.gif'),

        }
        # 方向
        self.direction = 'L'
        # 根据当前图片的方向获取图片 surface
        self.image = self.images[self.direction]
        # 根据图片获取区域
        self.rect = self.image.get_rect()
        # 设置区域的left 和top
        self.rect.left = left
        self.rect.top = top

        # 速度 决定移动的快慢
        self.speed = 4
        # 坦克移动的开关
        self.stop = True
        #是否活着
        self.live = True
        #新增加属性原来坐标
        self.oldLeft = self.rect.left
        self.oldLeft = self.rect.top

    # 移动
    def move(self):
        #移动后记录原始的坐标
        self.oldLeft = self.rect.left
        self.oldTop  = self.rect.top
        # 判断坦克的方向进行移动
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < screen_width:
                self.rect.left += self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < screen_height:
                self.rect.top += self.speed

    # 射击
    def shot(self):
        return Bullet(self)
    #
    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop
    #检测坦克是否与墙壁发生碰撞
    def hitWall(self):
        for wall in Maingame.walllist:
         if pygame.sprite.collide_rect(self,wall):
             #将坐标设置为移动之前的坐标
             self.stay()
    # 展示坦克的方法
    def displayTank(self):
        # 获取展示的对象
        self.image = self.images[self.direction]
        # 调用blit方法展示
        Maingame.window.blit(self.image, self.rect)


# 我方坦克
class MyTank(Tank):
    def __init__(self,left,top):
        super(MyTank,self).__init__(left,top)

    #检测我方坦克与敌方坦克发生碰撞
    def myTank_hit_enemyTank(self):
        #循环遍历敌方坦克列表
        for enemyTank in Maingame.enemyTanklist:
            if pygame.sprite.collide_rect(self,enemyTank):
                self.stay()
# 敌方坦克
class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        #调用父类的初始方法
        super(EnemyTank,self).__init__(left,top)
        # 加载图片集
        self.images = {
            'U': pygame.image.load('../img/enemy1U.gif'),
            'D': pygame.image.load('../img/enemy1D.gif'),
            'L': pygame.image.load('../img/enemy1L.gif'),
            'R': pygame.image.load('../img/enemy1R.gif'),
        }
        # 方向,随机生成坦克的方向
        self.direction = self.randDirection()
        # 根据方向获取图片
        self.image = self.images[self.direction]
        # 区域
        self.rect = self.image.get_rect()
        # 对left和top进行赋值
        self.rect.left = left
        self.rect.left = top
        # 速度
        self.speed = speed
        # 移动开关键
        self.flag = True
        # 新增步数变量
        self.step = 20

    #敌方坦克与我方坦克是否发生碰撞
    def enemyTank_hit_myTank(self):
        if pygame.sprite.collide_rect(self,Maingame.my_tank):
            self.stay()
    # 随机生成敌方坦克的方向
    def randDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'

    # 敌方坦克随机移动
    def randMove(self):
        if self.step <= 0:
            # 修改方向
            self.direction = self.randDirection()
            # 让步数复位
            self.step = 100
        else:
            self.move()
            # 让步数递减
            self.step -= 1

    # 重写shot()
    def shot(self):
        # 随机生成100以内的数
        num = random.randint(1,100)
        if num < 2:
            return Bullet(self)
# 子弹类
class Bullet(BaseItem):
    def __init__(self, tank):
        # 加载图片
        self.image = pygame.image.load('../img/enemymissile.gif')
        # 坦克的方向决定子弹的方向
        self.direction = tank.direction
        # 获取区域
        self.rect = self.image.get_rect()
        # 子弹的left和top与方向有关
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        # 子弹的速度
        self.speed = 10
        # 子弹的状态，是否碰到墙壁，如果碰到墙壁，修改此状态
        self.live = True

    # 移动
    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                # 修改子弹的状态
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < screen_width:
                self.rect.left += self.speed
            else:
                # 修改子弹的状态
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < screen_height:
                self.rect.top += self.speed
            else:
                # 修改子弹的状态
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                # 修改子弹的状态
                self.live = False

    #子弹是否碰撞墙壁
    def hitWall(self):
        #循环遍历墙壁列表
        for wall in Maingame.walllist:
            if pygame.sprite.collide_rect(self,wall):
                #修改子弹的生存状态，让子弹消失
                self.live = False
                #墙壁的生命值减小
                wall.hp-=1
                if wall.hp<=0:
                    #修改墙壁的生存状态
                    wall.live = False
    # 展示子弹的方法
    def displayBullet(self):
        # 将图片surface加载到窗口
        Maingame.window.blit(self.image, self.rect)
    #我方子弹与敌方坦克的碰撞
    def myBullet_hit_enemyTank(self):
        #循环遍历敌方坦克列表，判断是否发生碰撞
        for enemyTank in Maingame.enemyTanklist:
           if pygame.sprite.collide_rect(enemyTank,self):
               #修改敌方坦克和我方子弹的状态
               enemyTank.live = False
               self.live = False
               #创建爆炸的对象
               explod = Explode(enemyTank)
               #将爆炸添加到爆炸列表中
               Maingame.explodelist.append(explod)
    #敌方子弹与我方坦克的碰撞
    def enemyBullet_hit_myTank(self):
        if Maingame.my_tank and Maingame.my_tank.live:
            if pygame.sprite.collide_rect(Maingame.my_tank, self):
                # 产生爆炸对象
                explode = Explode(Maingame.my_tank)
                # 将爆炸对象添加到爆炸列表中
                Maingame.explodelist.append(explode)
                # 修改敌方子弹与我方坦克的状态
                self.live = False
                Maingame.my_tank.live = False

class Wall():
    def __init__(self,left,top):
       #加载墙壁图片
       self.image = pygame.image.load('../img/steels.gif')
       #获取墙壁的区域
       self.rect = self.image.get_rect()
       #设置位置(left,top)
       self.rect.left = left
       self.rect.top = top
       #是否存活
       self.live = True
       #设置生命值
       self.hp=3
    # 展示墙壁的方法
    def displayWall(self):
        Maingame.window.blit(self.image,self.rect)


class Explode():
    def __init__(self,tank):
        #爆炸的位置由当前子弹打中的坦克位置决定
       self.rect = tank.rect
       self.images=[
           pygame.image.load('../img/blast0.gif'),
           pygame.image.load('../img/blast1.gif'),
           pygame.image.load('../img/blast2.gif'),
           pygame.image.load('../img/blast3.gif'),
           pygame.image.load('../img/blast4.gif'),
       ]
       self.step=0
       self.image = self.images[self.step]
       # 是否活着
       self.live = True
    #展示爆炸效果的方法
    def displayExplode(self):
        if self.step<len(self.images):
            #根据索引获取爆炸对象
            self.image = self.images[self.step]
            self.step+=1
        #添加到主窗口
            Maingame.window.blit(self.image,self.rect)
        else:
          #修改活着的状态
          self.live = False
          self.step = 0


class Music():
    def __init__(self,filename):
        self.filename = filename
        #初始化音乐混合器
        pygame.mixer.init()
        #加载音乐
        pygame.mixer.music.load(self.filename)
    # 播放音乐
    def play(self):
        pygame.mixer.music.play()


if __name__ == '__main__':
    Maingame().starGame()
    # Maingame().getTextSuface()
