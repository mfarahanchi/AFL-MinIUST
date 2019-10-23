###
# authored and implemented by mohsen farahanchi
# given a set of afl-showmap results, the goal is to
# select a subset in such a way that saves the coverage of initial set
# but less elements. in other words, test suite minimisation!
###

import sys
import os


def run_showmap(in_dir, temp_dir, to_exec):
    for r, d, f in os.walk(in_dir):
        for test_case in f:
            in_file_name = str(test_case)
            out_file_name = os.path.splitext(str(test_case))[0]
            print(test_case)
            myCmd = "afl-showmap -o {} -- {} {}/{}".format(
                temp_dir+'/'+out_file_name+'.txt', to_exec, temp_dir, in_file_name)
            print(myCmd)
            os.system(myCmd)


def move_file(file, des_dir):
    pass


def main():
    """
    manual of minizer.py
    """

    global all_pathes
    all_pathes = set()

    # TODO: refactor below
    def compare_two_map(setA, setB):
        # returns similarity of two sets from 0 to 1
        # TODO: choosing between two similar file is important future work
        a_int_b = len(setA & setB)
        total = len(setA) + len(setB) - a_int_b
        return a_int_b / total

    def mega_dict(dir):
        """
        # this function generates a mega dict than
        # keys are filenames and values are set of their contents
        """
        mega_dict = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(dir):
            for file in f:
                if True:
                    # now i have all of afl-showmap results
                    # files.append(os.path.join(r, file))
                    set_fp = set()
                    with open(os.path.join(dir, file), 'r') as fp:
                        line = fp.readline()  # omit 00000000
                        line = fp.readline()
                        while line:
                            # print("Line {}: {}".format(cnt, line.strip()))
                            set_fp.add(int(line[0:-3]))
                            line = fp.readline()
                    mega_dict.append((str(file), set_fp))

                    print(file)
        return mega_dict
    # TODO: refactor above

    script = sys.argv[0]
    action = sys.argv[1]
    if action == "--in-dir":
        in_dir = sys.argv[2]
        print(mega_dict(in_dir))
        print("""
        hello minizaer
        """)
    # elif action == "--out_dir":
    #     out_dir = sys.argv[2]
    mega_dict = mega_dict(in_dir)
    no_of_cases = len(mega_dict)
    i = 0
    while i < no_of_cases:
        _file_name, _mapA = mega_dict[i]
        j = i+1
        while j < no_of_cases:
            _, _mapB = mega_dict[j]
            if(compare_two_map(_mapA, _mapB) > .9):
                mega_dict.pop(j)
                print("reduced", _file_name, _)
                no_of_cases -= 1  # reduced number of test cases
            j += 1
        i += 1

    # now the subset of initial test suite is computed
    # time to move it to a separate folder
    print(mega_dict)
    for _file_name, _ in mega_dict:
        pass

    # produce analytics


if __name__ == '__main__':
    run_showmap('/Users/faramohsen/Desktop/linuxvm/beta/my_in_dir',
                '/Users/faramohsen/Desktop/linuxvm/beta/my_temp_dir',
                '/home/mohsen/mupdf/build/release/mutool')
