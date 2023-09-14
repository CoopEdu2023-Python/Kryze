#include <iostream>
#include <curl/curl.h>
#include <json/json.h>

// ChatGPT API endpoint
const std::string API_URL = "https://api.openai.com/v1/engines/davinci-codex/completions";

// Your API key
const std::string API_KEY = "YOUR_API_KEY";

// The prompt text you want to send to ChatGPT
const std::string PROMPT_TEXT = "Translate the following English text to French: 'Hello, how are you?'";

// Callback function to handle the HTTP response
size_t WriteCallback(void* contents, size_t size, size_t nmemb, std::string* output) {
    size_t totalSize = size * nmemb;
    output->append(static_cast<char*>(contents), totalSize);
    return totalSize;
}

int main() {
    // Initialize libcurl
    CURL* curl = curl_easy_init();
    if (!curl) {
        std::cerr << "Failed to initialize libcurl." << std::endl;
        return 1;
    }

    // Set up the HTTP request headers
    struct curl_slist* headers = nullptr;
    headers = curl_slist_append(headers, ("Authorization: Bearer " + API_KEY).c_str());
    headers = curl_slist_append(headers, "Content-Type: application/json");

    // Set up the JSON data for the request
    Json::Value jsonRequest;
    jsonRequest["prompt"] = PROMPT_TEXT;
    jsonRequest["max_tokens"] = 50;  // Adjust the max tokens as needed

    // Convert JSON to string
    std::string jsonData = jsonRequest.toStyledString();

    // Set the HTTP request options
    curl_easy_setopt(curl, CURLOPT_URL, API_URL.c_str());
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, jsonData.c_str());

    // Set the callback function to handle the response
    std::string response;
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);

    // Perform the HTTP request
    CURLcode res = curl_easy_perform(curl);

    // Check for errors
    if (res != CURLE_OK) {
        std::cerr << "Failed to perform HTTP request: " << curl_easy_strerror(res) << std::endl;
    } else {
        // Parse the JSON response
        Json::Value jsonResponse;
        Json::CharReaderBuilder reader;
        std::istringstream iss(response);
        std::string parseError;
        Json::parseFromStream(reader, iss, &jsonResponse, &parseError);

        if (!parseError.empty()) {
            std::cerr << "Failed to parse JSON response: " << parseError << std::endl;
        } else {
            // Extract and print the generated text
            std::string generatedText = jsonResponse["choices"][0]["text"].asString();
            std::cout << "Generated Text: " << generatedText << std::endl;
        }
    }

    // Clean up libcurl and free resources
    curl_easy_cleanup(curl);
    curl_slist_free_all(headers);

    return 0;
}

