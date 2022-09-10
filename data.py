import datetime

now  = datetime.datetime.now()

print(now)
print(f"Today is {now:%d} {now:%B} {now:%Y}")
print(f"{now:%H} {now:%M}")