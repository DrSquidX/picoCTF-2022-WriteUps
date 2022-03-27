class Reader:
    def __init__(self, file, title=True):
        self.title = title
        self.file = file
        self.contents = open(self.file, "r").read()
    @staticmethod
    def get_category(string: str):
        return string.replace("(BE)"," (Binary Exploitation)").replace("(F)"," (Forensics)").\
                      replace("(WE)"," (Web Exploitation)").replace("(RE)"," (Reverse Engineering)").\
                      replace("(C)"," (Cryptography)")
    @property
    def help_msg(self):
        if self.title:
            try:
                print(f"\n[+] {self.contents.splitlines()[0].strip()}")
                print(f"[+] {self.contents.splitlines()[1].strip()}")
                print()
            except:
                pass
        return "[+] Problem Writeups:\n"+"".join(f'[+] {x[0]}: {x[1]}\n' for x in self.problems_writeups)+"[+] Any other inputs will display the help message.\n"
    def get_items(self):
        mode = 0
        self.problems = []
        self.problems_writeups = []
        inwriteup = False
        writeupname = ""
        writeup = ""
        index = 0
        line_no = 1
        for i in self.contents.splitlines():
            if i.startswith("Solved Problems:"):
                mode = 1
            if mode == 1:
                if i.strip() != "":
                    self.problems.append(i.strip())
                else:
                    mode += 1
            if mode == 2:
                if inwriteup:
                    if not i.startswith(" ") and ":" in i or line_no == len(self.contents.splitlines()):
                        inwriteup = False
                        self.problems_writeups.append([index,self.get_category(writeupname), writeup])
                        index += 1
                        if line_no == len(self.contents.splitlines()):
                            self.problems_writeups.append([index,"All",self.contents])
                    else:
                        writeup += i+"\n" if i.strip() != "" else ""
                if not i.startswith(" ") and not inwriteup and ":" in i:
                    inwriteup = True
                    writeup = ""
                    writeupname = i.replace(":","")
            line_no += 1
        print(self.help_msg)
        self.user_input()
    def user_input(self):
        while True:
            try:
                element = int(input("[+] Enter the number corresponding to the problem: "))
                print(f"[+] Write-up for {self.problems_writeups[element][1].strip()}:\n{self.problems_writeups[element][2]}")
            except KeyboardInterrupt:
                print("[+] Stopped due to interrupt.")
                break
            except:
                print(self.help_msg)
reader = Reader("picoCTF-2022-Write-Ups.txt")
reader.get_items()
