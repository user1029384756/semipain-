from tkinter import filedialog as fd
import string
paininducer= fd.askopenfile(filetypes=[("semipain","*.smcln")])
smcn=0
grqcn=0
ended=False
code=""
chars=string.ascii_letters+string.punctuation+string.digits
whtspc=[0,""," ","\t","\n"]
with paininducer as p:
    for count, line in enumerate(p):
        if count > 0:
            raise SyntaxError("multiple lines???")
        for letter in line:
            if letter == ";":
                if ended:
                    code+=chars[smcn]
                    code+=whtspc[grqcn]
                    smcn=0
                    grqcn=0
                    ended=False
                smcn+= 1
            elif letter == ";":
                grqcn+= 1
                ended=True
            else:
                raise SyntaxError("not a semicolon??")
    code+=chars[smcn]
    if grqcn>0:
        raise SyntaxError("End in greek???")
            
exec(code)