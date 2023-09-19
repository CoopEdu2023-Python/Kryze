#include <iostream>
#include <vector>

using namespace std;

// 大整数乘法函数
vector<int> multiply(vector<int>& num1, int num2) {
    vector<int> result;
    int carry = 0;
    for (int i = 0; i < num1.size() || carry; i++) {
        if (i == result.size()) {
            result.push_back(0);
        }
        
        long long product = (long long)num1[i] * num2 + carry;
        result[i] = product % 10;
        carry = product / 10;
    }
    
    while (result.size() > 1 && result.back() == 0) {
        result.pop_back();
    }
    
    return result;
}

// 计算阶乘
vector<int> factorial(int n) {
    vector<int> result;
    result.push_back(1);
    
    for (int i = 2; i <= n; i++) {
        result = multiply(result, i);
    }
    
    return result;
}

int main() {
    int n;
    cout << "输入要计算阶乘的数：";
    cin >> n;

    vector<int> result = factorial(n);

    cout << n << "的阶乘是：";
    for (int i = result.size() - 1; i >= 0; i--) {
        cout << result[i];
    }
    cout << endl;

    return 0;
}
