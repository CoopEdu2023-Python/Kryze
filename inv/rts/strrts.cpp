#include <iostream>
#include <vector>
#include <cmath>

const int WIDTH = 80; // 文本字符宽度
const int HEIGHT = 24; // 文本字符高度

// 定义向量类
class Vec2 {
public:
    double x, y;

    Vec2() : x(0), y(0) {}
    Vec2(double x, double y) : x(x), y(y) {}

    Vec2 operator+(const Vec2& other) const {
        return Vec2(x + other.x, y + other.y);
    }

    Vec2 operator-(const Vec2& other) const {
        return Vec2(x - other.x, y - other.y);
    }

    Vec2 operator*(double scalar) const {
        return Vec2(x * scalar, y * scalar);
    }

    double dot(const Vec2& other) const {
        return x * other.x + y * other.y;
    }

    double length() const {
        return std::sqrt(x * x + y * y);
    }
};

// 场景类
class Scene {
public:
    char pixels[WIDTH][HEIGHT];

    Scene() {
        for (int x = 0; x < WIDTH; ++x) {
            for (int y = 0; y < HEIGHT; ++y) {
                pixels[x][y] = ' ';
            }
        }
    }

    void setPixel(int x, int y, char pixel) {
        if (x >= 0 && x < WIDTH && y >= 0 && y < HEIGHT) {
            pixels[x][y] = pixel;
        }
    }

    void render() const {
        for (int y = 0; y < HEIGHT; ++y) {
            for (int x = 0; x < WIDTH; ++x) {
                std::cout << pixels[x][y];
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    Scene scene;

    // 设置光线的起始点和方向
    Vec2 origin(40, 12);
    Vec2 direction(-1, 0);

    // 模拟光线传播
    for (int x = 0; x < WIDTH; ++x) {
        for (int y = 0; y < HEIGHT; ++y) {
            Vec2 pixel_center(x + 0.5, y + 0.5);
            Vec2 ray = pixel_center - origin;
            double distance = ray.length();

            // 检查光线是否命中一个对象（在此示例中未进行碰撞检测）

            // 根据距离选择字符
            char pixel;
            if (distance < 10) {
                pixel = '@';
            } else if (distance < 20) {
                pixel = '#';
            } else if (distance < 30) {
                pixel = '*';
            } else {
                pixel = ' ';
            }

            scene.setPixel(x, y, pixel);
        }
    }

    scene.render();

    return 0;
}
