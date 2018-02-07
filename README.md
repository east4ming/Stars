# Stars
Show stars.

## 说明

1. 在屏幕上显示一系列整齐排列的星星
2. 让星星分布更逼真, 随机放置星星.

## 游戏屏幕相关

### screen全局变量

- 宽度/高度
- 背景颜色

### 初始化

`pygame.display.set_mode()`

### fill函数

`screen.fill()`

## 星星相关

### 星星类

#### 初始化函数

> 继承 `pygame.sprite.Sprite`类

1. 初始化超类
2. 初始化`screen`
3. 加载图片 → 得到星星的Surface
4. 通过Surface的`get_rect()`函数获取星星的rect
5. 星星rect的x, y 分别为星星的宽和高(空一个星星的距离)

#### 绘制函数

调用screen的blit函数, 绘制星星的Surface到rect位置.

### 星星相关函数

#### 获取一行/列的星星数

- 留出一个星星的空白
- 每个星星占用2个星星大小的位置(宽度高度都是)

#### 创建星星Group

1. 先初始化一个Star()对象
2. 访问其rect属性获取星星的宽度和高度
3. 调用上边的函数计算每行/列可以绘制多少个
4. 2层嵌套循环, 
    1. 初始化一个Star()对象, 
    2. 修改该对象的x/y坐标,
    3. 将每个星星加入到Group中.

##  主函数

1. `pygame.init()`
2. 初始化screen
3. 游戏标题
4. 创建stars Group
5. 调用`star_func.create_stars`往stars Group里添加一个个star

### 主循环

1. 捕获事件并处理
    1. 碰到QUIT事件就退出
2. 填充屏幕背景
3. 调用`stars.draw(the_screen)`绘制所有星星
4. 显示

