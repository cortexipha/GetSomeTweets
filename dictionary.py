# dict = ['Trakya']


dictionary = {
    'Organization':{
        'tag':'Organization',
        'words':[
            'disk trakya bölge temsilciliği',
            'bahçeşehir koleji bilim ve teknoloji lisesi',
            'millet ittifakı',
            'denizlispor',
            'fenerbahçe',
            'türk kızılay',
            'osmanlı devleti',
            'galatasaray',
            'kadın emek pazarı',
            'okul aile birliği',
            'keşan satranç şenliği',
            'türk ocakları',
            'otobüsçüler kooperatifi',
            'kadın kolektifi',
            'iyi parti',
            'türkiye gençlik vakfı ',
            'milli eğitim ',
            'fetö',
            'kariyer ve marka etkinliği trakya plus',
            'trakya tarımsal araştırma enstitüsü',
            'chp',
            'hdp',
            'polis',
            'halk eğitim',
            'kalkınma ajansı'
        ]
    },
    'Location':{
        'tag':'Location',
        'words':[
            'edirne',
            'eski edirne asfaltı',
            'selimiye camii',
            'bolluca sapağı',
            'aydın',
            'anadolu',
            'kahramanmaraş',
            'amasya',
            'e5',
            'çanakkale',
            'iran',
            'mersin',
            'merkez',
            'türkmenistan',
            'i̇stanbul',
            'ankara',
            'bolu',
            'bursa',
            'kars',
            'arnavutköy',
            'muğla',
            'izmir',
            'hatay',
            'gümüşhane',
            'uzunköpru',
            'trabzon',
            'türkiye',
            'kırklareli',
            'çerkezköy',
            'trakya',
            'silivri',
            'rumeli hisarı',
            'saray',
            'adıyaman',
            'çorlu',
            'kırklareli',
            'sakarya',
            'avrupa',
            'karaağaç',
            'elazığ',
            'almanya',
            'van',
            'kktc',
            'yunanistan',
            'yozgat',
            'meriç nehri',
            'tekirdağ',
            'saraçlar caddesi',
            'cebelitarık boğazı',
            'üç şerefeli cami',
            'anıtkabirde',
            'beylerbeyi cami',
            'edirne eski sarayı',
            'tem akşemsettin viyadüğü',
            'tunceli',
            'trakya üniversitesi eğitim fakültesi ',
            'd100',
            'marmaray',
            'ardahan',
            'tem istoç'
        ]
    },
    'Gender':{
        'tag':'Gender',
        'words':[
            'kadın',
            'erkek'
        ]
    },
    'Person':{
        'tag':'Person',
        'words':[
            'atatürk',
            'ali',
            'Süleyman Seba',
            'recep tayyip erdoğan',
            'recep gürkan',
            'fırat çakıroğlu',
            'emre',
            'selahattin demirtaş',
            'enver paşa',
            'fevzi pekcanlı',
            'gedik ahmed paşa',
            'sezai güler',
            'sultan 2. mehmed',
            'fatih',
            'ekrem canalp',
            'hidayet',
            'meral akşener',
            'ekrem i̇mamoğlu',
            'nevzat bilgic',
            'olgun birbey şahinbaş',
            'arzu çerkezoğlu',
            'mimar sinan',
            'ali gürbüz ',
            'i̇smail güner'

        ]
    },
    'Date':{
        'tag':'Date',
        'words':[
            'aralık',
            'ocak',
            'şubat',
            'mart',
            'nisan',
            'mayıs',
            'haziran',
            'temmuz',
            'agustos',
            'eylül',
            'ekim',
            'kasim',
            'pazartesi',
            'salı',
            'çarşamba',
            'perşembe',
            'cuma',
            'cumartesi',
            'pazar',

        ]
    },
    'Numeric':{
      'tag':'Numeric'
    },
    'banned':{
        'tag':'Banned',
        'words':[
            've',
            'veya'
        ]
    },
    'Unknown':{
        'tag':'unknown'
    },
    'Rules':{
        'tag':'rules',
        'words':{
            'dr':{
                'get':'after',
                'length':2,
                'type':'Person'
            },
            'sn':{
                'get':'after',
                'length':2,
                'type':'Person'
            },
            'üyesi':{
                'get':'after',
                'length':2,
                'type':'Person'
            },
            'sn.':{
                'get':'after',
                'length':2,
                'type':'Person'
            },
            'sayın':{
                'get':'after',
                'length':2,
                'type':'Person'
            },
            'müdürü':{
                'get':'after',
                'length':2,
                'type':'Person'
            },
            'fuarı':{
                'get':'before',
                'length':2,
                'type':'Location'
            },
            'lisesi':{
                'get':'before',
                'length':3,
                'type':'Location'
            },
            'ilkokulu':{
                'get':'before',
                'length':1,
                'type':'Location'
            },
            'şehit':{
                'get':'after',
                'length':2,
                'type':'Person'
            },
            'er':{
                'get':'after',
                'length':2,
                'type':'Person'
            },
            'gazi':{
                'get':'after',
                'length':2,
                'type':'Person'
            }
        }
    }
}