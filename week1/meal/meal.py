# Meal Time:
#
# Notify's the user whether they need to eat in the given time of the day



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

    example: 13:30 --> 13.5
    """

    hours, minutes = time.split(':')

    # There are 60 minutes in 1 hour
    return float(hours) + (float(minutes) / 60)


main()
