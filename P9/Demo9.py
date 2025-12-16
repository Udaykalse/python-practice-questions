def count_Failed(logs):
    return logs.count('fail')

print(count_Failed(["success","fail","fail"]))