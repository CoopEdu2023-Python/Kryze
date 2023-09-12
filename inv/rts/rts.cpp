#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <limits>
#include <SDL.h>
#include <windows.h>
// 定义常数
const int WIDTH = 800;
const int HEIGHT = 600;
const double PI = 3.14159265358979323846;

// 向量类
class Vec3 {
public:
    double x, y, z;

    Vec3() : x(0), y(0), z(0) {}
    Vec3(double x, double y, double z) : x(x), y(y), z(z) {}

    Vec3 operator+(const Vec3& other) const {
        return Vec3(x + other.x, y + other.y, z + other.z);
    }

    Vec3 operator-(const Vec3& other) const {
        return Vec3(x - other.x, y - other.y, z - other.z);
    }

    Vec3 operator*(double scalar) const {
        return Vec3(x * scalar, y * scalar, z * scalar);
    }

    Vec3 operator/(double scalar) const {
        return Vec3(x / scalar, y / scalar, z / scalar);
    }

    double length() const {
        return std::sqrt(x * x + y * y + z * z);
    }

    Vec3 normalize() const {
        return (*this) / length();
    }

    double dot(const Vec3& other) const {
        return x * other.x + y * other.y + z * other.z;
    }

    Vec3 cross(const Vec3& other) const {
        return Vec3(y * other.z - z * other.y, z * other.x - x * other.z, x * other.y - y * other.x);
    }
};

// 射线类
class Ray {
public:
    Vec3 origin, direction;

    Ray(const Vec3& origin, const Vec3& direction) : origin(origin), direction(direction) {}
};

// 球体类
class Sphere {
public:
    Vec3 center;
    double radius;

    Sphere(const Vec3& center, double radius) : center(center), radius(radius) {}

    bool intersect(const Ray& ray, double& t) const {
        Vec3 oc = ray.origin - center;
        double a = ray.direction.dot(ray.direction);
        double b = 2.0 * oc.dot(ray.direction);
        double c = oc.dot(oc) - radius * radius;
        double discriminant = b * b - 4 * a * c;

        if (discriminant > 0) {
            double t1 = (-b - std::sqrt(discriminant)) / (2.0 * a);
            double t2 = (-b + std::sqrt(discriminant)) / (2.0 * a);
            if (t1 >= 0 || t2 >= 0) {
                t = (t1 < t2) ? t1 : t2;
                return true;
            }
        }

        return false;
    }
};

// 渲染函数
Vec3 trace(const Ray& ray, const std::vector<Sphere>& spheres) {
    double t_min = std::numeric_limits<double>::max();
    Vec3 color(0, 0, 0);

    for (size_t i = 0; i < spheres.size(); ++i) {
    	const Sphere& sphere = spheres[i]; 
        double t;
        if (sphere.intersect(ray, t) && t < t_min) {
            t_min = t;
            color = Vec3(1, 0, 0); // 在交点上涂上红色
        }
    }

    return color;
}
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow){
    SDL_Init(SDL_INIT_VIDEO);

    SDL_Window* window = SDL_CreateWindow("Ray Tracing", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WIDTH, HEIGHT, SDL_WINDOW_SHOWN);
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    std::vector<Sphere> spheres;
    spheres.push_back(Sphere(Vec3(0, 0, -5), 1.0));

    while (true) {
        SDL_Event e;
        if (SDL_PollEvent(&e) && e.type == SDL_QUIT)
            break;

        for (int y = 0; y < HEIGHT; ++y) {
            for (int x = 0; x < WIDTH; ++x) {
                double u = double(x) / WIDTH;
                double v = double(y) / HEIGHT;
                Vec3 direction(u * 2 - 1, v * 2 - 1, -1);
                direction = direction.normalize();

                Ray ray(Vec3(0, 0, 0), direction);
                Vec3 pixel_color = trace(ray, spheres);

                SDL_SetRenderDrawColor(renderer, int(255 * pixel_color.x), int(255 * pixel_color.y), int(255 * pixel_color.z), 255);
                SDL_RenderDrawPoint(renderer, x, y);
            }
        }

        SDL_RenderPresent(renderer);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
