# Meal Time:
#
# Notify's the user whether they need to eat in the given time of the day
#
# This version supports 12-hour times too


def main():
    # Prompt the user for time
    time = input("Time: ").strip()

    # Get the numerical 24 hours value of the time
    time = convert(time)

    # Notify the user
    if convert("7:00") <= time <= convert("8:00"):
        print("breakfast time")
    elif convert("12:00") <= time <= convert("13:00"):
        print("lunch time")
    elif convert("18:00") <= time <= convert("19:00"):
        print("dinner time")


def convert(time: str) -> float:
    """
    converts time into a numerical value in 24-hour times
    example: 13:30 -> 13.5
    example: 12:30 a.m. -> 0.5
    example: 12:30 p.m. -> 12.5
    """

    time = time.strip()

    # 24-hour times
    if not is12hr(time):
        hours, minutes = time.split(':')
        return float(hours) + (float(minutes) / 60)

    # 12-hours times
    time, format = time.split()
    hours, minutes = time.split(':')
    hourse = float(hours)
    minutes = float(minutes)

    if format == "p.m.":
        if hours == 12:
            return 12 + (minutes / 60)
        else:
            return 12 + hours + (minutes / 60)
    else:
        if hours == 12:
            return minutes / 60
        else:
            return hours + (minutes / 60)


def is12hr(time: str) -> bool:
    if time.find("a.m.") != -1 or time.find("p.m") != -1:
        return True


main()
