from datetime import datetime, timedelta

# 当前日期
now = datetime.now()

# 计算 x 天前的日期，例如 x=10000
x = 49710
date_x_days_ago = now - timedelta(days=x)

# 输出结果
print(f"{x} 天前的日期是：", date_x_days_ago)
