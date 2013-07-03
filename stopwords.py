#!/usr/bin/env python

import random
import time

linkers1 = ["if", "because", "and", "or", "let", "then", "when", "but"]
linkers2 = ["if", "because", "and", "or", "let", "then", "failed", "loved"]
subjects = ["I", "you", "we"]
objects = ["her", "him", "I", "us"]
when = ["day", "month", "year", "moment"]
desc = ["same", "next", "longest", "previous", "forgotten"]
det = ["That", "The"]

while True:
    
    link1 = random.choice(linkers1)
    link2 = random.choice(linkers2)
    count = 0
    print "\n" + random.choice(det) + " " + random.choice(desc) + " " + random.choice(when) + "\n"
    for i in range(5):
        subj = random.choice(subjects)
        obj = random.choice(objects)     
        print count*".." + link1 + " " + subj + " " + link2 + " " + obj
        time.sleep(1.2)
        count += 1
