import subprocess as sp
import sys
pc, err = sp.Popen("/usr/local/bin/gs -q -o - -sDEVICE=inkcov {0}".format(sys.argv[1]).split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()

# with open("pagecolours", 'r') as pc:
colour = 0
black = 0
for line in pc.split('\n'):
    # print(line)
    if line.startswith(" 0.00000  0.00000  0.00000  "):
        black += 1
    else:
        colour += 1
print("Colour pages: {0}".format(colour))
print("Black Pages: {0}".format(black))
print("Total Pages: {0}".format(colour + black))
print("Estimated Price: {0}".format(((colour * 0.2) + (black * 0.06) + 9.50) * 3  + 16.4))
