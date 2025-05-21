import sys

class DBUnrollPlugin:
    def input(self, infile):
        self.infile = open(infile, 'r')
    def run(self):
        pass
    def output(self, outfile):
        self.outfile = open(outfile, 'w')
        self.infile.readline()
        self.outfile.write("\"SPOTS\",\"Passed\"\n")
        for line in self.infile:
            contents = line.strip().split(',')
            cic = contents[0]
            passed = int(contents[1])
            total = int(contents[2])
            failed = total-passed
            for i in range(0, passed):
                self.outfile.write("\"1\","+str(cic)+"\n")
            for i in range(0, failed):
                self.outfile.write("\"0\","+str(cic)+"\n")
