in_path = "E:\\Sem-6-Lab\\System Software and Compiler Design\\Ex0\\test.txt"
out_path = "E:\\Sem-6-Lab\\System Software and Compiler Design\\Ex0\\out.txt"

f = open(in_path, 'r')
x = open(out_path, 'w')
x.write(f.read())