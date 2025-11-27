import requests

# 添加请求头 模拟浏览器行为
user_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}
# 获取百度首页
response = requests.get("https://www.baidu.com", headers=user_header)
# 打印响应内容
print(response.text)
# 打印响应状态码
print(response.status_code)
with open("./baidu_index.html", mode="+ab") as f:
    f.write(response.content)
