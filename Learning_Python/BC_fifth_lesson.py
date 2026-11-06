# Exception handling, file detection, dates and time, alarm clock, Multithreading

# exception = an event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try, 2. except, 3. finally
# try:
#     number = int(input("Enter a number: "))
#     print(1/number)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("Enter only numbers please!")
# except Exception:
#     print("Something went wrong!")
# finally:
#     print("Do some cleanup here") # Always executes regardless of exceptions

# Python documentation for an extended list



# Python file detection, reading and writing files **************************

# import os # Provides a way for python programs to interact with the operating system

# file_path = "Learning_Python/test.txt"

# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")

#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("That location doesn't exist")


# Dates and Time **************************
# import datetime # allows us to work with our system's clock

# date = datetime.date(2020, 5, 12)
# today = datetime.date.today()

# time = datetime.time(10,30, 12)
# time_now = datetime.datetime.now()

# now = time_now.strftime("%d-%m-%Y ---- %H:%M:%S")

# print(date)
# print(today)

# print(time)
# print(now)

# Exercise - see if a date and time has passed a target date and time
# target_datetime = datetime.datetime(2026, 5, 12, 12, 30, 1)
# current_datetime = datetime.datetime.now()

# if target_datetime < current_datetime:
#     print("Target date has passed")
# else:
#     print("Target date has not passed")


# # Waking alarm clock using python **************************
# import time
# import datetime
# import pygame

# def set_alarm(alarm_time):
#     print(f"Alarm set for: '{alarm_time}'")
#     sound_file = "Learning_Python/Spaceship Alarm.mp3"
#     is_running = True

#     while is_running:
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print(current_time)

#         if current_time == alarm_time:
#             print("WAKE UP! 😠")

#             pygame.mixer.init()
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()

#             while pygame.mixer.music.get_busy():
#                 time.sleep(1)
#             is_running = False

#         time.sleep(1)

# if __name__ == "__main__":
#     alarm_time = input("Enter the alarm time (HH:MM:SS): ")
#     set_alarm(alarm_time)



# Multi-threading
