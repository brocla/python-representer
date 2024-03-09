from collections import defaultdict

def count_lines(filenames, extensions=("py", "md", "html", "js")):
    """
        for files with the given extensions:
          - count lines
          or
          - log the failure to open
    """

    counts = defaultdict(int)

    for filename in filenames:
        ext = filename.suffix.lstrip(".")

        if filename.is_dir():
            continue

        status = 'OK'
        try:
            fp = open(filename)

        except (IOError, IsADirectoryError) as e:
            status = e.strerror

        finally:
            # only log '.py' files that fail to open
            if ext == 'py' and status != 'OK':
                print("log:",filename, status)
                fp.close()
                continue

            if ext in extensions:
                for line in fp:
                    counts[ext] += 1
            fp.close()

    return counts


# This example comes from the Micropython test suite
# https://github.com/micropython/micropython/blob/master/tests/basics/try_finally_continue.py
def foo(x):
    for i in range(x):
        try:
            pass
        finally:
            try:
                try:
                    print(x, i)
                finally:
                    try:
                        1 / 0
                    finally:
                        return 42
            finally:
                print('continue')
                continue


## Expect
# foo(4)
# 4 0
# continue
# 4 1
# continue
# 4 2
# continue
# 4 3
# continue
