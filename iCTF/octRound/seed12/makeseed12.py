import os
import random

random.seed(12)
flags = ["ictf{hahayouthought}", "ictf{nottheflag}", "ictf{tryharder}", "ictf{notthisone}", "where could it be?", "ictf{no grep for you}", "what?", "asdofawrog", "yeah just look for it bro it's not that hard", "yooo flag where??"]
for i in range (1, 1000, 1):
    flag = ""
    if (i == 486 ):
        flag = "ictf{m4ny_m4ny_t4r5}"
    else:
        flag = flags[random.randint(0, 9)]

    os.system("echo '" + flag + "' > flag.txt")
    os.system("tar czvf " +  str(i)  + ".tar.gz " + str(i-1)+".tar.gz flag.txt")
    
