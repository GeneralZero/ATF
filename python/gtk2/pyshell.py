import subprocess as sub

p = sub.Popen('./testshell.sh', shell=True ,stdout = sub.PIPE, stderr = sub.PIPE)
prompt1 = p.stdout.readline()
p.stdin.write("4565421\n")
print prompt1

prompt2 = p.stdout.readline()
#p.stdin.write("123465789")
print prompt2
