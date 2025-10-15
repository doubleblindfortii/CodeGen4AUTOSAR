


if __name__ == '__main__':
    print("Hello, World!")
    import re

    text = "runnable3_subsystem.Delay.firstTrigger = time <= runnable3_subsystem.Delay.startTime + 0.5 * runnable3_subsystem.Delay.samplePeriod;"

    # 使用正则表达式来匹配以"="分割的部分，但是排除"<="，同时保留"<"号
    result = re.split(r'\s*=\s*', text, maxsplit=1)

    print(result)
