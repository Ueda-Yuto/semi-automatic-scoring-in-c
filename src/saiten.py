import os
import subprocess

os.makedirs("../data/a_01/error", exist_ok=True)


def execute_cmd(cmd: str):
    result = (
        subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True).communicate()[0]
    ).decode("utf-8")
    return result


def main():
    cmd = "cd ../data/a_01 && ls | grep .c"  # <=ここにコマンドを当てはめる
    result = (
        subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True).communicate()[0]
    ).decode("utf-8")

    files = result.split("\n")
    for file in files:
        cmd = f"gcc ../data/a_01/{file}"
        res = execute_cmd(cmd)
        # print("result:" + res + ";")
        if res != "":
            print("error!!!!!")
            # _res = execute_cmd(f"mv ../data/a_01/{file} ../data/a_01/error/")
            # print(_res)


if __name__ == "__main__":
    main()
