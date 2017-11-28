import os
import time
import argparse
import subprocess
import collections

Lang = collections.namedtuple('Lang', 'compile execute')

langs = {
    'py': Lang('cd .', 'python {name}.py {n}'),
    'c': Lang('gcc --std=gnu11 -O3 {name}.c', './a.out {n}'),
    'go': Lang('go build {name}.go', './{name} {n}'),
    'java': Lang('javac {name}.java', 'java {name} {n}'),
}

ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
ap.add_argument('folder', help='to process')
ap.add_argument('--critical', default=1.0, help='in seconds, break if exceed')
ap.add_argument('--warm-up', default=60.0, help='in seconds, break if exceed')
ap = ap.parse_args()


def one_file(name, ext):
    print('%s.%s' % (name, ext))
    lang = langs[ext]
    subprocess.check_output(lang.compile.format(**locals()).split())
    times = []
    n = 1
    subprocess.check_output(lang.execute.format(**locals()).split())
    while True:
        try:
            tic = time.time()
            t = subprocess.check_output(lang.execute.format(**locals()).split())
            toc = time.time()
            if toc - tic > ap.warm_up + ap.critical:
                break
        except subprocess.CalledProcessError:
            break
        print('%s %d %s' % (name, n, t))
        t = float(t)
        times.append(t)
        if t > ap.critical:
            break
        n *= 2
    Res = collections.namedtuple('Res', 'name times')
    return Res(name, times)


def main():
    os.chdir(ap.folder)

    res = []
    for filename in os.listdir('.'):
        name_ext = filename.rsplit('.', 1)
        if len(name_ext) == 2:
            name, ext = name_ext
            if ext in langs:
                res.append(one_file(name, ext))
    res.sort(key=lambda r: (-len(r.times), r.times[-1]))
    n = len(res[0].times)
    with open('summary.md', 'w') as f:
        f.writelines('|  Method  | %s |\n' % ' | '.join('N = %d' % 2**i for i in range(n)))
        f.writelines('| :------: | %s |\n' % ' | '.join(':---:' for _ in range(n)))
        for name, times in res:
            f.writelines('| %s | %s |\n' % (name, ' | '.join(
                '%.9f' % times[i] if i < len(times) else 'N/A' for i in range(n))))
    with open('summary.csv', 'w') as f:
        f.writelines('Method,N,Time\n')
        for name, times in res:
            for i, t in enumerate(times):
                f.writelines('%s,%d,%s\n' % (name, 2**i, t))


if __name__ == '__main__':
    main()
