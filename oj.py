#!/usr/bin/python
#coding: utf-8


__Author__ = "Yifei Kong"
__Email__ = "kongyifei@gmail.com"


"""Judge helper"""

import os
import re
import sys
from glob import glob
import subprocess32 as subprocess
import threading


def get_files (source_dir):

    source_files = []
    source_files.extend(glob(os.path.join(source_dir, "*.c")))
    source_files.extend(glob(os.path.join(source_dir, "*.cpp")))

    return source_files


def clean_up (source_dir):

    target_files = glob(os.path.join(source_dir, "*.bin"))
    for target_file in target_files:
        os.remove(target_file)


def compile (source_file, target_file, lazy=True):

    compile_return = 0
    if os.path.splitext(source_file)[1] == '.c':
        compile_return = subprocess.call(["gcc", "-std=c99", source_file, "-o", target_file])
    else:
        compile_return = subprocess.call(["g++", "-std=c++11", source_file, "-o", target_file])

    return compile_return


def judge (target_file, full_score, case_inline_count, case_outline_count):

    score = full_score
    input_cases = []
    output_cases = []

    with open("input.txt") as input_file:
        input_lines = input_file.readlines()
        for i in range(0, len(input_lines), case_inline_count):
            input_cases.append(''.join(input_lines[i:i+case_inline_count]) + '\n\x1a')

    with open("output.txt") as output_file:
        output_lines = output_file.readlines()
        for i in range(0, len(output_lines), case_outline_count):
            output_cases.append(''.join(output_lines[i:i+case_outline_count]))

    step = full_score / len(input_cases)

    for input_case, output_case in zip(input_cases, output_cases):
        try:
            p = subprocess.Popen(target_file, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            try:
                output, _ = p.communicate(input=input_case, timeout=3)
            except:
                pass
            if output.strip() != output_case.strip():
                score -= step
        except OSError:
            pass

    print("------{} got {}".format(target_file, score))
    return score


def main ():

    source_dir = sys.argv[1]
    source_files = get_files(source_dir)
    judge_results = []
    full_score = 10

    for source_file in source_files:
        #print(source_file)
        target_file = os.path.splitext(source_file)[0] + ".bin"
        compile_return = compile(source_file, target_file)
        #compile_return = 0
        if compile_return != 0:
            print("!!!!!!{} didn't pass compile".format(source_file))
            score = 0
        else:
            print("------{} compiled!".format(source_file))
            score = judge(target_file, full_score, 2, 1)
        judge_results.append((score, source_file))

    for judge_result in judge_results:
        print judge_result

    with open("result.txt", "w") as result_file:
        for judge_result in judge_results:
            result_file.write(str(judge_result) + os.linesep)
    clean_up(source_dir)

if __name__ == '__main__':
    main()
