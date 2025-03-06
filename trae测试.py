import schedule
import time
from twilio.rest import Client

# ========== 1) Twilio 配置部分 ==========
# 你需要先去 https://www.twilio.com/ 注册并获取账号的 SID 和 Auth Token
ACCOUNT_SID = "ACc141b9057fded3ab171c83686ed1a6d9"
AUTH_TOKEN = "79bc7b2757c53c262befc108510ac8a0"
FROM_NUMBER = "+12189554573"  # 形如 "+1234567890"
TO_NUMBER = "+6591910066"     # 形如 "+86138xxxx8888"（国内加上 +86）

# 初始化 Twilio 客户端
client = Client(ACCOUNT_SID, AUTH_TOKEN)


def make_a_call():
    """
    拨打电话的示例函数。
    这里是最简单的示例：当电话接通后，会播放一个 TwiML 的默认提示音，或者你也可以指定一个 mp3。
    详细可见 Twilio 文档:https://www.twilio.com/docs/voice/make-calls
    """
    call = client.calls.create(
        url="https://handler.twilio.com/twiml/EHxxxxxx",  # 这里可以是你自己的TwiML URL
        to=TO_NUMBER,
        from_=FROM_NUMBER
    )
    print(f"发起拨打电话,Call SID: {call.sid}")


def check_pool():
    """
    模拟检查池子可用额度。
    这里只是打个假数据占位,比如我们说“如果pool的利用率< 100% 就表示有额度”。
    """
    # ---------------- 这里是后面要替换成真实数据的地方 ----------------
    fake_utilization_rate = 98.0  # 假设使用率是 98%，表示还有 2% 的空间
    # -------------------------------------------------------------

    print(f"[模拟数据] 当前池子利用率: {fake_utilization_rate}%")

    # 如果利用率小于 100%，就说明有空余额度 -> 拨打电话提醒
    if fake_utilization_rate < 100.0:
        print("检测到池子还有额度，准备拨打电话提醒...")
        make_a_call()
    else:
        print("池子满了，没有可用额度。")


def job():
    """
    这是 schedule 定时要执行的任务函数。
    """
    print("开始检查池子状态...")
    check_pool()
    print("检查完毕。\n")


# ========== 2) 定时调度部分 ==========
# 例如每 1 分钟执行一次 job()，实际可以根据需求调整
schedule.every(10).seconds.do(job)


if __name__ == "__main__":
    print("脚本启动成功，开始执行定时任务...\n")
    # 让 schedule 一直运行
    while True:
        schedule.run_pending()
        time.sleep(1)
