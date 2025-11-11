import datetime

def create_test_file():
    """创建一个测试文件并写入内容"""
    # 定义要创建的文件名
    file_name = "test_output.txt"
    
    try:
        # 获取当前时间
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 打开文件并写入内容 (如果文件已存在，会覆盖内容)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(f"这是一个由 Python 脚本自动生成的测试文件。\n")
            f.write(f"生成时间: {current_time}\n")
            f.write(f"目的: 验证 Git 仓库的克隆和提交功能。\n")
        
        print(f"✅ 成功！测试文件 '{file_name}' 已创建。")
        print(f"文件内容预览:\n---")
        with open(file_name, 'r', encoding='utf-8') as f:
            print(f.read())
        print(f"---")

    except Exception as e:
        print(f"❌ 失败！创建文件时出错: {e}")

if __name__ == "__main__":
    print("开始执行测试用例...")
    create_test_file()
