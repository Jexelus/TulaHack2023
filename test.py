from datetime import datetime
def generate_analytic():
    mounths = [x for x in range(1, 13)]
    currentMonth = datetime.now().month
    return mounths, currentMonth

print(generate_analytic())