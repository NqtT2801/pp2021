import subprocess
for i in range (0,3):
    cmd = input('Run: ')
    p1 = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    with open('output.text', 'w') as f:
         p2 = subprocess.run("findstr -?", shell=True, text=True, input=p1.stdout, stdout=f)
