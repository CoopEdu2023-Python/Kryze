#include <iostream>
#include <vector>
#include <cmath>
const int WIDTH = 80; // 场景宽度
const int HEIGHT = 24; // 场景高度

// 表示场景的字符数组
char scene[WIDTH][HEIGHT];

// 表示光线的结构体
struct Ray {
    double x, y; // 光线的起点坐标
    double angle; // 光线的初始角度（弧度）

    Ray(double _x, double _y, double _angle) : x(_x), y(_y), angle(_angle) {}
};

// 初始化场景
void initializeScene() {
    for (int x = 0; x < WIDTH; ++x) {
        for (int y = 0; y < HEIGHT; ++y) {
            scene[x][y] = ' ';
        }
    }
}

// 在场景中设置一个点
void setPoint(int x, int y, char character) {
    if (x >= 0 && x < WIDTH && y >= 0 && y < HEIGHT) {
        scene[x][y] = character;
    }
}

// 绘制场景
void renderScene() {
    for (int y = 0; y < HEIGHT; ++y) {
        for (int x = 0; x < WIDTH; ++x) {
            std::cout << scene[x][y];
        }
        std::cout << std::endl;
    }
}

// 模拟光线传播和反射
void traceRays() {
    Ray ray(WIDTH / 2.0, HEIGHT / 2.0, 0.0); // 光线从场景中央水平开始

    while (ray.x >= 0 && ray.x < WIDTH && ray.y >= 0 && ray.y < HEIGHT) {
        setPoint(static_cast<int>(ray.x), static_cast<int>(ray.y), '*'); // 在光线路径上设置字符

        // 模拟光线的传播
        ray.x += std::cos(ray.angle);
        ray.y += std::sin(ray.angle);

        // 这里可以添加碰撞检测和反射规则，以改变光线的角度
    }
}

int main() {
    initializeScene(); // 初始化场景
    traceRays(); // 模拟光线传播
    renderScene(); // 绘制场景

    return 0;
}
