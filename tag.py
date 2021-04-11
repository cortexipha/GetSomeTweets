from collections import defaultdict
from snowballstemmer import stemmer
from TurkishStemmer import TurkishStemmer

import dictionary, re,\
    classes.Isim as Isim

lastType = ''
lastIndex = ''


def printTag(isimler, file):
    for isim in isimler:
        point = 0
        char = 'B'
        for word in isim.isim:
            sonuc = '{' + char + '-' + dictionary.dictionary[isim.type]['tag'] + '}' + word
            print(sonuc)
            file.write('\n'+sonuc)
            if point == 0:
                point = 1
                char = 'I'


def cleanName(oldName):
    newName = oldName.split('\'')[0]
    newName = newName.replace('"', '')
    return newName.split('’')[0].lower()


def getMaxLengthSentence(sentence):
    maxLength = max(sentence['allLength'])
    for i in range(len(sentence)):
        if (sentence[i]['length'] == maxLength):
            return sentence[i]
    return sentence[0]

def grupla(isimler):
    res = defaultdict(list)
    for isim in isimler:
        res[isim.baslangicIndex].append(isim)
    return res

def yuksekPunalilariGetir(bulunanIsimler):
    bulunanIsimler = grupla(bulunanIsimler)
    res = []
    for isimler in bulunanIsimler.items():
        for isim in isimler[1:]:
            res.append(max(isim, key=lambda x:x.puan))
    return res


def checkForRules(searchThing):
    # kokbul = stemmer('turkish')
    # kokbul = TurkishStemmer()
    isimler = []
    searchThingLength = len(searchThing)
    for i in range(0, searchThingLength):
        bulunanisimler = []
        for rules in dictionary.dictionary['Rules']['words'].keys():
            # if kokbul.stem(searchThing[i].lower()) == rules:
            if cleanName(searchThing[i]) == rules:
                rule = dictionary.dictionary['Rules']['words'][rules]
                indexes = {'start':i,'end':i}
                if rule['get'] == 'after':
                    indexes['start'] += 1
                    indexes['end'] += rule['length']+1
                else:
                    indexes['start'] -= rule['length']
                    indexes['end'] -= 1
                kelimeBasladi = 0
                sonIsim = ''
                for searchThingWord in searchThing[indexes['start']:indexes['end']]:
                    if kelimeBasladi == 0:
                        yeniIsim = Isim.Isim(searchThingWord, rule['type'], i)
                        sonIsim = yeniIsim
                        kelimeBasladi = 1
                    else:
                        sonIsim.isimeEkle(searchThingWord)
                if sonIsim:
                    bulunanisimler.append(sonIsim)
        if(bulunanisimler):
            isimler.extend(bulunanisimler)
    return  isimler


def searchInSubDict(name, searchThing):
    # kokbul = stemmer('turkish')
    # kokbul = TurkishStemmer()
    isimler = []
    searchThingLength = len(searchThing)
    for i in range(0, searchThingLength):
        baslangicIndex = i
        bulunanIsimler = []
        for j in range(len(dictionary.dictionary[name]['words'])):
            kutuphaneIsmi = dictionary.dictionary[name]['words'][j].split()
            # if kutuphaneIsmi[0] == kokbul.stem(cleanName(searchThing[i])):
            if kutuphaneIsmi[0] == cleanName(searchThing[i]):

                kelimeBasladi = 0
                sonIsim = ''
                for k in range(min(len(kutuphaneIsmi),searchThingLength)):
                    try:
                        if kutuphaneIsmi[k] == cleanName(searchThing[i + k]):
                            if kelimeBasladi == 0:
                                yeniIsim = Isim.Isim(kutuphaneIsmi[k], name, baslangicIndex)
                                sonIsim = yeniIsim
                                kelimeBasladi = 1
                            else:
                                sonIsim.isimeEkle(kutuphaneIsmi[k])
                            # if(i+1<=(searchThingLength-1)):
                            #     i+=1
                        else:
                            if kelimeBasladi == 1:
                                bulunanIsimler.append(sonIsim)
                                kelimeBasladi = 0
                    except IndexError:
                        ''
                if sonIsim != '':
                    bulunanIsimler.append(sonIsim)
        if(bulunanIsimler):
            isimler.extend(yuksekPunalilariGetir(bulunanIsimler))
    return  isimler

def findInDictionary(twitWord):
    tumBulunanlar = []
    tumBulunanlar.extend(searchInSubDict('Person', twitWord))
    tumBulunanlar.extend(searchInSubDict('Organization', twitWord))
    tumBulunanlar.extend(searchInSubDict('Location', twitWord))
    tumBulunanlar.extend(searchInSubDict('Date', twitWord))
    tumBulunanlar.extend(searchInSubDict('Gender', twitWord))
    tumBulunanlar.extend(checkForRules(twitWord))
    sonuc = yuksekPunalilariGetir(tumBulunanlar)
    return  sonuc


def twitArray(twit, file):
    twitArr = twit.split(' ')
    global lastType
    lastType = ''
    sonuc = findInDictionary(twitArr)
    printTag(sonuc, file)
    print('-----')
    file.write('\n\n\n--------------------------------------\n\n\n')
