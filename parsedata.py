from collections import Counter
import re

# 定义所有日志文件的路径
log_file_paths = [
    r'E:\file_path1',
    r'E:\file_path2',
    r'E:\file_path3',
    r'E:\file_path4'
]

# 正则表达式用于匹配IP地址
ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

# 用于存储IP地址的列表
ip_addresses = []

# 遍历每个日志文件路径
for log_file_path in log_file_paths:
    # 打开并读取每个日志文件
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            # 使用正则表达式查找并提取每行中的第一个IP地址
            match = ip_pattern.search(line)
            if match:
                ip_addresses.append(match.group())

# 使用Counter统计每个IP地址的出现次数
ip_counts = Counter(ip_addresses)

# 获取按出现次数从大到小排序的列表
sorted_ip_counts = ip_counts.most_common()

# 打印统计结果
for ip, count in sorted_ip_counts:
    print(f"{ip}: {count}")