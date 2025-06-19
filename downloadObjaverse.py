import os
import json
import objaverse
import time
import argparse

script_dir = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(description="Stable download of the Objaverse dataset under poor network conditions | 在较差的网络环境下稳定下载Objaverse数据集")
parser.add_argument("--json_path", type=str, required=True, help="JSON 文件(下载列表)的路径")
parser.add_argument("--todo_path", type=str, default=script_dir, help="生成 todo.txt 的路径，默认与脚本在同一目录下")
parser.add_argument("--done_path", type=str, default=script_dir, help="生成 done.txt 的路径，默认与脚本在同一目录下")
parser.add_argument("-d", "--delete", action="store_true", help="在全部下载完成后删除 todo.txt 与 done.txt")
args = parser.parse_args()

json_path = args.json_path
todo_path = os.path.join(args.todo_path,"todo.txt")
done_path = os.path.join(args.done_path,"done.txt")

if not os.path.exists(todo_path):
    with open(json_path, "r") as f:
        data = json.load(f)

    if isinstance(data, dict):
        object_uids = list(data.keys())
    elif isinstance(data, list):
        object_uids = data
    else:
        raise ValueError("不支持的 JSON 格式：必须是 dict 或 list")

    with open(todo_path, "w") as f:
        for uid in object_uids:
            f.write(uid + "\n")
    print(f"初始化待下载列表，共 {len(object_uids)} 个对象")

def load_uids(path):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_uids(path, uids):
    with open(path, "w") as f:
        for uid in uids:
            f.write(uid + "\n")

while True:
    todo_uids = load_uids(todo_path)
    if not todo_uids:
        print("全部对象下载完成！")
        if args.delete:
            for path in [todo_path, done_path]:
                if os.path.exists(path):
                    os.remove(path)
                    print(f"已删除文件：{path}")
        break

    uid = todo_uids[0]
    print(f"开始下载对象 {uid}，剩余 {len(todo_uids)} 个")

    try:
        objaverse.load_objects(uids=[uid], download_processes=1)
        print(f"对象 {uid} 下载成功")

        with open(done_path, "a") as f_done:
            f_done.write(uid + "\n")

        todo_uids.pop(0)
        save_uids(todo_path, todo_uids)

    except Exception as e:
        print(f"对象 {uid} 下载失败，错误：{e}")
        print("等待5秒后重试...")
        time.sleep(5)
