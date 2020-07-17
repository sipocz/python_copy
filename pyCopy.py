import datetime
import os
import shutil


def searchfiles(outFileName, extension='.ttf', folder='C:\\', deltaTime=3600 * 24):
    """
    ***************************
    Listát készít egy adott könyvtárban lévő megadott kiterjesztésű fájlokból rekurzívan.
    A listát eltárolja a outFileName -ban megadott helyre
    Csak azokat a fájlokat veszi figyelembe, amelyek kora kisebb mint a megadott idő [sec]
    ***************************
    :param outFileName:     ide menti a kimeneti listát
    :param extension:       ezeket a fájlokat keresi
    :param folder:          ebben a könyvtárban keres
    :param deltaTime:       ilyen korú, vagy fiatalabb fájlokat keresi [sec]-ben kell megadni!!
    :return: ---
    """
    "Create a txt file with all the file of a type"
    currentDateTimeStamp = datetime.datetime.now().timestamp()
    # print (currentDateTimeStamp)
    with open(outFileName, "w", encoding="utf-8") as filewrite:
        for r, d, f in os.walk(folder):
            for file in f:
                if file.endswith(extension):
                    # print(r+file)
                    fname = r + "\\" + file
                    fileTimeStamp = os.path.getctime(fname)
                    # print(fileTimeStamp)
                    if (currentDateTimeStamp - fileTimeStamp) <= deltaTime:
                        filewrite.write(f"{fname}\n")


searchfiles("C:\\test\\outfile.dat", ".txt", "C:\\test", 2000 * 60)


def filePattern(fname, lis):
    """
      ***************************
      Adott filename és minta illeszkedését viszgálja. ha a minta illeszkedik, a visszaadott érték a
      ***************************
      :param fname:           a file neve, STR
      :param list:            az illesztendő minta,
      :return:                ---
    """
    for index in lis:
        print(index)
        if fname.find(index) > 0:
            return (lis[index])


li = {"alma": "A1", "dio": "A2", "korte": "A3"}
fname = "sdioaas"
out = filePattern(fname, li)
print(f"output={out}")


# shutil.copy("c:\\test\\SRC\\txtfile.txt","c:\\test\\"+out+"\\almafa.txt")

def parseCSV(str):
    a = str.split(";")
    return (a)


print(parseCSV("asad;asdasd;2323;12;safas"))

a = [[4, "alma"], [3, "korte"]]


def Lsort(a, indx):
    a.sort(key=lambda alist: alist[indx])
    return (a)


print(Lsort(a, 1))


def printCSV(a, fname):
    csvfile = open(fname, "w")
    for i in a:
        s = ""
        for j in i:
            s = s + str(j) + ";"

        print(s[0:-1])
        csvfile.writelines(s[0:-1] + "\n")
    csvfile.close()


printCSV(a, "C:/test/csv1.txt")
#test alfa

