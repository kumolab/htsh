#
from bs4 import BeautifulSoup as b4
import csv

class regionTree(object):

    def __init__(self, input_file = "./data_source/inp.html"):
        self._filename = input_file
        self._rawFile = ""
        self._codeList = []
        self._nameList = []
        self._regionCount = 0
        print(f"${self._filename}: loaded")

    def readFile(self):
        with open(self._filename) as fi:
            self._rawFile = fi.read()
        return 0

    def readRegion(self):
        htmlPage = b4(self._rawFile, "html.parser")
        # htmlPage.span.extract()
        allRegions = htmlPage.find_all("tr")
        # print(allCities)
        for everyRegion in allRegions:
            allTags = everyRegion.find_all("td")
            try:
                if (allTags[1].span):
                    allTags[1].span.extract()
                if (allTags[2].span):
                    allTags[2].span.extract()
                regionCode = allTags[1].contents[0]
                regionName = allTags[2].contents[0]
            except IndexError as ie:
                print('tr tag but no region here')
                print(ie)
                continue
            except NameError as ne:
                print('tr tag but no region here')
                print(ne)
                continue
            self._codeList.append(regionCode)
            self._nameList.append(regionName)
        # print(htmlPage.pretty())
        print(self._codeList[0:20])
        print(self._nameList[0:20])
        self._regionCount = len(self._codeList)
        if len(self._nameList) != len(self._codeList):
            print('warning... (tbd)')
        return 0

    def writeFormattedRegion(self, format="csv", outpit_file="./data_export/exp.csv"):
        with open(outpit_file, 'w', newline='') as fo:
            csvWriter = csv.writer(fo,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for regionIndex in range(1, self._regionCount):
                csvWriter.writerow([self._codeList[regionIndex],
                                    self._nameList[regionIndex],
                                    self._nameList[regionIndex],
                                    self._nameList[regionIndex]])
        return 0

    def searchForCity(self):
        return 0

def main():
    myrt = regionTree()
    myrt.readFile()
    myrt.readRegion()
    myrt.writeFormattedRegion()
    print(myrt)


if __name__ == "__main__":
    main()
