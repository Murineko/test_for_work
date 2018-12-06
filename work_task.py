import wget
import xml.dom.minidom as minidom
answer=wget.download('https://tvzvezda.ru/export/test-task-1.xml')
print(answer)
k=''
chet=-1
while k!="stop":
    k=str(input("Введите необходимую команду на выбор: all, keywords или number"))
    if k=='all':
        try:
            doc = minidom.parse(answer)
            enum = doc.getElementsByTagName("title")
            for t in range(len (enum)):
                print(enum[t].firstChild.nodeValue, "\n")
        except:
             print("Ошибка при поиске")
    if k=='keywords':
        teg=str(input("Введите ключевое слово: "))
        try:
            doc = minidom.parse(answer)
            enum = doc.getElementsByTagName("news")
            data = []
            nameUID = []
            nameName = []
            for i in enum:
                dataObj = i.getElementsByTagName("keywords")
                chet+=1
                for t in range(len(dataObj)):
                    print(dataObj[t].firstChild.nodeValue, "\n")
                    if teg in dataObj[t].firstChild.nodeValue:
                        zagolovok = doc.getElementsByTagName("title")
                        print("С заданным тегом", teg, "найдена следующая новость: ", zagolovok[chet].firstChild.nodeValue, "\n")
        except:
            print("Ошибка при поиске")
    if k == 'number':
        number=int(input("Введите номер новости"))
        try:
            doc = minidom.parse(answer)
            enum = doc.getElementsByTagName("title")
            print(enum[number].firstChild.nodeValue, "\n")
        except:
             print("Ошибка при поиске, возможно вы ввели слишком большое число или же вместо числа буквы")



