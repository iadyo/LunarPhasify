import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

import scienceplots
plt.style.use(['science', 'notebook'])

def julian_day(year, month, day):
    L1 = year + 4716 - int((14 - month) / 12)
    M1 = (month + 9) % 12
    G = int(3/4 * int((L1 + 184) / 100)) - 38
    return int(365.25 * L1) + int(30.6 * M1 + 0.4) + day - G - 1402

def lunar_phase(date):
    year, month, day = date.year, date.month, date.day
    JD = julian_day(year, month, day)
    D = (297.85 + 12.19074912 * (JD - 2451545)) % 360

    if D < 0: D += 360
    return (np.sin(np.radians(D)) + 1) / 2

if __name__ == '__main__':
    start_date = datetime.now()
    end_date = start_date + timedelta(days=31)
    dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days)]
    phases = [lunar_phase(date) for date in dates]

    plt.figure(figsize=(10, 7))
    plt.plot(dates, phases)
    plt.ylim(-0.2, 1.2)
    plt.scatter(dates, phases, color='red', marker='o')
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d/%m'))
    plt.xticks(rotation=50)
    plt.show()