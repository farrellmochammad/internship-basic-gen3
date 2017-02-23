class BigRandom:
    def __init__(self):
        self.data = open("data.txt","r")
        # add attributes if you need more

    def answer(self):
        noh = 0# variable to store number of hashtag
                # ommiting line number's hashtag
        suc = 0 # variable to store sum of character's code in ascii,
                # ommiting line number and its hashtag

        # your algorithm
        a = 0
        txt = self.data
        for i in txt:
            for j in i:
                bla = 0
                if j=="#":
                    if bla == 1:
                        suc += ord(j)
                        noh += 1
                    else:
                        bla += 1
                        noh += 1
                elif j!=type(int):
                    suc += ord(j)

        print noh,suc

        return (noh,suc)

B = BigRandom()
B.answer()
