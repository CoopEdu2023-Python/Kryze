import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # 加载火星车图片
        self.image = tk.PhotoImage(file='mars_rover.png')

        # 创建canvas放置图片
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()

        # 初始化火星车位置和轨迹变量
        self.x = 200
        self.y = 200
        self.track = None

        # 在canvas上添加图片
        self.rover = self.canvas.create_image(self.x, self.y, image=self.image)

        # 绑定键盘事件
        self.bind_all('<Key>', self.move)

        self.pre_x = self.x
        self.pre_y = self.y

    def move(self, event):
        key = event.keysym

        # 根据按键移动火星车
        if key == 'Up':
            self.y -= 10
        elif key == 'Down':
            self.y += 10
        elif key == 'Left':
            self.x -= 10
        elif key == 'Right':
            self.x += 10

        current_track = self.track

        self.track = self.canvas.create_line(self.pre_x, self.pre_y, self.x, self.y, fill='blue')

        # 删除旧轨迹,绘制新蓝色轨迹线条
        if current_track:
            self.canvas.delete(current_track)
            self.track = None

        # 移动图片到新位置
        self.canvas.coords(self.rover, self.x, self.y)

        # 记录上一点坐标
        self.pre_x = self.x
        self.pre_y = self.y


if __name__ == '__main__':
    app = App()
    app.mainloop()