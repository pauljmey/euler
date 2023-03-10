
import datetime as dt
def main(start, end):
    count = 0

    d0 = dt.datetime(month=start[0], day=start[1], year=start[2])

    while True:
        cur_day, cur_month, cur_year = d0.day, d0.month, d0.year
        if cur_day == 1 and cur_month == 9:
            dt_str = d0.strftime("%A %d %m %Y")
            if 'Sunday' in dt_str:
                print(dt_str)
            hook = True

        if cur_day == 1 and d0.weekday() == 6:
            count += 1
        if cur_day == end[1] and cur_month == end[0] and cur_year == end[2]:
            break
        d0 += dt.timedelta(days=1)

    pass

    return count

if __name__ == "__main__":
    print(main(start=[1, 1, 1901], end=[12, 31, 2000] ))