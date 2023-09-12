#include <iostream>
#include <WinSock2.h>

#pragma comment(lib, "ws2_32.lib")

int main() {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "Failed to initialize WinSock." << std::endl;
        return 1;
    }

    SOCKET clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (clientSocket == INVALID_SOCKET) {
        std::cerr << "Failed to create socket." << std::endl;
        WSACleanup();
        return 1;
    }

    sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(8080); // 服务器端口
    serverAddress.sin_addr.s_addr = inet_addr("172.16.12.58"); // 替换为服务器的IP地址
			if (connect(clientSocket, (sockaddr*)&serverAddress, sizeof(serverAddress)) == SOCKET_ERROR) {
        	std::cerr << "Failed to connect to server." << std::endl;
        	closesocket(clientSocket);
        	WSACleanup();
        	return 1;
    std::cout << "Connected to server." << std::endl;
	}
    char buffer[4096];
    int bytesRead;

    while (true) {
        std::cout << "Enter a command (or 'exit' to quit): ";
        std::cin.getline(buffer, sizeof(buffer));
        if (strcmp(buffer, "exit") == 0) {
            break;
        }
        send(clientSocket, buffer, strlen(buffer), 0);
        memset(buffer, 0, sizeof(buffer));
        bytesRead = recv(clientSocket, buffer, sizeof(buffer), 0);
        if (bytesRead <= 0) {
            break;
        }
        std::cout << "Server response: " << buffer << std::endl;
    }

    closesocket(clientSocket);
    WSACleanup();
    return 0;
}






