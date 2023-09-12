#include <iostream>
#include <vector>
#include <cmath>
const int WIDTH = 80; // �������
const int HEIGHT = 24; // �����߶�

// ��ʾ�������ַ�����
char scene[WIDTH][HEIGHT];

// ��ʾ���ߵĽṹ��
struct Ray {
    double x, y; // ���ߵ��������
    double angle; // ���ߵĳ�ʼ�Ƕȣ����ȣ�

    Ray(double _x, double _y, double _angle) : x(_x), y(_y), angle(_angle) {}
};

// ��ʼ������
void initializeScene() {
    for (int x = 0; x < WIDTH; ++x) {
        for (int y = 0; y < HEIGHT; ++y) {
            scene[x][y] = ' ';
        }
    }
}

// �ڳ���������һ����
void setPoint(int x, int y, char character) {
    if (x >= 0 && x < WIDTH && y >= 0 && y < HEIGHT) {
        scene[x][y] = character;
    }
}

// ���Ƴ���
void renderScene() {
    for (int y = 0; y < HEIGHT; ++y) {
        for (int x = 0; x < WIDTH; ++x) {
            std::cout << scene[x][y];
        }
        std::cout << std::endl;
    }
}

// ģ����ߴ����ͷ���
void traceRays() {
    Ray ray(WIDTH / 2.0, HEIGHT / 2.0, 0.0); // ���ߴӳ�������ˮƽ��ʼ

    while (ray.x >= 0 && ray.x < WIDTH && ray.y >= 0 && ray.y < HEIGHT) {
        setPoint(static_cast<int>(ray.x), static_cast<int>(ray.y), '*'); // �ڹ���·���������ַ�

        // ģ����ߵĴ���
        ray.x += std::cos(ray.angle);
        ray.y += std::sin(ray.angle);

        // ������������ײ���ͷ�������Ըı���ߵĽǶ�
    }
}

int main() {
    initializeScene(); // ��ʼ������
    traceRays(); // ģ����ߴ���
    renderScene(); // ���Ƴ���

    return 0;
}
