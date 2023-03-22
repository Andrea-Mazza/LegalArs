from django.core.management.base import BaseCommand
from recuperoCredito.models import Comuni, Tribunali


class Command(BaseCommand):
    help = 'Populate the Comuni tribunale field with initial data'

    def handle(self, *args, **options):
        comuni = Comuni.objects.all()
        for comune in comuni:
            if comune.nome in ["AGUGLIANO",

                               "ANCONA",

                               "ARCEVIA",

                               "BARBARA",

                               "BELVEDERE OSTRENSE",

                               "CAMERANO",

                               "CAMERATA PICENA",

                               "CASTEL COLONNA",

                               "CASTELBELLINO",

                               "CASTELFIDARDO",

                               "CASTELLEONE DI SUASA",

                               "CASTELPLANIO",

                               "CERRETO D'ESI",

                               "CHIARAVALLE",

                               "CORINALDO",

                               "CUPRAMONTANA",

                               "FABRIANO",

                               "FALCONARA MARITTIMA",

                               "FILOTTRANO",

                               "GENGA",

                               "JESI",

                               "LORETO",

                               "MAIOLATI SPONTINI",

                               "MERGO",

                               "MONSANO",

                               "MONTE ROBERTO",

                               "MONTE SAN VITO",

                               "MONTECAROTTO",

                               "MONTEMARCIANO",

                               "MONTERADO",

                               "MORRO D'ALBA",

                               "NUMANA",

                               "OFFAGNA",

                               "OSIMO",

                               "OSTRA",

                               "OSTRA VETERE",

                               "POGGIO SAN MARCELLO",

                               "POLVERIGI",

                               "RIPE",

                               "ROSORA",

                               "SAN MARCELLO",

                               "SAN PAOLO DI JESI",

                               "SANTA MARIA NUOVA",

                               "SASSOFERRATO",

                               "SENIGALLIA",

                               "SERRA DE' CONTI",

                               "SERRA SAN QUIRICO",

                               "SIROLO",

                               "STAFFOLO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI ANCONA')
            elif comune.nome in ["ACQUASANTA TERME",

                                 "ACQUAVIVA PICENA",

                                 "AMANDOLA",

                                 "APPIGNANO DEL TRONTO",

                                 "ARQUATA DEL TRONTO",

                                 "ASCOLI PICENO",

                                 "CARASSAI",

                                 "CASTEL DI LAMA",

                                 "CASTIGNANO",

                                 "CASTORANO",

                                 "COLLI DEL TRONTO",

                                 "COMUNANZA",

                                 "FOLIGNANO",

                                 "FORCE",

                                 "MALTIGNANO",

                                 "MONSAMPOLO DEL TRONTO",

                                 "MONTALTO DELLE MARCHE",

                                 "MONTEDINOVE",

                                 "MONTEFORTINO",

                                 "MONTEGALLO",

                                 "MONTEMONACO",

                                 "MONTEPRANDONE",

                                 "OFFIDA",

                                 "PALMIANO",

                                 "ROCCAFLUVIONE",

                                 "ROTELLA",

                                 "SAN BENEDETTO DEL TRONTO",

                                 "SPINETOLI",

                                 "VALLE CASTELLANA",

                                 "VENAROTTA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI ASCOLI PICENO')
            elif comune.nome in ["ALTIDONA",

                                 "BELMONTE PICENO",

                                 "CAMPOFILONE",

                                 "COSSIGNANO",

                                 "CUPRA MARITTIMA",

                                 "FALERONE",

                                 "FERMO",

                                 "FRANCAVILLA D'ETE",

                                 "GROTTAMMARE",

                                 "GROTTAZZOLINA",

                                 "LAPEDONA",

                                 "MAGLIANO DI TENNA",

                                 "MASSA FERMANA",

                                 "MASSIGNANO",

                                 "MONSAMPIETRO MORICO",

                                 "MONTAPPONE",

                                 "MONTE GIBERTO",

                                 "MONTE RINALDO",

                                 "MONTE SAN PIETRANGELI",

                                 "MONTE URANO",

                                 "MONTE VIDON COMBATTE",

                                 "MONTE VIDON CORRADO",

                                 "MONTEFALCONE APPENNINO",

                                 "MONTEFIORE DELL'ASO",

                                 "MONTEGIORGIO",

                                 "MONTEGRANARO",

                                 "MONTELEONE DI FERMO",

                                 "MONTELPARO",

                                 "MONTERUBBIANO",

                                 "MONTOTTONE",

                                 "MORESCO",

                                 "ORTEZZANO",

                                 "PEDASO",

                                 "PETRITOLI",

                                 "PONZANO DI FERMO",

                                 "PORTO SAN GIORGIO",

                                 "PORTO SANT'ELPIDIO",

                                 "RAPAGNANO",

                                 "RIPATRANSONE",

                                 "SANTA VITTORIA IN MATENANO",

                                 "SANT'ELPIDIO A MARE",

                                 "SERVIGLIANO",

                                 "SMERILLO",

                                 "TORRE SAN PATRIZIO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI FERMO')
            elif comune.nome in ["ACQUACANINA",

                                 "APIRO",

                                 "APPIGNANO",

                                 "BELFORTE DEL CHIENTI",

                                 "BOLOGNOLA",

                                 "CALDAROLA",

                                 "CAMERINO",

                                 "CAMPOROTONDO DI FIASTRONE",

                                 "CASTELRAIMONDO",

                                 "CASTELSANTANGELO SUL NERA",

                                 "CESSAPALOMBO",

                                 "CINGOLI",

                                 "CIVITANOVA MARCHE",

                                 "COLMURANO",

                                 "CORRIDONIA",

                                 "ESANATOGLIA",

                                 "FIASTRA",

                                 "FIORDIMONTE",

                                 "FIUMINATA",

                                 "GAGLIOLE",

                                 "GUALDO",

                                 "LORO PICENO",

                                 "MACERATA",

                                 "MATELICA",

                                 "MOGLIANO",

                                 "MONTE CAVALLO",

                                 "MONTE SAN GIUSTO",

                                 "MONTE SAN MARTINO",

                                 "MONTECASSIANO",

                                 "MONTECOSARO",

                                 "MONTEFANO",

                                 "MONTELUPONE",

                                 "MORROVALLE",

                                 "MUCCIA",

                                 "PENNA SAN GIOVANNI",

                                 "PETRIOLO",

                                 "PIEVE TORINA",

                                 "PIEVEBOVIGLIANA",

                                 "PIORACO",

                                 "POGGIO SAN VICINO",

                                 "POLLENZA",

                                 "PORTO RECANATI",

                                 "POTENZA PICENA",

                                 "RECANATI",

                                 "RIPE SAN GINESIO",

                                 "SAN GINESIO",

                                 "SAN SEVERINO MARCHE",

                                 "SANT'ANGELO IN PONTANO",

                                 "SARNANO",

                                 "SEFRO",

                                 "SERRAPETRONA",

                                 "SERRAVALLE DI CHIENTI",

                                 "TOLENTINO",

                                 "TREIA",

                                 "URBISAGLIA",

                                 "USSITA",

                                 "VISSO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE CIVILE DI MACERATA')
            elif comune.nome in ["BARCHI",

                                 "CARTOCETO",

                                 "FANO",

                                 "FRATTE ROSA",

                                 "GABICCE MARE",

                                 "GRADARA",

                                 "MOMBAROCCIO",

                                 "MONDAVIO",

                                 "MONDOLFO",

                                 "MONTE PORZIO",

                                 "MONTECICCARDO",

                                 "MONTELABBATE",

                                 "MONTEMAGGIORE AL METAURO",

                                 "ORCIANO DI PESARO",

                                 "PERGOLA",

                                 "PESARO",

                                 "PIAGGE",

                                 "SALTARA",

                                 "SAN COSTANZO",

                                 "SAN GIORGIO DI PESARO",

                                 "SAN LORENZO IN CAMPO",

                                 "SANT'ANGELO IN LIZZOLA",

                                 "SERRA SANT'ABBONDIO",

                                 "SERRUNGARINA",

                                 "TAVULLIA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PESARO')
            elif comune.nome in ["ACQUALAGNA",

                                 "APECCHIO",

                                 "AUDITORE",

                                 "BELFORTE ALL'ISAURO",

                                 "BORGO PACE",

                                 "CAGLI",

                                 "CANTIANO",

                                 "CARPEGNA",

                                 "COLBORDOLO",

                                 "FERMIGNANO",

                                 "FOSSOMBRONE",

                                 "FRONTINO",

                                 "FRONTONE",

                                 "ISOLA DEL PIANO",

                                 "LUNANO",

                                 "MACERATA FELTRIA",

                                 "MERCATELLO SUL METAURO",

                                 "MERCATINO CONCA",

                                 "MONTE CERIGNONE",

                                 "MONTE GRIMANO TERME",

                                 "MONTECALVO IN FOGLIA",

                                 "MONTECOPIOLO",

                                 "MONTEFELCINO",

                                 "PEGLIO",

                                 "PETRIANO",

                                 "PIANDIMELETO",

                                 "PIETRARUBBIA",

                                 "PIOBBICO",

                                 "SANT'ANGELO IN VADO",

                                 "SANT'IPPOLITO",

                                 "SASSOCORVARO",

                                 "SASSOFELTRIO",

                                 "TAVOLETO",

                                 "URBANIA",

                                 "URBINO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI URBINO')
            elif comune.nome in ["ACQUAVIVA DELLE FONTI",

                                 "ADELFIA",

                                 "ALBEROBELLO",

                                 "ALTAMURA",

                                 "BARI",

                                 "BINETTO",

                                 "BITETTO",

                                 "BITONTO",

                                 "BITRITTO",

                                 "CAPURSO",

                                 "CASAMASSIMA",

                                 "CASSANO DELLE MURGE",

                                 "CASTELLANA GROTTE",

                                 "CELLAMARE",

                                 "CONVERSANO",

                                 "GIOIA DEL COLLE",

                                 "GIOVINAZZO",

                                 "GRAVINA IN PUGLIA",

                                 "GRUMO APPULA",

                                 "LOCOROTONDO",

                                 "MODUGNO",

                                 "MOLA DI BARI",

                                 "MONOPOLI",

                                 "NOCI",

                                 "NOICATTARO",

                                 "PALO DEL COLLE",

                                 "POGGIORSINI",

                                 "POLIGNANO A MARE",

                                 "PUTIGNANO",

                                 "RUTIGLIANO",

                                 "SAMMICHELE DI BARI",

                                 "SANNICANDRO DI BARI",

                                 "SANTERAMO IN COLLE",

                                 "TORITTO",

                                 "TRIGGIANO",

                                 "TURI",

                                 "VALENZANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI BARI')
            elif comune.nome in ["ACCADIA",

                                 "ALBERONA",

                                 "ANZANO DI PUGLIA",

                                 "APRICENA",

                                 "ASCOLI SATRIANO",

                                 "BICCARI",

                                 "BOVINO",

                                 "CAGNANO VARANO",

                                 "CANDELA",

                                 "CARAPELLE",

                                 "CARLANTINO",

                                 "CARPINO",

                                 "CASALNUOVO MONTEROTARO",

                                 "CASALVECCHIO DI PUGLIA",

                                 "CASTELLUCCIO DEI SAURI",

                                 "CASTELLUCCIO VALMAGGIORE",

                                 "CASTELNUOVO DELLA DAUNIA",

                                 "CELENZA VALFORTORE",

                                 "CELLE DI SAN VITO",

                                 "CERIGNOLA",

                                 "CHIEUTI",

                                 "DELICETO",

                                 "FAETO",

                                 "FOGGIA",

                                 "ISCHITELLA",

                                 "ISOLE TREMITI",

                                 "LESINA",

                                 "LUCERA",

                                 "MANFREDONIA",

                                 "MARGHERITA DI SAVOIA",

                                 "MATTINATA",

                                 "MONTE SANT'ANGELO",

                                 "MONTELEONE DI PUGLIA",

                                 "MOTTA MONTECORVINO",

                                 "ORDONA",

                                 "ORSARA DI PUGLIA",

                                 "ORTA NOVA",

                                 "PANNI",

                                 "PESCHICI",

                                 "PIETRAMONTECORVINO",

                                 "POGGIO IMPERIALE",

                                 "RIGNANO GARGANICO",

                                 "ROCCHETTA SANT'ANTONIO",

                                 "RODI GARGANICO",

                                 "ROSETO VALFORTORE",

                                 "SAN FERDINANDO DI PUGLIA",

                                 "SAN GIOVANNI ROTONDO",

                                 "SAN MARCO IN LAMIS",

                                 "SAN MARCO LA CATOLA",

                                 "SAN NICANDRO GARGANICO",

                                 "SAN PAOLO DI CIVITATE",

                                 "SAN SEVERO",

                                 "SANT'AGATA DI PUGLIA",

                                 "SERRACAPRIOLA",

                                 "STORNARA",

                                 "STORNARELLA",

                                 "TORREMAGGIORE",

                                 "TRINITAPOLI",

                                 "TROIA",

                                 "VICO DEL GARGANO",

                                 "VIESTE",

                                 "VOLTURARA APPULA",

                                 "VOLTURINO",

                                 "ZAPPONETA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI FOGGIA')
            elif comune.nome in ["ANDRIA",

                                 "BARLETTA",

                                 "BISCEGLIE",

                                 "CANOSA DI PUGLIA",

                                 "CORATO",

                                 "MINERVINO MURGE",

                                 "MOLFETTA",

                                 "RUVO DI PUGLIA",

                                 "SPINAZZOLA",

                                 "TERLIZZI",

                                 "TRANI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI TRANI')
            elif comune.nome in ["ANZOLA DELL'EMILIA",

                                 "ARGELATO",

                                 "BARICELLA",

                                 "BAZZANO",

                                 "BENTIVOGLIO",

                                 "BOLOGNA",

                                 "BORGO TOSSIGNANO",

                                 "BUDRIO",

                                 "CALDERARA DI RENO",

                                 "CAMUGNANO",

                                 "CASALECCHIO DI RENO",

                                 "CASALFIUMANESE",

                                 "CASTEL D'AIANO",

                                 "CASTEL DEL RIO",

                                 "CASTEL DI CASIO",

                                 "CASTEL GUELFO DI BOLOGNA",

                                 "CASTEL MAGGIORE",

                                 "CASTEL SAN PIETRO TERME",

                                 "CASTELLO D'ARGILE",

                                 "CASTELLO DI SERRAVALLE",

                                 "CASTENASO",

                                 "CASTIGLIONE DEI PEPOLI",

                                 "CRESPELLANO",

                                 "CREVALCORE",

                                 "DOZZA",

                                 "FONTANELICE",

                                 "GAGGIO MONTANO",

                                 "GALLIERA",

                                 "GRANAGLIONE",

                                 "GRANAROLO DELL'EMILIA",

                                 "GRIZZANA MORANDI",

                                 "IMOLA",

                                 "LIZZANO IN BELVEDERE",

                                 "LOIANO",

                                 "MALALBERGO",

                                 "MARZABOTTO",

                                 "MEDICINA",

                                 "MINERBIO",

                                 "MOLINELLA",

                                 "MONGHIDORO",

                                 "MONTE SAN PIETRO",

                                 "MONTERENZIO",

                                 "MONTEVEGLIO",

                                 "MONZUNO",

                                 "MORDANO",

                                 "OZZANO DELL'EMILIA",

                                 "PIANORO",

                                 "PORRETTA TERME",

                                 "SALA BOLOGNESE",

                                 "SAN BENEDETTO VAL DI SAMBRO",

                                 "SAN GIORGIO DI PIANO",

                                 "SAN GIOVANNI IN PERSICETO",

                                 "SAN LAZZARO DI SAVENA",

                                 "SAN PIETRO IN CASALE",

                                 "SANT'AGATA BOLOGNESE",

                                 "SASSO MARCONI",

                                 "SAVIGNO",

                                 "VERGATO",

                                 "ZOLA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI BOLOGNA')
            elif comune.nome in ["ARGENTA",

                                 "BERRA",

                                 "BONDENO",

                                 "CENTO",

                                 "CODIGORO",

                                 "COMACCHIO",

                                 "COPPARO",

                                 "FERRARA",

                                 "FORMIGNANA",

                                 "GORO",

                                 "JOLANDA DI SAVOIA",

                                 "LAGOSANTO",

                                 "MASI TORELLO",

                                 "MASSA FISCAGLIA",

                                 "MESOLA",

                                 "MIGLIARINO",

                                 "MIGLIARO",

                                 "MIRABELLO",

                                 "OSTELLATO",

                                 "PIEVE DI CENTO",

                                 "POGGIO RENATICO",

                                 "PORTOMAGGIORE",

                                 "RO",

                                 "SANT'AGOSTINO",

                                 "TRESIGALLO",

                                 "VIGARANO MAINARDA",

                                 "VOGHIERA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI FERRARA')
            elif comune.nome in ["BAGNO DI ROMAGNA",

                                 "BERTINORO",

                                 "BORGHI",

                                 "CASTROCARO TERME E TERRA DEL SOLE",

                                 "CESENA",

                                 "CESENATICO",

                                 "CIVITELLA DI ROMAGNA",

                                 "DOVADOLA",

                                 "FORLI'",

                                 "FORLIMPOPOLI",

                                 "GALEATA",

                                 "GAMBETTOLA",

                                 "GATTEO",

                                 "LONGIANO",

                                 "MELDOLA",

                                 "MERCATO SARACENO",

                                 "MODIGLIANA",

                                 "MONTIANO",

                                 "PORTICO E SAN BENEDETTO",

                                 "PREDAPPIO",

                                 "PREMILCUORE",

                                 "ROCCA SAN CASCIANO",

                                 "RONCOFREDDO",

                                 "SAN MAURO PASCOLI",

                                 "SANTA SOFIA",

                                 "SARSINA",

                                 "SAVIGNANO SUL RUBICONE",

                                 "SOGLIANO AL RUBICONE",

                                 "TREDOZIO",

                                 "VERGHERETO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome="TRIBUNALE CIVILE DI FORLI'")
            elif comune.nome in ["BASTIGLIA",

                                 "BOMPORTO",

                                 "CAMPOGALLIANO",

                                 "CAMPOSANTO",

                                 "CARPI",

                                 "CASTELFRANCO EMILIA",

                                 "CASTELNUOVO RANGONE",

                                 "CASTELVETRO DI MODENA",

                                 "CAVEZZO",

                                 "CONCORDIA SULLA SECCHIA",

                                 "FANANO",

                                 "FINALE EMILIA",

                                 "FIORANO MODENESE",

                                 "FIUMALBO",

                                 "FORMIGINE",

                                 "FRASSINORO",

                                 "GUIGLIA",

                                 "LAMA MOCOGNO",

                                 "MARANELLO",

                                 "MARANO SUL PANARO",

                                 "MEDOLLA",

                                 "MIRANDOLA",

                                 "MODENA",

                                 "MONTECRETO",

                                 "MONTEFIORINO",

                                 "MONTESE",

                                 "NONANTOLA",

                                 "NOVI DI MODENA",

                                 "PALAGANO",

                                 "PAVULLO NEL FRIGNANO",

                                 "PIEVEPELAGO",

                                 "POLINAGO",

                                 "PRIGNANO SULLA SECCHIA",

                                 "RAVARINO",

                                 "RIOLUNATO",

                                 "SAN CESARIO SUL PANARO",

                                 "SAN FELICE SUL PANARO",

                                 "SAN POSSIDONIO",

                                 "SAN PROSPERO",

                                 "SASSUOLO",

                                 "SAVIGNANO SUL PANARO",

                                 "SERRAMAZZONI",

                                 "SESTOLA",

                                 "SOLIERA",

                                 "SPILAMBERTO",

                                 "VIGNOLA",

                                 "ZOCCA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI MODENA')
            elif comune.nome in ["ALBARETO",

                                 "BARDI",

                                 "BEDONIA",

                                 "BERCETO",

                                 "BORE",

                                 "BORGO VAL DI TARO",

                                 "BUSSETO",

                                 "CALESTANO",

                                 "COLLECCHIO",

                                 "COLORNO",

                                 "COMPIANO",

                                 "CORNIGLIO",

                                 "FELINO",

                                 "FIDENZA",

                                 "FONTANELLATO",

                                 "FONTEVIVO",

                                 "FORNOVO DI TARO",

                                 "LANGHIRANO",

                                 "LESIGNANO DE' BAGNI",

                                 "MEDESANO",

                                 "MEZZANI",

                                 "MONCHIO DELLE CORTI",

                                 "MONTECHIARUGOLO",

                                 "NEVIANO DEGLI ARDUINI",

                                 "NOCETO",

                                 "PALANZANO",

                                 "PARMA",

                                 "PELLEGRINO PARMENSE",

                                 "POLESINE PARMENSE",

                                 "ROCCABIANCA",

                                 "SALA BAGANZA",

                                 "SALSOMAGGIORE TERME",

                                 "SAN SECONDO PARMENSE",

                                 "SISSA",

                                 "SOLIGNANO",

                                 "SORAGNA",

                                 "SORBOLO",

                                 "TERENZO",

                                 "TIZZANO VAL PARMA",

                                 "TORNOLO",

                                 "TORRILE",

                                 "TRAVERSETOLO",

                                 "TRECASALI",

                                 "VALMOZZOLA",

                                 "VARANO DE' MELEGARI",

                                 "VARSI",

                                 "ZIBELLO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PARMA')
            elif comune.nome in ["AGAZZANO",

                                 "ALSENO",

                                 "BESENZONE",

                                 "BETTOLA",

                                 "BOBBIO",

                                 "BORGONOVO VAL TIDONE",

                                 "CADEO",

                                 "CALENDASCO",

                                 "CAMINATA",

                                 "CAORSO",

                                 "CARPANETO PIACENTINO",

                                 "CASTEL SAN GIOVANNI",

                                 "CASTELL'ARQUATO",

                                 "CASTELVETRO PIACENTINO",

                                 "CERIGNALE",

                                 "COLI",

                                 "CORTE BRUGNATELLA",

                                 "CORTEMAGGIORE",

                                 "FARINI",

                                 "FERRIERE",

                                 "FIORENZUOLA D'ARDA",

                                 "GAZZOLA",

                                 "GOSSOLENGO",

                                 "GRAGNANO TREBBIENSE",

                                 "GROPPARELLO",

                                 "LUGAGNANO VAL D'ARDA",

                                 "MONTICELLI D'ONGINA",

                                 "MORFASSO",

                                 "NIBBIANO",

                                 "OTTONE",

                                 "PECORARA",

                                 "PIACENZA",

                                 "PIANELLO VAL TIDONE",

                                 "PIOZZANO",

                                 "PODENZANO",

                                 "PONTE DELL'OLIO",

                                 "PONTENURE",

                                 "RIVERGARO",

                                 "ROTTOFRENO",

                                 "SAN GIORGIO PIACENTINO",

                                 "SAN PIETRO IN CERRO",

                                 "SARMATO",

                                 "TRAVO",

                                 "VERNASCA",

                                 "VIGOLZONE",

                                 "VILLANOVA SULL'ARDA",

                                 "ZERBA",

                                 "ZIANO PIACENTINO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PIACENZA')
            elif comune.nome in ["ALFONSINE",

                                 "BAGNACAVALLO",

                                 "BAGNARA DI ROMAGNA",

                                 "BRISIGHELLA",

                                 "CASOLA VALSENIO",

                                 "CASTEL BOLOGNESE",

                                 "CERVIA",

                                 "CONSELICE",

                                 "COTIGNOLA",

                                 "FAENZA",

                                 "FUSIGNANO",

                                 "LUGO",

                                 "MASSA LOMBARDA",

                                 "RAVENNA",

                                 "RIOLO TERME",

                                 "RUSSI",

                                 "SANT'AGATA SUL SANTERNO",

                                 "SOLAROLO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI RAVENNA')
            elif comune.nome in ["ALBINEA",

                                 "BAGNOLO IN PIANO",

                                 "BAISO",

                                 "BIBBIANO",

                                 "BORETTO",

                                 "BRESCELLO",

                                 "BUSANA",

                                 "CADELBOSCO DI SOPRA",

                                 "CAMPAGNOLA EMILIA",

                                 "CAMPEGINE",

                                 "CANOSSA",

                                 "CARPINETI",

                                 "CASALGRANDE",

                                 "CASINA",

                                 "CASTELLARANO",

                                 "CASTELNOVO DI SOTTO",

                                 "CASTELNOVO NE' MONTI",

                                 "CAVRIAGO",

                                 "COLLAGNA",

                                 "CORREGGIO",

                                 "FABBRICO",

                                 "GATTATICO",

                                 "GUALTIERI",

                                 "GUASTALLA",

                                 "LIGONCHIO",

                                 "LUZZARA",

                                 "MONTECCHIO EMILIA",

                                 "NOVELLARA",

                                 "POVIGLIO",

                                 "QUATTRO CASTELLA",

                                 "RAMISETO",

                                 "REGGIO NELL'EMILIA",

                                 "REGGIOLO",

                                 "RIO SALICETO",

                                 "ROLO",

                                 "RUBIERA",

                                 "SAN MARTINO IN RIO",

                                 "SAN POLO D'ENZA",

                                 "SANT'ILARIO D'ENZA",

                                 "SCANDIANO",

                                 "TOANO",

                                 "VETTO",

                                 "VEZZANO SUL CROSTOLO",

                                 "VIANO",

                                 "VILLA MINOZZO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI REGGIO EMILIA')
            elif comune.nome in ["BELLARIA-IGEA MARINA",

                                 "CASTELDELCI",

                                 "CATTOLICA",

                                 "CORIANO",

                                 "GEMMANO",

                                 "MAIOLO",

                                 "MISANO ADRIATICO",

                                 "MONDAINO",

                                 "MONTE COLOMBO",

                                 "MONTEFIORE CONCA",

                                 "MONTEGRIDOLFO",

                                 "MONTESCUDO",

                                 "MORCIANO DI ROMAGNA",

                                 "NOVAFELTRIA",

                                 "PENNABILLI",

                                 "POGGIO BERNI",

                                 "RICCIONE",

                                 "RIMINI",

                                 "SALUDECIO",

                                 "SAN CLEMENTE",

                                 "SAN GIOVANNI IN MARIGNANO",

                                 "SAN LEO",

                                 "SANT'AGATA FELTRIA",

                                 "SANTARCANGELO DI ROMAGNA",

                                 "TALAMELLO",

                                 "TORRIANA",

                                 "VERUCCHIO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI RIMINI')
            elif comune.nome in ["ALDINO/ALDEIN",

                                 "ANDRIANO/ANDRIAN",

                                 "ANTERIVO/ALTREI",

                                 "APPIANO SULLA STRADA DEL VINO/EPPAN AN DER WEINSTRASSE",

                                 "AVELENGO/HAFLING",

                                 "BADIA/ABTEI",

                                 "BARBIANO/BARBIAN",

                                 "BOLZANO/BOZEN",

                                 "BRAIES/PRAGS",

                                 "BRENNERO/BRENNER",

                                 "BRESSANONE/BRIXEN",

                                 "BRONZOLO/BRANZOLL",

                                 "BRUNICO/BRUNECK",

                                 "CAINES/KUENS",

                                 "CALDARO SULLA STRADA DEL VINO/KALTERN AN DER WEINSTRASSE",

                                 "CAMPO DI TRENS/FREIENFELD",

                                 "CAMPO TURES/SAND IN TAUFERS",

                                 "CASTELBELLO-CIARDES/KASTELBELL-TSCHARS",

                                 "CASTELROTTO/KASTELRUTH",

                                 "CERMES/TSCHERMS",

                                 "CHIENES/KIENS",

                                 "CHIUSA/KLAUSEN",

                                 "CORNEDO ALL'ISARCO/KARNEID",

                                 "CORTACCIA SULLA STRADA DEL VINO/KURTATSCH AN DER WEINSTRASSE",

                                 "CORTINA SULLA STRADA DEL VINO/KURTINIG AN DER WEINSTRASSE",

                                 "CORVARA IN BADIA/CORVARA",

                                 "CURON VENOSTA/GRAUN IM VINSCHGAU",

                                 "DOBBIACO/TOBLACH",

                                 "EGNA/NEUMARKT",

                                 "FALZES/PFALZEN",

                                 "FIE' ALLO SCILIAR/VÖLS AM SCHLERN",

                                 "FORTEZZA/FRANZENSFESTE",

                                 "FUNES/VILLNÖSS",

                                 "GAIS/GAIS",

                                 "GARGAZZONE/GARGAZON",

                                 "GLORENZA/GLURNS",

                                 "LA VALLE/WENGEN",

                                 "LACES/LATSCH",

                                 "LAGUNDO/ALGUND",

                                 "LAION/LAJEN",

                                 "LAIVES/LEIFERS",

                                 "LANA/LANA",

                                 "LASA/LAAS",

                                 "LAUREGNO/LAUREIN",

                                 "LUSON/LÜSEN",

                                 "MAGRE' SULLA STRADA DEL VINO/MARGREID AN DER WEINSTRASSE",

                                 "MALLES VENOSTA/MALS",

                                 "MAREBBE/ENNEBERG",

                                 "MARLENGO/MARLING",

                                 "MARTELLO/MARTELL",

                                 "MELTINA/MÖLTEN",

                                 "MERANO/MERAN",

                                 "MONGUELFO-TESIDO/WELSBERGTAISTEN",

                                 "MONTAGNA/MONTAN",

                                 "MOSO IN PASSIRIA/MOOS IN PASSEIER",

                                 "NALLES/NALS",

                                 "NATURNO/NATURNS",

                                 "NAZ-SCIAVES/NATZ-SCHABS",

                                 "NOVA LEVANTE/WELSCHNOFEN",

                                 "NOVA PONENTE/DEUTSCHNOFEN",

                                 "ORA/AUER",

                                 "ORTISEI/ST. ULRICH",

                                 "PARCINES/PARTSCHINS",

                                 "PERCA/PERCHA",

                                 "PLAUS/PLAUS",

                                 "PONTE GARDENA/WAIDBRUCK",

                                 "POSTAL/BURGSTALL",

                                 "PRATO ALLO STELVIO/PRAD AM STILFSERJOCH",

                                 "PREDOI/PRETTAU",

                                 "PROVES/PROVEIS",

                                 "RACINES/RATSCHINGS",

                                 "RASUN-ANTERSELVA/RASEN-ANTHOLZ",

                                 "RENON/RITTEN",

                                 "RIFIANO/RIFFIAN",

                                 "RIO DI PUSTERIA/MÜHLBACH",

                                 "RODENGO/RODENECK",

                                 "SALORNO/SALURN",

                                 "SAN CANDIDO/INNICHEN",

                                 "SAN GENESIO ATESINO/JENESIEN",

                                 "SAN LEONARDO IN PASSIRIA/ST. LEONHARD IN PASSEIER",

                                 "SAN LORENZO DI SEBATO/ST. LORENZEN",

                                 "SAN MARTINO IN BADIA/ST. MARTIN IN THURN",

                                 "SAN MARTINO IN PASSIRIA/ST. MARTIN IN PASSEIER",

                                 "SAN PANCRAZIO/ST. PANKRAZ",

                                 "SANTA CRISTINA VALGARDENA/ST. CHRISTINA IN GRÖDEN",

                                 "SARENTINO/SARNTAL",

                                 "SCENA/SCHENNA",

                                 "SELVA DEI MOLINI/MÜHLWALD",

                                 "SELVA DI VAL GARDENA/WOLKENSTEIN IN GRÖDEN",

                                 "SENALES/SCHNALS",

                                 "SENALE-SAN FELICE/UNSERE LIEBE FRAU IM WALDE-ST. FELIX",

                                 "SESTO/SEXTEN",

                                 "SILANDRO/SCHLANDERS",

                                 "SLUDERNO/SCHLUDERNS",

                                 "STELVIO/STILFS",

                                 "TERENTO/TERENTEN",

                                 "TERLANO/TERLAN",

                                 "TERMENO SULLA STRADA DEL VINO/TRAMIN AN DER WEINSTRASSE",

                                 "TESIMO/TISENS",

                                 "TIRES/TIERS",

                                 "TIROLO/TIROL",

                                 "TRODENA NEL PARCO NATURALE/TRUDEN IM NATURPARK",

                                 "TUBRE/TAUFERS IM MÜNSTERTAL",

                                 "ULTIMO/ULTEN",

                                 "VADENA/PFATTEN",

                                 "VAL DI VIZZE/PFITSCH",

                                 "VALDAORA/OLANG",

                                 "VALLE AURINA/AHRNTAL",

                                 "VALLE DI CASIES/GSIES",

                                 "VANDOIES/VINTL",

                                 "VARNA/VAHRN",

                                 "VELTURNO/FELDTHURNS",

                                 "VERANO/VÖRAN",

                                 "VILLABASSA/NIEDERDORF",

                                 "VILLANDRO/VILLANDERS",

                                 "VIPITENO/STERZING"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI BOLZANO/BOZEN')
            elif comune.nome in ["ADRARA SAN MARTINO",

                                 "ADRARA SAN ROCCO",

                                 "ALBANO SANT'ALESSANDRO",

                                 "ALBINO",

                                 "ALGUA",

                                 "ALME'",

                                 "ALMENNO SAN BARTOLOMEO",

                                 "ALMENNO SAN SALVATORE",

                                 "ALZANO LOMBARDO",

                                 "AMBIVERE",

                                 "ANTEGNATE",

                                 "ARCENE",

                                 "ARDESIO",

                                 "ARZAGO D'ADDA",

                                 "AVERARA",

                                 "AVIATICO",

                                 "AZZANO SAN PAOLO",

                                 "AZZONE",

                                 "BAGNATICA",

                                 "BARBATA",

                                 "BARIANO",

                                 "BARZANA",

                                 "BEDULITA",

                                 "BERBENNO",

                                 "BERGAMO",

                                 "BERZO SAN FERMO",

                                 "BIANZANO",

                                 "BLELLO",

                                 "BOLGARE",

                                 "BOLTIERE",

                                 "BONATE SOPRA",

                                 "BONATE SOTTO",

                                 "BORGO DI TERZO",

                                 "BOSSICO",

                                 "BOTTANUCO",

                                 "BRACCA",

                                 "BRANZI",

                                 "BREMBATE",

                                 "BREMBATE DI SOPRA",

                                 "BREMBILLA",

                                 "BRIGNANO GERA D'ADDA",

                                 "BRUMANO",

                                 "BRUSAPORTO",

                                 "CALCINATE",

                                 "CALCIO",

                                 "CALUSCO D'ADDA",

                                 "CALVENZANO",

                                 "CAMERATA CORNELLO",

                                 "CANONICA D'ADDA",

                                 "CAPIZZONE",

                                 "CAPRIATE SAN GERVASIO",

                                 "CAPRINO BERGAMASCO",

                                 "CARAVAGGIO",

                                 "CAROBBIO DEGLI ANGELI",

                                 "CARONA",

                                 "CARVICO",

                                 "CASAZZA",

                                 "CASIRATE D'ADDA",

                                 "CASNIGO",

                                 "CASSIGLIO",

                                 "CASTEL ROZZONE",

                                 "CASTELLI CALEPIO",

                                 "CASTIONE DELLA PRESOLANA",

                                 "CASTRO",

                                 "CAVERNAGO",

                                 "CAZZANO SANT'ANDREA",

                                 "CENATE SOPRA",

                                 "CENATE SOTTO",

                                 "CENE",

                                 "CERETE",

                                 "CHIGNOLO D'ISOLA",

                                 "CHIUDUNO",

                                 "CISANO BERGAMASCO",

                                 "CISERANO",

                                 "CIVIDATE AL PIANO",

                                 "CLUSONE",

                                 "COLERE",

                                 "COLOGNO AL SERIO",

                                 "COLZATE",

                                 "COMUN NUOVO",

                                 "CORNA IMAGNA",

                                 "CORNALBA",

                                 "CORTENUOVA",

                                 "COSTA DI MEZZATE",

                                 "COSTA SERINA",

                                 "COSTA VALLE IMAGNA",

                                 "COSTA VOLPINO",

                                 "COVO",

                                 "CREDARO",

                                 "CURNO",

                                 "CUSIO",

                                 "DALMINE",

                                 "DOSSENA",

                                 "ENDINE GAIANO",

                                 "ENTRATICO",

                                 "FARA GERA D'ADDA",

                                 "FARA OLIVANA CON SOLA",

                                 "FILAGO",

                                 "FINO DEL MONTE",

                                 "FIORANO AL SERIO",

                                 "FONTANELLA",

                                 "FONTENO",

                                 "FOPPOLO",

                                 "FORESTO SPARSO",

                                 "FORNOVO SAN GIOVANNI",

                                 "FUIPIANO VALLE IMAGNA",

                                 "GANDELLINO",

                                 "GANDINO",

                                 "GANDOSSO",

                                 "GAVERINA TERME",

                                 "GAZZANIGA",

                                 "GEROSA",

                                 "GHISALBA",

                                 "GORLAGO",

                                 "GORLE",

                                 "GORNO",

                                 "GRASSOBBIO",

                                 "GROMO",

                                 "GRONE",

                                 "GRUMELLO DEL MONTE",

                                 "ISOLA DI FONDRA",

                                 "ISSO",

                                 "LALLIO",

                                 "LEFFE",

                                 "LENNA",

                                 "LEVATE",

                                 "LOCATELLO",

                                 "LOVERE",

                                 "LURANO",

                                 "LUZZANA",

                                 "MADONE",

                                 "MAPELLO",

                                 "MARTINENGO",

                                 "MEDOLAGO",

                                 "MEZZOLDO",

                                 "MISANO DI GERA D'ADDA",

                                 "MOIO DE' CALVI",

                                 "MONASTEROLO DEL CASTELLO",

                                 "MONTELLO",

                                 "MORENGO",

                                 "MORNICO AL SERIO",

                                 "MOZZANICA",

                                 "MOZZO",

                                 "NEMBRO",

                                 "OLMO AL BREMBO",

                                 "OLTRE IL COLLE",

                                 "OLTRESSENDA ALTA",

                                 "ONETA",

                                 "ONORE",

                                 "ORIO AL SERIO",

                                 "ORNICA",

                                 "OSIO SOPRA",

                                 "OSIO SOTTO",

                                 "PAGAZZANO",

                                 "PALADINA",

                                 "PALAZZAGO",

                                 "PALOSCO",

                                 "PARRE",

                                 "PARZANICA",

                                 "PEDRENGO",

                                 "PEIA",

                                 "PIANICO",

                                 "PIARIO",

                                 "PIAZZA BREMBANA",

                                 "PIAZZATORRE",

                                 "PIAZZOLO",

                                 "POGNANO",

                                 "PONTE NOSSA",

                                 "PONTE SAN PIETRO",

                                 "PONTERANICA",

                                 "PONTIDA",

                                 "PONTIROLO NUOVO",

                                 "PRADALUNGA",

                                 "PREDORE",

                                 "PREMOLO",

                                 "PRESEZZO",

                                 "PUMENENGO",

                                 "RANICA",

                                 "RANZANICO",

                                 "RIVA DI SOLTO",

                                 "ROGNO",

                                 "ROMANO DI LOMBARDIA",

                                 "RONCOBELLO",

                                 "RONCOLA",

                                 "ROTA D'IMAGNA",

                                 "ROVETTA",

                                 "SAN GIOVANNI BIANCO",

                                 "SAN PAOLO D'ARGON",

                                 "SAN PELLEGRINO TERME",

                                 "SANTA BRIGIDA",

                                 "SANT'OMOBONO TERME",

                                 "SARNICO",

                                 "SCANZOROSCIATE",

                                 "SCHILPARIO",

                                 "SEDRINA",

                                 "SELVINO",

                                 "SERIATE",

                                 "SERINA",

                                 "SOLTO COLLINA",

                                 "SOLZA",

                                 "SONGAVAZZO",

                                 "SORISOLE",

                                 "SOTTO IL MONTE GIOVANNI XXIII",

                                 "SOVERE",

                                 "SPINONE AL LAGO",

                                 "SPIRANO",

                                 "STEZZANO",

                                 "STROZZA",

                                 "SUISIO",

                                 "TALEGGIO",

                                 "TAVERNOLA BERGAMASCA",

                                 "TELGATE",

                                 "TERNO D'ISOLA",

                                 "TORRE BOLDONE",

                                 "TORRE DE' ROVERI",

                                 "TORRE PALLAVICINA",

                                 "TRESCORE BALNEARIO",

                                 "TREVIGLIO",

                                 "TREVIOLO",

                                 "UBIALE CLANEZZO",

                                 "URGNANO",

                                 "VALBONDIONE",

                                 "VALBREMBO",

                                 "VALGOGLIO",

                                 "VALLEVE",

                                 "VALNEGRA",

                                 "VALSECCA",

                                 "VALTORTA",

                                 "VEDESETA",

                                 "VERDELLINO",

                                 "VERDELLO",

                                 "VERTOVA",

                                 "VIADANICA",

                                 "VIGANO SAN MARTINO",

                                 "VIGOLO",

                                 "VILLA D'ADDA",

                                 "VILLA D'ALME'",

                                 "VILLA DI SERIO",

                                 "VILLA D'OGNA",

                                 "VILLONGO",

                                 "VILMINORE DI SCALVE",

                                 "ZANDOBBIO",

                                 "ZANICA",

                                 "ZOGNO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI BERGAMO')
            elif comune.nome in ["ACQUAFREDDA",

                                 "ADRO",

                                 "AGNOSINE",

                                 "ALFIANELLO",

                                 "ANFO",

                                 "ANGOLO TERME",

                                 "ARTOGNE",

                                 "AZZANO MELLA",

                                 "BAGNOLO MELLA",

                                 "BAGOLINO",

                                 "BARBARIGA",

                                 "BARGHE",

                                 "BASSANO BRESCIANO",

                                 "BEDIZZOLE",

                                 "BERLINGO",

                                 "BERZO DEMO",

                                 "BERZO INFERIORE",

                                 "BIENNO",

                                 "BIONE",

                                 "BORGO SAN GIACOMO",

                                 "BORGOSATOLLO",

                                 "BORNO",

                                 "BOTTICINO",

                                 "BOVEGNO",

                                 "BOVEZZO",

                                 "BRANDICO",

                                 "BRAONE",

                                 "BRENO",

                                 "BRESCIA",

                                 "BRIONE",

                                 "CAINO",

                                 "CALCINATO",

                                 "CALVAGESE DELLA RIVIERA",

                                 "CALVISANO",

                                 "CAPO DI PONTE",

                                 "CAPOVALLE",

                                 "CAPRIANO DEL COLLE",

                                 "CAPRIOLO",

                                 "CARPENEDOLO",

                                 "CASTEGNATO",

                                 "CASTEL MELLA",

                                 "CASTELCOVATI",

                                 "CASTENEDOLO",

                                 "CASTO",

                                 "CASTREZZATO",

                                 "CAZZAGO SAN MARTINO",

                                 "CEDEGOLO",

                                 "CELLATICA",

                                 "CERVENO",

                                 "CETO",

                                 "CEVO",

                                 "CHIARI",

                                 "CIGOLE",

                                 "CIMBERGO",

                                 "CIVIDATE CAMUNO",

                                 "COCCAGLIO",

                                 "COLLEBEATO",

                                 "COLLIO",

                                 "COLOGNE",

                                 "COMEZZANO-CIZZAGO",

                                 "CONCESIO",

                                 "CORTE FRANCA",

                                 "CORTENO GOLGI",

                                 "CORZANO",

                                 "DARFO BOARIO TERME",

                                 "DELLO",

                                 "DESENZANO DEL GARDA",

                                 "EDOLO",

                                 "ERBUSCO",

                                 "ESINE",

                                 "FIESSE",

                                 "FLERO",

                                 "GAMBARA",

                                 "GARDONE RIVIERA",

                                 "GARDONE VAL TROMPIA",

                                 "GARGNANO",

                                 "GAVARDO",

                                 "GHEDI",

                                 "GIANICO",

                                 "GOTTOLENGO",

                                 "GUSSAGO",

                                 "IDRO",

                                 "INCUDINE",

                                 "IRMA",

                                 "ISEO",

                                 "ISORELLA",

                                 "LAVENONE",

                                 "LENO",

                                 "LIMONE SUL GARDA",

                                 "LODRINO",

                                 "LOGRATO",

                                 "LONATO DEL GARDA",

                                 "LONGHENA",

                                 "LOSINE",

                                 "LOZIO",

                                 "LUMEZZANE",

                                 "MACLODIO",

                                 "MAIRANO",

                                 "MALEGNO",

                                 "MALONNO",

                                 "MANERBA DEL GARDA",

                                 "MANERBIO",

                                 "MARCHENO",

                                 "MARMENTINO",

                                 "MARONE",

                                 "MAZZANO",

                                 "MILZANO",

                                 "MONIGA DEL GARDA",

                                 "MONNO",

                                 "MONTE ISOLA",

                                 "MONTICELLI BRUSATI",

                                 "MONTICHIARI",

                                 "MONTIRONE",

                                 "MURA",

                                 "MUSCOLINE",

                                 "NAVE",

                                 "NIARDO",

                                 "NUVOLENTO",

                                 "NUVOLERA",

                                 "ODOLO",

                                 "OFFLAGA",

                                 "OME",

                                 "ONO SAN PIETRO",

                                 "ORZINUOVI",

                                 "ORZIVECCHI",

                                 "OSPITALETTO",

                                 "OSSIMO",

                                 "PADENGHE SUL GARDA",

                                 "PADERNO FRANCIACORTA",

                                 "PAISCO LOVENO",

                                 "PAITONE",

                                 "PALAZZOLO SULL'OGLIO",

                                 "PARATICO",

                                 "PASPARDO",

                                 "PASSIRANO",

                                 "PAVONE DEL MELLA",

                                 "PERTICA ALTA",

                                 "PERTICA BASSA",

                                 "PEZZAZE",

                                 "PIAN CAMUNO",

                                 "PIANCOGNO",

                                 "PISOGNE",

                                 "POLAVENO",

                                 "POLPENAZZE DEL GARDA",

                                 "POMPIANO",

                                 "PONCARALE",

                                 "PONTE DI LEGNO",

                                 "PONTEVICO",

                                 "PONTOGLIO",

                                 "POZZOLENGO",

                                 "PRALBOINO",

                                 "PRESEGLIE",

                                 "PRESTINE",

                                 "PREVALLE",

                                 "PROVAGLIO D'ISEO",

                                 "PROVAGLIO VAL SABBIA",

                                 "PUEGNAGO SUL GARDA",

                                 "QUINZANO D'OGLIO",

                                 "REMEDELLO",

                                 "REZZATO",

                                 "ROCCAFRANCA",

                                 "RODENGO SAIANO",

                                 "ROE' VOLCIANO",

                                 "RONCADELLE",

                                 "ROVATO",

                                 "RUDIANO",

                                 "SABBIO CHIESE",

                                 "SALE MARASINO",

                                 "SALO'",

                                 "SAN FELICE DEL BENACO",

                                 "SAN GERVASIO BRESCIANO",

                                 "SAN PAOLO",

                                 "SAN ZENO NAVIGLIO",

                                 "SAREZZO",

                                 "SAVIORE DELL'ADAMELLO",

                                 "SELLERO",

                                 "SENIGA",

                                 "SERLE",

                                 "SIRMIONE",

                                 "SOIANO DEL LAGO",

                                 "SONICO",

                                 "SULZANO",

                                 "TAVERNOLE SUL MELLA",

                                 "TEMU'",

                                 "TIGNALE",

                                 "TORBOLE CASAGLIA",

                                 "TOSCOLANO-MADERNO",

                                 "TRAVAGLIATO",

                                 "TREMOSINE",

                                 "TRENZANO",

                                 "TREVISO BRESCIANO",

                                 "URAGO D'OGLIO",

                                 "VALLIO TERME",

                                 "VEROLANUOVA",

                                 "VEROLAVECCHIA",

                                 "VESTONE",

                                 "VEZZA D'OGLIO",

                                 "VILLA CARCINA",

                                 "VILLACHIARA",

                                 "VILLANUOVA SUL CLISI",

                                 "VIONE",

                                 "VISANO",

                                 "VOBARNO",

                                 "ZONE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI BRESCIA')
            elif comune.nome in ["ACQUANEGRA CREMONESE",

                                 "AGNADELLO",

                                 "ANNICCO",

                                 "AZZANELLO",

                                 "BAGNOLO CREMASCO",

                                 "BONEMERSE",

                                 "BORDOLANO",

                                 "CA' D'ANDREA",

                                 "CAMISANO",

                                 "CAMPAGNOLA CREMASCA",

                                 "CAPERGNANICA",

                                 "CAPPELLA CANTONE",

                                 "CAPPELLA DE' PICENARDI",

                                 "CAPRALBA",

                                 "CASALBUTTANO ED UNITI",

                                 "CASALE CREMASCO-VIDOLASCO",

                                 "CASALETTO CEREDANO",

                                 "CASALETTO DI SOPRA",

                                 "CASALETTO VAPRIO",

                                 "CASALMAGGIORE",

                                 "CASALMORANO",

                                 "CASTEL GABBIANO",

                                 "CASTELDIDONE",

                                 "CASTELLEONE",

                                 "CASTELVERDE",

                                 "CASTELVISCONTI",

                                 "CELLA DATI",

                                 "CHIEVE",

                                 "CICOGNOLO",

                                 "CINGIA DE' BOTTI",

                                 "CORTE DE' CORTESI CON CIGNONE",

                                 "CORTE DE' FRATI",

                                 "CREDERA RUBBIANO",

                                 "CREMA",

                                 "CREMONA",

                                 "CREMOSANO",

                                 "CROTTA D'ADDA",

                                 "CUMIGNANO SUL NAVIGLIO",

                                 "DEROVERE",

                                 "DOVERA",

                                 "DRIZZONA",

                                 "FIESCO",

                                 "FORMIGARA",

                                 "GABBIONETA-BINANUOVA",

                                 "GADESCO-PIEVE DELMONA",

                                 "GENIVOLTA",

                                 "GERRE DE' CAPRIOLI",

                                 "GOMBITO",

                                 "GRONTARDO",

                                 "GRUMELLO CREMONESE ED UNITI",

                                 "GUSSOLA",

                                 "ISOLA DOVARESE",

                                 "IZANO",

                                 "MADIGNANO",

                                 "MALAGNINO",

                                 "MARTIGNANA DI PO",

                                 "MONTE CREMASCO",

                                 "MONTODINE",

                                 "MOSCAZZANO",

                                 "MOTTA BALUFFI",

                                 "OFFANENGO",

                                 "OLMENETA",

                                 "OSTIANO",

                                 "PADERNO PONCHIELLI",

                                 "PALAZZO PIGNANO",

                                 "PANDINO",

                                 "PERSICO DOSIMO",

                                 "PESCAROLO ED UNITI",

                                 "PESSINA CREMONESE",

                                 "PIADENA",

                                 "PIANENGO",

                                 "PIERANICA",

                                 "PIEVE D'OLMI",

                                 "PIEVE SAN GIACOMO",

                                 "PIZZIGHETTONE",

                                 "POZZAGLIO ED UNITI",

                                 "QUINTANO",

                                 "RICENGO",

                                 "RIPALTA ARPINA",

                                 "RIPALTA CREMASCA",

                                 "RIPALTA GUERINA",

                                 "RIVAROLO DEL RE ED UNITI",

                                 "RIVOLTA D'ADDA",

                                 "ROBECCO D'OGLIO",

                                 "ROMANENGO",

                                 "SALVIROLA",

                                 "SAN BASSANO",

                                 "SAN DANIELE PO",

                                 "SAN GIOVANNI IN CROCE",

                                 "SAN MARTINO DEL LAGO",

                                 "SCANDOLARA RAVARA",

                                 "SCANDOLARA RIPA D'OGLIO",

                                 "SERGNANO",

                                 "SESTO ED UNITI",

                                 "SOLAROLO RAINERIO",

                                 "SONCINO",

                                 "SORESINA",

                                 "SOSPIRO",

                                 "SPINADESCO",

                                 "SPINO D'ADDA",

                                 "STAGNO LOMBARDO",

                                 "TICENGO",

                                 "TORLINO VIMERCATI",

                                 "TORRE DE' PICENARDI",

                                 "TORRICELLA DEL PIZZO",

                                 "TRESCORE CREMASCO",

                                 "TRIGOLO",

                                 "VAIANO CREMASCO",

                                 "VAILATE",

                                 "VESCOVATO",

                                 "VOLONGO",

                                 "VOLTIDO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CREMONA')
            elif comune.nome in ["ACQUANEGRA SUL CHIESE",

                                 "ASOLA",

                                 "BAGNOLO SAN VITO",

                                 "BIGARELLO",

                                 "BORGOFORTE",

                                 "BORGOFRANCO SUL PO",

                                 "BOZZOLO",

                                 "CALVATONE",

                                 "CANNETO SULL'OGLIO",

                                 "CARBONARA DI PO",

                                 "CASALMORO",

                                 "CASALOLDO",

                                 "CASALROMANO",

                                 "CASTEL D'ARIO",

                                 "CASTEL GOFFREDO",

                                 "CASTELBELFORTE",

                                 "CASTELLUCCHIO",

                                 "CASTIGLIONE DELLE STIVIERE",

                                 "CAVRIANA",

                                 "CERESARA",

                                 "COMMESSAGGIO",

                                 "CURTATONE",

                                 "DOSOLO",

                                 "FELONICA",

                                 "GAZOLDO DEGLI IPPOLITI",

                                 "GAZZUOLO",

                                 "GOITO",

                                 "GONZAGA",

                                 "GUIDIZZOLO",

                                 "MAGNACAVALLO",

                                 "MANTOVA",

                                 "MARCARIA",

                                 "MARIANA MANTOVANA",

                                 "MARMIROLO",

                                 "MEDOLE",

                                 "MOGLIA",

                                 "MONZAMBANO",

                                 "MOTTEGGIANA",

                                 "OSTIGLIA",

                                 "PEGOGNAGA",

                                 "PIEVE DI CORIANO",

                                 "PIUBEGA",

                                 "POGGIO RUSCO",

                                 "POMPONESCO",

                                 "PONTI SUL MINCIO",

                                 "PORTO MANTOVANO",

                                 "QUINGENTOLE",

                                 "QUISTELLO",

                                 "REDONDESCO",

                                 "REVERE",

                                 "RIVAROLO MANTOVANO",

                                 "RODIGO",

                                 "RONCOFERRARO",

                                 "ROVERBELLA",

                                 "SABBIONETA",

                                 "SAN BENEDETTO PO",

                                 "SAN GIACOMO DELLE SEGNATE",

                                 "SAN GIORGIO DI MANTOVA",

                                 "SAN GIOVANNI DEL DOSSO",

                                 "SAN MARTINO DALL'ARGINE",

                                 "SCHIVENOGLIA",

                                 "SERMIDE",

                                 "SERRAVALLE A PO",

                                 "SOLFERINO",

                                 "SPINEDA",

                                 "SUSTINENTE",

                                 "SUZZARA",

                                 "TORNATA",

                                 "VIADANA",

                                 "VILLA POMA",

                                 "VILLIMPENTA",

                                 "VIRGILIO",

                                 "VOLTA MANTOVANA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI MANTOVA')
            elif comune.nome in ["ARBUS",

                                 "ARMUNGIA",

                                 "ASSEMINI",

                                 "BALLAO",

                                 "BARRALI",

                                 "BARUMINI",

                                 "BUGGERRU",

                                 "BURCEI",

                                 "CAGLIARI",

                                 "CALASETTA",

                                 "CAPOTERRA",

                                 "CARBONIA",

                                 "CARLOFORTE",

                                 "CASTIADAS",

                                 "COLLINAS",

                                 "DECIMOMANNU",

                                 "DECIMOPUTZU",

                                 "DOLIANOVA",

                                 "DOMUS DE MARIA",

                                 "DOMUSNOVAS",

                                 "DONORI",

                                 "ELMAS",

                                 "ESCALAPLANO",

                                 "ESCOLCA",

                                 "FLUMINIMAGGIORE",

                                 "FURTEI",

                                 "GENONI",

                                 "GENURI",

                                 "GERGEI",

                                 "GESICO",

                                 "GESTURI",

                                 "GIBA",

                                 "GONI",

                                 "GONNESA",

                                 "GONNOSFANADIGA",

                                 "GUAMAGGIORE",

                                 "GUASILA",

                                 "GUSPINI",

                                 "IGLESIAS",

                                 "ISILI",

                                 "LACONI",

                                 "LAS PLASSAS",

                                 "LUNAMATRONA",

                                 "MANDAS",

                                 "MARACALAGONIS",

                                 "MASAINAS",

                                 "MONASTIR",

                                 "MONSERRATO",

                                 "MURAVERA",

                                 "MUSEI",

                                 "NARCAO",

                                 "NURAGUS",

                                 "NURALLAO",

                                 "NURAMINIS",

                                 "NURRI",

                                 "NUXIS",

                                 "ORROLI",

                                 "ORTACESUS",

                                 "PABILLONIS",

                                 "PAULI ARBAREI",

                                 "PERDAXIUS",

                                 "PIMENTEL",

                                 "PISCINAS",

                                 "PORTOSCUSO",

                                 "PULA",

                                 "QUARTU SANT'ELENA",

                                 "QUARTUCCIU",

                                 "SAMASSI",

                                 "SAMATZAI",

                                 "SAN BASILIO",

                                 "SAN GAVINO MONREALE",

                                 "SAN GIOVANNI SUERGIU",

                                 "SAN NICOLO' GERREI",

                                 "SAN SPERATE",

                                 "SAN VITO",

                                 "SANLURI",

                                 "SANTADI",

                                 "SANT'ANDREA FRIUS",

                                 "SANT'ANNA ARRESI",

                                 "SANT'ANTIOCO",

                                 "SARDARA",

                                 "SARROCH",

                                 "SEGARIU",

                                 "SELARGIUS",

                                 "SELEGAS",

                                 "SENORBI'",

                                 "SERDIANA",

                                 "SERRAMANNA",

                                 "SERRENTI",

                                 "SERRI",

                                 "SESTU",

                                 "SETTIMO SAN PIETRO",

                                 "SETZU",

                                 "SIDDI",

                                 "SILIQUA",

                                 "SILIUS",

                                 "SINNAI",

                                 "SIURGUS DONIGALA",

                                 "SOLEMINIS",

                                 "SUELLI",

                                 "TEULADA",

                                 "TRATALIAS",

                                 "TUILI",

                                 "TURRI",

                                 "USSANA",

                                 "USSARAMANNA",

                                 "UTA",

                                 "VALLERMOSA",

                                 "VILLA SAN PIETRO",

                                 "VILLACIDRO",

                                 "VILLAMAR",

                                 "VILLAMASSARGIA",

                                 "VILLANOVA TULO",

                                 "VILLANOVAFORRU",

                                 "VILLANOVAFRANCA",

                                 "VILLAPERUCCIO",

                                 "VILLAPUTZU",

                                 "VILLASALTO",

                                 "VILLASIMIUS",

                                 "VILLASOR",

                                 "VILLASPECIOSA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CAGLIARI')
            elif comune.nome in ["ARZANA",

                                 "BARI SARDO",

                                 "BAUNEI",

                                 "CARDEDU",

                                 "ELINI",

                                 "ESTERZILI",

                                 "GAIRO",

                                 "GIRASOLE",

                                 "ILBONO",

                                 "JERZU",

                                 "LANUSEI",

                                 "LOCERI",

                                 "LOTZORAI",

                                 "OSINI",

                                 "PERDASDEFOGU",

                                 "SADALI",

                                 "SEUI",

                                 "SEULO",

                                 "TALANA",

                                 "TERTENIA",

                                 "TORTOLI'",

                                 "TRIEI",

                                 "ULASSAI",

                                 "URZULEI",

                                 "USSASSAI",

                                 "VILLAGRANDE STRISAILI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI LANUSEI')
            elif comune.nome in ["ABBASANTA",

                                 "AIDOMAGGIORE",

                                 "ALBAGIARA",

                                 "ALES",

                                 "ALLAI",

                                 "ARBOREA",

                                 "ARDAULI",

                                 "ARITZO",

                                 "ASSOLO",

                                 "ASUNI",

                                 "ATZARA",

                                 "AUSTIS",

                                 "BARADILI",

                                 "BARATILI SAN PIETRO",

                                 "BARESSA",

                                 "BAULADU",

                                 "BELVI'",

                                 "BIDONI'",

                                 "BIRORI",

                                 "BOLOTANA",

                                 "BONARCADO",

                                 "BORONEDDU",

                                 "BORORE",

                                 "BORTIGALI",

                                 "BOSA",

                                 "BUSACHI",

                                 "CABRAS",

                                 "CUGLIERI",

                                 "CURCURIS",

                                 "DESULO",

                                 "DUALCHI",

                                 "FLUSSIO",

                                 "FORDONGIANUS",

                                 "GADONI",

                                 "GHILARZA",

                                 "GONNOSCODINA",

                                 "GONNOSNO'",

                                 "GONNOSTRAMATZA",

                                 "LEI",

                                 "MACOMER",

                                 "MAGOMADAS",

                                 "MARRUBIU",

                                 "MASULLAS",

                                 "MEANA SARDO",

                                 "MILIS",

                                 "MODOLO",

                                 "MOGORELLA",

                                 "MOGORO",

                                 "MONTRESTA",

                                 "MORGONGIORI",

                                 "NARBOLIA",

                                 "NEONELI",

                                 "NORAGUGUME",

                                 "NORBELLO",

                                 "NUGHEDU SANTA VITTORIA",

                                 "NURACHI",

                                 "NURECI",

                                 "OLLASTRA",

                                 "ORISTANO",

                                 "ORTUERI",

                                 "PALMAS ARBOREA",

                                 "PAU",

                                 "PAULILATINO",

                                 "POMPU",

                                 "RIOLA SARDO",

                                 "RUINAS",

                                 "SAGAMA",

                                 "SAMUGHEO",

                                 "SAN NICOLO' D'ARCIDANO",

                                 "SAN VERO MILIS",

                                 "SANTA GIUSTA",

                                 "SANTU LUSSURGIU",

                                 "SCANO DI MONTIFERRO",

                                 "SEDILO",

                                 "SENEGHE",

                                 "SENIS",

                                 "SENNARIOLO",

                                 "SIAMAGGIORE",

                                 "SIAMANNA",

                                 "SIAPICCIA",

                                 "SILANUS",

                                 "SIMALA",

                                 "SIMAXIS",

                                 "SINDIA",

                                 "SINI",

                                 "SIRIS",

                                 "SODDI'",

                                 "SOLARUSSA",

                                 "SORGONO",

                                 "SORRADILE",

                                 "SUNI",

                                 "TADASUNI",

                                 "TERRALBA",

                                 "TETI",

                                 "TIANA",

                                 "TINNURA",

                                 "TONARA",

                                 "TRAMATZA",

                                 "TRESNURAGHES",

                                 "ULA' TIRSO",

                                 "URAS",

                                 "USELLUS",

                                 "VILLA SANT'ANTONIO",

                                 "VILLA VERDE",

                                 "VILLANOVA TRUSCHEDU",

                                 "VILLAURBANA",

                                 "ZEDDIANI",

                                 "ZERFALIU"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI ORISTANO')
            elif comune.nome in ["ACQUAVIVA PLATANI",

                                 "BOMPENSIERE",

                                 "CALTANISSETTA",

                                 "CAMPOFRANCO",

                                 "DELIA",

                                 "MARIANOPOLI",

                                 "MILENA",

                                 "MONTEDORO",

                                 "MUSSOMELI",

                                 "RESUTTANO",

                                 "RIESI",

                                 "SAN CATALDO",

                                 "SANTA CATERINA VILLARMOSA",

                                 "SERRADIFALCO",

                                 "SOMMATINO",

                                 "SUTERA",

                                 "VALLELUNGA PRATAMENO",

                                 "VILLALBA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CALTANISSETTA')
            elif comune.nome in ["AGIRA",

                                 "AIDONE",

                                 "ASSORO",

                                 "BARRAFRANCA",

                                 "CALASCIBETTA",

                                 "CAPIZZI",

                                 "CATENANUOVA",

                                 "CENTURIPE",

                                 "CERAMI",

                                 "ENNA",

                                 "GAGLIANO CASTELFERRATO",

                                 "LEONFORTE",

                                 "NICOSIA",

                                 "NISSORIA",

                                 "PIAZZA ARMERINA",

                                 "PIETRAPERZIA",

                                 "REGALBUTO",

                                 "SPERLINGA",

                                 "TROINA",

                                 "VALGUARNERA CAROPEPE",

                                 "VILLAROSA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI ENNA')
            elif comune.nome in ["BUTERA",

                                 "GELA",

                                 "MAZZARINO",

                                 "NISCEMI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI GELA')
            elif comune.nome in ["BARANELLO",

                                 "BOJANO",

                                 "BUSSO",

                                 "CAMPOBASSO",

                                 "CAMPOCHIARO",

                                 "CAMPODIPIETRA",

                                 "CAMPOLIETO",

                                 "CASALCIPRANO",

                                 "CASTELBOTTACCIO",

                                 "CASTELLINO DEL BIFERNO",

                                 "CASTELMAURO",

                                 "CASTROPIGNANO",

                                 "CERCEMAGGIORE",

                                 "CERCEPICCOLA",

                                 "CIVITACAMPOMARANO",

                                 "COLLE D'ANCHISE",

                                 "FERRAZZANO",

                                 "FOSSALTO",

                                 "GAMBATESA",

                                 "GILDONE",

                                 "GUARDIAREGIA",

                                 "JELSI",

                                 "LIMOSANO",

                                 "LUCITO",

                                 "LUPARA",

                                 "MATRICE",

                                 "MIRABELLO SANNITICO",

                                 "MOLISE",

                                 "MONACILIONI",

                                 "MONTAGANO",

                                 "MONTEFALCONE NEL SANNIO",

                                 "MONTEMITRO",

                                 "ORATINO",

                                 "PETRELLA TIFERNINA",

                                 "PIETRACUPA",

                                 "RICCIA",

                                 "RIPALIMOSANI",

                                 "ROCCAVIVARA",

                                 "SALCITO",

                                 "SAN BIASE",

                                 "SAN FELICE DEL MOLISE",

                                 "SAN GIOVANNI IN GALDO",

                                 "SAN GIULIANO DEL SANNIO",

                                 "SAN MASSIMO",

                                 "SAN POLO MATESE",

                                 "SANT'ANGELO LIMOSANO",

                                 "SEPINO",

                                 "SPINETE",

                                 "TORELLA DEL SANNIO",

                                 "TORO",

                                 "TRIVENTO",

                                 "TUFARA",

                                 "VINCHIATURO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CAMPOBASSO')
            elif comune.nome in ["ACQUAVIVA D'ISERNIA",

                                 "AGNONE",

                                 "BAGNOLI DEL TRIGNO",

                                 "BELMONTE DEL SANNIO",

                                 "CANTALUPO NEL SANNIO",

                                 "CAPRACOTTA",

                                 "CAROVILLI",

                                 "CARPINONE",

                                 "CASTEL DEL GIUDICE",

                                 "CASTEL SAN VINCENZO",

                                 "CASTELPETROSO",

                                 "CASTELPIZZUTO",

                                 "CASTELVERRINO",

                                 "CERRO AL VOLTURNO",

                                 "CHIAUCI",

                                 "CIVITANOVA DEL SANNIO",

                                 "COLLI A VOLTURNO",

                                 "CONCA CASALE",

                                 "DURONIA",

                                 "FILIGNANO",

                                 "FORLI' DEL SANNIO",

                                 "FORNELLI",

                                 "FROSOLONE",

                                 "ISERNIA",

                                 "LONGANO",

                                 "MACCHIA D'ISERNIA",

                                 "MACCHIAGODENA",

                                 "MIRANDA",

                                 "MONTAQUILA",

                                 "MONTENERO VAL COCCHIARA",

                                 "MONTERODUNI",

                                 "PESCHE",

                                 "PESCOLANCIANO",

                                 "PESCOPENNATARO",

                                 "PETTORANELLO DEL MOLISE",

                                 "PIETRABBONDANTE",

                                 "PIZZONE",

                                 "POGGIO SANNITA",

                                 "POZZILLI",

                                 "RIONERO SANNITICO",

                                 "ROCCAMANDOLFI",

                                 "ROCCASICURA",

                                 "ROCCHETTA A VOLTURNO",

                                 "SAN PIETRO AVELLANA",

                                 "SANTA MARIA DEL MOLISE",

                                 "SANT'AGAPITO",

                                 "SANT'ANGELO DEL PESCO",

                                 "SANT'ELENA SANNITA",

                                 "SCAPOLI",

                                 "SESSANO DEL MOLISE",

                                 "SESTO CAMPANO",

                                 "VASTOGIRARDI",

                                 "VENAFRO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI ISERNIA')
            elif comune.nome in ["ACQUAVIVA COLLECROCE",

                                 "BONEFRO",

                                 "CAMPOMARINO",

                                 "CASACALENDA",

                                 "COLLETORTO",

                                 "GUARDIALFIERA",

                                 "GUGLIONESI",

                                 "LARINO",

                                 "MACCHIA VALFORTORE",

                                 "MAFALDA",

                                 "MONTECILFONE",

                                 "MONTELONGO",

                                 "MONTENERO DI BISACCIA",

                                 "MONTORIO NEI FRENTANI",

                                 "MORRONE DEL SANNIO",

                                 "PALATA",

                                 "PETACCIATO",

                                 "PIETRACATELLA",

                                 "PORTOCANNONE",

                                 "PROVVIDENTI",

                                 "RIPABOTTONI",

                                 "ROTELLO",

                                 "SAN GIACOMO DEGLI SCHIAVONI",

                                 "SAN GIULIANO DI PUGLIA",

                                 "SAN MARTINO IN PENSILIS",

                                 "SANTA CROCE DI MAGLIANO",

                                 "SANT'ELIA A PIANISI",

                                 "TAVENNA",

                                 "TERMOLI",

                                 "URURI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI LARINO')
            elif comune.nome in ["CALTAGIRONE",

                                 "CASTEL DI IUDICA",

                                 "GRAMMICHELE",

                                 "LICODIA EUBEA",

                                 "MAZZARRONE",

                                 "MILITELLO IN VAL DI CATANIA",

                                 "MINEO",

                                 "MIRABELLA IMBACCARI",

                                 "PALAGONIA",

                                 "RADDUSA",

                                 "RAMACCA",

                                 "SAN CONO",

                                 "SAN MICHELE DI GANZARIA",

                                 "SCORDIA",

                                 "VIZZINI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CALTAGIRONE')
            elif comune.nome in ["ACI BONACCORSI",

                                 "ACI CASTELLO",

                                 "ACI CATENA",

                                 "ACI SANT'ANTONIO",

                                 "ACIREALE",

                                 "ADRANO",

                                 "BELPASSO",

                                 "BIANCAVILLA",

                                 "BRONTE",

                                 "CALATABIANO",

                                 "CAMPOROTONDO ETNEO",

                                 "CASTIGLIONE DI SICILIA",

                                 "CATANIA",

                                 "CESARO'",

                                 "FIUMEFREDDO DI SICILIA",

                                 "GIARRE",

                                 "GRAVINA DI CATANIA",

                                 "LINGUAGLOSSA",

                                 "MALETTO",

                                 "MANIACE",

                                 "MASCALI",

                                 "MASCALUCIA",

                                 "MILO",

                                 "MISTERBIANCO",

                                 "MOTTA SANT'ANASTASIA",

                                 "NICOLOSI",

                                 "PATERNO'",

                                 "PEDARA",

                                 "PIEDIMONTE ETNEO",

                                 "RAGALNA",

                                 "RANDAZZO",

                                 "RIPOSTO",

                                 "SAN GIOVANNI LA PUNTA",

                                 "SAN GREGORIO DI CATANIA",

                                 "SAN PIETRO CLARENZA",

                                 "SAN TEODORO",

                                 "SANTA MARIA DI LICODIA",

                                 "SANTA VENERINA",

                                 "SANT'AGATA LI BATTIATI",

                                 "SANT'ALFIO",

                                 "TRECASTAGNI",

                                 "TREMESTIERI ETNEO",

                                 "VALVERDE",

                                 "VIAGRANDE",

                                 "ZAFFERANA ETNEA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CATANIA')
            elif comune.nome in ["ACATE",

                                 "CHIARAMONTE GULFI",

                                 "COMISO",

                                 "GIARRATANA",

                                 "ISPICA",

                                 "MODICA",

                                 "MONTEROSSO ALMO",

                                 "POZZALLO",

                                 "RAGUSA",

                                 "SANTA CROCE CAMERINA",

                                 "SCICLI",

                                 "VITTORIA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI RAGUSA')
            elif comune.nome in ["AUGUSTA",

                                 "AVOLA",

                                 "BUCCHERI",

                                 "BUSCEMI",

                                 "CANICATTINI BAGNI",

                                 "CARLENTINI",

                                 "CASSARO",

                                 "FERLA",

                                 "FLORIDIA",

                                 "FRANCOFONTE",

                                 "LENTINI",

                                 "MELILLI",

                                 "NOTO",

                                 "PACHINO",

                                 "PALAZZOLO ACREIDE",

                                 "PORTOPALO DI CAPO PASSERO",

                                 "PRIOLO GARGALLO",

                                 "ROSOLINI",

                                 "SIRACUSA",

                                 "SOLARINO",

                                 "SORTINO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI SIRACUSA')
            elif comune.nome in ["ACQUAFORMOSA",

                                 "ALBIDONA",

                                 "ALESSANDRIA DEL CARRETTO",

                                 "ALTOMONTE",

                                 "AMENDOLARA",

                                 "BOCCHIGLIERO",

                                 "CALOPEZZATI",

                                 "CALOVETO",

                                 "CAMPANA",

                                 "CANNA",

                                 "CARIATI",

                                 "CASSANO ALL'IONIO",

                                 "CASTROREGIO",

                                 "CASTROVILLARI",

                                 "CERCHIARA DI CALABRIA",

                                 "CIVITA",

                                 "CORIGLIANO CALABRO",

                                 "CROPALATI",

                                 "CROSIA",

                                 "FIRMO",

                                 "FRANCAVILLA MARITTIMA",

                                 "FRASCINETO",

                                 "LAINO BORGO",

                                 "LAINO CASTELLO",

                                 "LONGOBUCCO",

                                 "LUNGRO",

                                 "MANDATORICCIO",

                                 "MONTEGIORDANO",

                                 "MORANO CALABRO",

                                 "MORMANNO",

                                 "MOTTAFOLLONE",

                                 "NOCARA",

                                 "ORIOLO",

                                 "PALUDI",

                                 "PAPASIDERO",

                                 "PIETRAPAOLA",

                                 "PLATACI",

                                 "ROCCA IMPERIALE",

                                 "ROSETO CAPO SPULICO",

                                 "ROSSANO",

                                 "SAN BASILE",

                                 "SAN COSMO ALBANESE",

                                 "SAN DEMETRIO CORONE",

                                 "SAN DONATO DI NINEA",

                                 "SAN GIORGIO ALBANESE",

                                 "SAN LORENZO BELLIZZI",

                                 "SAN LORENZO DEL VALLO",

                                 "SAN SOSTI",

                                 "SANTA SOFIA D'EPIRO",

                                 "SANT'AGATA DI ESARO",

                                 "SARACENA",

                                 "SCALA COELI",

                                 "SPEZZANO ALBANESE",

                                 "TARSIA",

                                 "TERRANOVA DA SIBARI",

                                 "TERRAVECCHIA",

                                 "TREBISACCE",

                                 "VACCARIZZO ALBANESE",

                                 "VILLAPIANA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CASTROVILLARI')
            elif comune.nome in ["ALBI",

                                 "AMARONI",

                                 "AMATO",

                                 "ANDALI",

                                 "ARGUSTO",

                                 "BADOLATO",

                                 "BELCASTRO",

                                 "BORGIA",

                                 "BOTRICELLO",

                                 "CARAFFA DI CATANZARO",

                                 "CARDINALE",

                                 "CATANZARO",

                                 "CENADI",

                                 "CENTRACHE",

                                 "CERVA",

                                 "CHIARAVALLE CENTRALE",

                                 "CROPANI",

                                 "DAVOLI",

                                 "FOSSATO SERRALTA",

                                 "GAGLIATO",

                                 "GASPERINA",

                                 "GIMIGLIANO",

                                 "GIRIFALCO",

                                 "GUARDAVALLE",

                                 "ISCA SULLO IONIO",

                                 "MAGISANO",

                                 "MARCEDUSA",

                                 "MARCELLINARA",

                                 "MIGLIERINA",

                                 "MONTAURO",

                                 "MONTEPAONE",

                                 "OLIVADI",

                                 "PALERMITI",

                                 "PENTONE",

                                 "PETRIZZI",

                                 "SAN FLORO",

                                 "SAN PIETRO APOSTOLO",

                                 "SAN SOSTENE",

                                 "SAN VITO SULLO IONIO",

                                 "SANTA CATERINA DELLO IONIO",

                                 "SANT'ANDREA APOSTOLO DELLO IONIO",

                                 "SATRIANO",

                                 "SELLIA",

                                 "SELLIA MARINA",

                                 "SERSALE",

                                 "SETTINGIANO",

                                 "SIMERI CRICHI",

                                 "SORBO SAN BASILE",

                                 "SOVERATO",

                                 "SOVERIA SIMERI",

                                 "SQUILLACE",

                                 "STALETTI'",

                                 "TAVERNA",

                                 "TIRIOLO",

                                 "TORRE DI RUGGIERO",

                                 "VALLEFIORITA",

                                 "ZAGARISE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CATANZARO')
            elif comune.nome in ["ACRI",

                                 "ALTILIA",

                                 "APRIGLIANO",

                                 "BELSITO",

                                 "BIANCHI",

                                 "BISIGNANO",

                                 "CAROLEI",

                                 "CARPANZANO",

                                 "CASOLE BRUZIO",

                                 "CASTIGLIONE COSENTINO",

                                 "CASTROLIBERO",

                                 "CELICO",

                                 "CELLARA",

                                 "CERISANO",

                                 "CERVICATI",

                                 "CERZETO",

                                 "COLOSIMI",

                                 "COSENZA",

                                 "DIPIGNANO",

                                 "DOMANICO",

                                 "FAGNANO CASTELLO",

                                 "FIGLINE VEGLIATURO",

                                 "GRIMALDI",

                                 "LAPPANO",

                                 "LATTARICO",

                                 "LUZZI",

                                 "MALITO",

                                 "MALVITO",

                                 "MANGONE",

                                 "MARANO MARCHESATO",

                                 "MARANO PRINCIPATO",

                                 "MARZI",

                                 "MENDICINO",

                                 "MONGRASSANO",

                                 "MONTALTO UFFUGO",

                                 "PANETTIERI",

                                 "PARENTI",

                                 "PATERNO CALABRO",

                                 "PEDACE",

                                 "PEDIVIGLIANO",

                                 "PIANE CRATI",

                                 "PIETRAFITTA",

                                 "RENDE",

                                 "ROGGIANO GRAVINA",

                                 "ROGLIANO",

                                 "ROSE",

                                 "ROTA GRECA",

                                 "ROVITO",

                                 "SAN BENEDETTO ULLANO",

                                 "SAN FILI",

                                 "SAN GIOVANNI IN FIORE",

                                 "SAN MARCO ARGENTANO",

                                 "SAN MARTINO DI FINITA",

                                 "SAN PIETRO IN GUARANO",

                                 "SAN VINCENZO LA COSTA",

                                 "SANTA CATERINA ALBANESE",

                                 "SANTO STEFANO DI ROGLIANO",

                                 "SCIGLIANO",

                                 "SERRA PEDACE",

                                 "SPEZZANO DELLA SILA",

                                 "SPEZZANO PICCOLO",

                                 "TORANO CASTELLO",

                                 "TRENTA",

                                 "ZUMPANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI COSENZA')
            elif comune.nome in ["BELVEDERE DI SPINELLO",

                                 "CACCURI",

                                 "CARFIZZI",

                                 "CASABONA",

                                 "CASTELSILANO",

                                 "CERENZIA",

                                 "CIRO'",

                                 "CIRO' MARINA",

                                 "COTRONEI",

                                 "CROTONE",

                                 "CRUCOLI",

                                 "CUTRO",

                                 "ISOLA DI CAPO RIZZUTO",

                                 "MELISSA",

                                 "MESORACA",

                                 "PALLAGORIO",

                                 "PETILIA POLICASTRO",

                                 "PETRONA'",

                                 "ROCCA DI NETO",

                                 "ROCCABERNARDA",

                                 "SAN MAURO MARCHESATO",

                                 "SAN NICOLA DELL'ALTO",

                                 "SANTA SEVERINA",

                                 "SAVELLI",

                                 "SCANDALE",

                                 "STRONGOLI",

                                 "UMBRIATICO",

                                 "VERZINO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CROTONE')
            elif comune.nome in ["CARLOPOLI",

                                 "CICALA",

                                 "CONFLENTI",

                                 "CORTALE",

                                 "CURINGA",

                                 "DECOLLATURA",

                                 "FALERNA",

                                 "FEROLETO ANTICO",

                                 "FILADELFIA",

                                 "FRANCAVILLA ANGITOLA",

                                 "GIZZERIA",

                                 "JACURSO",

                                 "LAMEZIA TERME",

                                 "MAIDA",

                                 "MARTIRANO",

                                 "MARTIRANO LOMBARDO",

                                 "MOTTA SANTA LUCIA",

                                 "NOCERA TERINESE",

                                 "PIANOPOLI",

                                 "PLATANIA",

                                 "POLIA",

                                 "SAN MANGO D'AQUINO",

                                 "SAN PIETRO A MAIDA",

                                 "SERRASTRETTA",

                                 "SOVERIA MANNELLI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI LAMEZIA TERME')
            elif comune.nome in ["ACQUAPPESA",

                                 "AIELLO CALABRO",

                                 "AIETA",

                                 "AMANTEA",

                                 "BELMONTE CALABRO",

                                 "BELVEDERE MARITTIMO",

                                 "BONIFATI",

                                 "BUONVICINO",

                                 "CETRARO",

                                 "CLETO",

                                 "DIAMANTE",

                                 "FALCONARA ALBANESE",

                                 "FIUMEFREDDO BRUZIO",

                                 "FUSCALDO",

                                 "GRISOLIA",

                                 "GUARDIA PIEMONTESE",

                                 "LAGO",

                                 "LONGOBARDI",

                                 "MAIERA'",

                                 "ORSOMARSO",

                                 "PAOLA",

                                 "PRAIA A MARE",

                                 "SAN LUCIDO",

                                 "SAN NICOLA ARCELLA",

                                 "SAN PIETRO IN AMANTEA",

                                 "SANGINETO",

                                 "SANTA DOMENICA TALAO",

                                 "SANTA MARIA DEL CEDRO",

                                 "SCALEA",

                                 "SERRA D'AIELLO",

                                 "TORTORA",

                                 "VERBICARO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PAOLA')
            elif comune.nome in ["ACQUARO",

                                 "ARENA",

                                 "BRIATICO",

                                 "BROGNATURO",

                                 "CAPISTRANO",

                                 "CESSANITI",

                                 "DASA'",

                                 "DINAMI",

                                 "DRAPIA",

                                 "FABRIZIA",

                                 "FILANDARI",

                                 "FILOGASO",

                                 "FRANCICA",

                                 "GEROCARNE",

                                 "IONADI",

                                 "JOPPOLO",

                                 "LIMBADI",

                                 "MAIERATO",

                                 "MILETO",

                                 "MONGIANA",

                                 "MONTEROSSO CALABRO",

                                 "NARDODIPACE",

                                 "NICOTERA",

                                 "PARGHELIA",

                                 "PIZZO",

                                 "PIZZONI",

                                 "RICADI",

                                 "ROMBIOLO",

                                 "SAN CALOGERO",

                                 "SAN COSTANTINO CALABRO",

                                 "SAN GREGORIO D'IPPONA",

                                 "SAN NICOLA DA CRISSA",

                                 "SANT'ONOFRIO",

                                 "SERRA SAN BRUNO",

                                 "SIMBARIO",

                                 "SORIANELLO",

                                 "SORIANO CALABRO",

                                 "SPADOLA",

                                 "SPILINGA",

                                 "STEFANACONI",

                                 "TROPEA",

                                 "VALLELONGA",

                                 "VAZZANO",

                                 "VIBO VALENTIA",

                                 "ZACCANOPOLI",

                                 "ZAMBRONE",

                                 "ZUNGRI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI VIBO VALENTIA')
            elif comune.nome in ["ANGHIARI",

                                 "AREZZO",

                                 "BADIA TEDALDA",

                                 "BIBBIENA",

                                 "BUCINE",

                                 "CAPOLONA",

                                 "CAPRESE MICHELANGELO",

                                 "CASTEL FOCOGNANO",

                                 "CASTEL SAN NICCOLO'",

                                 "CASTELFRANCO DI SOPRA",

                                 "CASTIGLION FIBOCCHI",

                                 "CASTIGLION FIORENTINO",

                                 "CAVRIGLIA",

                                 "CHITIGNANO",

                                 "CHIUSI DELLA VERNA",

                                 "CIVITELLA IN VAL DI CHIANA",

                                 "CORTONA",

                                 "FOIANO DELLA CHIANA",

                                 "LATERINA",

                                 "LORO CIUFFENNA",

                                 "LUCIGNANO",

                                 "MARCIANO DELLA CHIANA",

                                 "MONTE SAN SAVINO",

                                 "MONTEMIGNAIO",

                                 "MONTERCHI",

                                 "MONTEVARCHI",

                                 "ORTIGNANO RAGGIOLO",

                                 "PERGINE VALDARNO",

                                 "PIAN DI SCO",

                                 "PIEVE SANTO STEFANO",

                                 "POPPI",

                                 "PRATOVECCHIO",

                                 "SAN GIOVANNI VALDARNO",

                                 "SANSEPOLCRO",

                                 "SESTINO",

                                 "STIA",

                                 "SUBBIANO",

                                 "TALLA",

                                 "TERRANUOVA BRACCIOLINI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI AREZZO')
            elif comune.nome in ["BAGNO A RIPOLI",

                                 "BARBERINO DI MUGELLO",

                                 "BARBERINO VAL D'ELSA",

                                 "BORGO SAN LORENZO",

                                 "CAMPI BISENZIO",

                                 "CAPRAIA E LIMITE",

                                 "CASTELFIORENTINO",

                                 "CERRETO GUIDI",

                                 "CERTALDO",

                                 "DICOMANO",

                                 "EMPOLI",

                                 "FIESOLE",

                                 "FIGLINE VALDARNO",

                                 "FIRENZE",

                                 "FIRENZUOLA",

                                 "FUCECCHIO",

                                 "GAMBASSI TERME",

                                 "GREVE IN CHIANTI",

                                 "IMPRUNETA",

                                 "INCISA IN VAL D'ARNO",

                                 "LASTRA A SIGNA",

                                 "LONDA",

                                 "MARRADI",

                                 "MONTAIONE",

                                 "MONTELUPO FIORENTINO",

                                 "MONTESPERTOLI",

                                 "PALAZZUOLO SUL SENIO",

                                 "PELAGO",

                                 "PONTASSIEVE",

                                 "REGGELLO",

                                 "RIGNANO SULL'ARNO",

                                 "RUFINA",

                                 "SAN CASCIANO IN VAL DI PESA",

                                 "SAN GODENZO",

                                 "SAN PIERO A SIEVE",

                                 "SCANDICCI",

                                 "SCARPERIA",

                                 "SESTO FIORENTINO",

                                 "SIGNA",

                                 "TAVARNELLE VAL DI PESA",

                                 "VAGLIA",

                                 "VICCHIO",

                                 "VINCI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI FIRENZE')
            elif comune.nome in ["ARCIDOSSO",

                                 "CAMPAGNATICO",

                                 "CAPALBIO",

                                 "CASTEL DEL PIANO",

                                 "CASTELL'AZZARA",

                                 "CASTIGLIONE DELLA PESCAIA",

                                 "CINIGIANO",

                                 "CIVITELLA PAGANICO",

                                 "FOLLONICA",

                                 "GAVORRANO",

                                 "GROSSETO",

                                 "ISOLA DEL GIGLIO",

                                 "MAGLIANO IN TOSCANA",

                                 "MANCIANO",

                                 "MASSA MARITTIMA",

                                 "MONTE ARGENTARIO",

                                 "MONTEROTONDO MARITTIMO",

                                 "MONTIERI",

                                 "ORBETELLO",

                                 "PITIGLIANO",

                                 "ROCCALBEGNA",

                                 "ROCCASTRADA",

                                 "SANTA FIORA",

                                 "SCANSANO",

                                 "SCARLINO",

                                 "SEGGIANO",

                                 "SEMPRONIANO",

                                 "SORANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI GROSSETO')
            elif comune.nome in ["BIBBONA",

                                 "CAMPIGLIA MARITTIMA",

                                 "CAMPO NELL'ELBA",

                                 "CAPOLIVERI",

                                 "CAPRAIA ISOLA",

                                 "CASALE MARITTIMO",

                                 "CASTAGNETO CARDUCCI",

                                 "CASTELLINA MARITTIMA",

                                 "CECINA",

                                 "COLLESALVETTI",

                                 "GUARDISTALLO",

                                 "LIVORNO",

                                 "MARCIANA",

                                 "MARCIANA MARINA",

                                 "MONTESCUDAIO",

                                 "MONTEVERDI MARITTIMO",

                                 "PIOMBINO",

                                 "PORTO AZZURRO",

                                 "PORTOFERRAIO",

                                 "RIO MARINA",

                                 "RIO NELL'ELBA",

                                 "RIPARBELLA",

                                 "ROSIGNANO MARITTIMO",

                                 "SAN VINCENZO",

                                 "SASSETTA",

                                 "SUVERETO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI LIVORNO')
            elif comune.nome in ["ALTOPASCIO",

                                 "BAGNI DI LUCCA",

                                 "BARGA",

                                 "BORGO A MOZZANO",

                                 "CAMAIORE",

                                 "CAMPORGIANO",

                                 "CAPANNORI",

                                 "CAREGGINE",

                                 "CASTELNUOVO DI GARFAGNANA",

                                 "CASTIGLIONE DI GARFAGNANA",

                                 "COREGLIA ANTELMINELLI",

                                 "FABBRICHE DI VALLICO",

                                 "FORTE DEI MARMI",

                                 "FOSCIANDORA",

                                 "GALLICANO",

                                 "GIUNCUGNANO",

                                 "LUCCA",

                                 "MASSAROSA",

                                 "MINUCCIANO",

                                 "MOLAZZANA",

                                 "MONTECARLO",

                                 "PESCAGLIA",

                                 "PIAZZA AL SERCHIO",

                                 "PIETRASANTA",

                                 "PIEVE FOSCIANA",

                                 "PORCARI",

                                 "SAN ROMANO IN GARFAGNANA",

                                 "SERAVEZZA",

                                 "SILLANO",

                                 "STAZZEMA",

                                 "VAGLI SOTTO",

                                 "VERGEMOLI",

                                 "VIAREGGIO",

                                 "VILLA BASILICA",

                                 "VILLA COLLEMANDINA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI LUCCA')
            elif comune.nome in ["BIENTINA",

                                 "BUTI",

                                 "CALCI",

                                 "CALCINAIA",

                                 "CAPANNOLI",

                                 "CASCIANA TERME",

                                 "CASCINA",

                                 "CASTELFRANCO DI SOTTO",

                                 "CASTELNUOVO DI VAL DI CECINA",

                                 "CHIANNI",

                                 "CRESPINA",

                                 "FAUGLIA",

                                 "LAJATICO",

                                 "LARI",

                                 "LORENZANA",

                                 "MONTECATINI VAL DI CECINA",

                                 "MONTOPOLI IN VAL D'ARNO",

                                 "ORCIANO PISANO",

                                 "PALAIA",

                                 "PECCIOLI",

                                 "PISA",

                                 "POMARANCE",

                                 "PONSACCO",

                                 "PONTEDERA",

                                 "SAN GIULIANO TERME",

                                 "SAN MINIATO",

                                 "SANTA CROCE SULL'ARNO",

                                 "SANTA LUCE",

                                 "SANTA MARIA A MONTE",

                                 "TERRICCIOLA",

                                 "VECCHIANO",

                                 "VICOPISANO",

                                 "VOLTERRA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PISA')
            elif comune.nome in ["ABETONE",

                                 "AGLIANA",

                                 "BUGGIANO",

                                 "CHIESINA UZZANESE",

                                 "CUTIGLIANO",

                                 "LAMPORECCHIO",

                                 "LARCIANO",

                                 "MARLIANA",

                                 "MASSA E COZZILE",

                                 "MONSUMMANO TERME",

                                 "MONTALE",

                                 "MONTECATINI-TERME",

                                 "PESCIA",

                                 "PIEVE A NIEVOLE",

                                 "PISTOIA",

                                 "PITEGLIO",

                                 "PONTE BUGGIANESE",

                                 "QUARRATA",

                                 "SAMBUCA PISTOIESE",

                                 "SAN MARCELLO PISTOIESE",

                                 "SERRAVALLE PISTOIESE",

                                 "UZZANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PISTOIA')
            elif comune.nome in ["CALENZANO",

                                 "CANTAGALLO",

                                 "CARMIGNANO",

                                 "MONTEMURLO",

                                 "POGGIO A CAIANO",

                                 "PRATO",

                                 "VAIANO",

                                 "VERNIO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PRATO')
            elif comune.nome in ["ABBADIA SAN SALVATORE",

                                 "ASCIANO",

                                 "BUONCONVENTO",

                                 "CASOLE D'ELSA",

                                 "CASTELLINA IN CHIANTI",

                                 "CASTELNUOVO BERARDENGA",

                                 "CASTIGLIONE D'ORCIA",

                                 "CETONA",

                                 "CHIANCIANO TERME",

                                 "CHIUSDINO",

                                 "CHIUSI",

                                 "COLLE DI VAL D'ELSA",

                                 "GAIOLE IN CHIANTI",

                                 "MONTALCINO",

                                 "MONTEPULCIANO",

                                 "MONTERIGGIONI",

                                 "MONTERONI D'ARBIA",

                                 "MONTICIANO",

                                 "MURLO",

                                 "PIANCASTAGNAIO",

                                 "PIENZA",

                                 "POGGIBONSI",

                                 "RADDA IN CHIANTI",

                                 "RADICOFANI",

                                 "RADICONDOLI",

                                 "RAPOLANO TERME",

                                 "SAN CASCIANO DEI BAGNI",

                                 "SAN GIMIGNANO",

                                 "SAN GIOVANNI D'ASSO",

                                 "SAN QUIRICO D'ORCIA",

                                 "SARTEANO",

                                 "SIENA",

                                 "SINALUNGA",

                                 "SOVICILLE",

                                 "TORRITA DI SIENA",

                                 "TREQUANDA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI SIENA')
            elif comune.nome in ["ARENZANO",

                                 "AVEGNO",

                                 "BARGAGLI",

                                 "BOGLIASCO",

                                 "BORZONASCA",

                                 "BUSALLA",

                                 "CAMOGLI",

                                 "CAMPO LIGURE",

                                 "CAMPOMORONE",

                                 "CARASCO",

                                 "CARRO",

                                 "CASARZA LIGURE",

                                 "CASELLA",

                                 "CASTIGLIONE CHIAVARESE",

                                 "CERANESI",

                                 "CHIAVARI",

                                 "CICAGNA",

                                 "COGOLETO",

                                 "COGORNO",

                                 "COREGLIA LIGURE",

                                 "CROCEFIESCHI",

                                 "DAVAGNA",

                                 "FASCIA",

                                 "FAVALE DI MALVARO",

                                 "FONTANIGORDA",

                                 "GENOVA",

                                 "GORRETO",

                                 "ISOLA DEL CANTONE",

                                 "LAVAGNA",

                                 "LEIVI",

                                 "LORSICA",

                                 "LUMARZO",

                                 "MAISSANA",

                                 "MASONE",

                                 "MELE",

                                 "MEZZANEGO",

                                 "MIGNANEGO",

                                 "MOCONESI",

                                 "MONEGLIA",

                                 "MONTEBRUNO",

                                 "MONTOGGIO",

                                 "NE",

                                 "NEIRONE",

                                 "ORERO",

                                 "PIEVE LIGURE",

                                 "PORTOFINO",

                                 "PROPATA",

                                 "RAPALLO",

                                 "RECCO",

                                 "REZZOAGLIO",

                                 "RONCO SCRIVIA",

                                 "RONDANINA",

                                 "ROSSIGLIONE",

                                 "ROVEGNO",

                                 "SAN COLOMBANO CERTENOLI",

                                 "SANTA MARGHERITA LIGURE",

                                 "SANTO STEFANO D'AVETO",

                                 "SANT'OLCESE",

                                 "SAVIGNONE",

                                 "SERRA RICCO'",

                                 "SESTRI LEVANTE",

                                 "SORI",

                                 "TIGLIETO",

                                 "TORRIGLIA",

                                 "TRIBOGNA",

                                 "USCIO",

                                 "VALBREVENNA",

                                 "VARESE LIGURE",

                                 "VOBBIA",

                                 "ZOAGLI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI GENOVA')
            elif comune.nome in ["AIROLE",

                                 "APRICALE",

                                 "AQUILA D'ARROSCIA",

                                 "ARMO",

                                 "AURIGO",

                                 "BADALUCCO",

                                 "BAJARDO",

                                 "BORDIGHERA",

                                 "BORGHETTO D'ARROSCIA",

                                 "BORGOMARO",

                                 "CAMPOROSSO",

                                 "CARAVONICA",

                                 "CARPASIO",

                                 "CASTEL VITTORIO",

                                 "CASTELLARO",

                                 "CERIANA",

                                 "CERVO",

                                 "CESIO",

                                 "CHIUSANICO",

                                 "CHIUSAVECCHIA",

                                 "CIPRESSA",

                                 "CIVEZZA",

                                 "COSIO D'ARROSCIA",

                                 "COSTARAINERA",

                                 "DIANO ARENTINO",

                                 "DIANO CASTELLO",

                                 "DIANO MARINA",

                                 "DIANO SAN PIETRO",

                                 "DOLCEACQUA",

                                 "DOLCEDO",

                                 "IMPERIA",

                                 "ISOLABONA",

                                 "LUCINASCO",

                                 "MENDATICA",

                                 "MOLINI DI TRIORA",

                                 "MONTALTO LIGURE",

                                 "MONTEGROSSO PIAN LATTE",

                                 "OLIVETTA SAN MICHELE",

                                 "OSPEDALETTI",

                                 "PERINALDO",

                                 "PIETRABRUNA",

                                 "PIEVE DI TECO",

                                 "PIGNA",

                                 "POMPEIANA",

                                 "PONTEDASSIO",

                                 "PORNASSIO",

                                 "PRELA'",

                                 "RANZO",

                                 "REZZO",

                                 "RIVA LIGURE",

                                 "ROCCHETTA NERVINA",

                                 "SAN BARTOLOMEO AL MARE",

                                 "SAN BIAGIO DELLA CIMA",

                                 "SAN LORENZO AL MARE",

                                 "SANREMO",

                                 "SANTO STEFANO AL MARE",

                                 "SEBORGA",

                                 "SOLDANO",

                                 "TAGGIA",

                                 "TERZORIO",

                                 "TRIORA",

                                 "VALLEBONA",

                                 "VALLECROSIA",

                                 "VASIA",

                                 "VENTIMIGLIA",

                                 "VESSALICO",

                                 "VILLA FARALDI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI IMPERIA')
            elif comune.nome in ["AMEGLIA",

                                 "ARCOLA",

                                 "BEVERINO",

                                 "BOLANO",

                                 "BONASSOLA",

                                 "BORGHETTO DI VARA",

                                 "BRUGNATO",

                                 "CALICE AL CORNOVIGLIO",

                                 "CARRODANO",

                                 "CASTELNUOVO MAGRA",

                                 "DEIVA MARINA",

                                 "FOLLO",

                                 "FRAMURA",

                                 "LA SPEZIA",

                                 "LERICI",

                                 "LEVANTO",

                                 "MONTEROSSO AL MARE",

                                 "ORTONOVO",

                                 "PIGNONE",

                                 "PORTOVENERE",

                                 "RICCO' DEL GOLFO DI SPEZIA",

                                 "RIOMAGGIORE",

                                 "ROCCHETTA DI VARA",

                                 "SANTO STEFANO DI MAGRA",

                                 "SARZANA",

                                 "SESTA GODANO",

                                 "VERNAZZA",

                                 "VEZZANO LIGURE",

                                 "ZIGNAGO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI LA SPEZIA')
            elif comune.nome in ["AULLA",

                                 "BAGNONE",

                                 "CARRARA",

                                 "CASOLA IN LUNIGIANA",

                                 "COMANO",

                                 "FILATTIERA",

                                 "FIVIZZANO",

                                 "FOSDINOVO",

                                 "LICCIANA NARDI",

                                 "MASSA",

                                 "MONTIGNOSO",

                                 "MULAZZO",

                                 "PODENZANA",

                                 "PONTREMOLI",

                                 "TRESANA",

                                 "VILLAFRANCA IN LUNIGIANA",

                                 "ZERI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI MASSA')
            elif comune.nome in ["ALASSIO",

                                 "ALBENGA",

                                 "ALBISOLA SUPERIORE",

                                 "ALBISSOLA MARINA",

                                 "ALTARE",

                                 "ANDORA",

                                 "ARNASCO",

                                 "BALESTRINO",

                                 "BARDINETO",

                                 "BERGEGGI",

                                 "BOISSANO",

                                 "BORGHETTO SANTO SPIRITO",

                                 "BORGIO VEREZZI",

                                 "BORMIDA",

                                 "CAIRO MONTENOTTE",

                                 "CALICE LIGURE",

                                 "CALIZZANO",

                                 "CARCARE",

                                 "CASANOVA LERRONE",

                                 "CASTELBIANCO",

                                 "CASTELVECCHIO DI ROCCA BARBENA",

                                 "CELLE LIGURE",

                                 "CENGIO",

                                 "CERIALE",

                                 "CISANO SUL NEVA",

                                 "COSSERIA",

                                 "DEGO",

                                 "ERLI",

                                 "FINALE LIGURE",

                                 "GARLENDA",

                                 "GIUSTENICE",

                                 "GIUSVALLA",

                                 "LAIGUEGLIA",

                                 "LOANO",

                                 "MAGLIOLO",

                                 "MALLARE",

                                 "MASSIMINO",

                                 "MILLESIMO",

                                 "MIOGLIA",

                                 "MURIALDO",

                                 "NASINO",

                                 "NOLI",

                                 "ONZO",

                                 "ORCO FEGLINO",

                                 "ORTOVERO",

                                 "OSIGLIA",

                                 "PALLARE",

                                 "PIANA CRIXIA",

                                 "PIETRA LIGURE",

                                 "PLODIO",

                                 "PONTINVREA",

                                 "QUILIANO",

                                 "RIALTO",

                                 "ROCCAVIGNALE",

                                 "SASSELLO",

                                 "SAVONA",

                                 "SPOTORNO",

                                 "STELLA",

                                 "STELLANELLO",

                                 "TESTICO",

                                 "TOIRANO",

                                 "TOVO SAN GIACOMO",

                                 "URBE",

                                 "VADO LIGURE",

                                 "VARAZZE",

                                 "VENDONE",

                                 "VEZZI PORTIO",

                                 "VILLANOVA D'ALBENGA",

                                 "ZUCCARELLO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI SAVONA')
            elif comune.nome in ["ALTINO",

                                 "ARCHI",

                                 "ARI",

                                 "ARIELLI",

                                 "ATESSA",

                                 "BOMBA",

                                 "BORRELLO",

                                 "BUCCHIANICO",

                                 "CANOSA SANNITA",

                                 "CARPINETO SINELLO",

                                 "CARUNCHIO",

                                 "CASACANDITELLA",

                                 "CASALANGUIDA",

                                 "CASALBORDINO",

                                 "CASALINCONTRADA",

                                 "CASOLI",

                                 "CASTEL FRENTANO",

                                 "CASTELGUIDONE",

                                 "CASTIGLIONE MESSER MARINO",

                                 "CELENZA SUL TRIGNO",

                                 "CHIETI",

                                 "CIVITALUPARELLA",

                                 "CIVITELLA MESSER RAIMONDO",

                                 "COLLEDIMACINE",

                                 "COLLEDIMEZZO",

                                 "CRECCHIO",

                                 "CUPELLO",

                                 "DOGLIOLA",

                                 "FALLO",

                                 "FARA FILIORUM PETRI",

                                 "FARA SAN MARTINO",

                                 "FILETTO",

                                 "FOSSACESIA",

                                 "FRAINE",

                                 "FRANCAVILLA AL MARE",

                                 "FRESAGRANDINARIA",

                                 "FRISA",

                                 "FURCI",

                                 "GAMBERALE",

                                 "GESSOPALENA",

                                 "GISSI",

                                 "GIULIANO TEATINO",

                                 "GUARDIAGRELE",

                                 "GUILMI",

                                 "LAMA DEI PELIGNI",

                                 "LANCIANO",

                                 "LENTELLA",

                                 "LETTOPALENA",

                                 "LISCIA",

                                 "MIGLIANICO",

                                 "MONTAZZOLI",

                                 "MONTEBELLO SUL SANGRO",

                                 "MONTEFERRANTE",

                                 "MONTELAPIANO",

                                 "MONTENERODOMO",

                                 "MONTEODORISIO",

                                 "MOZZAGROGNA",

                                 "ORSOGNA",

                                 "ORTONA",

                                 "PAGLIETA",

                                 "PALENA",

                                 "PALMOLI",

                                 "PALOMBARO",

                                 "PENNADOMO",

                                 "PENNAPIEDIMONTE",

                                 "PERANO",

                                 "PIETRAFERRAZZANA",

                                 "PIZZOFERRATO",

                                 "POGGIOFIORITO",

                                 "POLLUTRI",

                                 "PRETORO",

                                 "QUADRI",

                                 "RAPINO",

                                 "RIPA TEATINA",

                                 "ROCCA SAN GIOVANNI",

                                 "ROCCAMONTEPIANO",

                                 "ROCCASCALEGNA",

                                 "ROCCASPINALVETI",

                                 "ROIO DEL SANGRO",

                                 "ROSELLO",

                                 "SAN BUONO",

                                 "SAN GIOVANNI LIPIONI",

                                 "SAN GIOVANNI TEATINO",

                                 "SAN MARTINO SULLA MARRUCINA",

                                 "SAN SALVO",

                                 "SAN VITO CHIETINO",

                                 "SANTA MARIA IMBARO",

                                 "SANT'EUSANIO DEL SANGRO",

                                 "SCERNI",

                                 "SCHIAVI DI ABRUZZO",

                                 "TARANTA PELIGNA",

                                 "TOLLO",

                                 "TORINO DI SANGRO",

                                 "TORNARECCIO",

                                 "TORREBRUNA",

                                 "TORREVECCHIA TEATINA",

                                 "TORRICELLA PELIGNA",

                                 "TREGLIO",

                                 "TUFILLO",

                                 "VACRI",

                                 "VASTO",

                                 "VILLA SANTA MARIA",

                                 "VILLALFONSINA",

                                 "VILLAMAGNA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CHIETI')
            elif comune.nome in ["ACCIANO",

                                 "AIELLI",

                                 "ALFEDENA",

                                 "ANVERSA DEGLI ABRUZZI",

                                 "ATELETA",

                                 "AVEZZANO",

                                 "BALSORANO",

                                 "BARETE",

                                 "BARISCIANO",

                                 "BARREA",

                                 "BISEGNA",

                                 "BUGNARA",

                                 "CAGNANO AMITERNO",

                                 "CALASCIO",

                                 "CAMPO DI GIOVE",

                                 "CAMPOTOSTO",

                                 "CANISTRO",

                                 "CANSANO",

                                 "CAPESTRANO",

                                 "CAPISTRELLO",

                                 "CAPITIGNANO",

                                 "CAPORCIANO",

                                 "CAPPADOCIA",

                                 "CARAPELLE CALVISIO",

                                 "CARSOLI",

                                 "CASTEL DEL MONTE",

                                 "CASTEL DI IERI",

                                 "CASTEL DI SANGRO",

                                 "CASTELLAFIUME",

                                 "CASTELVECCHIO CALVISIO",

                                 "CASTELVECCHIO SUBEQUO",

                                 "CELANO",

                                 "CERCHIO",

                                 "CIVITA D'ANTINO",

                                 "CIVITELLA ALFEDENA",

                                 "CIVITELLA ROVETO",

                                 "COCULLO",

                                 "COLLARMELE",

                                 "COLLELONGO",

                                 "COLLEPIETRO",

                                 "CORFINIO",

                                 "FAGNANO ALTO",

                                 "FONTECCHIO",

                                 "FOSSA",

                                 "GAGLIANO ATERNO",

                                 "GIOIA DEI MARSI",

                                 "GORIANO SICOLI",

                                 "INTRODACQUA",

                                 "L'AQUILA",

                                 "LECCE NEI MARSI",

                                 "LUCO DEI MARSI",

                                 "LUCOLI",

                                 "MAGLIANO DE' MARSI",

                                 "MASSA D'ALBE",

                                 "MOLINA ATERNO",

                                 "MONTEREALE",

                                 "MORINO",

                                 "NAVELLI",

                                 "OCRE",

                                 "OFENA",

                                 "OPI",

                                 "ORICOLA",

                                 "ORTONA DEI MARSI",

                                 "ORTUCCHIO",

                                 "OVINDOLI",

                                 "PACENTRO",

                                 "PERETO",

                                 "PESCASSEROLI",

                                 "PESCINA",

                                 "PESCOCOSTANZO",

                                 "PETTORANO SUL GIZIO",

                                 "PIZZOLI",

                                 "POGGIO PICENZE",

                                 "PRATA D'ANSIDONIA",

                                 "PRATOLA PELIGNA",

                                 "PREZZA",

                                 "RAIANO",

                                 "RIVISONDOLI",

                                 "ROCCA DI BOTTE",

                                 "ROCCA DI CAMBIO",

                                 "ROCCA DI MEZZO",

                                 "ROCCA PIA",

                                 "ROCCACASALE",

                                 "ROCCARASO",

                                 "SAN BENEDETTO DEI MARSI",

                                 "SAN BENEDETTO IN PERILLIS",

                                 "SAN DEMETRIO NE' VESTINI",

                                 "SAN PIO DELLE CAMERE",

                                 "SAN VINCENZO VALLE ROVETO",

                                 "SANTE MARIE",

                                 "SANT'EUSANIO FORCONESE",

                                 "SANTO STEFANO DI SESSANIO",

                                 "SCANNO",

                                 "SCONTRONE",

                                 "SCOPPITO",

                                 "SCURCOLA MARSICANA",

                                 "SECINARO",

                                 "SULMONA",

                                 "TAGLIACOZZO",

                                 "TIONE DEGLI ABRUZZI",

                                 "TORNIMPARTE",

                                 "TRASACCO",

                                 "VILLA SANTA LUCIA DEGLI ABRUZZI",

                                 "VILLA SANT'ANGELO",

                                 "VILLALAGO",

                                 "VILLAVALLELONGA",

                                 "VILLETTA BARREA",

                                 "VITTORITO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome="TRIBUNALE CIVILE DI L'AQUILA")
            elif comune.nome in ["ABBATEGGIO",

                                 "ALANNO",

                                 "BOLOGNANO",

                                 "BRITTOLI",

                                 "BUSSI SUL TIRINO",

                                 "CAPPELLE SUL TAVO",

                                 "CARAMANICO TERME",

                                 "CARPINETO DELLA NORA",

                                 "CASTIGLIONE A CASAURIA",

                                 "CATIGNANO",

                                 "CEPAGATTI",

                                 "CITTA' SANT'ANGELO",

                                 "CIVITAQUANA",

                                 "CIVITELLA CASANOVA",

                                 "COLLECORVINO",

                                 "CORVARA",

                                 "CUGNOLI",

                                 "ELICE",

                                 "FARINDOLA",

                                 "LETTOMANOPPELLO",

                                 "LORETO APRUTINO",

                                 "MANOPPELLO",

                                 "MONTEBELLO DI BERTONA",

                                 "MONTESILVANO",

                                 "MOSCUFO",

                                 "NOCCIANO",

                                 "PENNE",

                                 "PESCARA",

                                 "PESCOSANSONESCO",

                                 "PIANELLA",

                                 "PICCIANO",

                                 "PIETRANICO",

                                 "POPOLI",

                                 "ROCCAMORICE",

                                 "ROSCIANO",

                                 "SALLE",

                                 "SAN VALENTINO IN ABRUZZO CITERIORE",

                                 "SANT'EUFEMIA A MAIELLA",

                                 "SCAFA",

                                 "SERRAMONACESCA",

                                 "SPOLTORE",

                                 "TOCCO DA CASAURIA",

                                 "TORRE DE' PASSERI",

                                 "TURRIVALIGNANI",

                                 "VICOLI",

                                 "VILLA CELIERA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PESCARA')
            elif comune.nome in ["ALBA ADRIATICA",

                                 "ANCARANO",

                                 "ARSITA",

                                 "ATRI",

                                 "BASCIANO",

                                 "BELLANTE",

                                 "BISENTI",

                                 "CAMPLI",

                                 "CANZANO",

                                 "CASTEL CASTAGNA",

                                 "CASTELLALTO",

                                 "CASTELLI",

                                 "CASTIGLIONE MESSER RAIMONDO",

                                 "CASTILENTI",

                                 "CELLINO ATTANASIO",

                                 "CERMIGNANO",

                                 "CIVITELLA DEL TRONTO",

                                 "COLLEDARA",

                                 "COLONNELLA",

                                 "CONTROGUERRA",

                                 "CORROPOLI",

                                 "CORTINO",

                                 "CROGNALETO",

                                 "FANO ADRIANO",

                                 "GIULIANOVA",

                                 "ISOLA DEL GRAN SASSO D'ITALIA",

                                 "MARTINSICURO",

                                 "MONTEFINO",

                                 "MONTORIO AL VOMANO",

                                 "MORRO D'ORO",

                                 "MOSCIANO SANT'ANGELO",

                                 "NERETO",

                                 "NOTARESCO",

                                 "PENNA SANT'ANDREA",

                                 "PIETRACAMELA",

                                 "PINETO",

                                 "ROCCA SANTA MARIA",

                                 "ROSETO DEGLI ABRUZZI",

                                 "SANT'EGIDIO ALLA VIBRATA",

                                 "SANT'OMERO",

                                 "SILVI",

                                 "TERAMO",

                                 "TORANO NUOVO",

                                 "TORRICELLA SICURA",

                                 "TORTORETO",

                                 "TOSSICIA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI TERAMO')
            elif comune.nome in ["BRINDISI",

                                 "CAROVIGNO",

                                 "CEGLIE MESSAPICA",

                                 "CELLINO SAN MARCO",

                                 "CISTERNINO",

                                 "ERCHIE",

                                 "FASANO",

                                 "FRANCAVILLA FONTANA",

                                 "LATIANO",

                                 "MESAGNE",

                                 "ORIA",

                                 "OSTUNI",

                                 "SAN DONACI",

                                 "SAN MICHELE SALENTINO",

                                 "SAN PANCRAZIO SALENTINO",

                                 "SAN PIETRO VERNOTICO",

                                 "SAN VITO DEI NORMANNI",

                                 "TORCHIAROLO",

                                 "TORRE SANTA SUSANNA",

                                 "VILLA CASTELLI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI BRINDISI')
            elif comune.nome in ["ACQUARICA DEL CAPO",

                                 "ALESSANO",

                                 "ALEZIO",

                                 "ALLISTE",

                                 "ANDRANO",

                                 "ARADEO",

                                 "ARNESANO",

                                 "BAGNOLO DEL SALENTO",

                                 "BOTRUGNO",

                                 "CALIMERA",

                                 "CAMPI SALENTINA",

                                 "CANNOLE",

                                 "CAPRARICA DI LECCE",

                                 "CARMIANO",

                                 "CARPIGNANO SALENTINO",

                                 "CASARANO",

                                 "CASTRI DI LECCE",

                                 "CASTRIGNANO DE' GRECI",

                                 "CASTRIGNANO DEL CAPO",

                                 "CASTRO",

                                 "CAVALLINO",

                                 "COLLEPASSO",

                                 "COPERTINO",

                                 "CORIGLIANO D'OTRANTO",

                                 "CORSANO",

                                 "CURSI",

                                 "CUTROFIANO",

                                 "DISO",

                                 "GAGLIANO DEL CAPO",

                                 "GALATINA",

                                 "GALATONE",

                                 "GALLIPOLI",

                                 "GIUGGIANELLO",

                                 "GIURDIGNANO",

                                 "GUAGNANO",

                                 "LECCE",

                                 "LEQUILE",

                                 "LEVERANO",

                                 "LIZZANELLO",

                                 "MAGLIE",

                                 "MARTANO",

                                 "MARTIGNANO",

                                 "MATINO",

                                 "MELENDUGNO",

                                 "MELISSANO",

                                 "MELPIGNANO",

                                 "MIGGIANO",

                                 "MINERVINO DI LECCE",

                                 "MONTERONI DI LECCE",

                                 "MONTESANO SALENTINO",

                                 "MORCIANO DI LEUCA",

                                 "MURO LECCESE",

                                 "NARDO'",

                                 "NEVIANO",

                                 "NOCIGLIA",

                                 "NOVOLI",

                                 "ORTELLE",

                                 "OTRANTO",

                                 "PALMARIGGI",

                                 "PARABITA",

                                 "PATU'",

                                 "POGGIARDO",

                                 "PORTO CESAREO",

                                 "PRESICCE",

                                 "RACALE",

                                 "RUFFANO",

                                 "SALICE SALENTINO",

                                 "SALVE",

                                 "SAN CASSIANO",

                                 "SAN CESARIO DI LECCE",

                                 "SAN DONATO DI LECCE",

                                 "SAN PIETRO IN LAMA",

                                 "SANARICA",

                                 "SANNICOLA",

                                 "SANTA CESAREA TERME",

                                 "SCORRANO",

                                 "SECLI'",

                                 "SOGLIANO CAVOUR",

                                 "SOLETO",

                                 "SPECCHIA",

                                 "SPONGANO",

                                 "SQUINZANO",

                                 "STERNATIA",

                                 "SUPERSANO",

                                 "SURANO",

                                 "SURBO",

                                 "TAURISANO",

                                 "TAVIANO",

                                 "TIGGIANO",

                                 "TREPUZZI",

                                 "TRICASE",

                                 "TUGLIE",

                                 "UGENTO",

                                 "UGGIANO LA CHIESA",

                                 "VEGLIE",

                                 "VERNOLE",

                                 "ZOLLINO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI LECCE')
            elif comune.nome in ["BARCELLONA POZZO DI GOTTO",

                                 "BASICO'",

                                 "CASTROREALE",

                                 "CONDRO'",

                                 "FONDACHELLI-FANTINA",

                                 "FURNARI",

                                 "GUALTIERI SICAMINO'",

                                 "LENI",

                                 "LIPARI",

                                 "MALFA",

                                 "MAZZARRA' SANT'ANDREA",

                                 "MERI'",

                                 "MILAZZO",

                                 "MONFORTE SAN GIORGIO",

                                 "MONTALBANO ELICONA",

                                 "NOVARA DI SICILIA",

                                 "PACE DEL MELA",

                                 "RODI' MILICI",

                                 "SAN FILIPPO DEL MELA",

                                 "SAN PIER NICETO",

                                 "SANTA LUCIA DEL MELA",

                                 "SANTA MARINA SALINA",

                                 "TERME VIGLIATORE",

                                 "TRIPI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI BARCELLONA POZZO DI GOTTO')
            elif comune.nome in ["ALI'",

                                 "ALI' TERME",

                                 "ANTILLO",

                                 "CASALVECCHIO SICULO",

                                 "CASTELMOLA",

                                 "FIUMEDINISI",

                                 "FORZA D'AGRO'",

                                 "FRANCAVILLA DI SICILIA",

                                 "FURCI SICULO",

                                 "GAGGI",

                                 "GALLODORO",

                                 "GIARDINI-NAXOS",

                                 "GRANITI",

                                 "ITALA",

                                 "LETOJANNI",

                                 "LIMINA",

                                 "MALVAGNA",

                                 "MANDANICI",

                                 "MESSINA",

                                 "MOIO ALCANTARA",

                                 "MONGIUFFI MELIA",

                                 "MOTTA CAMASTRA",

                                 "NIZZA DI SICILIA",

                                 "PAGLIARA",

                                 "ROCCAFIORITA",

                                 "ROCCALUMERA",

                                 "ROCCAVALDINA",

                                 "ROCCELLA VALDEMONE",

                                 "ROMETTA",

                                 "SANTA DOMENICA VITTORIA",

                                 "SANTA TERESA DI RIVA",

                                 "SANT'ALESSIO SICULO",

                                 "SAPONARA",

                                 "SAVOCA",

                                 "SCALETTA ZANCLEA",

                                 "SPADAFORA",

                                 "TAORMINA",

                                 "TORREGROTTA",

                                 "VALDINA",

                                 "VENETICO",

                                 "VILLAFRANCA TIRRENA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI MESSINA')
            elif comune.nome in ["ACQUEDOLCI",

                                 "ALCARA LI FUSI",

                                 "BROLO",

                                 "CAPO D'ORLANDO",

                                 "CAPRI LEONE",

                                 "CARONIA",

                                 "CASTEL DI LUCIO",

                                 "CASTELL'UMBERTO",

                                 "FALCONE",

                                 "FICARRA",

                                 "FLORESTA",

                                 "FRAZZANO'",

                                 "GALATI MAMERTINO",

                                 "GIOIOSA MAREA",

                                 "LIBRIZZI",

                                 "LONGI",

                                 "MILITELLO ROSMARINO",

                                 "MIRTO",

                                 "MISTRETTA",

                                 "MONTAGNAREALE",

                                 "MOTTA D'AFFERMO",

                                 "NASO",

                                 "OLIVERI",

                                 "PATTI",

                                 "PETTINEO",

                                 "PIRAINO",

                                 "RACCUJA",

                                 "REITANO",

                                 "SAN FRATELLO",

                                 "SAN MARCO D'ALUNZIO",

                                 "SAN PIERO PATTI",

                                 "SAN SALVATORE DI FITALIA",

                                 "SANT'AGATA DI MILITELLO",

                                 "SANT'ANGELO DI BROLO",

                                 "SANTO STEFANO DI CAMASTRA",

                                 "SINAGRA",

                                 "TORRENOVA",

                                 "TORTORICI",

                                 "TUSA",

                                 "UCRIA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PATTI')
            elif comune.nome in ["ALBIZZATE",

                                 "ARCONATE",

                                 "ARSAGO SEPRIO",

                                 "BESNATE",

                                 "BUSCATE",

                                 "BUSTO ARSIZIO",

                                 "BUSTO GAROLFO",

                                 "CAIRATE",

                                 "CANEGRATE",

                                 "CARDANO AL CAMPO",

                                 "CARONNO PERTUSELLA",

                                 "CASALE LITTA",

                                 "CASORATE SEMPIONE",

                                 "CASSANO MAGNAGO",

                                 "CASTANO PRIMO",

                                 "CASTELLANZA",

                                 "CAVARIA CON PREMEZZO",

                                 "CERRO MAGGIORE",

                                 "CISLAGO",

                                 "DAIRAGO",

                                 "FAGNANO OLONA",

                                 "FERNO",

                                 "GALLARATE",

                                 "GERENZANO",

                                 "GOLASECCA",

                                 "GORLA MAGGIORE",

                                 "GORLA MINORE",

                                 "INARZO",

                                 "JERAGO CON ORAGO",

                                 "LEGNANO",

                                 "LONATE POZZOLO",

                                 "MAGNAGO",

                                 "MARNATE",

                                 "MORNAGO",

                                 "NOSATE",

                                 "OGGIONA CON SANTO STEFANO",

                                 "OLGIATE OLONA",

                                 "ORIGGIO",

                                 "PARABIAGO",

                                 "RESCALDINA",

                                 "ROBECCHETTO CON INDUNO",

                                 "SAMARATE",

                                 "SAN GIORGIO SU LEGNANO",

                                 "SAN VITTORE OLONA",

                                 "SARONNO",

                                 "SESTO CALENDE",

                                 "SOLBIATE ARNO",

                                 "SOLBIATE OLONA",

                                 "SOMMA LOMBARDO",

                                 "SUMIRAGO",

                                 "TURBIGO",

                                 "UBOLDO",

                                 "VANZAGHELLO",

                                 "VERGIATE",

                                 "VILLA CORTESE",

                                 "VIZZOLA TICINO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI BUSTO ARSIZIO')
            elif comune.nome in ["ALBAVILLA",

                                 "ALBESE CON CASSANO",

                                 "ALBIOLO",

                                 "ALSERIO",

                                 "ALZATE BRIANZA",

                                 "ANZANO DEL PARCO",

                                 "APPIANO GENTILE",

                                 "ARGEGNO",

                                 "AROSIO",

                                 "ASSO",

                                 "BARNI",

                                 "BELLAGIO",

                                 "BENE LARIO",

                                 "BEREGAZZO CON FIGLIARO",

                                 "BINAGO",

                                 "BIZZARONE",

                                 "BLESSAGNO",

                                 "BLEVIO",

                                 "BREGNANO",

                                 "BRENNA",

                                 "BRIENNO",

                                 "BRUNATE",

                                 "BULGAROGRASSO",

                                 "CABIATE",

                                 "CADORAGO",

                                 "CAGLIO",

                                 "CAGNO",

                                 "CAMPIONE D'ITALIA",

                                 "CANTU'",

                                 "CANZO",

                                 "CAPIAGO INTIMIANO",

                                 "CARATE URIO",

                                 "CARBONATE",

                                 "CARIMATE",

                                 "CARLAZZO",

                                 "CARUGO",

                                 "CASASCO D'INTELVI",

                                 "CASLINO D'ERBA",

                                 "CASNATE CON BERNATE",

                                 "CASSINA RIZZARDI",

                                 "CASTELMARTE",

                                 "CASTELNUOVO BOZZENTE",

                                 "CASTIGLIONE D'INTELVI",

                                 "CAVALLASCA",

                                 "CAVARGNA",

                                 "CERANO D'INTELVI",

                                 "CERMENATE",

                                 "CERNOBBIO",

                                 "CIRIMIDO",

                                 "CIVENNA",

                                 "CLAINO CON OSTENO",

                                 "COLONNO",

                                 "COMO",

                                 "CORRIDO",

                                 "CREMIA",

                                 "CUCCIAGO",

                                 "CUSINO",

                                 "DIZZASCO",

                                 "DOMASO",

                                 "DONGO",

                                 "DOSSO DEL LIRO",

                                 "DREZZO",

                                 "ERBA",

                                 "EUPILIO",

                                 "FAGGETO LARIO",

                                 "FALOPPIO",

                                 "FENEGRO'",

                                 "FIGINO SERENZA",

                                 "FINO MORNASCO",

                                 "GARZENO",

                                 "GERA LARIO",

                                 "GIRONICO",

                                 "GRANDATE",

                                 "GRANDOLA ED UNITI",

                                 "GRAVEDONA ED UNITI",

                                 "GRIANTE",

                                 "GUANZATE",

                                 "INVERIGO",

                                 "LAGLIO",

                                 "LAINO",

                                 "LAMBRUGO",

                                 "LANZO D'INTELVI",

                                 "LASNIGO",

                                 "LENNO",

                                 "LEZZENO",

                                 "LIMIDO COMASCO",

                                 "LIPOMO",

                                 "LIVO",

                                 "LOCATE VARESINO",

                                 "LOMAZZO",

                                 "LONGONE AL SEGRINO",

                                 "LUISAGO",

                                 "LURAGO D'ERBA",

                                 "LURAGO MARINONE",

                                 "LURATE CACCIVIO",

                                 "MAGREGLIO",

                                 "MARIANO COMENSE",

                                 "MASLIANICO",

                                 "MENAGGIO",

                                 "MERONE",

                                 "MEZZEGRA",

                                 "MOLTRASIO",

                                 "MONGUZZO",

                                 "MONTANO LUCINO",

                                 "MONTEMEZZO",

                                 "MONTORFANO",

                                 "MOZZATE",

                                 "MUSSO",

                                 "NESSO",

                                 "NOVEDRATE",

                                 "OLGIATE COMASCO",

                                 "OLTRONA DI SAN MAMETTE",

                                 "ORSENIGO",

                                 "OSSUCCIO",

                                 "PARE'",

                                 "PEGLIO",

                                 "PELLIO INTELVI",

                                 "PIANELLO DEL LARIO",

                                 "PIGRA",

                                 "PLESIO",

                                 "POGNANA LARIO",

                                 "PONNA",

                                 "PONTE LAMBRO",

                                 "PORLEZZA",

                                 "PROSERPIO",

                                 "PUSIANO",

                                 "RAMPONIO VERNA",

                                 "REZZAGO",

                                 "RODERO",

                                 "RONAGO",

                                 "ROVELLASCA",

                                 "ROVELLO PORRO",

                                 "SALA COMACINA",

                                 "SAN BARTOLOMEO VAL CAVARGNA",

                                 "SAN FEDELE INTELVI",

                                 "SAN FERMO DELLA BATTAGLIA",

                                 "SAN NAZZARO VAL CAVARGNA",

                                 "SAN SIRO",

                                 "SCHIGNANO",

                                 "SENNA COMASCO",

                                 "SOLBIATE",

                                 "SORICO",

                                 "SORMANO",

                                 "STAZZONA",

                                 "TAVERNERIO",

                                 "TORNO",

                                 "TREMEZZO",

                                 "TREZZONE",

                                 "TURATE",

                                 "UGGIATE-TREVANO",

                                 "VAL REZZO",

                                 "VALBRONA",

                                 "VALMOREA",

                                 "VALSOLDA",

                                 "VELESO",

                                 "VENIANO",

                                 "VERCANA",

                                 "VERTEMATE CON MINOPRIO",

                                 "VILLA GUARDIA",

                                 "ZELBIO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI COMO')
            elif comune.nome in ["ABBADIA LARIANA",

                                 "AIRUNO",

                                 "ANNONE DI BRIANZA",

                                 "BALLABIO",

                                 "BARZAGO",

                                 "BARZANO'",

                                 "BARZIO",

                                 "BELLANO",

                                 "BOSISIO PARINI",

                                 "BRIVIO",

                                 "BULCIAGO",

                                 "CALCO",

                                 "CALOLZIOCORTE",

                                 "CARENNO",

                                 "CASARGO",

                                 "CASATENOVO",

                                 "CASSAGO BRIANZA",

                                 "CASSINA VALSASSINA",

                                 "CASTELLO DI BRIANZA",

                                 "CERNUSCO LOMBARDONE",

                                 "CESANA BRIANZA",

                                 "CIVATE",

                                 "COLICO",

                                 "COLLE BRIANZA",

                                 "CORTENOVA",

                                 "COSTA MASNAGA",

                                 "CRANDOLA VALSASSINA",

                                 "CREMELLA",

                                 "CREMENO",

                                 "DERVIO",

                                 "DOLZAGO",

                                 "DORIO",

                                 "ELLO",

                                 "ERVE",

                                 "ESINO LARIO",

                                 "GALBIATE",

                                 "GARBAGNATE MONASTERO",

                                 "GARLATE",

                                 "IMBERSAGO",

                                 "INTROBIO",

                                 "INTROZZO",

                                 "LECCO",

                                 "LIERNA",

                                 "LOMAGNA",

                                 "MALGRATE",

                                 "MANDELLO DEL LARIO",

                                 "MARGNO",

                                 "MERATE",

                                 "MISSAGLIA",

                                 "MOGGIO",

                                 "MOLTENO",

                                 "MONTE MARENZO",

                                 "MONTEVECCHIA",

                                 "MONTICELLO BRIANZA",

                                 "MORTERONE",

                                 "NIBIONNO",

                                 "OGGIONO",

                                 "OLGIATE MOLGORA",

                                 "OLGINATE",

                                 "OLIVETO LARIO",

                                 "OSNAGO",

                                 "PADERNO D'ADDA",

                                 "PAGNONA",

                                 "PARLASCO",

                                 "PASTURO",

                                 "PEREGO",

                                 "PERLEDO",

                                 "PESCATE",

                                 "PREMANA",

                                 "PRIMALUNA",

                                 "ROBBIATE",

                                 "ROGENO",

                                 "ROVAGNATE",

                                 "SANTA MARIA HOE'",

                                 "SIRONE",

                                 "SIRTORI",

                                 "SUEGLIO",

                                 "SUELLO",

                                 "TACENO",

                                 "TORRE DE' BUSI",

                                 "TREMENICO",

                                 "VALGREGHENTINO",

                                 "VALMADRERA",

                                 "VARENNA",

                                 "VENDROGNO",

                                 "VERCURAGO",

                                 "VERDERIO INFERIORE",

                                 "VERDERIO SUPERIORE",

                                 "VESTRENO",

                                 "VIGANO'"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI LECCO')
            elif comune.nome in ["ABBADIA CERRETO",

                                 "BERTONICO",

                                 "BOFFALORA D'ADDA",

                                 "BORGHETTO LODIGIANO",

                                 "BORGO SAN GIOVANNI",

                                 "BREMBIO",

                                 "CAMAIRAGO",

                                 "CARPIANO",

                                 "CASALETTO LODIGIANO",

                                 "CASALMAIOCCO",

                                 "CASALPUSTERLENGO",

                                 "CASELLE LANDI",

                                 "CASELLE LURANI",

                                 "CASTELNUOVO BOCCA D'ADDA",

                                 "CASTIGLIONE D'ADDA",

                                 "CASTIRAGA VIDARDO",

                                 "CAVACURTA",

                                 "CAVENAGO D'ADDA",

                                 "CERRO AL LAMBRO",

                                 "CERVIGNANO D'ADDA",

                                 "CODOGNO",

                                 "COLTURANO",

                                 "COMAZZO",

                                 "CORNEGLIANO LAUDENSE",

                                 "CORNO GIOVINE",

                                 "CORNOVECCHIO",

                                 "CORTE PALASIO",

                                 "CRESPIATICA",

                                 "DRESANO",

                                 "FOMBIO",

                                 "GALGAGNANO",

                                 "GRAFFIGNANA",

                                 "GUARDAMIGLIO",

                                 "LIVRAGA",

                                 "LOCATE DI TRIULZI",

                                 "LODI",

                                 "LODI VECCHIO",

                                 "MACCASTORNA",

                                 "MAIRAGO",

                                 "MALEO",

                                 "MARUDO",

                                 "MASSALENGO",

                                 "MEDIGLIA",

                                 "MELEGNANO",

                                 "MELETI",

                                 "MERLINO",

                                 "MONTANASO LOMBARDO",

                                 "MULAZZANO",

                                 "ORIO LITTA",

                                 "OSPEDALETTO LODIGIANO",

                                 "OSSAGO LODIGIANO",

                                 "PAULLO",

                                 "PIEVE FISSIRAGA",

                                 "SALERANO SUL LAMBRO",

                                 "SAN COLOMBANO AL LAMBRO",

                                 "SAN FIORANO",

                                 "SAN GIULIANO MILANESE",

                                 "SAN MARTINO IN STRADA",

                                 "SAN ROCCO AL PORTO",

                                 "SAN ZENONE AL LAMBRO",

                                 "SANT'ANGELO LODIGIANO",

                                 "SANTO STEFANO LODIGIANO",

                                 "SECUGNAGO",

                                 "SENNA LODIGIANA",

                                 "SOMAGLIA",

                                 "SORDIO",

                                 "TAVAZZANO CON VILLAVESCO",

                                 "TERRANOVA DEI PASSERINI",

                                 "TRIBIANO",

                                 "TURANO LODIGIANO",

                                 "VALERA FRATTA",

                                 "VILLANOVA DEL SILLARO",

                                 "VIZZOLO PREDABISSI",

                                 "ZELO BUON PERSICO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI LODI')
            elif comune.nome in ["ARESE",

                                 "ARLUNO",

                                 "ASSAGO",

                                 "BARANZATE",

                                 "BAREGGIO",

                                 "BASIANO",

                                 "BASIGLIO",

                                 "BELLINZAGO LOMBARDO",

                                 "BERNATE TICINO",

                                 "BOFFALORA SOPRA TICINO",

                                 "BOLLATE",

                                 "BRESSO",

                                 "BUCCINASCO",

                                 "BUSSERO",

                                 "CAMBIAGO",

                                 "CASOREZZO",

                                 "CASSANO D'ADDA",

                                 "CASSINA DE' PECCHI",

                                 "CERNUSCO SUL NAVIGLIO",

                                 "CESANO BOSCONE",

                                 "CESATE",

                                 "CORBETTA",

                                 "CORMANO",

                                 "CORNAREDO",

                                 "CORSICO",

                                 "CUGGIONO",

                                 "CUSAGO",

                                 "GARBAGNATE MILANESE",

                                 "GESSATE",

                                 "GORGONZOLA",

                                 "GREZZAGO",

                                 "INVERUNO",

                                 "INZAGO",

                                 "LAINATE",

                                 "LIMBIATE",

                                 "LISCATE",

                                 "MAGENTA",

                                 "MARCALLO CON CASONE",

                                 "MASATE",

                                 "MELZO",

                                 "MESERO",

                                 "MILANO",

                                 "NERVIANO",

                                 "NOVATE MILANESE",

                                 "OPERA",

                                 "OSSONA",

                                 "PANTIGLIATE",

                                 "PERO",

                                 "PESCHIERA BORROMEO",

                                 "PESSANO CON BORNAGO",

                                 "PIEVE EMANUELE",

                                 "PIOLTELLO",

                                 "POGLIANO MILANESE",

                                 "POZZO D'ADDA",

                                 "POZZUOLO MARTESANA",

                                 "PREGNANA MILANESE",

                                 "RHO",

                                 "RODANO",

                                 "ROZZANO",

                                 "SAN DONATO MILANESE",

                                 "SANTO STEFANO TICINO",

                                 "SEDRIANO",

                                 "SEGRATE",

                                 "SENAGO",

                                 "SETTALA",

                                 "SETTIMO MILANESE",

                                 "TREZZANO ROSA",

                                 "TREZZANO SUL NAVIGLIO",

                                 "TREZZO SULL'ADDA",

                                 "TRUCCAZZANO",

                                 "VANZAGO",

                                 "VAPRIO D'ADDA",

                                 "VIGNATE",

                                 "VITTUONE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI MILANO')
            elif comune.nome in ["AGRATE BRIANZA",

                                 "AICURZIO",

                                 "ALBIATE",

                                 "ARCORE",

                                 "BARLASSINA",

                                 "BELLUSCO",

                                 "BERNAREGGIO",

                                 "BESANA IN BRIANZA",

                                 "BIASSONO",

                                 "BOVISIO-MASCIAGO",

                                 "BRIOSCO",

                                 "BRUGHERIO",

                                 "BURAGO DI MOLGORA",

                                 "BUSNAGO",

                                 "CAMPARADA",

                                 "CAPONAGO",

                                 "CARATE BRIANZA",

                                 "CARNATE",

                                 "CARUGATE",

                                 "CAVENAGO DI BRIANZA",

                                 "CERIANO LAGHETTO",

                                 "CESANO MADERNO",

                                 "CINISELLO BALSAMO",

                                 "COGLIATE",

                                 "COLOGNO MONZESE",

                                 "CONCOREZZO",

                                 "CORNATE D'ADDA",

                                 "CORREZZANA",

                                 "CUSANO MILANINO",

                                 "DESIO",

                                 "GIUSSANO",

                                 "LAZZATE",

                                 "LENTATE SUL SEVESO",

                                 "LESMO",

                                 "LISSONE",

                                 "MACHERIO",

                                 "MEDA",

                                 "MEZZAGO",

                                 "MISINTO",

                                 "MONZA",

                                 "MUGGIO'",

                                 "NOVA MILANESE",

                                 "ORNAGO",

                                 "PADERNO DUGNANO",

                                 "RENATE",

                                 "RONCELLO",

                                 "RONCO BRIANTINO",

                                 "SEREGNO",

                                 "SESTO SAN GIOVANNI",

                                 "SEVESO",

                                 "SOLARO",

                                 "SOVICO",

                                 "SULBIATE",

                                 "TRIUGGIO",

                                 "USMATE VELATE",

                                 "VAREDO",

                                 "VEDANO AL LAMBRO",

                                 "VEDUGGIO CON COLZANO",

                                 "VERANO BRIANZA",

                                 "VILLASANTA",

                                 "VIMERCATE",

                                 "VIMODRONE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI MONZA')
            elif comune.nome in ["ABBIATEGRASSO",

                                 "ALAGNA",

                                 "ALBAIRATE",

                                 "ALBAREDO ARNABOLDI",

                                 "ALBONESE",

                                 "ALBUZZANO",

                                 "ARENA PO",

                                 "BADIA PAVESE",

                                 "BAGNARIA",

                                 "BARBIANELLO",

                                 "BASCAPE'",

                                 "BASTIDA DE' DOSSI",

                                 "BASTIDA PANCARANA",

                                 "BATTUDA",

                                 "BELGIOIOSO",

                                 "BEREGUARDO",

                                 "BESATE",

                                 "BINASCO",

                                 "BORGARELLO",

                                 "BORGO PRIOLO",

                                 "BORGO SAN SIRO",

                                 "BORGORATTO MORMOROLO",

                                 "BORNASCO",

                                 "BOSNASCO",

                                 "BRALLO DI PREGOLA",

                                 "BREME",

                                 "BRESSANA BOTTARONE",

                                 "BRONI",

                                 "BUBBIANO",

                                 "CALVIGNANO",

                                 "CALVIGNASCO",

                                 "CAMPOSPINOSO",

                                 "CANDIA LOMELLINA",

                                 "CANEVINO",

                                 "CANNETO PAVESE",

                                 "CARBONARA AL TICINO",

                                 "CASANOVA LONATI",

                                 "CASARILE",

                                 "CASATISMA",

                                 "CASEI GEROLA",

                                 "CASORATE PRIMO",

                                 "CASSINETTA DI LUGAGNANO",

                                 "CASSOLNOVO",

                                 "CASTANA",

                                 "CASTEGGIO",

                                 "CASTELLETTO DI BRANDUZZO",

                                 "CASTELLO D'AGOGNA",

                                 "CASTELNOVETTO",

                                 "CAVA MANARA",

                                 "CECIMA",

                                 "CERANOVA",

                                 "CERETTO LOMELLINA",

                                 "CERGNAGO",

                                 "CERTOSA DI PAVIA",

                                 "CERVESINA",

                                 "CHIGNOLO PO",

                                 "CIGOGNOLA",

                                 "CILAVEGNA",

                                 "CISLIANO",

                                 "CODEVILLA",

                                 "CONFIENZA",

                                 "COPIANO",

                                 "CORANA",

                                 "CORNALE",

                                 "CORTEOLONA",

                                 "CORVINO SAN QUIRICO",

                                 "COSTA DE' NOBILI",

                                 "COZZO",

                                 "CURA CARPIGNANO",

                                 "DORNO",

                                 "FERRERA ERBOGNONE",

                                 "FILIGHERA",

                                 "FORTUNAGO",

                                 "FRASCAROLO",

                                 "GAGGIANO",

                                 "GALLIAVOLA",

                                 "GAMBARANA",

                                 "GAMBOLO'",

                                 "GARLASCO",

                                 "GENZONE",

                                 "GERENZAGO",

                                 "GIUSSAGO",

                                 "GODIASCO SALICE TERME",

                                 "GOLFERENZO",

                                 "GRAVELLONA LOMELLINA",

                                 "GROPELLO CAIROLI",

                                 "GUDO VISCONTI",

                                 "INVERNO E MONTELEONE",

                                 "LACCHIARELLA",

                                 "LANDRIANO",

                                 "LANGOSCO",

                                 "LARDIRAGO",

                                 "LINAROLO",

                                 "LIRIO",

                                 "LOMELLO",

                                 "LUNGAVILLA",

                                 "MAGHERNO",

                                 "MARCIGNAGO",

                                 "MARZANO",

                                 "MEDE",

                                 "MENCONICO",

                                 "MEZZANA BIGLI",

                                 "MEZZANA RABATTONE",

                                 "MEZZANINO",

                                 "MIRADOLO TERME",

                                 "MONTALTO PAVESE",

                                 "MONTEBELLO DELLA BATTAGLIA",

                                 "MONTECALVO VERSIGGIA",

                                 "MONTESCANO",

                                 "MONTESEGALE",

                                 "MONTICELLI PAVESE",

                                 "MONTU' BECCARIA",

                                 "MORIMONDO",

                                 "MORNICO LOSANA",

                                 "MORTARA",

                                 "MOTTA VISCONTI",

                                 "NICORVO",

                                 "NOVIGLIO",

                                 "OLEVANO DI LOMELLINA",

                                 "OLIVA GESSI",

                                 "OTTOBIANO",

                                 "OZZERO",

                                 "PALESTRO",

                                 "PANCARANA",

                                 "PARONA",

                                 "PAVIA",

                                 "PIETRA DE' GIORGI",

                                 "PIEVE ALBIGNOLA",

                                 "PIEVE DEL CAIRO",

                                 "PIEVE PORTO MORONE",

                                 "PINAROLO PO",

                                 "PIZZALE",

                                 "PONTE NIZZA",

                                 "PORTALBERA",

                                 "REA",

                                 "REDAVALLE",

                                 "RETORBIDO",

                                 "RIVANAZZANO TERME",

                                 "ROBBIO",

                                 "ROBECCO PAVESE",

                                 "ROBECCO SUL NAVIGLIO",

                                 "ROCCA DE' GIORGI",

                                 "ROCCA SUSELLA",

                                 "ROGNANO",

                                 "ROMAGNESE",

                                 "RONCARO",

                                 "ROSASCO",

                                 "ROSATE",

                                 "ROVESCALA",

                                 "RUINO",

                                 "SAN CIPRIANO PO",

                                 "SAN DAMIANO AL COLLE",

                                 "SAN GENESIO ED UNITI",

                                 "SAN GIORGIO DI LOMELLINA",

                                 "SAN MARTINO SICCOMARIO",

                                 "SAN ZENONE AL PO",

                                 "SANNAZZARO DE' BURGONDI",

                                 "SANTA CRISTINA E BISSONE",

                                 "SANTA GIULETTA",

                                 "SANTA MARGHERITA DI STAFFORA",

                                 "SANTA MARIA DELLA VERSA",

                                 "SANT'ALESSIO CON VIALONE",

                                 "SANT'ANGELO LOMELLINA",

                                 "SARTIRANA LOMELLINA",

                                 "SCALDASOLE",

                                 "SEMIANA",

                                 "SILVANO PIETRA",

                                 "SIZIANO",

                                 "SOMMO",

                                 "SPESSA",

                                 "STRADELLA",

                                 "SUARDI",

                                 "TORRAZZA COSTE",

                                 "TORRE BERETTI E CASTELLARO",

                                 "TORRE D'ARESE",

                                 "TORRE DE' NEGRI",

                                 "TORRE D'ISOLA",

                                 "TORREVECCHIA PIA",

                                 "TORRICELLA VERZATE",

                                 "TRAVACO' SICCOMARIO",

                                 "TRIVOLZIO",

                                 "TROMELLO",

                                 "TROVO",

                                 "VAL DI NIZZA",

                                 "VALEGGIO",

                                 "VALLE LOMELLINA",

                                 "VALLE SALIMBENE",

                                 "VALVERDE",

                                 "VARZI",

                                 "VELEZZO LOMELLINA",

                                 "VELLEZZO BELLINI",

                                 "VERMEZZO",

                                 "VERNATE",

                                 "VERRETTO",

                                 "VERRUA PO",

                                 "VIDIGULFO",

                                 "VIGEVANO",

                                 "VILLA BISCOSSI",

                                 "VILLANOVA D'ARDENGHI",

                                 "VILLANTERIO",

                                 "VISTARINO",

                                 "VOGHERA",

                                 "VOLPARA",

                                 "ZAVATTARELLO",

                                 "ZECCONE",

                                 "ZELO SURRIGONE",

                                 "ZEME",

                                 "ZENEVREDO",

                                 "ZERBO",

                                 "ZERBOLO'",

                                 "ZIBIDO SAN GIACOMO",

                                 "ZINASCO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PAVIA')
            elif comune.nome in ["ALBAREDO PER SAN MARCO",

                                 "ALBOSAGGIA",

                                 "ANDALO VALTELLINO",

                                 "APRICA",

                                 "ARDENNO",

                                 "BEMA",

                                 "BERBENNO DI VALTELLINA",

                                 "BIANZONE",

                                 "BORMIO",

                                 "BUGLIO IN MONTE",

                                 "CAIOLO",

                                 "CAMPODOLCINO",

                                 "CASPOGGIO",

                                 "CASTELLO DELL'ACQUA",

                                 "CASTIONE ANDEVENNO",

                                 "CEDRASCO",

                                 "CERCINO",

                                 "CHIAVENNA",

                                 "CHIESA IN VALMALENCO",

                                 "CHIURO",

                                 "CINO",

                                 "CIVO",

                                 "COLORINA",

                                 "COSIO VALTELLINO",

                                 "DAZIO",

                                 "DELEBIO",

                                 "DUBINO",

                                 "FAEDO VALTELLINO",

                                 "FORCOLA",

                                 "FUSINE",

                                 "GEROLA ALTA",

                                 "GORDONA",

                                 "GROSIO",

                                 "GROSOTTO",

                                 "LANZADA",

                                 "LIVIGNO",

                                 "LOVERO",

                                 "MADESIMO",

                                 "MANTELLO",

                                 "MAZZO DI VALTELLINA",

                                 "MELLO",

                                 "MENAROLA",

                                 "MESE",

                                 "MONTAGNA IN VALTELLINA",

                                 "MORBEGNO",

                                 "NOVATE MEZZOLA",

                                 "PEDESINA",

                                 "PIANTEDO",

                                 "PIATEDA",

                                 "PIURO",

                                 "POGGIRIDENTI",

                                 "PONTE IN VALTELLINA",

                                 "POSTALESIO",

                                 "PRATA CAMPORTACCIO",

                                 "RASURA",

                                 "ROGOLO",

                                 "SAMOLACO",

                                 "SAN GIACOMO FILIPPO",

                                 "SERNIO",

                                 "SONDALO",

                                 "SONDRIO",

                                 "SPRIANA",

                                 "TALAMONA",

                                 "TARTANO",

                                 "TEGLIO",

                                 "TIRANO",

                                 "TORRE DI SANTA MARIA",

                                 "TOVO DI SANT'AGATA",

                                 "TRAONA",

                                 "TRESIVIO",

                                 "VAL MASINO",

                                 "VALDIDENTRO",

                                 "VALDISOTTO",

                                 "VALFURVA",

                                 "VERCEIA",

                                 "VERVIO",

                                 "VILLA DI CHIAVENNA",

                                 "VILLA DI TIRANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI SONDRIO')
            elif comune.nome in ["AGRA",

                                 "ANGERA",

                                 "ARCISATE",

                                 "AZZATE",

                                 "AZZIO",

                                 "BARASSO",

                                 "BARDELLO",

                                 "BEDERO VALCUVIA",

                                 "BESANO",

                                 "BESOZZO",

                                 "BIANDRONNO",

                                 "BISUSCHIO",

                                 "BODIO LOMNAGO",

                                 "BREBBIA",

                                 "BREGANO",

                                 "BRENTA",

                                 "BREZZO DI BEDERO",

                                 "BRINZIO",

                                 "BRISSAGO-VALTRAVAGLIA",

                                 "BRUNELLO",

                                 "BRUSIMPIANO",

                                 "BUGUGGIATE",

                                 "CADEGLIANO-VICONAGO",

                                 "CADREZZATE",

                                 "CANTELLO",

                                 "CARAVATE",

                                 "CARNAGO",

                                 "CARONNO VARESINO",

                                 "CASALZUIGNO",

                                 "CASCIAGO",

                                 "CASSANO VALCUVIA",

                                 "CASTELLO CABIAGLIO",

                                 "CASTELSEPRIO",

                                 "CASTELVECCANA",

                                 "CASTIGLIONE OLONA",

                                 "CASTRONNO",

                                 "CAZZAGO BRABBIA",

                                 "CITTIGLIO",

                                 "CLIVIO",

                                 "COCQUIO-TREVISAGO",

                                 "COMABBIO",

                                 "COMERIO",

                                 "CREMENAGA",

                                 "CROSIO DELLA VALLE",

                                 "CUASSO AL MONTE",

                                 "CUGLIATE-FABIASCO",

                                 "CUNARDO",

                                 "CURIGLIA CON MONTEVIASCO",

                                 "CUVEGLIO",

                                 "CUVIO",

                                 "DAVERIO",

                                 "DUMENZA",

                                 "DUNO",

                                 "FERRERA DI VARESE",

                                 "GALLIATE LOMBARDO",

                                 "GAVIRATE",

                                 "GAZZADA SCHIANNO",

                                 "GEMONIO",

                                 "GERMIGNAGA",

                                 "GORNATE-OLONA",

                                 "GRANTOLA",

                                 "INDUNO OLONA",

                                 "ISPRA",

                                 "LAVENA PONTE TRESA",

                                 "LAVENO-MOMBELLO",

                                 "LEGGIUNO",

                                 "LONATE CEPPINO",

                                 "LOZZA",

                                 "LUINO",

                                 "LUVINATE",

                                 "MACCAGNO",

                                 "MALGESSO",

                                 "MALNATE",

                                 "MARCHIROLO",

                                 "MARZIO",

                                 "MASCIAGO PRIMO",

                                 "MERCALLO",

                                 "MESENZANA",

                                 "MONTEGRINO VALTRAVAGLIA",

                                 "MONVALLE",

                                 "MORAZZONE",

                                 "ORINO",

                                 "OSMATE",

                                 "PINO SULLA SPONDA DEL LAGO MAGGIORE",

                                 "PORTO CERESIO",

                                 "PORTO VALTRAVAGLIA",

                                 "RANCIO VALCUVIA",

                                 "RANCO",

                                 "SALTRIO",

                                 "SANGIANO",

                                 "TAINO",

                                 "TERNATE",

                                 "TRADATE",

                                 "TRAVEDONAMONATE",

                                 "TRONZANO LAGO MAGGIORE",

                                 "VALGANNA",

                                 "VARANO BORGHI",

                                 "VARESE",

                                 "VEDANO OLONA",

                                 "VEDDASCA",

                                 "VENEGONO INFERIORE",

                                 "VENEGONO SUPERIORE",

                                 "VIGGIU'"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI VARESE')
            elif comune.nome in ["AIELLO DEL SABATO",

                                 "ALTAVILLA IRPINA",

                                 "ANDRETTA",

                                 "AQUILONIA",

                                 "ATRIPALDA",

                                 "AVELLA",

                                 "AVELLINO",

                                 "BAGNOLI IRPINO",

                                 "BAIANO",

                                 "BISACCIA",

                                 "CAIRANO",

                                 "CALABRITTO",

                                 "CALITRI",

                                 "CANDIDA",

                                 "CAPOSELE",

                                 "CAPRIGLIA IRPINA",

                                 "CASSANO IRPINO",

                                 "CASTELFRANCI",

                                 "CASTELVETERE SUL CALORE",

                                 "CERVINARA",

                                 "CESINALI",

                                 "CHIUSANO DI SAN DOMENICO",

                                 "CONTRADA",

                                 "CONZA DELLA CAMPANIA",

                                 "DOMICELLA",

                                 "FORINO",

                                 "FRIGENTO",

                                 "GESUALDO",

                                 "GROTTOLELLA",

                                 "GUARDIA LOMBARDI",

                                 "LACEDONIA",

                                 "LAPIO",

                                 "LAURO",

                                 "LIONI",

                                 "MANOCALZATI",

                                 "MARZANO DI NOLA",

                                 "MERCOGLIANO",

                                 "MONTEFALCIONE",

                                 "MONTEFORTE IRPINO",

                                 "MONTEFREDANE",

                                 "MONTELLA",

                                 "MONTEMARANO",

                                 "MONTEMILETTO",

                                 "MONTEVERDE",

                                 "MONTORO INFERIORE",

                                 "MONTORO SUPERIORE",

                                 "MORRA DE SANCTIS",

                                 "MOSCHIANO",

                                 "MUGNANO DEL CARDINALE",

                                 "NUSCO",

                                 "OSPEDALETTO D'ALPINOLO",

                                 "PAGO DEL VALLO DI LAURO",

                                 "PAROLISE",

                                 "PIETRASTORNINA",

                                 "PRATA DI PRINCIPATO ULTRA",

                                 "PRATOLA SERRA",

                                 "QUADRELLE",

                                 "QUINDICI",

                                 "ROCCA SAN FELICE",

                                 "ROCCABASCERANA",

                                 "ROTONDI",

                                 "SALZA IRPINA",

                                 "SAN MANGO SUL CALORE",

                                 "SAN MARTINO VALLE CAUDINA",

                                 "SAN MICHELE DI SERINO",

                                 "SAN POTITO ULTRA",

                                 "SANTA LUCIA DI SERINO",

                                 "SANTA PAOLINA",

                                 "SANT'ANDREA DI CONZA",

                                 "SANT'ANGELO A SCALA",

                                 "SANT'ANGELO DEI LOMBARDI",

                                 "SANTO STEFANO DEL SOLE",

                                 "SENERCHIA",

                                 "SERINO",

                                 "SIRIGNANO",

                                 "SOLOFRA",

                                 "SORBO SERPICO",

                                 "SPERONE",

                                 "STURNO",

                                 "SUMMONTE",

                                 "TAURANO",

                                 "TEORA",

                                 "TORELLA DEI LOMBARDI",

                                 "TORRE LE NOCELLE",

                                 "TUFO",

                                 "VILLAMAINA",

                                 "VOLTURARA IRPINA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI AVELLINO')
            elif comune.nome in ["AIROLA",

                                 "AMOROSI",

                                 "APICE",

                                 "APOLLOSA",

                                 "ARIANO IRPINO",

                                 "ARPAIA",

                                 "ARPAISE",

                                 "BASELICE",

                                 "BENEVENTO",

                                 "BONEA",

                                 "BONITO",

                                 "BUCCIANO",

                                 "BUONALBERGO",

                                 "CALVI",

                                 "CAMPOLATTARO",

                                 "CAMPOLI DEL MONTE TABURNO",

                                 "CARIFE",

                                 "CASALBORE",

                                 "CASALDUNI",

                                 "CASTEL BARONIA",

                                 "CASTELFRANCO IN MISCANO",

                                 "CASTELPAGANO",

                                 "CASTELPOTO",

                                 "CASTELVENERE",

                                 "CASTELVETERE IN VAL FORTORE",

                                 "CAUTANO",

                                 "CEPPALONI",

                                 "CERRETO SANNITA",

                                 "CHIANCHE",

                                 "CIRCELLO",

                                 "COLLE SANNITA",

                                 "CUSANO MUTRI",

                                 "DUGENTA",

                                 "DURAZZANO",

                                 "FAICCHIO",

                                 "FLUMERI",

                                 "FOGLIANISE",

                                 "FOIANO DI VAL FORTORE",

                                 "FONTANAROSA",

                                 "FORCHIA",

                                 "FRAGNETO L'ABATE",

                                 "FRAGNETO MONFORTE",

                                 "FRASSO TELESINO",

                                 "GINESTRA DEGLI SCHIAVONI",

                                 "GRECI",

                                 "GROTTAMINARDA",

                                 "GUARDIA SANFRAMONDI",

                                 "LIMATOLA",

                                 "LUOGOSANO",

                                 "MELITO IRPINO",

                                 "MELIZZANO",

                                 "MIRABELLA ECLANO",

                                 "MOIANO",

                                 "MOLINARA",

                                 "MONTAGUTO",

                                 "MONTECALVO IRPINO",

                                 "MONTEFALCONE DI VAL FORTORE",

                                 "MONTEFUSCO",

                                 "MONTESARCHIO",

                                 "MORCONE",

                                 "PADULI",

                                 "PAGO VEIANO",

                                 "PANNARANO",

                                 "PAOLISI",

                                 "PATERNOPOLI",

                                 "PAUPISI",

                                 "PESCO SANNITA",

                                 "PETRURO IRPINO",

                                 "PIETRADEFUSI",

                                 "PIETRAROJA",

                                 "PIETRELCINA",

                                 "PONTE",

                                 "PONTELANDOLFO",

                                 "PUGLIANELLO",

                                 "REINO",

                                 "SAN BARTOLOMEO IN GALDO",

                                 "SAN GIORGIO DEL SANNIO",

                                 "SAN GIORGIO LA MOLARA",

                                 "SAN LEUCIO DEL SANNIO",

                                 "SAN LORENZELLO",

                                 "SAN LORENZO MAGGIORE",

                                 "SAN LUPO",

                                 "SAN MARCO DEI CAVOTI",

                                 "SAN MARTINO SANNITA",

                                 "SAN NAZZARO",

                                 "SAN NICOLA BARONIA",

                                 "SAN NICOLA MANFREDI",

                                 "SAN SALVATORE TELESINO",

                                 "SAN SOSSIO BARONIA",

                                 "SANTA CROCE DEL SANNIO",

                                 "SANT'AGATA DE' GOTI",

                                 "SANT'ANGELO A CUPOLO",

                                 "SANT'ANGELO ALL'ESCA",

                                 "SANT'ARCANGELO TRIMONTE",

                                 "SASSINORO",

                                 "SAVIGNANO IRPINO",

                                 "SCAMPITELLA",

                                 "SOLOPACA",

                                 "TAURASI",

                                 "TELESE TERME",

                                 "TOCCO CAUDIO",

                                 "TORRECUSO",

                                 "TORRIONI",

                                 "TREVICO",

                                 "VALLATA",

                                 "VALLESACCARDA",

                                 "VENTICANO",

                                 "VILLANOVA DEL BATTISTA",

                                 "VITULANO",

                                 "ZUNGOLI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI BENEVENTO')
            elif comune.nome in ["ANACAPRI",

                                 "BACOLI",

                                 "BARANO D'ISCHIA",

                                 "CAPRI",

                                 "CASAMICCIOLA TERME",

                                 "ERCOLANO",

                                 "FORIO",

                                 "ISCHIA",

                                 "LACCO AMENO",

                                 "MONTE DI PROCIDA",

                                 "NAPOLI",

                                 "PORTICI",

                                 "POZZUOLI",

                                 "PROCIDA",

                                 "QUARTO",

                                 "SAN GIORGIO A CREMANO",

                                 "SERRARA FONTANA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI NAPOLI')
            elif comune.nome in ["AFRAGOLA",

                                 "ARZANO",

                                 "AVERSA",

                                 "CAIVANO",

                                 "CALVIZZANO",

                                 "CARDITO",

                                 "CARINARO",

                                 "CASAL DI PRINCIPE",

                                 "CASALUCE",

                                 "CASANDRINO",

                                 "CASAPESENNA",

                                 "CASAVATORE",

                                 "CASORIA",

                                 "CESA",

                                 "CRISPANO",

                                 "FRATTAMAGGIORE",

                                 "FRATTAMINORE",

                                 "FRIGNANO",

                                 "GIUGLIANO IN CAMPANIA",

                                 "GRICIGNANO DI AVERSA",

                                 "GRUMO NEVANO",

                                 "LUSCIANO",

                                 "MARANO DI NAPOLI",

                                 "MELITO DI NAPOLI",

                                 "MUGNANO DI NAPOLI",

                                 "ORTA DI ATELLA",

                                 "PARETE",

                                 "QUALIANO",

                                 "SAN CIPRIANO D'AVERSA",

                                 "SAN MARCELLINO",

                                 "SANT'ANTIMO",

                                 "SANT'ARPINO",

                                 "SUCCIVO",

                                 "TEVEROLA",

                                 "TRENTOLA-DUCENTA",

                                 "VILLA DI BRIANO",

                                 "VILLA LITERNO",

                                 "VILLARICCA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI NAPOLI NORD in AVERSA')
            elif comune.nome in ["ACERRA",

                                 "BRUSCIANO",

                                 "CAMPOSANO",

                                 "CARBONARA DI NOLA",

                                 "CASALNUOVO DI NAPOLI",

                                 "CASAMARCIANO",

                                 "CASTELLO DI CISTERNA",

                                 "CERCOLA",

                                 "CICCIANO",

                                 "CIMITILE",

                                 "COMIZIANO",

                                 "LIVERI",

                                 "MARIGLIANELLA",

                                 "MARIGLIANO",

                                 "MASSA DI SOMMA",

                                 "NOLA",

                                 "OTTAVIANO",

                                 "PALMA CAMPANIA",

                                 "POLLENA TROCCHIA",

                                 "POMIGLIANO D'ARCO",

                                 "ROCCARAINOLA",

                                 "SAN GENNARO VESUVIANO",

                                 "SAN GIUSEPPE VESUVIANO",

                                 "SAN PAOLO BEL SITO",

                                 "SAN SEBASTIANO AL VESUVIO",

                                 "SAN VITALIANO",

                                 "SANT'ANASTASIA",

                                 "SAVIANO",

                                 "SCISCIANO",

                                 "SOMMA VESUVIANA",

                                 "TERZIGNO",

                                 "TUFINO",

                                 "VISCIANO",

                                 "VOLLA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI NOLA')
            elif comune.nome in ["AILANO",

                                 "ALIFE",

                                 "ALVIGNANO",

                                 "ARIENZO",

                                 "BAIA E LATINA",

                                 "BELLONA",

                                 "CAIANELLO",

                                 "CAIAZZO",

                                 "CALVI RISORTA",

                                 "CAMIGLIANO",

                                 "CANCELLO ED ARNONE",

                                 "CAPODRISE",

                                 "CAPRIATI A VOLTURNO",

                                 "CAPUA",

                                 "CARINOLA",

                                 "CASAGIOVE",

                                 "CASAPULLA",

                                 "CASERTA",

                                 "CASTEL CAMPAGNANO",

                                 "CASTEL DI SASSO",

                                 "CASTEL MORRONE",

                                 "CASTEL VOLTURNO",

                                 "CASTELLO DEL MATESE",

                                 "CELLOLE",

                                 "CERVINO",

                                 "CIORLANO",

                                 "CONCA DELLA CAMPANIA",

                                 "CURTI",

                                 "DRAGONI",

                                 "FALCIANO DEL MASSICO",

                                 "FONTEGRECA",

                                 "FORMICOLA",

                                 "FRANCOLISE",

                                 "GALLO MATESE",

                                 "GIANO VETUSTO",

                                 "GIOIA SANNITICA",

                                 "GRAZZANISE",

                                 "LETINO",

                                 "LIBERI",

                                 "MACERATA CAMPANIA",

                                 "MADDALONI",

                                 "MARCIANISE",

                                 "MARZANO APPIO",

                                 "MONDRAGONE",

                                 "PASTORANO",

                                 "PIANA DI MONTE VERNA",

                                 "PIEDIMONTE MATESE",

                                 "PIETRAMELARA",

                                 "PIETRAVAIRANO",

                                 "PIGNATARO MAGGIORE",

                                 "PONTELATONE",

                                 "PORTICO DI CASERTA",

                                 "PRATA SANNITA",

                                 "PRATELLA",

                                 "RAVISCANINA",

                                 "RECALE",

                                 "RIARDO",

                                 "ROCCAMONFINA",

                                 "ROCCAROMANA",

                                 "ROCCHETTA E CROCE",

                                 "RUVIANO",

                                 "SAN FELICE A CANCELLO",

                                 "SAN GREGORIO MATESE",

                                 "SAN MARCO EVANGELISTA",

                                 "SAN NICOLA LA STRADA",

                                 "SAN POTITO SANNITICO",

                                 "SAN PRISCO",

                                 "SAN TAMMARO",

                                 "SANTA MARIA A VICO",

                                 "SANTA MARIA CAPUA VETERE",

                                 "SANTA MARIA LA FOSSA",

                                 "SANT'ANGELO D'ALIFE",

                                 "SESSA AURUNCA",

                                 "SPARANISE",

                                 "TEANO",

                                 "TORA E PICCILLI",

                                 "VAIRANO PATENORA",

                                 "VALLE AGRICOLA",

                                 "VALLE DI MADDALONI",

                                 "VITULAZIO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI SANTA MARIA CAPUA VETERE')
            elif comune.nome in ["AGEROLA",

                                 "BOSCOREALE",

                                 "BOSCOTRECASE",

                                 "CASOLA DI NAPOLI",

                                 "CASTELLAMMARE DI STABIA",

                                 "GRAGNANO",

                                 "LETTERE",

                                 "MASSA LUBRENSE",

                                 "META",

                                 "PIANO DI SORRENTO",

                                 "PIMONTE",

                                 "POGGIOMARINO",

                                 "POMPEI",

                                 "SANTA MARIA LA CARITA'",

                                 "SANT'AGNELLO",

                                 "SANT'ANTONIO ABATE",

                                 "SORRENTO",

                                 "STRIANO",

                                 "TORRE ANNUNZIATA",

                                 "TORRE DEL GRECO",

                                 "TRECASE",

                                 "VICO EQUENSE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI TORRE ANNUNZIATA')
            elif comune.nome in ["AGRIGENTO",

                                 "ARAGONA",

                                 "CAMASTRA",

                                 "CAMMARATA",

                                 "CAMPOBELLO DI LICATA",

                                 "CANICATTI'",

                                 "CASTELTERMINI",

                                 "CASTROFILIPPO",

                                 "CATTOLICA ERACLEA",

                                 "COMITINI",

                                 "FAVARA",

                                 "GROTTE",

                                 "JOPPOLO GIANCAXIO",

                                 "LAMPEDUSA E LINOSA",

                                 "LICATA",

                                 "MONTALLEGRO",

                                 "NARO",

                                 "PALMA DI MONTECHIARO",

                                 "PORTO EMPEDOCLE",

                                 "RACALMUTO",

                                 "RAFFADALI",

                                 "RAVANUSA",

                                 "REALMONTE",

                                 "SAN BIAGIO PLATANI",

                                 "SAN GIOVANNI GEMINI",

                                 "SANTA ELISABETTA",

                                 "SANT'ANGELO MUXARO",

                                 "SICULIANA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI AGRIGENTO')
            elif comune.nome in ["CAMPOBELLO DI MAZARA",

                                 "CASTELVETRANO",

                                 "MARSALA",

                                 "MAZARA DEL VALLO",

                                 "PANTELLERIA",

                                 "PETROSINO",

                                 "SALEMI",

                                 "VITA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI MARSALA')
            elif comune.nome in ["ALTOFONTE",

                                 "BALESTRATE",

                                 "BORGETTO",

                                 "CAMPOREALE",

                                 "CAPACI",

                                 "CARINI",

                                 "CINISI",

                                 "GIARDINELLO",

                                 "ISOLA DELLE FEMMINE",

                                 "MONREALE",

                                 "MONTELEPRE",

                                 "PALERMO",

                                 "PARTINICO",

                                 "SAN CIPIRELLO",

                                 "SAN GIUSEPPE JATO",

                                 "TERRASINI",

                                 "TORRETTA",

                                 "TRAPPETO",

                                 "USTICA",

                                 "VILLABATE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PALERMO')
            elif comune.nome in ["ALESSANDRIA DELLA ROCCA",

                                 "BIVONA",

                                 "BURGIO",

                                 "CALAMONACI",

                                 "CALTABELLOTTA",

                                 "CIANCIANA",

                                 "GIBELLINA",

                                 "LUCCA SICULA",

                                 "MENFI",

                                 "MONTEVAGO",

                                 "PARTANNA",

                                 "POGGIOREALE",

                                 "RIBERA",

                                 "SALAPARUTA",

                                 "SAMBUCA DI SICILIA",

                                 "SANTA MARGHERITA DI BELICE",

                                 "SANTA NINFA",

                                 "SANTO STEFANO QUISQUINA",

                                 "SCIACCA",

                                 "VILLAFRANCA SICULA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI SCIACCA')
            elif comune.nome in ["ALIA",

                                 "ALIMENA",

                                 "ALIMINUSA",

                                 "ALTAVILLA MILICIA",

                                 "BAGHERIA",

                                 "BAUCINA",

                                 "BELMONTE MEZZAGNO",

                                 "BISACQUINO",

                                 "BLUFI",

                                 "BOLOGNETTA",

                                 "BOMPIETRO",

                                 "CACCAMO",

                                 "CALTAVUTURO",

                                 "CAMPOFELICE DI FITALIA",

                                 "CAMPOFELICE DI ROCCELLA",

                                 "CAMPOFIORITO",

                                 "CASTELBUONO",

                                 "CASTELDACCIA",

                                 "CASTELLANA SICULA",

                                 "CASTRONOVO DI SICILIA",

                                 "CEFALA' DIANA",

                                 "CEFALU'",

                                 "CERDA",

                                 "CHIUSA SCLAFANI",

                                 "CIMINNA",

                                 "COLLESANO",

                                 "CONTESSA ENTELLINA",

                                 "CORLEONE",

                                 "FICARAZZI",

                                 "GANGI",

                                 "GERACI SICULO",

                                 "GIULIANA",

                                 "GODRANO",

                                 "GRATTERI",

                                 "ISNELLO",

                                 "LASCARI",

                                 "LERCARA FRIDDI",

                                 "MARINEO",

                                 "MEZZOJUSO",

                                 "MISILMERI",

                                 "MONTEMAGGIORE BELSITO",

                                 "PALAZZO ADRIANO",

                                 "PETRALIA SOPRANA",

                                 "PETRALIA SOTTANA",

                                 "PIANA DEGLI ALBANESI",

                                 "POLIZZI GENEROSA",

                                 "POLLINA",

                                 "PRIZZI",

                                 "ROCCAMENA",

                                 "ROCCAPALUMBA",

                                 "SAN MAURO CASTELVERDE",

                                 "SANTA CRISTINA GELA",

                                 "SANTA FLAVIA",

                                 "SCIARA",

                                 "SCILLATO",

                                 "SCLAFANI BAGNI",

                                 "TERMINI IMERESE",

                                 "TRABIA",

                                 "VALLEDOLMO",

                                 "VENTIMIGLIA DI SICILIA",

                                 "VICARI",

                                 "VILLAFRATI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI TERMINI IMERESE')
            elif comune.nome in ["ALCAMO",

                                 "BUSETO PALIZZOLO",

                                 "CALATAFIMI-SEGESTA",

                                 "CASTELLAMMARE DEL GOLFO",

                                 "CUSTONACI",

                                 "ERICE",

                                 "FAVIGNANA",

                                 "PACECO",

                                 "SAN VITO LO CAPO",

                                 "TRAPANI",

                                 "VALDERICE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI TRAPANI')
            elif comune.nome in ["ASSISI",

                                 "BASTIA UMBRA",

                                 "BETTONA",

                                 "CASTIGLIONE DEL LAGO",

                                 "CITERNA",

                                 "CITTA' DI CASTELLO",

                                 "CORCIANO",

                                 "COSTACCIARO",

                                 "FOSSATO DI VICO",

                                 "GUALDO TADINO",

                                 "GUBBIO",

                                 "LISCIANO NICCONE",

                                 "MAGIONE",

                                 "MONTE SANTA MARIA TIBERINA",

                                 "MONTONE",

                                 "PANICALE",

                                 "PASSIGNANO SUL TRASIMENO",

                                 "PERUGIA",

                                 "PIETRALUNGA",

                                 "SAN GIUSTINO",

                                 "SCHEGGIA E PASCELUPO",

                                 "SIGILLO",

                                 "TORGIANO",

                                 "TUORO SUL TRASIMENO",

                                 "UMBERTIDE",

                                 "VALFABBRICA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PERUGIA')
            elif comune.nome in ["BEVAGNA",

                                 "CAMPELLO SUL CLITUNNO",

                                 "CANNARA",

                                 "CASCIA",

                                 "CASTEL RITALDI",

                                 "CERRETO DI SPOLETO",

                                 "COLLAZZONE",

                                 "DERUTA",

                                 "FOLIGNO",

                                 "FRATTA TODINA",

                                 "GIANO DELL'UMBRIA",

                                 "GUALDO CATTANEO",

                                 "MARSCIANO",

                                 "MASSA MARTANA",

                                 "MONTE CASTELLO DI VIBIO",

                                 "MONTEFALCO",

                                 "MONTELEONE DI SPOLETO",

                                 "NOCERA UMBRA",

                                 "NORCIA",

                                 "POGGIODOMO",

                                 "PRECI",

                                 "SANT'ANATOLIA DI NARCO",

                                 "SCHEGGINO",

                                 "SELLANO",

                                 "SPELLO",

                                 "SPOLETO",

                                 "TODI",

                                 "TREVI",

                                 "VALLO DI NERA",

                                 "VALTOPINA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI SPOLETO')
            elif comune.nome in ["ACQUASPARTA",

                                 "ALLERONA",

                                 "ALVIANO",

                                 "AMELIA",

                                 "ARRONE",

                                 "ATTIGLIANO",

                                 "AVIGLIANO UMBRO",

                                 "BASCHI",

                                 "CALVI DELL'UMBRIA",

                                 "CASTEL GIORGIO",

                                 "CASTEL VISCARDO",

                                 "CITTA' DELLA PIEVE",

                                 "FABRO",

                                 "FERENTILLO",

                                 "FICULLE",

                                 "GIOVE",

                                 "GUARDEA",

                                 "LUGNANO IN TEVERINA",

                                 "MONTECASTRILLI",

                                 "MONTECCHIO",

                                 "MONTEFRANCO",

                                 "MONTEGABBIONE",

                                 "MONTELEONE D'ORVIETO",

                                 "NARNI",

                                 "ORVIETO",

                                 "OTRICOLI",

                                 "PACIANO",

                                 "PARRANO",

                                 "PENNA IN TEVERINA",

                                 "PIEGARO",

                                 "POLINO",

                                 "PORANO",

                                 "SAN GEMINI",

                                 "SAN VENANZO",

                                 "STRONCONE",

                                 "TERNI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI TERNI')
            elif comune.nome in ["ATENA LUCANA",

                                 "AULETTA",

                                 "BUONABITACOLO",

                                 "CAGGIANO",

                                 "CALVERA",

                                 "CARBONE",

                                 "CASALBUONO",

                                 "CASALETTO SPARTANO",

                                 "CASELLE IN PITTARI",

                                 "CASTELLUCCIO INFERIORE",

                                 "CASTELLUCCIO SUPERIORE",

                                 "CASTELSARACENO",

                                 "CASTRONUOVO DI SANT'ANDREA",

                                 "CERSOSIMO",

                                 "CHIAROMONTE",

                                 "EPISCOPIA",

                                 "FARDELLA",

                                 "FRANCAVILLA IN SINNI",

                                 "GALLICCHIO",

                                 "ISPANI",

                                 "LAGONEGRO",

                                 "LATRONICO",

                                 "LAURIA",

                                 "MARATEA",

                                 "MISSANELLO",

                                 "MOLITERNO",

                                 "MONTE SAN GIACOMO",

                                 "MONTESANO SULLA MARCELLANA",

                                 "MORIGERATI",

                                 "NEMOLI",

                                 "NOEPOLI",

                                 "PADULA",

                                 "PERTOSA",

                                 "PETINA",

                                 "POLLA",

                                 "RIVELLO",

                                 "ROCCANOVA",

                                 "ROTONDA",

                                 "SALA CONSILINA",

                                 "SALVITELLE",

                                 "SAN CHIRICO RAPARO",

                                 "SAN COSTANTINO ALBANESE",

                                 "SAN MARTINO D'AGRI",

                                 "SAN PAOLO ALBANESE",

                                 "SAN PIETRO AL TANAGRO",

                                 "SAN RUFO",

                                 "SAN SEVERINO LUCANO",

                                 "SANTA MARINA",

                                 "SANT'ARCANGELO",

                                 "SANT'ARSENIO",

                                 "SANZA",

                                 "SAPRI",

                                 "SARCONI",

                                 "SASSANO",

                                 "SENISE",

                                 "SPINOSO",

                                 "TEANA",

                                 "TEGGIANO",

                                 "TERRANOVA DI POLLINO",

                                 "TORRACA",

                                 "TORTORELLA",

                                 "TRECCHINA",

                                 "VIBONATI",

                                 "VIGGIANELLO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI LAGONEGRO')
            elif comune.nome in ["ACCETTURA",

                                 "ALIANO",

                                 "BERNALDA",

                                 "CALCIANO",

                                 "CIRIGLIANO",

                                 "COLOBRARO",

                                 "CRACO",

                                 "FERRANDINA",

                                 "GARAGUSO",

                                 "GORGOGLIONE",

                                 "GRASSANO",

                                 "GROTTOLE",

                                 "IRSINA",

                                 "MATERA",

                                 "MIGLIONICO",

                                 "MONTALBANO JONICO",

                                 "MONTESCAGLIOSO",

                                 "NOVA SIRI",

                                 "OLIVETO LUCANO",

                                 "PISTICCI",

                                 "POLICORO",

                                 "POMARICO",

                                 "ROTONDELLA",

                                 "SALANDRA",

                                 "SAN GIORGIO LUCANO",

                                 "SAN MAURO FORTE",

                                 "SCANZANO JONICO",

                                 "STIGLIANO",

                                 "TRICARICO",

                                 "TURSI",

                                 "VALSINNI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI MATERA')
            elif comune.nome in ["ABRIOLA",

                                 "ACERENZA",

                                 "ALBANO DI LUCANIA",

                                 "ANZI",

                                 "ARMENTO",

                                 "ATELLA",

                                 "AVIGLIANO",

                                 "BALVANO",

                                 "BANZI",

                                 "BARAGIANO",

                                 "BARILE",

                                 "BELLA",

                                 "BRIENZA",

                                 "BRINDISI MONTAGNA",

                                 "CALVELLO",

                                 "CAMPOMAGGIORE",

                                 "CANCELLARA",

                                 "CASTELGRANDE",

                                 "CASTELMEZZANO",

                                 "CORLETO PERTICARA",

                                 "FILIANO",

                                 "FORENZA",

                                 "GENZANO DI LUCANIA",

                                 "GINESTRA",

                                 "GRUMENTO NOVA",

                                 "GUARDIA PERTICARA",

                                 "LAURENZANA",

                                 "LAVELLO",

                                 "MARSICO NUOVO",

                                 "MARSICOVETERE",

                                 "MASCHITO",

                                 "MELFI",

                                 "MONTEMILONE",

                                 "MONTEMURRO",

                                 "MURO LUCANO",

                                 "OPPIDO LUCANO",

                                 "PALAZZO SAN GERVASIO",

                                 "PATERNO",

                                 "PESCOPAGANO",

                                 "PICERNO",

                                 "PIETRAGALLA",

                                 "PIETRAPERTOSA",

                                 "PIGNOLA",

                                 "POTENZA",

                                 "RAPOLLA",

                                 "RAPONE",

                                 "RIONERO IN VULTURE",

                                 "RIPACANDIDA",

                                 "RUOTI",

                                 "RUVO DEL MONTE",

                                 "SAN CHIRICO NUOVO",

                                 "SAN FELE",

                                 "SANT'ANGELO LE FRATTE",

                                 "SASSO DI CASTALDA",

                                 "SATRIANO DI LUCANIA",

                                 "SAVOIA DI LUCANIA",

                                 "TITO",

                                 "TOLVE",

                                 "TRAMUTOLA",

                                 "TRIVIGNO",

                                 "VAGLIO BASILICATA",

                                 "VENOSA",

                                 "VIETRI DI POTENZA",

                                 "VIGGIANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI POTENZA')
            elif comune.nome in ["AGNANA CALABRA",

                                 "ANTONIMINA",

                                 "ARDORE",

                                 "BENESTARE",

                                 "BIANCO",

                                 "BIVONGI",

                                 "BOVALINO",

                                 "BRANCALEONE",

                                 "BRUZZANO ZEFFIRIO",

                                 "CAMINI",

                                 "CANOLO",

                                 "CARAFFA DEL BIANCO",

                                 "CARERI",

                                 "CASIGNANA",

                                 "CAULONIA",

                                 "CIMINA'",

                                 "FERRUZZANO",

                                 "GERACE",

                                 "GIOIOSA IONICA",

                                 "GROTTERIA",

                                 "LOCRI",

                                 "MAMMOLA",

                                 "MARINA DI GIOIOSA IONICA",

                                 "MARTONE",

                                 "MONASTERACE",

                                 "PALIZZI",

                                 "PAZZANO",

                                 "PLACANICA",

                                 "PLATI'",

                                 "PORTIGLIOLA",

                                 "RIACE",

                                 "ROCCELLA IONICA",

                                 "SAMO",

                                 "SAN GIOVANNI DI GERACE",

                                 "SAN LUCA",

                                 "SANT'AGATA DEL BIANCO",

                                 "SANT'ILARIO DELLO IONIO",

                                 "SIDERNO",

                                 "STAITI",

                                 "STIGNANO",

                                 "STILO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI LOCRI')
            elif comune.nome in ["ANOIA",

                                 "CANDIDONI",

                                 "CINQUEFRONDI",

                                 "CITTANOVA",

                                 "COSOLETO",

                                 "DELIANUOVA",

                                 "FEROLETO DELLA CHIESA",

                                 "GALATRO",

                                 "GIFFONE",

                                 "GIOIA TAURO",

                                 "LAUREANA DI BORRELLO",

                                 "MAROPATI",

                                 "MELICUCCA'",

                                 "MELICUCCO",

                                 "MOLOCHIO",

                                 "OPPIDO MAMERTINA",

                                 "PALMI",

                                 "POLISTENA",

                                 "RIZZICONI",

                                 "ROSARNO",

                                 "SAN FERDINANDO",

                                 "SAN GIORGIO MORGETO",

                                 "SAN PIETRO DI CARIDA'",

                                 "SAN PROCOPIO",

                                 "SANTA CRISTINA D'ASPROMONTE",

                                 "SANT'EUFEMIA D'ASPROMONTE",

                                 "SCIDO",

                                 "SEMINARA",

                                 "SERRATA",

                                 "SINOPOLI",

                                 "TAURIANOVA",

                                 "TERRANOVA SAPPO MINULIO",

                                 "VARAPODIO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PALMI')
            elif comune.nome in ["AFRICO",

                                 "BAGALADI",

                                 "BAGNARA CALABRA",

                                 "BOVA",

                                 "BOVA MARINA",

                                 "CALANNA",

                                 "CAMPO CALABRO",

                                 "CARDETO",

                                 "CONDOFURI",

                                 "FIUMARA",

                                 "LAGANADI",

                                 "MELITO DI PORTO SALVO",

                                 "MONTEBELLO IONICO",

                                 "MOTTA SAN GIOVANNI",

                                 "REGGIO DI CALABRIA",

                                 "ROCCAFORTE DEL GRECO",

                                 "ROGHUDI",

                                 "SAN LORENZO",

                                 "SAN ROBERTO",

                                 "SANT'ALESSIO IN ASPROMONTE",

                                 "SANTO STEFANO IN ASPROMONTE",

                                 "SCILLA",

                                 "VILLA SAN GIOVANNI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI REGGIO CALABRIA')
            elif comune.nome in ["ACQUAFONDATA",

                                 "ALVITO",

                                 "AQUINO",

                                 "ARCE",

                                 "ARPINO",

                                 "ATINA",

                                 "AUSONIA",

                                 "BELMONTE CASTELLO",

                                 "BROCCOSTELLA",

                                 "CAMPOLI APPENNINO",

                                 "CASALATTICO",

                                 "CASALVIERI",

                                 "CASSINO",

                                 "CASTELFORTE",

                                 "CASTELLIRI",

                                 "CASTELNUOVO PARANO",

                                 "CASTROCIELO",

                                 "CERVARO",

                                 "COLFELICE",

                                 "COLLE SAN MAGNO",

                                 "CORENO AUSONIO",

                                 "ESPERIA",

                                 "FONTANA LIRI",

                                 "FONTECHIARI",

                                 "FORMIA",

                                 "GAETA",

                                 "GALLINARO",

                                 "GALLUCCIO",

                                 "ISOLA DEL LIRI",

                                 "ITRI",

                                 "MIGNANO MONTE LUNGO",

                                 "MINTURNO",

                                 "PASTENA",

                                 "PESCOSOLIDO",

                                 "PICINISCO",

                                 "PICO",

                                 "PIEDIMONTE SAN GERMANO",

                                 "PIGNATARO INTERAMNA",

                                 "PONTECORVO",

                                 "PONZA",

                                 "POSTA FIBRENO",

                                 "PRESENZANO",

                                 "ROCCA D'ARCE",

                                 "ROCCA D'EVANDRO",

                                 "ROCCASECCA",

                                 "SAN BIAGIO SARACINISCO",

                                 "SAN DONATO VAL DI COMINO",

                                 "SAN GIORGIO A LIRI",

                                 "SAN GIOVANNI INCARICO",

                                 "SAN PIETRO INFINE",

                                 "SAN VITTORE DEL LAZIO",

                                 "SANT'AMBROGIO SUL GARIGLIANO",

                                 "SANT'ANDREA DEL GARIGLIANO",

                                 "SANT'APOLLINARE",

                                 "SANT'ELIA FIUMERAPIDO",

                                 "SANTI COSMA E DAMIANO",

                                 "SANTOPADRE",

                                 "SETTEFRATI",

                                 "SORA",

                                 "SPIGNO SATURNIA",

                                 "TERELLE",

                                 "VALLEMAIO",

                                 "VALLEROTONDA",

                                 "VENTOTENE",

                                 "VICALVI",

                                 "VILLA LATINA",

                                 "VILLA SANTA LUCIA",

                                 "VITICUSO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CASSINO')
            elif comune.nome in ["ALLUMIERE",

                                 "ANGUILLARA SABAZIA",

                                 "BRACCIANO",

                                 "CANALE MONTERANO",

                                 "CERVETERI",

                                 "CIVITAVECCHIA",

                                 "FIUMICINO",

                                 "LADISPOLI",

                                 "MANZIANA",

                                 "MONTALTO DI CASTRO",

                                 "SANTA MARINELLA",

                                 "TARQUINIA",

                                 "TOLFA",

                                 "TREVIGNANO ROMANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CIVITAVECCHIA')
            elif comune.nome in ["ACUTO",

                                 "ALATRI",

                                 "AMASENO",

                                 "ANAGNI",

                                 "ARNARA",

                                 "BOVILLE ERNICA",

                                 "CASTRO DEI VOLSCI",

                                 "CECCANO",

                                 "CEPRANO",

                                 "COLLEPARDO",

                                 "FALVATERRA",

                                 "FERENTINO",

                                 "FILETTINO",

                                 "FIUGGI",

                                 "FROSINONE",

                                 "FUMONE",

                                 "GIULIANO DI ROMA",

                                 "GUARCINO",

                                 "MONTE SAN GIOVANNI CAMPANO",

                                 "MOROLO",

                                 "PALIANO",

                                 "PATRICA",

                                 "PIGLIO",

                                 "POFI",

                                 "RIPI",

                                 "SERRONE",

                                 "SGURGOLA",

                                 "STRANGOLAGALLI",

                                 "SUPINO",

                                 "TORRE CAJETANI",

                                 "TORRICE",

                                 "TREVI NEL LAZIO",

                                 "TRIVIGLIANO",

                                 "VALLECORSA",

                                 "VEROLI",

                                 "VICO NEL LAZIO",

                                 "VILLA SANTO STEFANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI FROSINONE')
            elif comune.nome in ["APRILIA",

                                 "BASSIANO",

                                 "CAMPODIMELE",

                                 "CISTERNA DI LATINA",

                                 "CORI",

                                 "FONDI",

                                 "LATINA",

                                 "LENOLA",

                                 "MAENZA",

                                 "MONTE SAN BIAGIO",

                                 "NORMA",

                                 "PONTINIA",

                                 "PRIVERNO",

                                 "PROSSEDI",

                                 "ROCCA MASSIMA",

                                 "ROCCAGORGA",

                                 "ROCCASECCA DEI VOLSCI",

                                 "SABAUDIA",

                                 "SAN FELICE CIRCEO",

                                 "SERMONETA",

                                 "SEZZE",

                                 "SONNINO",

                                 "SPERLONGA",

                                 "TERRACINA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI LATINA')
            elif comune.nome in ["ACCUMOLI",

                                 "AMATRICE",

                                 "ANTRODOCO",

                                 "ASCREA",

                                 "BELMONTE IN SABINA",

                                 "BORBONA",

                                 "BORGO VELINO",

                                 "BORGOROSE",

                                 "CANTALICE",

                                 "CANTALUPO IN SABINA",

                                 "CASAPROTA",

                                 "CASPERIA",

                                 "CASTEL DI TORA",

                                 "CASTEL SANT'ANGELO",

                                 "CASTELNUOVO DI FARFA",

                                 "CITTADUCALE",

                                 "CITTAREALE",

                                 "COLLALTO SABINO",

                                 "COLLE DI TORA",

                                 "COLLEGIOVE",

                                 "COLLEVECCHIO",

                                 "COLLI SUL VELINO",

                                 "CONCERVIANO",

                                 "CONFIGNI",

                                 "CONTIGLIANO",

                                 "COTTANELLO",

                                 "FARA IN SABINA",

                                 "FIAMIGNANO",

                                 "FIANO ROMANO",

                                 "FILACCIANO",

                                 "FORANO",

                                 "FRASSO SABINO",

                                 "GRECCIO",

                                 "LABRO",

                                 "LEONESSA",

                                 "LONGONE SABINO",

                                 "MAGLIANO SABINA",

                                 "MARCETELLI",

                                 "MICIGLIANO",

                                 "MOMPEO",

                                 "MONTASOLA",

                                 "MONTE SAN GIOVANNI IN SABINA",

                                 "MONTEBUONO",

                                 "MONTELEONE SABINO",

                                 "MONTENERO SABINO",

                                 "MONTOPOLI DI SABINA",

                                 "MORRO REATINO",

                                 "NAZZANO",

                                 "ORVINIO",

                                 "PAGANICO SABINO",

                                 "PESCOROCCHIANO",

                                 "PETRELLA SALTO",

                                 "POGGIO BUSTONE",

                                 "POGGIO CATINO",

                                 "POGGIO MIRTETO",

                                 "POGGIO MOIANO",

                                 "POGGIO NATIVO",

                                 "POGGIO SAN LORENZO",

                                 "PONZANO ROMANO",

                                 "POSTA",

                                 "POZZAGLIA SABINA",

                                 "RIETI",

                                 "RIVODUTRI",

                                 "ROCCA SINIBALDA",

                                 "ROCCANTICA",

                                 "SALISANO",

                                 "SCANDRIGLIA",

                                 "SELCI",

                                 "STIMIGLIANO",

                                 "TARANO",

                                 "TOFFIA",

                                 "TORRI IN SABINA",

                                 "TORRICELLA IN SABINA",

                                 "TORRITA TIBERINA",

                                 "VACONE",

                                 "VARCO SABINO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI RIETI')
            elif comune.nome in ["ROMA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI ROMA')
            elif comune.nome in ["AFFILE",

                                 "AGOSTA",

                                 "ANTICOLI CORRADO",

                                 "ARCINAZZO ROMANO",

                                 "ARSOLI",

                                 "BELLEGRA",

                                 "CAMERATA NUOVA",

                                 "CAMPAGNANO DI ROMA",

                                 "CANTERANO",

                                 "CAPENA",

                                 "CAPRANICA PRENESTINA",

                                 "CASAPE",

                                 "CASTEL MADAMA",

                                 "CASTEL SAN PIETRO ROMANO",

                                 "CASTELNUOVO DI PORTO",

                                 "CAVE",

                                 "CERRETO LAZIALE",

                                 "CERVARA DI ROMA",

                                 "CICILIANO",

                                 "CINETO ROMANO",

                                 "CIVITELLA SAN PAOLO",

                                 "FONTE NUOVA",

                                 "FORMELLO",

                                 "GALLICANO NEL LAZIO",

                                 "GENAZZANO",

                                 "GERANO",

                                 "GUIDONIA MONTECELIO",

                                 "JENNE",

                                 "LICENZA",

                                 "MAGLIANO ROMANO",

                                 "MANDELA",

                                 "MARANO EQUO",

                                 "MARCELLINA",

                                 "MAZZANO ROMANO",

                                 "MENTANA",

                                 "MONTEFLAVIO",

                                 "MONTELIBRETTI",

                                 "MONTEROTONDO",

                                 "MONTORIO ROMANO",

                                 "MORICONE",

                                 "MORLUPO",

                                 "NEROLA",

                                 "NESPOLO",

                                 "OLEVANO ROMANO",

                                 "PALESTRINA",

                                 "PALOMBARA SABINA",

                                 "PERCILE",

                                 "PISONIANO",

                                 "POLI",

                                 "RIANO",

                                 "RIGNANO FLAMINIO",

                                 "RIOFREDDO",

                                 "ROCCA CANTERANO",

                                 "ROCCA DI CAVE",

                                 "ROCCA SANTO STEFANO",

                                 "ROCCAGIOVINE",

                                 "ROIATE",

                                 "ROVIANO",

                                 "SACROFANO",

                                 "SAMBUCI",

                                 "SAN CESAREO",

                                 "SAN GREGORIO DA SASSOLA",

                                 "SAN POLO DEI CAVALIERI",

                                 "SAN VITO ROMANO",

                                 "SANT'ANGELO ROMANO",

                                 "SANT'ORESTE",

                                 "SARACINESCO",

                                 "SUBIACO",

                                 "TIVOLI",

                                 "TURANIA",

                                 "VALLEPIETRA",

                                 "VALLINFREDA",

                                 "VICOVARO",

                                 "VIVARO ROMANO",

                                 "ZAGAROLO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI TIVOLI')
            elif comune.nome in ["ALBANO LAZIALE",

                                 "ANZIO",

                                 "ARDEA",

                                 "ARICCIA",

                                 "ARTENA",

                                 "CARPINETO ROMANO",

                                 "CASTEL GANDOLFO",

                                 "CIAMPINO",

                                 "COLLEFERRO",

                                 "COLONNA",

                                 "FRASCATI",

                                 "GAVIGNANO",

                                 "GENZANO DI ROMA",

                                 "GORGA",

                                 "GROTTAFERRATA",

                                 "LABICO",

                                 "LANUVIO",

                                 "LARIANO",

                                 "MARINO",

                                 "MONTE COMPATRI",

                                 "MONTE PORZIO CATONE",

                                 "MONTELANICO",

                                 "NEMI",

                                 "NETTUNO",

                                 "POMEZIA",

                                 "ROCCA DI PAPA",

                                 "ROCCA PRIORA",

                                 "SEGNI",

                                 "VALMONTONE",

                                 "VELLETRI"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI VELLETRI')
            elif comune.nome in ["ACQUAPENDENTE",

                                 "ARLENA DI CASTRO",

                                 "BAGNOREGIO",

                                 "BARBARANO ROMANO",

                                 "BASSANO IN TEVERINA",

                                 "BASSANO ROMANO",

                                 "BLERA",

                                 "BOLSENA",

                                 "BOMARZO",

                                 "CALCATA",

                                 "CANEPINA",

                                 "CANINO",

                                 "CAPODIMONTE",

                                 "CAPRANICA",

                                 "CAPRAROLA",

                                 "CARBOGNANO",

                                 "CASTEL SANT'ELIA",

                                 "CASTIGLIONE IN TEVERINA",

                                 "CELLENO",

                                 "CELLERE",

                                 "CIVITA CASTELLANA",

                                 "CIVITELLA D'AGLIANO",

                                 "CORCHIANO",

                                 "FABRICA DI ROMA",

                                 "FALERIA",

                                 "FARNESE",

                                 "GALLESE",

                                 "GRADOLI",

                                 "GRAFFIGNANO",

                                 "GROTTE DI CASTRO",

                                 "ISCHIA DI CASTRO",

                                 "LATERA",

                                 "LUBRIANO",

                                 "MARTA",

                                 "MONTE ROMANO",

                                 "MONTEFIASCONE",

                                 "MONTEROSI",

                                 "NEPI",

                                 "ONANO",

                                 "ORIOLO ROMANO",

                                 "ORTE",

                                 "PIANSANO",

                                 "PROCENO",

                                 "RONCIGLIONE",

                                 "SAN LORENZO NUOVO",

                                 "SORIANO NEL CIMINO",

                                 "SUTRI",

                                 "TESSENNANO",

                                 "TUSCANIA",

                                 "VALENTANO",

                                 "VALLERANO",

                                 "VASANELLO",

                                 "VEJANO",

                                 "VETRALLA",

                                 "VIGNANELLO",

                                 "VILLA SAN GIOVANNI IN TUSCIA",

                                 "VITERBO",

                                 "VITORCHIANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI VITERBO')
            elif comune.nome in ["ANGRI",

                                 "BARONISSI",

                                 "BRACIGLIANO",

                                 "CALVANICO",

                                 "CASTEL SAN GIORGIO",

                                 "CAVA DE' TIRRENI",

                                 "CORBARA",

                                 "FISCIANO",

                                 "MERCATO SAN SEVERINO",

                                 "NOCERA INFERIORE",

                                 "NOCERA SUPERIORE",

                                 "PAGANI",

                                 "ROCCAPIEMONTE",

                                 "SAN MARZANO SUL SARNO",

                                 "SAN VALENTINO TORIO",

                                 "SANT'EGIDIO DEL MONTE ALBINO",

                                 "SARNO",

                                 "SCAFATI",

                                 "SIANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI NOCERA INFERIORE')
            elif comune.nome in ["ACERNO",

                                 "ALBANELLA",

                                 "ALTAVILLA SILENTINA",

                                 "AMALFI",

                                 "AQUARA",

                                 "ATRANI",

                                 "BATTIPAGLIA",

                                 "BELLIZZI",

                                 "BELLOSGUARDO",

                                 "BUCCINO",

                                 "CAMPAGNA",

                                 "CAPACCIO",

                                 "CASTEL SAN LORENZO",

                                 "CASTELCIVITA",

                                 "CASTELNUOVO DI CONZA",

                                 "CASTIGLIONE DEL GENOVESI",

                                 "CETARA",

                                 "COLLIANO",

                                 "CONCA DEI MARINI",

                                 "CONTRONE",

                                 "CONTURSI TERME",

                                 "CORLETO MONFORTE",

                                 "EBOLI",

                                 "FELITTO",

                                 "FURORE",

                                 "GIFFONI SEI CASALI",

                                 "GIFFONI VALLE PIANA",

                                 "GIUNGANO",

                                 "LAVIANO",

                                 "MAIORI",

                                 "MINORI",

                                 "MONTECORVINO PUGLIANO",

                                 "MONTECORVINO ROVELLA",

                                 "OLEVANO SUL TUSCIANO",

                                 "OLIVETO CITRA",

                                 "OTTATI",

                                 "PALOMONTE",

                                 "PELLEZZANO",

                                 "PONTECAGNANO FAIANO",

                                 "POSITANO",

                                 "POSTIGLIONE",

                                 "PRAIANO",

                                 "RAVELLO",

                                 "RICIGLIANO",

                                 "ROCCADASPIDE",

                                 "ROMAGNANO AL MONTE",

                                 "ROSCIGNO",

                                 "SALERNO",

                                 "SAN CIPRIANO PICENTINO",

                                 "SAN GREGORIO MAGNO",

                                 "SAN MANGO PIEMONTE",

                                 "SANT'ANGELO A FASANELLA",

                                 "SANTOMENNA",

                                 "SCALA",

                                 "SERRE",

                                 "SICIGNANO DEGLI ALBURNI",

                                 "TRAMONTI",

                                 "TRENTINARA",

                                 "VALVA",

                                 "VIETRI SUL MARE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI SALERNO')
            elif comune.nome in ["AGROPOLI",

                                 "ALFANO",

                                 "ASCEA",

                                 "CAMEROTA",

                                 "CAMPORA",

                                 "CANNALONGA",

                                 "CASAL VELINO",

                                 "CASTELLABATE",

                                 "CASTELNUOVO CILENTO",

                                 "CELLE DI BULGHERIA",

                                 "CENTOLA",

                                 "CERASO",

                                 "CICERALE",

                                 "CUCCARO VETERE",

                                 "FUTANI",

                                 "GIOI",

                                 "LAUREANA CILENTO",

                                 "LAURINO",

                                 "LAURITO",

                                 "LUSTRA",

                                 "MAGLIANO VETERE",

                                 "MOIO DELLA CIVITELLA",

                                 "MONTANO ANTILIA",

                                 "MONTECORICE",

                                 "MONTEFORTE CILENTO",

                                 "NOVI VELIA",

                                 "OGLIASTRO CILENTO",

                                 "OMIGNANO",

                                 "ORRIA",

                                 "PERDIFUMO",

                                 "PERITO",

                                 "PIAGGINE",

                                 "PISCIOTTA",

                                 "POLLICA",

                                 "PRIGNANO CILENTO",

                                 "ROCCAGLORIOSA",

                                 "ROFRANO",

                                 "RUTINO",

                                 "SACCO",

                                 "SALENTO",

                                 "SAN GIOVANNI A PIRO",

                                 "SAN MAURO CILENTO",

                                 "SAN MAURO LA BRUCA",

                                 "SERRAMEZZANA",

                                 "SESSA CILENTO",

                                 "STELLA CILENTO",

                                 "STIO",

                                 "TORCHIARA",

                                 "TORRE ORSAIA",

                                 "VALLE DELL'ANGELO",

                                 "VALLO DELLA LUCANIA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI VALLO DELLA LUCANIA')
            elif comune.nome in ["ANELA",

                                 "BENETUTTI",

                                 "BITTI",

                                 "BONO",

                                 "BOTTIDDA",

                                 "BUDONI",

                                 "BULTEI",

                                 "BURGOS",

                                 "DORGALI",

                                 "ESPORLATU",

                                 "FONNI",

                                 "GALTELLI'",

                                 "GAVOI",

                                 "ILLORAI",

                                 "IRGOLI",

                                 "LOCULI",

                                 "LODE'",

                                 "LODINE",

                                 "LULA",

                                 "MAMOIADA",

                                 "NULE",

                                 "NUORO",

                                 "OLIENA",

                                 "OLLOLAI",

                                 "OLZAI",

                                 "ONANI'",

                                 "ONIFAI",

                                 "ONIFERI",

                                 "ORANI",

                                 "ORGOSOLO",

                                 "OROSEI",

                                 "OROTELLI",

                                 "ORUNE",

                                 "OSIDDA",

                                 "OTTANA",

                                 "OVODDA",

                                 "POSADA",

                                 "SAN TEODORO",

                                 "SARULE",

                                 "SINISCOLA",

                                 "TORPE'"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI NUORO')
            elif comune.nome in ["ALA' DEI SARDI",

                                 "ALGHERO",

                                 "ARDARA",

                                 "BANARI",

                                 "BESSUDE",

                                 "BONNANARO",

                                 "BONORVA",

                                 "BORUTTA",

                                 "BUDDUSO'",

                                 "BULZI",

                                 "CARGEGHE",

                                 "CASTELSARDO",

                                 "CHEREMULE",

                                 "CHIARAMONTI",

                                 "CODRONGIANOS",

                                 "COSSOINE",

                                 "FLORINAS",

                                 "GIAVE",

                                 "ITTIREDDU",

                                 "ITTIRI",

                                 "LAERRU",

                                 "MARA",

                                 "MARTIS",

                                 "MONTELEONE ROCCA DORIA",

                                 "MORES",

                                 "MUROS",

                                 "NUGHEDU SAN NICOLO'",

                                 "NULVI",

                                 "OLMEDO",

                                 "OSCHIRI",

                                 "OSILO",

                                 "OSSI",

                                 "OZIERI",

                                 "PADRIA",

                                 "PADRU",

                                 "PATTADA",

                                 "PLOAGHE",

                                 "PORTO TORRES",

                                 "POZZOMAGGIORE",

                                 "PUTIFIGARI",

                                 "ROMANA",

                                 "SANTA MARIA COGHINAS",

                                 "SASSARI",

                                 "SEDINI",

                                 "SEMESTENE",

                                 "SENNORI",

                                 "SILIGO",

                                 "SORSO",

                                 "STINTINO",

                                 "TERGU",

                                 "THIESI",

                                 "TISSI",

                                 "TORRALBA",

                                 "TULA",

                                 "URI",

                                 "USINI",

                                 "VALLEDORIA",

                                 "VILLANOVA MONTELEONE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI SASSARI')
            elif comune.nome in ["AGGIUS",

                                 "AGLIENTU",

                                 "ARZACHENA",

                                 "BADESI",

                                 "BERCHIDDA",

                                 "BORTIGIADAS",

                                 "CALANGIANUS",

                                 "ERULA",

                                 "GOLFO ARANCI",

                                 "LA MADDALENA",

                                 "LOIRI PORTO SAN PAOLO",

                                 "LUOGOSANTO",

                                 "LURAS",

                                 "MONTI",

                                 "OLBIA",

                                 "PALAU",

                                 "PERFUGAS",

                                 "SANTA TERESA GALLURA",

                                 "SANT'ANTONIO DI GALLURA",

                                 "TELTI",

                                 "TEMPIO PAUSANIA",

                                 "TRINITA' D'AGULTU E VIGNOLA",

                                 "VIDDALBA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI TEMPIO PAUSANIA')
            elif comune.nome in ["AVETRANA",

                                 "CAROSINO",

                                 "CASTELLANETA",

                                 "CRISPIANO",

                                 "FAGGIANO",

                                 "FRAGAGNANO",

                                 "GINOSA",

                                 "GROTTAGLIE",

                                 "LATERZA",

                                 "LEPORANO",

                                 "LIZZANO",

                                 "MANDURIA",

                                 "MARTINA FRANCA",

                                 "MARUGGIO",

                                 "MASSAFRA",

                                 "MONTEIASI",

                                 "MONTEMESOLA",

                                 "MONTEPARANO",

                                 "MOTTOLA",

                                 "PALAGIANELLO",

                                 "PALAGIANO",

                                 "PULSANO",

                                 "ROCCAFORZATA",

                                 "SAN GIORGIO IONICO",

                                 "SAN MARZANO DI SAN GIUSEPPE",

                                 "SAVA",

                                 "STATTE",

                                 "TARANTO",

                                 "TORRICELLA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI TARANTO')
            elif comune.nome in ["ACQUI TERME",

                                 "ALBERA LIGURE",

                                 "ALESSANDRIA",

                                 "ALICE BEL COLLE",

                                 "ALLUVIONI CAMBIO'",

                                 "ALZANO SCRIVIA",

                                 "ARQUATA SCRIVIA",

                                 "AVOLASCA",

                                 "BASALUZZO",

                                 "BASSIGNANA",

                                 "BELFORTE MONFERRATO",

                                 "BERGAMASCO",

                                 "BERZANO DI TORTONA",

                                 "BISTAGNO",

                                 "BORGHETTO DI BORBERA",

                                 "BORGORATTO ALESSANDRINO",

                                 "BOSCO MARENGO",

                                 "BOSIO",

                                 "BRIGNANO-FRASCATA",

                                 "BRUNO",

                                 "BUBBIO",

                                 "CABELLA LIGURE",

                                 "CALAMANDRANA",

                                 "CANTALUPO LIGURE",

                                 "CAPRIATA D'ORBA",

                                 "CARBONARA SCRIVIA",

                                 "CARENTINO",

                                 "CAREZZANO",

                                 "CARPENETO",

                                 "CARREGA LIGURE",

                                 "CARROSIO",

                                 "CARTOSIO",

                                 "CASAL CERMELLI",

                                 "CASALEGGIO BOIRO",

                                 "CASALNOCETO",

                                 "CASASCO",

                                 "CASSANO SPINOLA",

                                 "CASSINE",

                                 "CASSINELLE",

                                 "CASTEL BOGLIONE",

                                 "CASTEL ROCCHERO",

                                 "CASTELLANIA",

                                 "CASTELLAR GUIDOBONO",

                                 "CASTELLAZZO BORMIDA",

                                 "CASTELLETTO D'ERRO",

                                 "CASTELLETTO D'ORBA",

                                 "CASTELLETTO MOLINA",

                                 "CASTELLETTO MONFERRATO",

                                 "CASTELNUOVO BELBO",

                                 "CASTELNUOVO BORMIDA",

                                 "CASTELNUOVO SCRIVIA",

                                 "CASTELSPINA",

                                 "CAVATORE",

                                 "CERRETO GRUE",

                                 "CESSOLE",

                                 "CORTIGLIONE",

                                 "COSTA VESCOVATO",

                                 "CREMOLINO",

                                 "DENICE",

                                 "DERNICE",

                                 "FABBRICA CURONE",

                                 "FELIZZANO",

                                 "FONTANILE",

                                 "FRACONALTO",

                                 "FRANCAVILLA BISIO",

                                 "FRASCARO",

                                 "FRESONARA",

                                 "FRUGAROLO",

                                 "GAMALERO",

                                 "GARBAGNA",

                                 "GAVAZZANA",

                                 "GAVI",

                                 "GREMIASCO",

                                 "GROGNARDO",

                                 "GRONDONA",

                                 "GUAZZORA",

                                 "INCISA SCAPACCINO",

                                 "ISOLA SANT'ANTONIO",

                                 "LERMA",

                                 "LU",

                                 "MALVICINO",

                                 "MARANZANA",

                                 "MASIO",

                                 "MELAZZO",

                                 "MERANA",

                                 "MOLARE",

                                 "MOLINO DEI TORTI",

                                 "MOMBALDONE",

                                 "MOMBARUZZO",

                                 "MOMPERONE",

                                 "MONASTERO BORMIDA",

                                 "MONGIARDINO LIGURE",

                                 "MONLEALE",

                                 "MONTABONE",

                                 "MONTACUTO",

                                 "MONTALDEO",

                                 "MONTALDO BORMIDA",

                                 "MONTECASTELLO",

                                 "MONTECHIARO D'ACQUI",

                                 "MONTEGIOCO",

                                 "MONTEMARZINO",

                                 "MORBELLO",

                                 "MORNESE",

                                 "MORSASCO",

                                 "NIZZA MONFERRATO",

                                 "NOVI LIGURE",

                                 "OLMO GENTILE",

                                 "ORSARA BORMIDA",

                                 "OVADA",

                                 "OVIGLIO",

                                 "PADERNA",

                                 "PARETO",

                                 "PARODI LIGURE",

                                 "PASTURANA",

                                 "PECETTO DI VALENZA",

                                 "PIETRA MARAZZI",

                                 "PIOVERA",

                                 "PONTECURONE",

                                 "PONTI",

                                 "PONZONE",

                                 "POZZOL GROPPO",

                                 "POZZOLO FORMIGARO",

                                 "PRASCO",

                                 "PREDOSA",

                                 "QUARANTI",

                                 "QUARGNENTO",

                                 "QUATTORDIO",

                                 "RICALDONE",

                                 "RIVALTA BORMIDA",

                                 "RIVARONE",

                                 "ROCCA GRIMALDA",

                                 "ROCCAFORTE LIGURE",

                                 "ROCCAVERANO",

                                 "ROCCHETTA LIGURE",

                                 "ROCCHETTA PALAFEA",

                                 "SALE",

                                 "SAN CRISTOFORO",

                                 "SAN GIORGIO SCARAMPI",

                                 "SAN SALVATORE MONFERRATO",

                                 "SAN SEBASTIANO CURONE",

                                 "SANT'AGATA FOSSILI",

                                 "SARDIGLIANO",

                                 "SAREZZANO",

                                 "SEROLE",

                                 "SERRAVALLE SCRIVIA",

                                 "SESSAME",

                                 "SEZZADIO",

                                 "SILVANO D'ORBA",

                                 "SOLERO",

                                 "SPIGNO MONFERRATO",

                                 "SPINETO SCRIVIA",

                                 "STAZZANO",

                                 "STREVI",

                                 "TAGLIOLO MONFERRATO",

                                 "TASSAROLO",

                                 "TERZO",

                                 "TORTONA",

                                 "TRISOBBIO",

                                 "VAGLIO SERRA",

                                 "VALENZA",

                                 "VESIME",

                                 "VIGNOLE BORBERA",

                                 "VIGUZZOLO",

                                 "VILLALVERNIA",

                                 "VILLAROMAGNANO",

                                 "VISONE",

                                 "VOLPEDO",

                                 "VOLPEGLINO",

                                 "VOLTAGGIO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI ALESSANDRIA')
            elif comune.nome in ["ALLEIN",

                                 "ANTEY-SAINT-ANDRE'",

                                 "AOSTA",

                                 "ARNAD",

                                 "ARVIER",

                                 "AVISE",

                                 "AYAS",

                                 "AYMAVILLES",

                                 "BARD",

                                 "BIONAZ",

                                 "BRISSOGNE",

                                 "BRUSSON",

                                 "CHALLAND-SAINT-ANSELME",

                                 "CHALLAND-SAINT-VICTOR",

                                 "CHAMBAVE",

                                 "CHAMOIS",

                                 "CHAMPDEPRAZ",

                                 "CHAMPORCHER",

                                 "CHARVENSOD",

                                 "CHÂTILLON",

                                 "COGNE",

                                 "COURMAYEUR",

                                 "DONNAS",

                                 "DOUES",

                                 "EMARESE",

                                 "ETROUBLES",

                                 "FENIS",

                                 "FONTAINEMORE",

                                 "GABY",

                                 "GIGNOD",

                                 "GRESSAN",

                                 "GRESSONEY-LA-TRINITE'",

                                 "GRESSONEY-SAINT-JEAN",

                                 "HÔNE",

                                 "INTROD",

                                 "ISSIME",

                                 "ISSOGNE",

                                 "JOVENÇAN",

                                 "LA MAGDELEINE",

                                 "LA SALLE",

                                 "LA THUILE",

                                 "LILLIANES",

                                 "MONTJOVET",

                                 "MORGEX",

                                 "NUS",

                                 "OLLOMONT",

                                 "OYACE",

                                 "PERLOZ",

                                 "POLLEIN",

                                 "PONTBOSET",

                                 "PONTEY",

                                 "PONT-SAINTMARTIN",

                                 "PRE-SAINT-DIDIER",

                                 "QUART",

                                 "RHÊMES-NOTRE-DAME",

                                 "RHÊMES-SAINT-GEORGES",

                                 "ROISAN",

                                 "SAINT-CHRISTOPHE",

                                 "SAINT-DENIS",

                                 "SAINT-MARCEL",

                                 "SAINT-NICOLAS",

                                 "SAINT-OYEN",

                                 "SAINT-PIERRE",

                                 "SAINT-RHEMY-EN-BOSSES",

                                 "SAINT-VINCENT",

                                 "SARRE",

                                 "TORGNON",

                                 "VALGRISENCHE",

                                 "VALPELLINE",

                                 "VALSAVARENCHE",

                                 "VALTOURNENCHE",

                                 "VERRAYES",

                                 "VERRES",

                                 "VILLENEUVE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI AOSTA')
            elif comune.nome in ["AGLIANO TERME",

                                 "ALBA",

                                 "ALBARETTO DELLA TORRE",

                                 "ALBUGNANO",

                                 "ANTIGNANO",

                                 "ARAMENGO",

                                 "ARGUELLO",

                                 "ASTI",

                                 "AZZANO D'ASTI",

                                 "BALDICHIERI D'ASTI",

                                 "BALDISSERO D'ALBA",

                                 "BARBARESCO",

                                 "BAROLO",

                                 "BELVEGLIO",

                                 "BENEVELLO",

                                 "BERGOLO",

                                 "BERZANO DI SAN PIETRO",

                                 "BORGOMALE",

                                 "BOSIA",

                                 "BOSSOLASCO",

                                 "BRA",

                                 "BUTTIGLIERA D'ASTI",

                                 "CALOSSO",

                                 "CAMERANO CASASCO",

                                 "CAMO",

                                 "CANALE",

                                 "CANELLI",

                                 "CANTARANA",

                                 "CAPRIGLIO",

                                 "CARMAGNOLA",

                                 "CASORZO",

                                 "CASSINASCO",

                                 "CASTAGNITO",

                                 "CASTAGNOLE DELLE LANZE",

                                 "CASTAGNOLE MONFERRATO",

                                 "CASTELL'ALFERO",

                                 "CASTELLERO",

                                 "CASTELLETTO UZZONE",

                                 "CASTELLINALDO",

                                 "CASTELLO DI ANNONE",

                                 "CASTELNUOVO CALCEA",

                                 "CASTELNUOVO DON BOSCO",

                                 "CASTIGLIONE FALLETTO",

                                 "CASTIGLIONE TINELLA",

                                 "CASTINO",

                                 "CELLARENGO",

                                 "CELLE ENOMONDO",

                                 "CERESOLE ALBA",

                                 "CERRETO D'ASTI",

                                 "CERRETTO LANGHE",

                                 "CERRO TANARO",

                                 "CERVERE",

                                 "CHERASCO",

                                 "CHIUSANO D'ASTI",

                                 "CINAGLIO",

                                 "CISSONE",

                                 "CISTERNA D'ASTI",

                                 "COAZZOLO",

                                 "COCCONATO",

                                 "CORNELIANO D'ALBA",

                                 "CORSIONE",

                                 "CORTANDONE",

                                 "CORTANZE",

                                 "CORTAZZONE",

                                 "CORTEMILIA",

                                 "COSSANO BELBO",

                                 "COSSOMBRATO",

                                 "COSTIGLIOLE D'ASTI",

                                 "CRAVANZANA",

                                 "CUNICO",

                                 "DIANO D'ALBA",

                                 "DUSINO SAN MICHELE",

                                 "FEISOGLIO",

                                 "FERRERE",

                                 "FRINCO",

                                 "GORZEGNO",

                                 "GOVONE",

                                 "GRANA",

                                 "GRINZANE CAVOUR",

                                 "GUARENE",

                                 "ISOLA D'ASTI",

                                 "ISOLABELLA",

                                 "LA MORRA",

                                 "LEQUIO BERRIA",

                                 "LEVICE",

                                 "LOAZZOLO",

                                 "MAGLIANO ALFIERI",

                                 "MANGO",

                                 "MARETTO",

                                 "MOASCA",

                                 "MOMBERCELLI",

                                 "MONALE",

                                 "MONCUCCO TORINESE",

                                 "MONFORTE D'ALBA",

                                 "MONGARDINO",

                                 "MONTA'",

                                 "MONTAFIA",

                                 "MONTALDO ROERO",

                                 "MONTALDO SCARAMPI",

                                 "MONTECHIARO D'ASTI",

                                 "MONTEGROSSO D'ASTI",

                                 "MONTELUPO ALBESE",

                                 "MONTEMAGNO",

                                 "MONTEU ROERO",

                                 "MONTICELLO D'ALBA",

                                 "MONTIGLIO MONFERRATO",

                                 "MORANSENGO",

                                 "NARZOLE",

                                 "NEIVE",

                                 "NEVIGLIE",

                                 "NIELLA BELBO",

                                 "NOVELLO",

                                 "PASSERANO MARMORITO",

                                 "PERLETTO",

                                 "PEZZOLO VALLE UZZONE",

                                 "PIEA",

                                 "PINO D'ASTI",

                                 "PIOBESI D'ALBA",

                                 "PIOVA' MASSAIA",

                                 "POCAPAGLIA",

                                 "POIRINO",

                                 "PORTACOMARO",

                                 "PRALORMO",

                                 "PRIOCCA",

                                 "REFRANCORE",

                                 "REVIGLIASCO D'ASTI",

                                 "ROATTO",

                                 "ROBELLA",

                                 "ROCCA D'ARAZZO",

                                 "ROCCHETTA BELBO",

                                 "ROCCHETTA TANARO",

                                 "RODDI",

                                 "RODDINO",

                                 "RODELLO",

                                 "SAN BENEDETTO BELBO",

                                 "SAN DAMIANO D'ASTI",

                                 "SAN MARTINO ALFIERI",

                                 "SAN MARZANO OLIVETO",

                                 "SAN PAOLO SOLBRITO",

                                 "SANFRE'",

                                 "SANTA VITTORIA D'ALBA",

                                 "SANTO STEFANO BELBO",

                                 "SANTO STEFANO ROERO",

                                 "SCURZOLENGO",

                                 "SERRALUNGA D'ALBA",

                                 "SERRAVALLE LANGHE",

                                 "SETTIME",

                                 "SINIO",

                                 "SOGLIO",

                                 "SOMMARIVA DEL BOSCO",

                                 "SOMMARIVA PERNO",

                                 "TIGLIOLE",

                                 "TONENGO",

                                 "TORRE BORMIDA",

                                 "TREISO",

                                 "TREZZO TINELLA",

                                 "VALFENERA",

                                 "VERDUNO",

                                 "VEZZA D'ALBA",

                                 "VIALE",

                                 "VIARIGI",

                                 "VIGLIANO D'ASTI",

                                 "VILLA SAN SECONDO",

                                 "VILLAFRANCA D'ASTI",

                                 "VILLANOVA D'ASTI",

                                 "VINCHIO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI ASTI')
            elif comune.nome in ["ANDORNO MICCA",

                                 "BENNA",

                                 "BIELLA",

                                 "BIOGLIO",

                                 "BORRIANA",

                                 "BRUSNENGO",

                                 "CALLABIANA",

                                 "CAMANDONA",

                                 "CAMBURZANO",

                                 "CAMPIGLIA CERVO",

                                 "CANDELO",

                                 "CASAPINTA",

                                 "CASTELLETTO CERVO",

                                 "CAVAGLIA'",

                                 "CERRETO CASTELLO",

                                 "CERRIONE",

                                 "COGGIOLA",

                                 "COSSATO",

                                 "CROSA",

                                 "CURINO",

                                 "DONATO",

                                 "DORZANO",

                                 "GAGLIANICO",

                                 "GRAGLIA",

                                 "LESSONA",

                                 "MAGNANO",

                                 "MASSAZZA",

                                 "MASSERANO",

                                 "MEZZANA MORTIGLIENGO",

                                 "MIAGLIANO",

                                 "MONGRANDO",

                                 "MOSSO",

                                 "MOTTALCIATA",

                                 "MUZZANO",

                                 "NETRO",

                                 "OCCHIEPPO INFERIORE",

                                 "OCCHIEPPO SUPERIORE",

                                 "PETTINENGO",

                                 "PIATTO",

                                 "PIEDICAVALLO",

                                 "POLLONE",

                                 "PONDERANO",

                                 "PORTULA",

                                 "PRALUNGO",

                                 "PRAY",

                                 "QUAREGNA",

                                 "QUITTENGO",

                                 "RONCO BIELLESE",

                                 "ROPPOLO",

                                 "ROSAZZA",

                                 "SAGLIANO MICCA",

                                 "SALA BIELLESE",

                                 "SALUSSOLA",

                                 "SAN PAOLO CERVO",

                                 "SANDIGLIANO",

                                 "SELVE MARCONE",

                                 "SOPRANA",

                                 "SORDEVOLO",

                                 "STRONA",

                                 "TAVIGLIANO",

                                 "TERNENGO",

                                 "TOLLEGNO",

                                 "TORRAZZO",

                                 "TRIVERO",

                                 "VALDENGO",

                                 "VALLANZENGO",

                                 "VALLE MOSSO",

                                 "VALLE SAN NICOLAO",

                                 "VEGLIO",

                                 "VERRONE",

                                 "VIGLIANO BIELLESE",

                                 "VILLANOVA BIELLESE",

                                 "VIVERONE",

                                 "ZIMONE",

                                 "ZUBIENA",

                                 "ZUMAGLIA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI BIELLA')
            elif comune.nome in ["ACCEGLIO",

                                 "AISONE",

                                 "ALTO",

                                 "ARGENTERA",

                                 "BAGNASCO",

                                 "BAGNOLO PIEMONTE",

                                 "BARGE",

                                 "BASTIA MONDOVI'",

                                 "BATTIFOLLO",

                                 "BEINETTE",

                                 "BELLINO",

                                 "BELVEDERE LANGHE",

                                 "BENE VAGIENNA",

                                 "BERNEZZO",

                                 "BONVICINO",

                                 "BORGO SAN DALMAZZO",

                                 "BOVES",

                                 "BRIAGLIA",

                                 "BRIGA ALTA",

                                 "BRONDELLO",

                                 "BROSSASCO",

                                 "BUSCA",

                                 "CAMERANA",

                                 "CANOSIO",

                                 "CAPRAUNA",

                                 "CARAGLIO",

                                 "CARAMAGNA PIEMONTE",

                                 "CARDE'",

                                 "CARRU'",

                                 "CARTIGNANO",

                                 "CASALGRASSO",

                                 "CASTELDELFINO",

                                 "CASTELLAR",

                                 "CASTELLETTO STURA",

                                 "CASTELLINO TANARO",

                                 "CASTELMAGNO",

                                 "CASTELNUOVO DI CEVA",

                                 "CAVALLERLEONE",

                                 "CAVALLERMAGGIORE",

                                 "CELLE DI MACRA",

                                 "CENTALLO",

                                 "CERVASCA",

                                 "CEVA",

                                 "CHIUSA DI PESIO",

                                 "CIGLIE'",

                                 "CLAVESANA",

                                 "COSTIGLIOLE SALUZZO",

                                 "CRISSOLO",

                                 "CUNEO",

                                 "DEMONTE",

                                 "DOGLIANI",

                                 "DRONERO",

                                 "ELVA",

                                 "ENTRACQUE",

                                 "ENVIE",

                                 "FARIGLIANO",

                                 "FAULE",

                                 "FOSSANO",

                                 "FRABOSA SOPRANA",

                                 "FRABOSA SOTTANA",

                                 "FRASSINO",

                                 "GAIOLA",

                                 "GAMBASCA",

                                 "GARESSIO",

                                 "GENOLA",

                                 "GOTTASECCA",

                                 "IGLIANO",

                                 "ISASCA",

                                 "LAGNASCO",

                                 "LEQUIO TANARO",

                                 "LESEGNO",

                                 "LIMONE PIEMONTE",

                                 "LISIO",

                                 "MACRA",

                                 "MAGLIANO ALPI",

                                 "MANTA",

                                 "MARENE",

                                 "MARGARITA",

                                 "MARMORA",

                                 "MARSAGLIA",

                                 "MARTINIANA PO",

                                 "MELLE",

                                 "MOIOLA",

                                 "MOMBARCARO",

                                 "MOMBASIGLIO",

                                 "MONASTERO DI VASCO",

                                 "MONASTEROLO CASOTTO",

                                 "MONASTEROLO DI SAVIGLIANO",

                                 "MONCHIERO",

                                 "MONDOVI'",

                                 "MONESIGLIO",

                                 "MONTALDO DI MONDOVI'",

                                 "MONTANERA",

                                 "MONTEMALE DI CUNEO",

                                 "MONTEROSSO GRANA",

                                 "MONTEZEMOLO",

                                 "MORETTA",

                                 "MOROZZO",

                                 "MURAZZANO",

                                 "MURELLO",

                                 "NIELLA TANARO",

                                 "NUCETTO",

                                 "ONCINO",

                                 "ORMEA",

                                 "OSTANA",

                                 "PAESANA",

                                 "PAGNO",

                                 "PAMPARATO",

                                 "PAROLDO",

                                 "PERLO",

                                 "PEVERAGNO",

                                 "PIANFEI",

                                 "PIASCO",

                                 "PIETRAPORZIO",

                                 "PIOZZO",

                                 "POLONGHERA",

                                 "PONTECHIANALE",

                                 "PRADLEVES",

                                 "PRAZZO",

                                 "PRIERO",

                                 "PRIOLA",

                                 "PRUNETTO",

                                 "RACCONIGI",

                                 "REVELLO",

                                 "RIFREDDO",

                                 "RITTANA",

                                 "ROASCHIA",

                                 "ROASCIO",

                                 "ROBILANTE",

                                 "ROBURENT",

                                 "ROCCA CIGLIE'",

                                 "ROCCA DE' BALDI",

                                 "ROCCABRUNA",

                                 "ROCCAFORTE MONDOVI'",

                                 "ROCCASPARVERA",

                                 "ROCCAVIONE",

                                 "ROSSANA",

                                 "RUFFIA",

                                 "SALE DELLE LANGHE",

                                 "SALE SAN GIOVANNI",

                                 "SALICETO",

                                 "SALMOUR",

                                 "SALUZZO",

                                 "SAMBUCO",

                                 "SAMPEYRE",

                                 "SAN DAMIANO MACRA",

                                 "SAN MICHELE MONDOVI'",

                                 "SANFRONT",

                                 "SANT'ALBANO STURA",

                                 "SAVIGLIANO",

                                 "SCAGNELLO",

                                 "SCARNAFIGI",

                                 "SOMANO",

                                 "STROPPO",

                                 "TARANTASCA",

                                 "TORRE MONDOVI'",

                                 "TORRE SAN GIORGIO",

                                 "TORRESINA",

                                 "TRINITA'",

                                 "VALDIERI",

                                 "VALGRANA",

                                 "VALLORIATE",

                                 "VALMALA",

                                 "VENASCA",

                                 "VERNANTE",

                                 "VERZUOLO",

                                 "VICOFORTE",

                                 "VIGNOLO",

                                 "VILLAFALLETTO",

                                 "VILLANOVA MONDOVI'",

                                 "VILLANOVA SOLARO",

                                 "VILLAR SAN COSTANZO",

                                 "VINADIO",

                                 "VIOLA",

                                 "VOTTIGNASCO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI CUNEO')
            elif comune.nome in ["AGLIE'",

                                 "ALA DI STURA",

                                 "ALBIANO D'IVREA",

                                 "ALICE SUPERIORE",

                                 "ALPETTE",

                                 "ANDRATE",

                                 "AZEGLIO",

                                 "BAIRO",

                                 "BALANGERO",

                                 "BALDISSERO CANAVESE",

                                 "BALME",

                                 "BANCHETTE",

                                 "BARBANIA",

                                 "BARONE CANAVESE",

                                 "BOLLENGO",

                                 "BORGARO TORINESE",

                                 "BORGIALLO",

                                 "BORGOFRANCO D'IVREA",

                                 "BORGOMASINO",

                                 "BOSCONERO",

                                 "BRANDIZZO",

                                 "BROSSO",

                                 "BROZOLO",

                                 "BRUSASCO",

                                 "BUROLO",

                                 "BUSANO",

                                 "CAFASSE",

                                 "CALUSO",

                                 "CANDIA CANAVESE",

                                 "CANISCHIO",

                                 "CANTOIRA",

                                 "CARAVINO",

                                 "CAREMA",

                                 "CASALBORGONE",

                                 "CASCINETTE D'IVREA",

                                 "CASTAGNETO PO",

                                 "CASTELLAMONTE",

                                 "CASTELNUOVO NIGRA",

                                 "CASTIGLIONE TORINESE",

                                 "CAVAGNOLO",

                                 "CERES",

                                 "CERESOLE REALE",

                                 "CHIALAMBERTO",

                                 "CHIAVERANO",

                                 "CHIESANUOVA",

                                 "CHIVASSO",

                                 "CICONIO",

                                 "CINTANO",

                                 "CINZANO",

                                 "CIRIE'",

                                 "COASSOLO TORINESE",

                                 "COLLERETTO CASTELNUOVO",

                                 "COLLERETTO GIACOSA",

                                 "CORIO",

                                 "COSSANO CANAVESE",

                                 "CUCEGLIO",

                                 "CUORGNE'",

                                 "FAVRIA",

                                 "FELETTO",

                                 "FIANO",

                                 "FIORANO CANAVESE",

                                 "FOGLIZZO",

                                 "FORNO CANAVESE",

                                 "FRASSINETTO",

                                 "FRONT",

                                 "GASSINO TORINESE",

                                 "GERMAGNANO",

                                 "GROSCAVALLO",

                                 "GROSSO",

                                 "INGRIA",

                                 "ISSIGLIO",

                                 "IVREA",

                                 "LANZO TORINESE",

                                 "LAURIANO",

                                 "LEINI",

                                 "LEMIE",

                                 "LESSOLO",

                                 "LEVONE",

                                 "LOCANA",

                                 "LOMBARDORE",

                                 "LORANZE'",

                                 "LUGNACCO",

                                 "LUSIGLIE'",

                                 "MAGLIONE",

                                 "MATHI",

                                 "MAZZE'",

                                 "MERCENASCO",

                                 "MEUGLIANO",

                                 "MEZZENILE",

                                 "MONASTERO DI LANZO",

                                 "MONTALENGHE",

                                 "MONTALTO DORA",

                                 "MONTANARO",

                                 "MONTEU DA PO",

                                 "NOASCA",

                                 "NOLE",

                                 "NOMAGLIO",

                                 "OGLIANICO",

                                 "ORIO CANAVESE",

                                 "OZEGNA",

                                 "PALAZZO CANAVESE",

                                 "PARELLA",

                                 "PAVONE CANAVESE",

                                 "PECCO",

                                 "PEROSA CANAVESE",

                                 "PERTUSIO",

                                 "PESSINETTO",

                                 "PIVERONE",

                                 "PONT-CANAVESE",

                                 "PRASCORSANO",

                                 "PRATIGLIONE",

                                 "QUAGLIUZZO",

                                 "QUASSOLO",

                                 "QUINCINETTO",

                                 "RIBORDONE",

                                 "RIVALBA",

                                 "RIVARA",

                                 "RIVAROLO CANAVESE",

                                 "RIVAROSSA",

                                 "ROBASSOMERO",

                                 "ROCCA CANAVESE",

                                 "ROMANO CANAVESE",

                                 "RONCO CANAVESE",

                                 "RONDISSONE",

                                 "RUEGLIO",

                                 "SALASSA",

                                 "SALERANO CANAVESE",

                                 "SAMONE",

                                 "SAN BENIGNO CANAVESE",

                                 "SAN CARLO CANAVESE",

                                 "SAN COLOMBANO BELMONTE",

                                 "SAN FRANCESCO AL CAMPO",

                                 "SAN GIORGIO CANAVESE",

                                 "SAN GIUSTO CANAVESE",

                                 "SAN MARTINO CANAVESE",

                                 "SAN MAURIZIO CANAVESE",

                                 "SAN MAURO TORINESE",

                                 "SAN PONSO",

                                 "SAN RAFFAELE CIMENA",

                                 "SAN SEBASTIANO DA PO",

                                 "SCARMAGNO",

                                 "SCIOLZE",

                                 "SETTIMO ROTTARO",

                                 "SETTIMO TORINESE",

                                 "SETTIMO VITTONE",

                                 "SPARONE",

                                 "STRAMBINELLO",

                                 "STRAMBINO",

                                 "TAVAGNASCO",

                                 "TORRAZZA PIEMONTE",

                                 "TORRE CANAVESE",

                                 "TRAUSELLA",

                                 "TRAVERSELLA",

                                 "TRAVES",

                                 "USSEGLIO",

                                 "VALLO TORINESE",

                                 "VALPERGA",

                                 "VALPRATO SOANA",

                                 "VARISELLA",

                                 "VAUDA CANAVESE",

                                 "VENARIA REALE",

                                 "VEROLENGO",

                                 "VERRUA SAVOIA",

                                 "VESTIGNE'",

                                 "VIALFRE'",

                                 "VICO CANAVESE",

                                 "VIDRACCO",

                                 "VILLANOVA CANAVESE",

                                 "VILLAREGGIA",

                                 "VISCHE",

                                 "VISTRORIO",

                                 "VIU'",

                                 "VOLPIANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI IVREA')
            elif comune.nome in ["AGRATE CONTURBIA",

                                 "BARENGO",

                                 "BELLINZAGO NOVARESE",

                                 "BIANDRATE",

                                 "BOCA",

                                 "BOGOGNO",

                                 "BOLZANO NOVARESE",

                                 "BORGO TICINO",

                                 "BORGOLAVEZZARO",

                                 "BORGOMANERO",

                                 "BRIGA NOVARESE",

                                 "BRIONA",

                                 "CALTIGNAGA",

                                 "CAMERI",

                                 "CARPIGNANO SESIA",

                                 "CASALBELTRAME",

                                 "CASALEGGIO NOVARA",

                                 "CASALINO",

                                 "CASALVOLONE",

                                 "CASTELLAZZO NOVARESE",

                                 "CASTELLETTO SOPRA TICINO",

                                 "CAVAGLIETTO",

                                 "CAVAGLIO D'AGOGNA",

                                 "CAVALLIRIO",

                                 "CERANO",

                                 "COMIGNAGO",

                                 "CRESSA",

                                 "CUREGGIO",

                                 "DIVIGNANO",

                                 "FARA NOVARESE",

                                 "FONTANETO D'AGOGNA",

                                 "GALLIATE",

                                 "GARBAGNA NOVARESE",

                                 "GARGALLO",

                                 "GATTICO",

                                 "GHEMME",

                                 "GOZZANO",

                                 "GRANOZZO CON MONTICELLO",

                                 "GRIGNASCO",

                                 "LANDIONA",

                                 "MAGGIORA",

                                 "MANDELLO VITTA",

                                 "MARANO TICINO",

                                 "MEZZOMERICO",

                                 "MOMO",

                                 "NIBBIOLA",

                                 "NOVARA",

                                 "OLEGGIO",

                                 "POGNO",

                                 "POMBIA",

                                 "PRATO SESIA",

                                 "RECETTO",

                                 "ROMAGNANO SESIA",

                                 "ROMENTINO",

                                 "SAN MAURIZIO D'OPAGLIO",

                                 "SAN NAZZARO SESIA",

                                 "SAN PIETRO MOSEZZO",

                                 "SILLAVENGO",

                                 "SIZZANO",

                                 "SORISO",

                                 "SOZZAGO",

                                 "SUNO",

                                 "TERDOBBIATE",

                                 "TORNACO",

                                 "TRECATE",

                                 "VAPRIO D'AGOGNA",

                                 "VARALLO POMBIA",

                                 "VERUNO",

                                 "VESPOLATE",

                                 "VICOLUNGO",

                                 "VINZAGLIO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI NOVARA')
            elif comune.nome in ["AIRASCA",

                                 "ALMESE",

                                 "ALPIGNANO",

                                 "ANDEZENO",

                                 "ANGROGNA",

                                 "ARIGNANO",

                                 "AVIGLIANA",

                                 "BALDISSERO TORINESE",

                                 "BARDONECCHIA",

                                 "BEINASCO",

                                 "BIBIANA",

                                 "BOBBIO PELLICE",

                                 "BORGONE SUSA",

                                 "BRICHERASIO",

                                 "BRUINO",

                                 "BRUZOLO",

                                 "BURIASCO",

                                 "BUSSOLENO",

                                 "BUTTIGLIERA ALTA",

                                 "CAMBIANO",

                                 "CAMPIGLIONE FENILE",

                                 "CANDIOLO",

                                 "CANTALUPA",

                                 "CAPRIE",

                                 "CARIGNANO",

                                 "CASELETTE",

                                 "CASELLE TORINESE",

                                 "CASTAGNOLE PIEMONTE",

                                 "CAVOUR",

                                 "CERCENASCO",

                                 "CESANA TORINESE",

                                 "CHIANOCCO",

                                 "CHIERI",

                                 "CHIOMONTE",

                                 "CHIUSA DI SAN MICHELE",

                                 "CLAVIERE",

                                 "COAZZE",

                                 "COLLEGNO",

                                 "CONDOVE",

                                 "CUMIANA",

                                 "DRUENTO",

                                 "EXILLES",

                                 "FENESTRELLE",

                                 "FROSSASCO",

                                 "GARZIGLIANA",

                                 "GIAGLIONE",

                                 "GIAVENO",

                                 "GIVOLETTO",

                                 "GRAVERE",

                                 "GRUGLIASCO",

                                 "INVERSO PINASCA",

                                 "LA CASSA",

                                 "LA LOGGIA",

                                 "LOMBRIASCO",

                                 "LUSERNA SAN GIOVANNI",

                                 "LUSERNETTA",

                                 "MACELLO",

                                 "MARENTINO",

                                 "MASSELLO",

                                 "MATTIE",

                                 "MEANA DI SUSA",

                                 "MOMBELLO DI TORINO",

                                 "MOMPANTERO",

                                 "MONCALIERI",

                                 "MONCENISIO",

                                 "MONTALDO TORINESE",

                                 "MORIONDO TORINESE",

                                 "NICHELINO",

                                 "NONE",

                                 "NOVALESA",

                                 "ORBASSANO",

                                 "OSASCO",

                                 "OSASIO",

                                 "OULX",

                                 "PANCALIERI",

                                 "PAVAROLO",

                                 "PECETTO TORINESE",

                                 "PEROSA ARGENTINA",

                                 "PERRERO",

                                 "PIANEZZA",

                                 "PINASCA",

                                 "PINEROLO",

                                 "PINO TORINESE",

                                 "PIOBESI TORINESE",

                                 "PIOSSASCO",

                                 "PISCINA",

                                 "POMARETTO",

                                 "PORTE",

                                 "PRAGELATO",

                                 "PRALI",

                                 "PRAMOLLO",

                                 "PRAROSTINO",

                                 "REANO",

                                 "RIVA PRESSO CHIERI",

                                 "RIVALTA DI TORINO",

                                 "RIVOLI",

                                 "ROLETTO",

                                 "RORA'",

                                 "ROSTA",

                                 "ROURE",

                                 "RUBIANA",

                                 "SALBERTRAND",

                                 "SALZA DI PINEROLO",

                                 "SAN DIDERO",

                                 "SAN GERMANO CHISONE",

                                 "SAN GILLIO",

                                 "SAN GIORIO DI SUSA",

                                 "SAN PIETRO VAL LEMINA",

                                 "SAN SECONDO DI PINEROLO",

                                 "SANGANO",

                                 "SANT'AMBROGIO DI TORINO",

                                 "SANT'ANTONINO DI SUSA",

                                 "SANTENA",

                                 "SAUZE DI CESANA",

                                 "SAUZE D'OULX",

                                 "SCALENGHE",

                                 "SESTRIERE",

                                 "SUSA",

                                 "TORINO",

                                 "TORRE PELLICE",

                                 "TRANA",

                                 "TROFARELLO",

                                 "USSEAUX",

                                 "VAIE",

                                 "VAL DELLA TORRE",

                                 "VALGIOIE",

                                 "VENAUS",

                                 "VIGONE",

                                 "VILLAFRANCA PIEMONTE",

                                 "VILLAR DORA",

                                 "VILLAR FOCCHIARDO",

                                 "VILLAR PELLICE",

                                 "VILLAR PEROSA",

                                 "VILLARBASSE",

                                 "VILLASTELLONE",

                                 "VINOVO",

                                 "VIRLE PIEMONTE",

                                 "VOLVERA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI TORINO')
            elif comune.nome in ["AMENO",

                                 "ANTRONA SCHIERANCO",

                                 "ANZOLA D'OSSOLA",

                                 "ARIZZANO",

                                 "ARMENO",

                                 "AROLA",

                                 "ARONA",

                                 "AURANO",

                                 "BACENO",

                                 "BANNIO ANZINO",

                                 "BAVENO",

                                 "BEE",

                                 "BELGIRATE",

                                 "BEURA-CARDEZZA",

                                 "BOGNANCO",

                                 "BROVELLO-CARPUGNINO",

                                 "CALASCA-CASTIGLIONE",

                                 "CAMBIASCA",

                                 "CANNERO RIVIERA",

                                 "CANNOBIO",

                                 "CAPREZZO",

                                 "CASALE CORTE CERRO",

                                 "CAVAGLIO-SPOCCIA",

                                 "CEPPO MORELLI",

                                 "CESARA",

                                 "COLAZZA",

                                 "COSSOGNO",

                                 "CRAVEGGIA",

                                 "CREVOLADOSSOLA",

                                 "CRODO",

                                 "CURSOLO-ORASSO",

                                 "DOMODOSSOLA",

                                 "DORMELLETTO",

                                 "DRUOGNO",

                                 "FALMENTA",

                                 "FORMAZZA",

                                 "GERMAGNO",

                                 "GHIFFA",

                                 "GIGNESE",

                                 "GRAVELLONA TOCE",

                                 "GURRO",

                                 "INTRAGNA",

                                 "INVORIO",

                                 "LESA",

                                 "LOREGLIA",

                                 "MACUGNAGA",

                                 "MADONNA DEL SASSO",

                                 "MALESCO",

                                 "MASERA",

                                 "MASSINO VISCONTI",

                                 "MASSIOLA",

                                 "MEINA",

                                 "MERGOZZO",

                                 "MIASINO",

                                 "MIAZZINA",

                                 "MONTECRESTESE",

                                 "MONTESCHENO",

                                 "NEBBIUNO",

                                 "NONIO",

                                 "OGGEBBIO",

                                 "OLEGGIO CASTELLO",

                                 "OMEGNA",

                                 "ORNAVASSO",

                                 "ORTA SAN GIULIO",

                                 "PALLANZENO",

                                 "PARUZZARO",

                                 "PELLA",

                                 "PETTENASCO",

                                 "PIEDIMULERA",

                                 "PIEVE VERGONTE",

                                 "PISANO",

                                 "PREMENO",

                                 "PREMIA",

                                 "PREMOSELLO-CHIOVENDA",

                                 "QUARNA SOPRA",

                                 "QUARNA SOTTO",

                                 "RE",

                                 "SAN BERNARDINO VERBANO",

                                 "SANTA MARIA MAGGIORE",

                                 "SEPPIANA",

                                 "STRESA",

                                 "TOCENO",

                                 "TRAREGO VIGGIONA",

                                 "TRASQUERA",

                                 "TRONTANO",

                                 "VALSTRONA",

                                 "VANZONE CON SAN CARLO",

                                 "VARZO",

                                 "VERBANIA",

                                 "VIGANELLA",

                                 "VIGNONE",

                                 "VILLADOSSOLA",

                                 "VILLETTE",

                                 "VOGOGNA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI VERBANIA')
            elif comune.nome in ["AILOCHE",

                                 "ALAGNA VALSESIA",

                                 "ALBANO VERCELLESE",

                                 "ALFIANO NATTA",

                                 "ALICE CASTELLO",

                                 "ALTAVILLA MONFERRATO",

                                 "ARBORIO",

                                 "ASIGLIANO VERCELLESE",

                                 "BALMUCCIA",

                                 "BALOCCO",

                                 "BALZOLA",

                                 "BIANZE'",

                                 "BOCCIOLETO",

                                 "BORGO D'ALE",

                                 "BORGO SAN MARTINO",

                                 "BORGO VERCELLI",

                                 "BORGOSESIA",

                                 "BOZZOLE",

                                 "BREIA",

                                 "BURONZO",

                                 "CALLIANO",

                                 "CAMAGNA MONFERRATO",

                                 "CAMINO",

                                 "CAMPERTOGNO",

                                 "CAPRILE",

                                 "CARCOFORO",

                                 "CARESANA",

                                 "CARESANABLOT",

                                 "CARISIO",

                                 "CASALE MONFERRATO",

                                 "CASANOVA ELVO",

                                 "CASTELLETTO MERLI",

                                 "CELLA MONTE",

                                 "CELLIO",

                                 "CERESETO",

                                 "CERRINA MONFERRATO",

                                 "CERVATTO",

                                 "CIGLIANO",

                                 "CIVIASCO",

                                 "COLLOBIANO",

                                 "CONIOLO",

                                 "CONZANO",

                                 "COSTANZANA",

                                 "CRAVAGLIANA",

                                 "CRESCENTINO",

                                 "CREVACUORE",

                                 "CROVA",

                                 "CUCCARO MONFERRATO",

                                 "DESANA",

                                 "FOBELLO",

                                 "FONTANETTO PO",

                                 "FORMIGLIANA",

                                 "FRASSINELLO MONFERRATO",

                                 "FRASSINETO PO",

                                 "FUBINE",

                                 "GABIANO",

                                 "GATTINARA",

                                 "GHISLARENGO",

                                 "GIAROLE",

                                 "GIFFLENGA",

                                 "GRAZZANO BADOGLIO",

                                 "GREGGIO",

                                 "GUARDABOSONE",

                                 "LAMPORO",

                                 "LENTA",

                                 "LIGNANA",

                                 "LIVORNO FERRARIS",

                                 "LOZZOLO",

                                 "MIRABELLO MONFERRATO",

                                 "MOLLIA",

                                 "MOMBELLO MONFERRATO",

                                 "MONCALVO",

                                 "MONCESTINO",

                                 "MONCRIVELLO",

                                 "MORANO SUL PO",

                                 "MOTTA DE' CONTI",

                                 "MURISENGO",

                                 "OCCIMIANO",

                                 "ODALENGO GRANDE",

                                 "ODALENGO PICCOLO",

                                 "OLCENENGO",

                                 "OLDENICO",

                                 "OLIVOLA",

                                 "OTTIGLIO",

                                 "OZZANO MONFERRATO",

                                 "PALAZZOLO VERCELLESE",

                                 "PENANGO",

                                 "PERTENGO",

                                 "PEZZANA",

                                 "PILA",

                                 "PIODE",

                                 "POMARO MONFERRATO",

                                 "PONTESTURA",

                                 "PONZANO MONFERRATO",

                                 "POSTUA",

                                 "PRAROLO",

                                 "QUARONA",

                                 "QUINTO VERCELLESE",

                                 "RASSA",

                                 "RIMA SAN GIUSEPPE",

                                 "RIMASCO",

                                 "RIMELLA",

                                 "RIVA VALDOBBIA",

                                 "RIVE",

                                 "ROASIO",

                                 "RONSECCO",

                                 "ROSIGNANO MONFERRATO",

                                 "ROSSA",

                                 "ROVASENDA",

                                 "SABBIA",

                                 "SALA MONFERRATO",

                                 "SALASCO",

                                 "SALI VERCELLESE",

                                 "SALUGGIA",

                                 "SAN GERMANO VERCELLESE",

                                 "SAN GIACOMO VERCELLESE",

                                 "SAN GIORGIO MONFERRATO",

                                 "SANTHIA'",

                                 "SCOPA",

                                 "SCOPELLO",

                                 "SERRALUNGA DI CREA",

                                 "SERRAVALLE SESIA",

                                 "SOLONGHELLO",

                                 "SOSTEGNO",

                                 "STROPPIANA",

                                 "TERRUGGIA",

                                 "TICINETO",

                                 "TONCO",

                                 "TREVILLE",

                                 "TRICERRO",

                                 "TRINO",

                                 "TRONZANO VERCELLESE",

                                 "VALDUGGIA",

                                 "VALMACCA",

                                 "VARALLO",

                                 "VERCELLI",

                                 "VIGNALE MONFERRATO",

                                 "VILLA DEL BOSCO",

                                 "VILLADEATI",

                                 "VILLAMIROGLIO",

                                 "VILLANOVA MONFERRATO",

                                 "VILLARBOIT",

                                 "VILLATA",

                                 "VOCCA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI VERCELLI')
            elif comune.nome in ["ALA",

                                 "ARCO",

                                 "AVIO",

                                 "BESENELLO",

                                 "BRENTONICO",

                                 "CALLIANO",

                                 "DRENA",

                                 "DRO",

                                 "FOLGARIA",

                                 "ISERA",

                                 "LEDRO",

                                 "MAGASA",

                                 "MORI",

                                 "NAGO-TORBOLE",

                                 "NOGAREDO",

                                 "NOMI",

                                 "POMAROLO",

                                 "RIVA DEL GARDA",

                                 "RONZOCHIENIS",

                                 "ROVERETO",

                                 "TENNO",

                                 "TERRAGNOLO",

                                 "TRAMBILENO",

                                 "VALLARSA",

                                 "VALVESTINO",

                                 "VILLA LAGARINA",

                                 "VOLANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI ROVERETO')
            elif comune.nome in ["ALBIANO",

                                 "ALDENO",

                                 "AMBLAR",

                                 "ANDALO",

                                 "BASELGA DI PINE'",

                                 "BEDOLLO",

                                 "BERSONE",

                                 "BIENO",

                                 "BLEGGIO SUPERIORE",

                                 "BOCENAGO",

                                 "BOLBENO",

                                 "BONDO",

                                 "BONDONE",

                                 "BORGO VALSUGANA",

                                 "BOSENTINO",

                                 "BREGUZZO",

                                 "BRESIMO",

                                 "BREZ",

                                 "BRIONE",

                                 "CADERZONE TERME",

                                 "CAGNO'",

                                 "CALAVINO",

                                 "CALCERANICA AL LAGO",

                                 "CALDES",

                                 "CALDONAZZO",

                                 "CAMPITELLO DI FASSA",

                                 "CAMPODENNO",

                                 "CANAL SAN BOVO",

                                 "CANAZEI",

                                 "CAPRIANA",

                                 "CARANO",

                                 "CARISOLO",

                                 "CARZANO",

                                 "CASTEL CONDINO",

                                 "CASTELFONDO",

                                 "CASTELLO TESINO",

                                 "CASTELLO-MOLINA DI FIEMME",

                                 "CASTELNUOVO",

                                 "CAVALESE",

                                 "CAVARENO",

                                 "CAVEDAGO",

                                 "CAVEDINE",

                                 "CAVIZZANA",

                                 "CEMBRA",

                                 "CENTA SAN NICOLO'",

                                 "CIMEGO",

                                 "CIMONE",

                                 "CINTE TESINO",

                                 "CIS",

                                 "CIVEZZANO",

                                 "CLES",

                                 "CLOZ",

                                 "COMANO TERME",

                                 "COMMEZZADURA",

                                 "CONDINO",

                                 "COREDO",

                                 "CROVIANA",

                                 "CUNEVO",

                                 "DAIANO",

                                 "DAMBEL",

                                 "DAONE",

                                 "DARE'",

                                 "DENNO",

                                 "DIMARO",

                                 "DON",

                                 "DORSINO",

                                 "FAEDO",

                                 "FAI DELLA PAGANELLA",

                                 "FAVER",

                                 "FIAVE'",

                                 "FIERA DI PRIMIERO",

                                 "FIEROZZO",

                                 "FLAVON",

                                 "FONDO",

                                 "FORNACE",

                                 "FRASSILONGO",

                                 "GARNIGA TERME",

                                 "GIOVO",

                                 "GIUSTINO",

                                 "GRAUNO",

                                 "GRIGNO",

                                 "GRUMES",

                                 "IMER",

                                 "IVANO-FRACENA",

                                 "LARDARO",

                                 "LASINO",

                                 "LAVARONE",

                                 "LAVIS",

                                 "LEVICO TERME",

                                 "LISIGNAGO",

                                 "LIVO",

                                 "LONA-LASES",

                                 "LUSERNA",

                                 "MALE'",

                                 "MALOSCO",

                                 "MASSIMENO",

                                 "MAZZIN",

                                 "MEZZANA",

                                 "MEZZANO",

                                 "MEZZOCORONA",

                                 "MEZZOLOMBARDO",

                                 "MOENA",

                                 "MOLVENO",

                                 "MONCLASSICO",

                                 "MONTAGNE",

                                 "NANNO",

                                 "NAVE SAN ROCCO",

                                 "NOVALEDO",

                                 "OSPEDALETTO",

                                 "OSSANA",

                                 "PADERGNONE",

                                 "PALU' DEL FERSINA",

                                 "PANCHIA'",

                                 "PEIO",

                                 "PELLIZZANO",

                                 "PELUGO",

                                 "PERGINE VALSUGANA",

                                 "PIEVE DI BONO",

                                 "PIEVE TESINO",

                                 "PINZOLO",

                                 "POZZA DI FASSA",

                                 "PRASO",

                                 "PREDAZZO",

                                 "PREORE",

                                 "PREZZO",

                                 "RABBI",

                                 "RAGOLI",

                                 "REVO'",

                                 "ROMALLO",

                                 "ROMENO",

                                 "RONCEGNO TERME",

                                 "RONCHI VALSUGANA",

                                 "RONCONE",

                                 "RONZONE",

                                 "ROVERE' DELLA LUNA",

                                 "RUFFRE-MENDOLA",

                                 "RUMO",

                                 "SAGRON MIS",

                                 "SAMONE",

                                 "SAN LORENZO IN BANALE",

                                 "SAN MICHELE ALL'ADIGE",

                                 "SANT'ORSOLA TERME",

                                 "SANZENO",

                                 "SARNONICO",

                                 "SCURELLE",

                                 "SEGONZANO",

                                 "SFRUZ",

                                 "SIROR",

                                 "SMARANO",

                                 "SORAGA",

                                 "SOVER",

                                 "SPERA",

                                 "SPIAZZO",

                                 "SPORMAGGIORE",

                                 "SPORMINORE",

                                 "STENICO",

                                 "STORO",

                                 "STREMBO",

                                 "STRIGNO",

                                 "TAIO",

                                 "TASSULLO",

                                 "TELVE",

                                 "TELVE DI SOPRA",

                                 "TENNA",

                                 "TERLAGO",

                                 "TERRES",

                                 "TERZOLAS",

                                 "TESERO",

                                 "TIONE DI TRENTO",

                                 "TON",

                                 "TONADICO",

                                 "TORCEGNO",

                                 "TRANSACQUA",

                                 "TRENTO",

                                 "TRES",

                                 "TUENNO",

                                 "VALDA",

                                 "VALFLORIANA",

                                 "VARENA",

                                 "VATTARO",

                                 "VERMIGLIO",

                                 "VERVO'",

                                 "VEZZANO",

                                 "VIGNOLA-FALESINA",

                                 "VIGO DI FASSA",

                                 "VIGO RENDENA",

                                 "VIGOLO VATTARO",

                                 "VILLA AGNEDO",

                                 "VILLA RENDENA",

                                 "ZAMBANA",

                                 "ZIANO DI FIEMME",

                                 "ZUCLO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI ROVERETO')
            elif comune.nome in ["CAPRIVA DEL FRIULI",

                                 "CORMONS",

                                 "DOBERDO' DEL LAGO",

                                 "DOLEGNA DEL COLLIO",

                                 "FARRA D'ISONZO",

                                 "FOGLIANO REDIPUGLIA",

                                 "GORIZIA",

                                 "GRADISCA D'ISONZO",

                                 "GRADO",

                                 "MARIANO DEL FRIULI",

                                 "MEDEA",

                                 "MONFALCONE",

                                 "MORARO",

                                 "MOSSA",

                                 "ROMANS D'ISONZO",

                                 "RONCHI DEI LEGIONARI",

                                 "SAGRADO",

                                 "SAN CANZIAN D'ISONZO",

                                 "SAN FLORIANO DEL COLLIO",

                                 "SAN LORENZO ISONTINO",

                                 "SAN PIER D'ISONZO",

                                 "SAVOGNA D'ISONZO",

                                 "STARANZANO",

                                 "TURRIACO",

                                 "VILLESSE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI GORIZIA')
            elif comune.nome in ["ANDREIS",

                                 "ANNONE VENETO",

                                 "ARBA",

                                 "ARZENE",

                                 "AVIANO",

                                 "AZZANO DECIMO",

                                 "BARCIS",

                                 "BRUGNERA",

                                 "BUDOIA",

                                 "CANEVA",

                                 "CAORLE",

                                 "CASARSA DELLA DELIZIA",

                                 "CASTELNOVO DEL FRIULI",

                                 "CAVASSO NUOVO",

                                 "CHIONS",

                                 "CIMOLAIS",

                                 "CINTO CAOMAGGIORE",

                                 "CLAUT",

                                 "CLAUZETTO",

                                 "CONCORDIA SAGITTARIA",

                                 "CORDENONS",

                                 "CORDOVADO",

                                 "FANNA",

                                 "FIUME VENETO",

                                 "FONTANAFREDDA",

                                 "FORGARIA NEL FRIULI",

                                 "FOSSALTA DI PORTOGRUARO",

                                 "FRISANCO",

                                 "GRUARO",

                                 "MANIAGO",

                                 "MEDUNO",

                                 "MONTEREALE VALCELLINA",

                                 "MORSANO AL TAGLIAMENTO",

                                 "PASIANO DI PORDENONE",

                                 "PINZANO AL TAGLIAMENTO",

                                 "POLCENIGO",

                                 "PORCIA",

                                 "PORDENONE",

                                 "PORTOGRUARO",

                                 "PRAMAGGIORE",

                                 "PRATA DI PORDENONE",

                                 "PRAVISDOMINI",

                                 "ROVEREDO IN PIANO",

                                 "SACILE",

                                 "SAN GIORGIO DELLA RICHINVELDA",

                                 "SAN MARTINO AL TAGLIAMENTO",

                                 "SAN MICHELE AL TAGLIAMENTO",

                                 "SAN QUIRINO",

                                 "SAN STINO DI LIVENZA",

                                 "SAN VITO AL TAGLIAMENTO",

                                 "SEQUALS",

                                 "SESTO AL REGHENA",

                                 "SPILIMBERGO",

                                 "TEGLIO VENETO",

                                 "TRAMONTI DI SOPRA",

                                 "TRAMONTI DI SOTTO",

                                 "TRAVESIO",

                                 "VAJONT",

                                 "VALVASONE",

                                 "VITO D'ASIO",

                                 "VIVARO",

                                 "ZOPPOLA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PORDENONE')
            elif comune.nome in ["DUINO-AURISINA",

                                 "MONRUPINO",

                                 "MUGGIA",

                                 "SAN DORLIGO DELLA VALLE-DOLINA",

                                 "SGONICO",

                                 "TRIESTE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI TRIESTE')
            elif comune.nome in ["AIELLO DEL FRIULI",

                                 "AMARO",

                                 "AMPEZZO",

                                 "AQUILEIA",

                                 "ARTA TERME",

                                 "ARTEGNA",

                                 "ATTIMIS",

                                 "BAGNARIA ARSA",

                                 "BASILIANO",

                                 "BERTIOLO",

                                 "BICINICCO",

                                 "BORDANO",

                                 "BUJA",

                                 "BUTTRIO",

                                 "CAMINO AL TAGLIAMENTO",

                                 "CAMPOFORMIDO",

                                 "CAMPOLONGO TAPOGLIANO",

                                 "CARLINO",

                                 "CASSACCO",

                                 "CASTIONS DI STRADA",

                                 "CAVAZZO CARNICO",

                                 "CERCIVENTO",

                                 "CERVIGNANO DEL FRIULI",

                                 "CHIOPRIS-VISCONE",

                                 "CHIUSAFORTE",

                                 "CIVIDALE DEL FRIULI",

                                 "CODROIPO",

                                 "COLLOREDO DI MONTE ALBANO",

                                 "COMEGLIANS",

                                 "CORNO DI ROSAZZO",

                                 "COSEANO",

                                 "DIGNANO",

                                 "DOGNA",

                                 "DRENCHIA",

                                 "ENEMONZO",

                                 "FAEDIS",

                                 "FAGAGNA",

                                 "FIUMICELLO",

                                 "FLAIBANO",

                                 "FORNI AVOLTRI",

                                 "FORNI DI SOPRA",

                                 "FORNI DI SOTTO",

                                 "GEMONA DEL FRIULI",

                                 "GONARS",

                                 "GRIMACCO",

                                 "LATISANA",

                                 "LAUCO",

                                 "LESTIZZA",

                                 "LIGNANO SABBIADORO",

                                 "LIGOSULLO",

                                 "LUSEVERA",

                                 "MAGNANO IN RIVIERA",

                                 "MAJANO",

                                 "MALBORGHETTO VALBRUNA",

                                 "MANZANO",

                                 "MARANO LAGUNARE",

                                 "MARTIGNACCO",

                                 "MERETO DI TOMBA",

                                 "MOGGIO UDINESE",

                                 "MOIMACCO",

                                 "MONTENARS",

                                 "MORTEGLIANO",

                                 "MORUZZO",

                                 "MUZZANA DEL TURGNANO",

                                 "NIMIS",

                                 "OSOPPO",

                                 "OVARO",

                                 "PAGNACCO",

                                 "PALAZZOLO DELLO STELLA",

                                 "PALMANOVA",

                                 "PALUZZA",

                                 "PASIAN DI PRATO",

                                 "PAULARO",

                                 "PAVIA DI UDINE",

                                 "POCENIA",

                                 "PONTEBBA",

                                 "PORPETTO",

                                 "POVOLETTO",

                                 "POZZUOLO DEL FRIULI",

                                 "PRADAMANO",

                                 "PRATO CARNICO",

                                 "PRECENICCO",

                                 "PREMARIACCO",

                                 "PREONE",

                                 "PREPOTTO",

                                 "PULFERO",

                                 "RAGOGNA",

                                 "RAVASCLETTO",

                                 "RAVEO",

                                 "REANA DEL ROJALE",

                                 "REMANZACCO",

                                 "RESIA",

                                 "RESIUTTA",

                                 "RIGOLATO",

                                 "RIVE D'ARCANO",

                                 "RIVIGNANO",

                                 "RONCHIS",

                                 "RUDA",

                                 "SAN DANIELE DEL FRIULI",

                                 "SAN GIORGIO DI NOGARO",

                                 "SAN GIOVANNI AL NATISONE",

                                 "SAN LEONARDO",

                                 "SAN PIETRO AL NATISONE",

                                 "SAN VITO AL TORRE",

                                 "SAN VITO DI FAGAGNA",

                                 "SANTA MARIA LA LONGA",

                                 "SAURIS",

                                 "SAVOGNA",

                                 "SEDEGLIANO",

                                 "SOCCHIEVE",

                                 "STREGNA",

                                 "SUTRIO",

                                 "TAIPANA",

                                 "TALMASSONS",

                                 "TARCENTO",

                                 "TARVISIO",

                                 "TAVAGNACCO",

                                 "TEOR",

                                 "TERZO D'AQUILEIA",

                                 "TOLMEZZO",

                                 "TORREANO",

                                 "TORVISCOSA",

                                 "TRASAGHIS",

                                 "TREPPO CARNICO",

                                 "TREPPO GRANDE",

                                 "TRICESIMO",

                                 "TRIVIGNANO UDINESE",

                                 "UDINE",

                                 "VARMO",

                                 "VENZONE",

                                 "VERZEGNIS",

                                 "VILLA SANTINA",

                                 "VILLA VICENTINA",

                                 "VISCO",

                                 "ZUGLIO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI UDINE')
            elif comune.nome in ["AGORDO",

                                 "ALANO DI PIAVE",

                                 "ALLEGHE",

                                 "ARSIE'",

                                 "AURONZO DI CADORE",

                                 "BELLUNO",

                                 "BORCA DI CADORE",

                                 "CALALZO DI CADORE",

                                 "CANALE D'AGORDO",

                                 "CASTELLAVAZZO",

                                 "CENCENIGHE AGORDINO",

                                 "CESIOMAGGIORE",

                                 "CHIES D'ALPAGO",

                                 "CIBIANA DI CADORE",

                                 "COLLE SANTA LUCIA",

                                 "COMELICO SUPERIORE",

                                 "CORTINA D'AMPEZZO",

                                 "DANTA DI CADORE",

                                 "DOMEGGE DI CADORE",

                                 "ERTO E CASSO",

                                 "FALCADE",

                                 "FARRA D'ALPAGO",

                                 "FELTRE",

                                 "FONZASO",

                                 "FORNO DI ZOLDO",

                                 "GOSALDO",

                                 "LA VALLE AGORDINA",

                                 "LAMON",

                                 "LENTIAI",

                                 "LIMANA",

                                 "LIVINALLONGO DEL COL DI LANA",

                                 "LONGARONE",

                                 "LORENZAGO DI CADORE",

                                 "LOZZO DI CADORE",

                                 "MEL",

                                 "OSPITALE DI CADORE",

                                 "PEDAVENA",

                                 "PERAROLO DI CADORE",

                                 "PIEVE D'ALPAGO",

                                 "PIEVE DI CADORE",

                                 "PONTE NELLE ALPI",

                                 "PUOS D'ALPAGO",

                                 "QUERO",

                                 "RIVAMONTE AGORDINO",

                                 "ROCCA PIETORE",

                                 "SAN GREGORIO NELLE ALPI",

                                 "SAN NICOLO' DI COMELICO",

                                 "SAN PIETRO DI CADORE",

                                 "SAN TOMASO AGORDINO",

                                 "SAN VITO DI CADORE",

                                 "SANTA GIUSTINA",

                                 "SANTO STEFANO DI CADORE",

                                 "SAPPADA",

                                 "SEDICO",

                                 "SELVA DI CADORE",

                                 "SEREN DEL GRAPPA",

                                 "SOSPIROLO",

                                 "SOVERZENE",

                                 "SOVRAMONTE",

                                 "TAIBON AGORDINO",

                                 "TAMBRE",

                                 "TRICHIANA",

                                 "VALLADA AGORDINA",

                                 "VALLE DI CADORE",

                                 "VAS",

                                 "VIGO DI CADORE",

                                 "VODO CADORE",

                                 "VOLTAGO AGORDINO",

                                 "ZOLDO ALTO",

                                 "ZOPPE' DI CADORE"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI BELLUNO')
            elif comune.nome in ["ABANO TERME",

                                 "AGNA",

                                 "ALBIGNASEGO",

                                 "ANGUILLARA VENETA",

                                 "ARQUA' PETRARCA",

                                 "ARRE",

                                 "ARZERGRANDE",

                                 "BAGNOLI DI SOPRA",

                                 "BATTAGLIA TERME",

                                 "BORGORICCO",

                                 "BOVOLENTA",

                                 "BRUGINE",

                                 "CADONEGHE",

                                 "CAMPO SAN MARTINO",

                                 "CAMPODARSEGO",

                                 "CAMPODORO",

                                 "CAMPOSAMPIERO",

                                 "CANDIANA",

                                 "CARMIGNANO DI BRENTA",

                                 "CARTURA",

                                 "CASALSERUGO",

                                 "CERVARESE SANTA CROCE",

                                 "CITTADELLA",

                                 "CODEVIGO",

                                 "CONSELVE",

                                 "CORREZZOLA",

                                 "CURTAROLO",

                                 "DUE CARRARE",

                                 "FONTANIVA",

                                 "GALLIERA VENETA",

                                 "GALZIGNANO TERME",

                                 "GAZZO",

                                 "GRANTORTO",

                                 "LEGNARO",

                                 "LIMENA",

                                 "LOREGGIA",

                                 "MASERA' DI PADOVA",

                                 "MASSANZAGO",

                                 "MESTRINO",

                                 "MONSELICE",

                                 "MONTEGROTTO TERME",

                                 "NOVENTA PADOVANA",

                                 "PADOVA",

                                 "PIAZZOLA SUL BRENTA",

                                 "PIOMBINO DESE",

                                 "PIOVE DI SACCO",

                                 "POLVERARA",

                                 "PONTE SAN NICOLO'",

                                 "PONTELONGO",

                                 "ROVOLON",

                                 "RUBANO",

                                 "SACCOLONGO",

                                 "SAN GIORGIO DELLE PERTICHE",

                                 "SAN GIORGIO IN BOSCO",

                                 "SAN MARTINO DI LUPARI",

                                 "SAN PIETRO IN GU",

                                 "SANTA GIUSTINA IN COLLE",

                                 "SANT'ANGELO DI PIOVE DI SACCO",

                                 "SAONARA",

                                 "SELVAZZANO DENTRO",

                                 "TEOLO",

                                 "TERRASSA PADOVANA",

                                 "TOMBOLO",

                                 "TORREGLIA",

                                 "TREBASELEGHE",

                                 "TRIBANO",

                                 "VEGGIANO",

                                 "VIGODARZERE",

                                 "VIGONZA",

                                 "VILLA DEL CONTE",

                                 "VILLAFRANCA PADOVANA",

                                 "VILLANOVA DI CAMPOSAMPIERO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI PADOVA')
            elif comune.nome in ["ADRIA",

                                 "ARIANO NEL POLESINE",

                                 "ARQUA' POLESINE",

                                 "BADIA POLESINE",

                                 "BAGNOLO DI PO",

                                 "BAONE",

                                 "BARBONA",

                                 "BERGANTINO",

                                 "BOARA PISANI",

                                 "BOSARO",

                                 "CALTO",

                                 "CANARO",

                                 "CANDA",

                                 "CARCERI",

                                 "CASALE DI SCODOSIA",

                                 "CASTELBALDO",

                                 "CASTELGUGLIELMO",

                                 "CASTELMASSA",

                                 "CASTELNOVO BARIANO",

                                 "CENESELLI",

                                 "CEREGNANO",

                                 "CINTO EUGANEO",

                                 "CORBOLA",

                                 "COSTA DI ROVIGO",

                                 "CRESPINO",

                                 "ESTE",

                                 "FICAROLO",

                                 "FIESSO UMBERTIANO",

                                 "FRASSINELLE POLESINE",

                                 "FRATTA POLESINE",

                                 "GAIBA",

                                 "GAVELLO",

                                 "GIACCIANO CON BARUCHELLA",

                                 "GRANZE",

                                 "GUARDA VENETA",

                                 "LENDINARA",

                                 "LOREO",

                                 "LOZZO ATESTINO",

                                 "LUSIA",

                                 "MASI",

                                 "MEGLIADINO SAN FIDENZIO",

                                 "MEGLIADINO SAN VITALE",

                                 "MELARA",

                                 "MERLARA",

                                 "MONTAGNANA",

                                 "OCCHIOBELLO",

                                 "OSPEDALETTO EUGANEO",

                                 "PAPOZZE",

                                 "PERNUMIA",

                                 "PETTORAZZA GRIMANI",

                                 "PIACENZA D'ADIGE",

                                 "PINCARA",

                                 "POLESELLA",

                                 "PONSO",

                                 "PONTECCHIO POLESINE",

                                 "PORTO TOLLE",

                                 "PORTO VIRO",

                                 "POZZONOVO",

                                 "ROSOLINA",

                                 "ROVIGO",

                                 "SALARA",

                                 "SALETTO",

                                 "SAN BELLINO",

                                 "SAN MARTINO DI VENEZZE",

                                 "SAN PIETRO VIMINARIO",

                                 "SANTA MARGHERITA D'ADIGE",

                                 "SANT'ELENA",

                                 "SANT'URBANO",

                                 "SOLESINO",

                                 "STANGHELLA",

                                 "STIENTA",

                                 "TAGLIO DI PO",

                                 "TRECENTA",

                                 "URBANA",

                                 "VESCOVANA",

                                 "VIGHIZZOLO D'ESTE",

                                 "VILLA ESTENSE",

                                 "VILLADOSE",

                                 "VILLAMARZANA",

                                 "VILLANOVA DEL GHEBBO",

                                 "VILLANOVA MARCHESANA",

                                 "VO'"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI ROVIGO')
            elif comune.nome in ["ALTIVOLE",

                                 "ARCADE",

                                 "ASOLO",

                                 "BORSO DEL GRAPPA",

                                 "BREDA DI PIAVE",

                                 "CAERANO DI SAN MARCO",

                                 "CAPPELLA MAGGIORE",

                                 "CARBONERA",

                                 "CASALE SUL SILE",

                                 "CASIER",

                                 "CASTELCUCCO",

                                 "CASTELFRANCO VENETO",

                                 "CASTELLO DI GODEGO",

                                 "CAVASO DEL TOMBA",

                                 "CESSALTO",

                                 "CHIARANO",

                                 "CIMADOLMO",

                                 "CISON DI VALMARINO",

                                 "CODOGNE'",

                                 "COLLE UMBERTO",

                                 "CONEGLIANO",

                                 "CORDIGNANO",

                                 "CORNUDA",

                                 "CRESPANO DEL GRAPPA",

                                 "CROCETTA DEL MONTELLO",

                                 "FARRA DI SOLIGO",

                                 "FOLLINA",

                                 "FONTANELLE",

                                 "FONTE",

                                 "FREGONA",

                                 "GAIARINE",

                                 "GIAVERA DEL MONTELLO",

                                 "GODEGA DI SANT'URBANO",

                                 "GORGO AL MONTICANO",

                                 "ISTRANA",

                                 "LORIA",

                                 "MANSUE'",

                                 "MARENO DI PIAVE",

                                 "MASER",

                                 "MASERADA SUL PIAVE",

                                 "MEDUNA DI LIVENZA",

                                 "MIANE",

                                 "MOGLIANO VENETO",

                                 "MONASTIER DI TREVISO",

                                 "MONFUMO",

                                 "MONTEBELLUNA",

                                 "MORGANO",

                                 "MORIAGO DELLA BATTAGLIA",

                                 "MOTTA DI LIVENZA",

                                 "NERVESA DELLA BATTAGLIA",

                                 "ODERZO",

                                 "ORMELLE",

                                 "ORSAGO",

                                 "PADERNO DEL GRAPPA",

                                 "PAESE",

                                 "PEDEROBBA",

                                 "PIEVE DI SOLIGO",

                                 "PONTE DI PIAVE",

                                 "PONZANO VENETO",

                                 "PORTOBUFFOLE'",

                                 "POSSAGNO",

                                 "POVEGLIANO",

                                 "PREGANZIOL",

                                 "QUINTO DI TREVISO",

                                 "REFRONTOLO",

                                 "RESANA",

                                 "REVINE LAGO",

                                 "RIESE PIO X",

                                 "RONCADE",

                                 "SALGAREDA",

                                 "SAN BIAGIO DI CALLALTA",

                                 "SAN FIOR",

                                 "SAN PIETRO DI FELETTO",

                                 "SAN POLO DI PIAVE",

                                 "SAN VENDEMIANO",

                                 "SAN ZENONE DEGLI EZZELINI",

                                 "SANTA LUCIA DI PIAVE",

                                 "SARMEDE",

                                 "SEGUSINO",

                                 "SERNAGLIA DELLA BATTAGLIA",

                                 "SILEA",

                                 "SPRESIANO",

                                 "SUSEGANA",

                                 "TARZO",

                                 "TREVIGNANO",

                                 "TREVISO",

                                 "VALDOBBIADENE",

                                 "VAZZOLA",

                                 "VEDELAGO",

                                 "VIDOR",

                                 "VILLORBA",

                                 "VITTORIO VENETO",

                                 "VOLPAGO DEL MONTELLO",

                                 "ZENSON DI PIAVE",

                                 "ZERO BRANCO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI TREVISO')
            elif comune.nome in ["CAMPAGNA LUPIA",

                                 "CAMPOLONGO MAGGIORE",

                                 "CAMPONOGARA",

                                 "CAVALLINO-TREPORTI",

                                 "CAVARZERE",

                                 "CEGGIA",

                                 "CHIOGGIA",

                                 "CONA",

                                 "DOLO",

                                 "ERACLEA",

                                 "FIESSO D'ARTICO",

                                 "FOSSALTA DI PIAVE",

                                 "FOSSO'",

                                 "JESOLO",

                                 "MARCON",

                                 "MARTELLAGO",

                                 "MEOLO",

                                 "MIRA",

                                 "MIRANO",

                                 "MUSILE DI PIAVE",

                                 "NOALE",

                                 "NOVENTA DI PIAVE",

                                 "PIANIGA",

                                 "QUARTO D'ALTINO",

                                 "SALZANO",

                                 "SAN DONA' DI PIAVE",

                                 "SANTA MARIA DI SALA",

                                 "SCORZE'",

                                 "SPINEA",

                                 "STRA",

                                 "TORRE DI MOSTO",

                                 "VENEZIA",

                                 "VIGONOVO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI VENEZIA')
            elif comune.nome in ["AFFI",

                                 "ALBAREDO D'ADIGE",

                                 "ANGIARI",

                                 "ARCOLE",

                                 "BADIA CALAVENA",

                                 "BARDOLINO",

                                 "BELFIORE",

                                 "BEVILACQUA",

                                 "BONAVIGO",

                                 "BOSCHI SANT'ANNA",

                                 "BOSCO CHIESANUOVA",

                                 "BOVOLONE",

                                 "BRENTINO BELLUNO",

                                 "BRENZONE",

                                 "BUSSOLENGO",

                                 "BUTTAPIETRA",

                                 "CALDIERO",

                                 "CAPRINO VERONESE",

                                 "CASALEONE",

                                 "CASTAGNARO",

                                 "CASTEL D'AZZANO",

                                 "CASTELNUOVO DEL GARDA",

                                 "CAVAION VERONESE",

                                 "CAZZANO DI TRAMIGNA",

                                 "CEREA",

                                 "CERRO VERONESE",

                                 "COLOGNA VENETA",

                                 "COLOGNOLA AI COLLI",

                                 "CONCAMARISE",

                                 "COSTERMANO",

                                 "DOLCE'",

                                 "ERBE'",

                                 "ERBEZZO",

                                 "FERRARA DI MONTE BALDO",

                                 "FUMANE",

                                 "GARDA",

                                 "GAZZO VERONESE",

                                 "GREZZANA",

                                 "ILLASI",

                                 "ISOLA DELLA SCALA",

                                 "ISOLA RIZZA",

                                 "LAVAGNO",

                                 "LAZISE",

                                 "LEGNAGO",

                                 "MALCESINE",

                                 "MARANO DI VALPOLICELLA",

                                 "MEZZANE DI SOTTO",

                                 "MINERBE",

                                 "MONTECCHIA DI CROSARA",

                                 "MONTEFORTE D'ALPONE",

                                 "MOZZECANE",

                                 "NEGRAR",

                                 "NOGARA",

                                 "NOGAROLE ROCCA",

                                 "OPPEANO",

                                 "PALU'",

                                 "PASTRENGO",

                                 "PESCANTINA",

                                 "PESCHIERA DEL GARDA",

                                 "POVEGLIANO VERONESE",

                                 "PRESSANA",

                                 "RIVOLI VERONESE",

                                 "RONCA'",

                                 "RONCO ALL'ADIGE",

                                 "ROVERCHIARA",

                                 "ROVERE' VERONESE",

                                 "ROVEREDO DI GUA'",

                                 "SALIZZOLE",

                                 "SAN BONIFACIO",

                                 "SAN GIOVANNI ILARIONE",

                                 "SAN GIOVANNI LUPATOTO",

                                 "SAN MARTINO BUON ALBERGO",

                                 "SAN MAURO DI SALINE",

                                 "SAN PIETRO DI MORUBIO",

                                 "SAN PIETRO IN CARIANO",

                                 "SAN ZENO DI MONTAGNA",

                                 "SANGUINETTO",

                                 "SANT'AMBROGIO DI VALPOLICELLA",

                                 "SANT'ANNA D'ALFAEDO",

                                 "SELVA DI PROGNO",

                                 "SOAVE",

                                 "SOMMACAMPAGNA",

                                 "SONA",

                                 "SORGA'",

                                 "TERRAZZO",

                                 "TORRI DEL BENACO",

                                 "TREGNAGO",

                                 "TREVENZUOLO",

                                 "VALEGGIO SUL MINCIO",

                                 "VELO VERONESE",

                                 "VERONA",

                                 "VERONELLA",

                                 "VESTENANOVA",

                                 "VIGASIO",

                                 "VILLA BARTOLOMEA",

                                 "VILLAFRANCA DI VERONA",

                                 "ZEVIO",

                                 "ZIMELLA"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI VERONA')
            elif comune.nome in ["AGUGLIARO",

                                 "ALBETTONE",

                                 "ALONTE",

                                 "ALTAVILLA VICENTINA",

                                 "ALTISSIMO",

                                 "ARCUGNANO",

                                 "ARSIERO",

                                 "ARZIGNANO",

                                 "ASIAGO",

                                 "ASIGLIANO VENETO",

                                 "BARBARANO VICENTINO",

                                 "BASSANO DEL GRAPPA",

                                 "BOLZANO VICENTINO",

                                 "BREGANZE",

                                 "BRENDOLA",

                                 "BRESSANVIDO",

                                 "BROGLIANO",

                                 "CALDOGNO",

                                 "CALTRANO",

                                 "CALVENE",

                                 "CAMISANO VICENTINO",

                                 "CAMPIGLIA DEI BERICI",

                                 "CAMPOLONGO SUL BRENTA",

                                 "CARRE'",

                                 "CARTIGLIANO",

                                 "CASSOLA",

                                 "CASTEGNERO",

                                 "CASTELGOMBERTO",

                                 "CHIAMPO",

                                 "CHIUPPANO",

                                 "CISMON DEL GRAPPA",

                                 "COGOLLO DEL CENGIO",

                                 "CONCO",

                                 "CORNEDO VICENTINO",

                                 "COSTABISSARA",

                                 "CREAZZO",

                                 "CRESPADORO",

                                 "DUEVILLE",

                                 "ENEGO",

                                 "FARA VICENTINO",

                                 "FOZA",

                                 "GALLIO",

                                 "GAMBELLARA",

                                 "GAMBUGLIANO",

                                 "GRANCONA",

                                 "GRISIGNANO DI ZOCCO",

                                 "GRUMOLO DELLE ABBADESSE",

                                 "ISOLA VICENTINA",

                                 "LAGHI",

                                 "LASTEBASSE",

                                 "LONGARE",

                                 "LONIGO",

                                 "LUGO DI VICENZA",

                                 "LUSIANA",

                                 "MALO",

                                 "MARANO VICENTINO",

                                 "MAROSTICA",

                                 "MASON VICENTINO",

                                 "MOLVENA",

                                 "MONTE DI MALO",

                                 "MONTEBELLO VICENTINO",

                                 "MONTECCHIO MAGGIORE",

                                 "MONTECCHIO PRECALCINO",

                                 "MONTEGALDA",

                                 "MONTEGALDELLA",

                                 "MONTEVIALE",

                                 "MONTICELLO CONTE OTTO",

                                 "MONTORSO VICENTINO",

                                 "MOSSANO",

                                 "MUSSOLENTE",

                                 "NANTO",

                                 "NOGAROLE VICENTINO",

                                 "NOVE",

                                 "NOVENTA VICENTINA",

                                 "ORGIANO",

                                 "PEDEMONTE",

                                 "PIANEZZE",

                                 "PIOVENE ROCCHETTE",

                                 "POJ ANA MAGGIORE",

                                 "POSINA",

                                 "POVE DEL GRAPPA",

                                 "POZZOLEONE",

                                 "QUINTO VICENTINO",

                                 "RECOARO TERME",

                                 "ROANA",

                                 "ROMANO D'EZZELINO",

                                 "ROSA'",

                                 "ROSSANO VENETO",

                                 "ROTZO",

                                 "SALCEDO",

                                 "SAN GERMANO DEI BERICI",

                                 "SAN NAZARIO",

                                 "SAN PIETRO MUSSOLINO",

                                 "SAN VITO DI LEGUZZANO",

                                 "SANDRIGO",

                                 "SANTORSO",

                                 "SARCEDO",

                                 "SAREGO",

                                 "SCHIAVON",

                                 "SCHIO",

                                 "SOLAGNA",

                                 "SOSSANO",

                                 "SOVIZZO",

                                 "TEZZE SUL BRENTA",

                                 "THIENE",

                                 "TONEZZA DEL CIMONE",

                                 "TORREBELVICINO",

                                 "TORRI DI QUARTESOLO",

                                 "TRISSINO",

                                 "VALDAGNO",

                                 "VALDASTICO",

                                 "VALLI DEL PASUBIO",

                                 "VALSTAGNA",

                                 "VELO D'ASTICO",

                                 "VICENZA",

                                 "VILLAGA",

                                 "VILLAVERLA",

                                 "ZANE'",

                                 "ZERMEGHEDO",

                                 "ZOVENCEDO",

                                 "ZUGLIANO"]:
                comune.tribunale = Tribunali.objects.get(
                    nome='TRIBUNALE CIVILE DI VICENZA')
            comune.save()
