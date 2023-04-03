import os
import subprocess

with open('test2.py', 'w') as f:
    f.write('''import time
print('start')
time.sleep(2)
print('done')
            ''')

(readend, writeend) = os.pipe()

p = subprocess.Popen(['python', '-u', 'test2.py'],
                     stdout=subprocess.PIPE, bufsize=1,
                     universal_newlines=True)
output = ""
output_buf = p.stdout.readline()
while output_buf:
    print(output_buf, end="")
    output += output_buf
    output_buf = p.stdout.readline()


        