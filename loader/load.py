import csv


class AreaDTO:

    def __init__(self, line, index):
        self.code = line[0]
        self.title = line[1]
        self.useYn = line[2] == "존재"
        self.index = index + 1
        self.titleArray = self.create_title_array()
        self.type = self.get_type()
        self.origin_code = self.get_code()

    def get_code(self):
        return self.code[0:5]

    def create_title_array(self):
        return str(self.title).split()

    def check_title(self):
        titleArray = self.titleArray
        return len(titleArray)

    def is_parents(self):
        return self.check_title() == 1

    def is_child(self):
        return self.check_title() == 2

    def is_child_child(self):
        lastStr = self.titleArray[2][-1]
        return self.check_title() == 3 and (
                lastStr != "동" and lastStr != "가" and lastStr != "동" and lastStr != "면" and lastStr != "읍" and lastStr != "로" and lastStr != "리"
        )

    def get_type(self):
        if self.is_parents():
            return "P"
        elif self.is_child():
            return "C"
        elif self.is_child_child():
            return "CC"
        else:
            return None

    def get_title(self):
        type = self.type
        titleArray = self.titleArray
        if type == "P":
            return self.title
        elif type == "C":
            return "{0}".format(titleArray[1])
        elif type == "CC":
            return "{0}/{1}".format(titleArray[1], titleArray[2])

    def get_parents_index(self, areaList):
        type = self.type
        if type == "P":
            return 0
        elif type == "C":
            selfTitle = self.titleArray[0]
            parentsList = list(filter(lambda area: area.is_parents(), areaList))
            foundList = list(filter(lambda parents: parents.title == selfTitle, parentsList))
            return foundList[0].index
        elif type == "CC":
            try:
                selfTitle = self.titleArray[0]
                parentsList = list(filter(lambda area: area.is_parents(), areaList))
                foundList = list(filter(lambda parents: parents.titleArray[0] == selfTitle, parentsList))
                return foundList[0].index
            except Exception as e:
                print(e)
                return "NONE"

        # elif type == "CC":
        #     try:
        #         selfTitle = self.titleArray[1]
        #         parentsList = list(filter(lambda area: area.is_child(), areaList))
        #         foundList = list(filter(lambda parents: parents.titleArray[1] == selfTitle, parentsList))
        #         return foundList[0].index
        #     except Exception as e:
        #         print(e)
        #         return "NONE"

    def check_code(self, areaList):
        type = self.type
        if type == "C":
            parentsList = list(filter(lambda area: area.is_parents(), areaList))
            foundList = list(filter(lambda parents: parents.origin_code == self.origin_code, parentsList))
            return len(foundList) == 0

        return True


file = open('test.csv', 'r', encoding="cp949")
loader = csv.reader(file, delimiter="\t")

areaList = list()

for index, line in enumerate(loader):
    dto = AreaDTO(line, index)
    type = dto.type
    if type is not None:
        areaList.append(dto)

file.close()

areaFile = open('area.csv', 'w', newline='', encoding="utf-8")
wr = csv.writer(areaFile)

for index, area in enumerate(areaList):
    type = area.type
    title = area.get_title()
    number = area.index
    parents_index = area.get_parents_index(areaList)
    code = area.origin_code
    is_code = area.check_code(areaList)
    if area.useYn and type is not None and is_code:
        wr.writerow([number, code, title, type, parents_index])

areaFile.close()
