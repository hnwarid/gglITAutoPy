#!/usr/bin/env python3

import csv
import operator
import re


error = {}
per_user = {}

with open('syslog.log', 'r') as logs:
    for log in logs.readlines():
        user = re.search(r"\((.*)\)", log).group(1)
        report = re.search(r"(INFO|ERROR)", log).group()
        # print(user)
        # print(report)

        user_count = {'INFO': 0, 'ERROR': 0}
        if user not in per_user:
            per_user[user] = user_count

        if report == 'INFO':
            per_user[user]['INFO'] += 1
        elif report == 'ERROR':
            per_user[user]['ERROR'] += 1
            msg = re.search(r"ERROR (.*) ", log).group(1)
            # print(msg)
            error[msg] = error.get(msg, 0) +1

# print(error)
# print(per_user)

# error_desc = []
per_user_asc = []
error_desc = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
for user in sorted(per_user.keys()):
    per_user_asc.append((user, per_user[user]['INFO'], per_user[user]['ERROR']))
error_desc.insert(0, ('Error', 'Count'))
per_user_asc.insert(0, ('Username', 'INFO', 'ERROR'))
# print("error sorted by descending: \n", error_desc, "\n\n")
# print("per_user sorted by ascending: \n", per_user_asc, "\n\n")
# print(type(error_desc), type(per_user_asc))
# for item in per_user_asc:
#     print(item)

with open("error_message.csv", "w") as output_1:
    for item in error_desc:
        item = str(item).strip("()").replace("'", "").replace('"', "").replace(", ", ",") + "\n"
        if "doesnt" in item:
           item = item.replace("doesnt", "doesn't")
        output_1.write(item)
    output_1.close()

with open("user_statistics.csv", "w") as output_2:
    for item in per_user_asc:
        item = str(item).strip("()").replace("'", "").replace('"', "").replace(", ", ",") + "\n"
        output_2.write(item)
    output_2.close()





# ./csv_to_html.py error_message.csv /var/www/html/error_message.html
# ./csv_to_html.py user_statistics.csv /var/www/html/user_statistics.html