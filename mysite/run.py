"""
执行命令
"""
import os

"""
1. 启动服务器 manage.py
"""
default_port = "8080"

base_command = "manage.py"

run_server_default = f"{base_command} runserver"

run_server_allow_other = f"{run_server_default} 0:0:0:0:{default_port}"


def run_server(command: str = base_command):
    res = os.popen(command)
    f = res.read()
    print(f)


if __name__ == '__main__':
    run_server()
