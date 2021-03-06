## 1. The Time Module ##

import time
current_time = time.time()
print(current_time)
# print how many seconds now from the 1970

## 2. Converting Timestamps ##

# time.gmtime has many attributes like tm_year,tm_mon,tm_mday,tm_hour,tm_min

import time
current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour

## 3. UTC ##

import datetime
current_datetime = datetime.datetime.utcnow() # return the current utc time
current_year = current_datetime.year
current_month = current_datetime.month

## 4. Timedelta ##

import datetime
kirks_birthday = datetime.datetime(year = 2233,month = 3,day = 22)
diff = datetime.timedelta(weeks = 15)
before_kirk = kirks_birthday - diff

## 5. Formatting Dates ##

import datetime
print(mystery_date)
mystery_date_formatted_string = mystery_date.strftime('%I:%M%p on %A %B %d, %Y')
print(mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime
mystery_date_2 = datetime.datetime.strptime(mystery_date_formatted_string,'%I:%M%p on %A %B %d, %Y')
print(mystery_date_2)

## 8. Reformatting Our Data ##

import datetime
for item in posts:
    time = float(item[2])
    time = datetime.datetime.fromtimestamp(time)
    item[2] = time

## 9. Counting Posts from March ##

march_count = 0
for item in posts:
    month = item[2].month
    if month == 3:
        march_count += 1

## 10. Counting Posts from Any Month ##

march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1
def month_posts(month):
    user_posts = 0
    for item in posts:
        if item[2].month == month:
            user_posts += 1
    return user_posts
feb_count = month_posts(2)
aug_count = month_posts(8)
