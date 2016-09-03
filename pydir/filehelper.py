#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

success_result = 0
fail_reason_unknown=-1
fail_reason_not_a_file = -100
fail_reason_not_a_directory= -200
fail_reason_file_not_exist = -300
fail_reason_directory_not_exist = -400
fail_reason_target_file_exists_already = -500

ERRORS = {
    0: "Successful operation on {val}",
    -100: "{val} is not a valid file",
    -200: "{val} is not a valid directory",
    -300: "file {val} does not exist",
    -400: "directory {val} does not exist",
    -500: "target file {val} exists already"
}

def error_define():
    for k in ERRORS:
        print("{key}:{val}".format(key=k, val=ERRORS[k].replace("{val}", "")))

def equals(first, second):
   return first == second

if(equals(__name__, "__main__")):
    error_define()
