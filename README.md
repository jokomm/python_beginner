# python_beginner
Homework from Introduction to Programming course

## PR01 - Python

Loo programm, mis küsib kasutajalt tema nime ja sünniaasta. Seejärel ütleb programm, kui vana kasutaja oli siis, kui Python 3.0 ametlikult välja tuli (2008).

Näideted
Kui kasutaja on sündinud samal aastal või vanem kui Python 3.0:

What is your name? Mati

Hello, Mati! What year were you born in? 1999

You were 9 years old when Python 3.0 was released.

Kui Python 3.0 tuli enne kasutaja sünniaastat välja:

What is your name? Kati

Hello, Kati! What year were you born in? 2010

Python 3 was 2 years old when you were born.

NB! Programmis peavad olema sõned täpselt samal kujul:

"What is your name?"
"Hello, (nimi)! What year were you born in?"
"You were x years old when Python 3.0 was released." Kui Python 3 on vanem kui kasutaja, on programmi väljundiks: "Python 3 was x years old when you were born."

## EX01 - Cashier

Kujuta ette, et oled kassapidaja. Iga kord, kui on vaja kliendile sente tagasi anda, mingi summa x, tahad sa teada, mitu senti (täpsemalt münti) on sul minimaalselt vaja kliendile tagasi anda.

Sinu ülesandeks on luua programm, mis saab sisendiks numbri (alati vahemikus 1-100) ning prindib konsooli, mitu senti on vaja minimaalselt tagastada, et sisestatud summat katta. Kassas on ühikuga sendid järgmiste väärtustega: (1,5,10,20,50)

Näited
Näide sisendiga 63:

Enter a sum: 63

Amount of coins needed: 5

Näide sisendiga 6:

Enter a sum: 6

Amount of coins needed: 2

NB! Programmis peavad olema sõned täpselt samal kujul. Sisendi küsimise puhul: "Enter a sum: " ja väljundi puhul: "Amount of coins needed: (_sentide arv_)"

## PR02 - Primes

Ülesandeks on kirjutada programm, mis tuvastab, kas antud arv on algarv. Tuvastatav arv on antud funktsiooni parameetrina.

Kui tegemist on algarvuga, tagastab funktsioon True.

is_prime_number(7) -> True

Kui tegemist pole algarvuga, tagastab funktsioon False.

is_prime_number(6) -> False

## EX02 - Cypher

Ülesande eesmärk on kodeerida sõnesid.

Caesari šiffer
Caesari nihe on salakiri, kus teksti iga täht asendatakse mõne teisega, mis on tähestikus kindel arv tähti ees- või tagapool. Teksti kodeerimisel ja dekodeerimisel on kõige tähtsam kaasa antav võti. Näiteks kui võti on 2, siis a -> c, b -> d, aab -> ccd

Sisu
message - sõne, mida on vaja (de)krüpteerida
key - võti, mis ütleb, mitu kohta tähestikus on vaja iga tähte nihutada
Programm peab opereerima inglise tähestikuga, ainult väikeste tähtedega (a, b, c, ... x, y, z). Funktsioon peab käima läbi sisendsõne tähthaaval ja selle põhjal ehitama uue kodeeritud sõne.

Iga tähega on vaja teha järgnev:

Kui tegu pole tähega, liida see tulemusse ilma seda muutmata (kasulik oleks kasutada sõne .isalpha() meetodit)
Muul juhul leia tähe järjekorranumber tähestikus ja liida sellele võti
Selle uue järjekorranumbri põhjal leia täht, mis liita tulemusse

 ## PR03 - Pancakes

Oled kokk pannkoogirestoranis ja pead hästi palju pannkooke tegema.

make_n_pancakes(n: int, ingredients: list) - peamine funktsioon.
Funktsiooni sisenditeks on täisarv n ja järjend ingredients. n näitab, mitu pannkooki on vaja teha, ingredients on etteantud järjend koostisosadest, millest pannkooke teha. ingredients on kujul [koostisosa1, koostisosa2, ...], kus koostisosa on sõne.
Juhul, kui pannkooke ei saa teha n koguses, siis tee neid nii palju, kui saab. Kuid kui neid saab rohkem kui n tükki, siis tuleb teha täpselt n tükki.
Selles funktsioonis tuleb kasutada teisi funktsioone (allpool). Kõigepealt tuleks valmis teha tainas (make_dough funktioon()) ning siis hakata ükshaaval pannkooke tegema (can_make_pancake() ning make_a_pancake()).

make_dough(ingredients: list) - funktsioon, milles tehakse valmis pannkoogitainas.
Funktsioon saab sisendiks koostisosad (ingredients) järjendina. ingredients on kujul [koostisosa1, koostisosa2, ...], kus koostisosa on sõne.
Näide järjendist: ["egg", "egg", "flour", "milk", "butter", "sugar", "milk", "sugar"].
Siin funktsioonis tee alati valmis nii palju tainast kui võimalik.
Tainast saab teha 7 dl kaupa (ehk saad korraga teha 7*x koguses - 0, 7, 14, 21, 28 jne, aga mitte 4, 10, 12 vms).
7 dl taina tegemiseks kulub üks kogus muna, 5 kogust piima, 4 kogust jahu, üks kogus võid, 2 kogust suhkrut. Need andmed on mallis juba kirjas.
Funktsioon tagastab tehtud taigna koguse (dl).

can_make_pancake(dough: float) - funktsioon kontrollimaks, kas meil on piisavalt tainast, et teha üks pannkook.
Funktsioon saab sisendiks ujukomaarvu dough, mis näitab, kui palju tainast (dl) meil on ning tagastab tõeväärtuse olenevalt sellest, kas meil on piisavalt tainast, et teha üks pannkook.
Kui on piisavalt tainast, tagastab funktsioon True, vastasel juhul False.
Ühe pannkoogi tegemiseks kulub 0.8 dl tainast.

make_a_pancake(dough: float) - funktsioon, milles tehakse valmis pannkook.
Tegelikult ei tule pannkoogi tegemist implementeerida. Funktsiooni eesmärk on tagastada taigna kogus (dl) peale pannkoogi tegemist.
Funktsioon saab sisendiks taigna koguse (dl) ning tagastab taigna koguse (dl) peale pannkoogi tegemist.
Tagastatav pannkoogi taigna kogus tuleb ümardada kahe komakohani.
Nagu juba mainitud, siis ühe pannkoogi tegemiseks kulub 0.8 dl tainast.

## EX03 - Booksortation

Oled Twilight Sparkle'i hea sõber ja aitad teda ta lemmiktegevusega - booksortationiga.

booksortation(books: list) - peamine funktsioon.
Funktsiooni sisendiks on järjend (list) raamatutest (õigemini raamatute pealkirjadest, mis on sõned).
Sinu ülesandeks on kõik need raamatud jagada 5 kategooriasse: spell books, history books, relics books, potion books ja other books. Raamatu kategooria selgekstegemise nõuded on allpool järgnevates meetodites. Juhul, kui üks raamat kuulub tingimuste järgi mitmesse erinevasse kategooriasse, tuleb see panna esimesse kategooriasse, mis mainitud. Ehk prioriteetjärjestus on spell books, history books, relics books, potion books. Juhul, kui raamat ei kuulu ühtegi kategooriasse nimetatud neljast, läheb ta kategooriasse other books.
Funktsiooni väljundiks on sõnastik (dict), kus võtmeteks on kategooriad (sõnena) ning väärtusteks järjend raamatutest, mis antud kategooriasse kuuluvad. Tagastavas sõnastikus peaksid olema kõik järjendid tähestiku järgi sorteeritud.
Juhul, kui mingi kategooria raamatuid pole üldse, ei tohi seda kategooriat ka sõnastikus esineda (ehk ei ole mingit sellist asja {"potion books": []}).
Sõnastiku elementide järjekord pole oluline ehk samaväärsed on nii {"spell books": ["\*Spells\*"], "relics books": ["ThE StAfF"]} kui ka {"relics books": ["ThE StAfF"], "spell books": ["\*Spells\*"]}.

add_book_to_category(book: str, category: str, categorised_books: dict) - abimeetod lisamaks raamatut sõnastikku õige kategooria alla.
Funktsiooni sisendiks on parameetrid book (sõne - raamat, mis tuleb sõnastikku lisada), category (sõne - kategooria, millesse antud raamat kuulub), categorised_books (sõnastik, kuhu tuleb raamat lisada).
Raamatu lisamine õigesse kategooriasse võiks käia umbes nii:

kui antud kategooria on juba sõnastiku võtmete hulgas, siis lisa sellele kategooriale vastavasse järjendisse antud raamat
kui antud kategooriat pole veel sõnastikus, siis lisa see kategooria sõnastikku ning pane tema väärtuseks järjend, milles on antud raamat
Funktsioon peab tagastama muudetud sõnastiku.

Järgnevad neli funktsiooni on sarnased.
Need kõik kontrollivad, kas antud raamat kuulub vastavasse kategooriasse. Funktsioon saab sisendiks raamatu nime (sõne) ning kontrollib selles kuuluvust antud kategooriasse. Kui raamat kuulub sellesse kategooriasse, tagastab funktsioon True, vastasel juhul False.

is_spell_book(book: str)
Raamat kuulub kategooriasse "spell books", kui ta nimi algab ja lõpeb sümboliga *, kuid alguse ja lõpu sümbol ei tohi olla üks ja sama *.
Näiteks kuulub sellesse kategooriasse raamat nimega "*The Horrible Spells*".

is_history_book(book: str)
Raamat kuulub kategooriasse "history books", kui iga selle raamatu nimes esinev sõna (k.a. esimene sõna) ei alga väikese algustähega. Siin juhul loeme sõnadeks kõike, mis algab peale tühikut (ehk lihtsamalt öeldes on sõnade eraldajaks tühikud).
Näiteks kuulub sellesse kategooriasse raamat nimega "The Mighty King", kuid siia ei kuulu "the Ugly Duckling", sest sõna 'the' ei alga suure tähega.

is_relics_book(book: str)
Raamat kuulub kategooriasse "relics books", kui ta nimi järgib mustrit, kus kõik tähed on vaheldumisi suured ja väiksed (võib alata nii suure kui ka väikse tähega). Ettevaatust tühikutega - tühikud ei ole erandiks.
Näiteks kuuluvad sellesse kategooriasse raamatud "ThE StAfF" ning "rAiNiNg dUmPlInGs", kuid siia ei kuulu "ThE sTaFf" ega "rAiNiNg DuMpLiNgS" (tühikud!).

is_potion_book(book: str)
Raamat kuulub kategooriasse "potion books" juhul, kui tema nimes on võrdselt kaas- ja täishäälikuid või kui nende kogus erineb ühe võrra.
Siin ülesandes loeme täishäälikuteks ainult a, e, i, o, u ning kaashäälikuteks b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, x, z, w, y.
Kõiki teisi tähti ja sümboleid võib nimes esineda kui tahes palju - need ei mõjuta raamatu kategoriseerimist.
Siia kategooriasse sobiksid raamatud "The Banana Juice" (7 täishäälikut, 7 kaashäälikut) ja "The tomato potion" (7 täishäälikut, 8 kaashäälikut - kogus erineb ühe võrra). Sellesse kategooriasse ei kuulu aga "The Green Liquid" (6 täishäälikut, 8 kaashäälikut - kogus erineb kahe võrra).

## PR04 - Census

Sinu väikse riigi statistikaamet on näinud palju vaeva ja kogunud kokku kõigi inimeste nimed. Kahjuks ei osanud nad midagi paremat nendega teha, kui need kõik ühte teksti faili panna. Kahjuks pole neil võimalik oma tööd edasi teha, kuna keegi ei suuda käsitsi neid kokku lugeda.

Sinu ülesandeks on panna need nimed ilusamasse vormi ehk sõnastikku.

Ülesandes on failist lugemine ette antud.

Funktsioonid
to_dictionary(names) Lisab kõik nimed sõnastikku. Tagastab sõnastiku.

to_sex_dicts(names_dict) Jaotab meeste ja naiste nimed eraldi sõnastikesse. Tagastab kaks sõnastikku.

most_popular(names_dict) Leiab kõige populaarsema nime sõnastikus. Tagastab sõne. Tühja sõnastiku puhul tagastab "Empty dictionary.".

number_of_people(names_dict) Tagastab inimeste arvu.

names_by_popularity(names_dict) Tagastab sõne, kus on kõik nimed populaarsuse järjekorras. Kui sisend on tühi, tagastab tühja sõne.

Funktsioonide most_popular, number_of_people ja names_by_popularity sisendiks on sõnastik, mille võti on inimese nimi ja väärtus on selle nimega inimeste kogus.

## EX04 - Hobbies

Ülesande eesmärk on teha programm, mis loeb info tekstifailist ja töötleb saadud andmeid erinevatel viisidel.

Kujutame ette, et andmebaasis hoitakse info inimestest ja nende huvidest. Seoses sellega, et info kogutakse erinevatest allikatest, on andmebaasis korduvad nimed, aga erinevate hobidega. Põhiülesanne on teha andmebaas korda ehk leida kõik hobid, mis kuuluvad ühele inimesele ja siduda need selle inimesega.

hobbies_database

Parameeter file siin on algseisus olevate andmetega tekstifail, mis tuleb enda kausta (ex04_hobbies) alla laadida ja ülesande lahendamisel kasutada.

Failis igal real on üks nimi ja üks hobi, mis om omavahel eraldatud kooloniga :
create_list_from_file(file) - funktioon, kus toimub failist lugemine. Tagastab järjendi (listi) faili ridadega, sisendparameetriks on faili nimi;
create_dictionary(file) - funktsioon, mis peab tagastama sõnastiku (dict) kujul Nimi: [hobi_1, hobi_2] (sõnastiku võti (key) on nimi ning väärtus (value) on selle inimese leitud hobide nimekiri järjendina); sisendparameeter on faili nimi, kust andmed laetakse. Siin ülesandes on mõistlik kasutada create_list_from_file funktsiooni.
find_person_with_most_hobbies(file) - funktsioon, mis leiab kõige rohkemate hobidega inimese. Tagastab järjendi (list) inimese nimega (või inimeste nimedega, kui leidub mitu inimest, kellel on sama palju hobisid);
find_person_with_least_hobbies(file) - funktsioonil on umbes sama ülesanne, nagu eelmisel, aga seekord tuleb leida kõige vähemate huvidega inimese. Tagastab järjendi (list) inimese nimega (või inimeste nimedega, kui leidub mitu inimest, kellel on sama palju hobisid);
find_most_popular_hobby(file) - funktsioon leiab kõige polulaarsema hobi andmebaasis olevate inimeste hulgas. Populaarsemaid hobisid võib olla mitu. Sama hobi samal inimesel mitu korda arvesse ei lähe. Funktsioon tagastab list;
find_least_popular_hobby(file) - funktsioonil on umbes sama ülesanne, nagu eelmisel, aga seekord tuleb leida kõige ebapopulaarsema hobi andmebaasis olevate inimeste hulgas. Ebapopulaarsemaid hobisid võib olla mitu. Funktsioon tagastab list;
write_corrected_database(file, file_to_write) - funktsioon kirjutab .csv faili, kus andmed on paremini vormindatud. file - fail, kust andmed loetakse. file_to_write - csv-fail, kuhu andmed tuleb kirjutada. Ei tagasta midagi, aga tulemusena näete Korrektselt koostatud .csv fail

## EX05 - OEE

Kodumaine toiduainetootja "Sarvest" pöördus sinu poole murega, nimelt soovivad nad oma tootmise digitaliseerimisega minna järgmisesse etappi. Selle jaoks leidsid nad enda tootmise efektiivsuse mõõtmiseks OEE.

Lähteandmete näitena on neil sulle anda CSV fail, kus on kirjas ühe reedese päeva tootmistulemused. Lisaks oskavad nad sulle öelda, et reedel oli neil vahetus 8 tundi pikk, millest üks tund kulus lõuna ja pauside peale, ehk kokku oli tööaega 7 tundi.

Funktsioonid
read_production_data(filename: str) -> dict - Loeb sisse parameetriga filename etteantud CSV faili ning tagastab sõnastiku, mille võtmeks on liini nimetus e. Machine Name ning väärtuseks järjend sisendandmetest. Nimetame seda sõnastikku edaspidi tootmisandmete sõnastikuks.

{'Sildistaja': [358, 57, 18602, 18388]}

NB! Vahel võib juhtuda, et üritatakse lugeda faili mida ei eksisteeri. Selle funktsiooni puhul on oluline püüda kinni erind FileNotFoundError ning tagastada selle erindi korral tühi sõnastik {}.

calculate_quality(production_data: dict) -> dict - Võtab sisse tootmisandmete sõnastiku ning arvutab eeltoodud lehel välja toodud OEE valemite põhjal kvaliteedi protsendi. Tagastab sõnastiku, mille võtmeks on liini nimetus ja väärtus kvaliteedi protsent ühe komakoha täpsusega.

{'Sildistaja': 98.8}

calculate_availability(production_data: dict) -> dict - Võtab sisse tootmisandmete sõnastiku ning arvutab OEE valemite põhjal saadavuse protsendi. Tagastab sõnastiku, mille võtmeks on liini nimetus ja väärtus saadavuse protsent ühe komakoha täpsusega.

{'Sildistaja': 85.2}

calculate_performance(production_data: dict) -> dict - Võtab sisse tootmisandmete sõnastiku ning arvutab eeltoodud lehel välja toodud OEE valemite põhjal tootlikuse protsendi. Tagastab sõnastiku, mille võtmeks on liini nimetus ja väärtus kvaliteedi protsent ühe komakoha täpsusega.

{'Sildistaja': 91.2}

calculate_oee(production_data: dict) -> dict - Võtab sisse tootmisandmete sõnastiku ning arvutab eeltoodud lehel välja toodud OEE valemite põhjal OEE protsendi. Siin oleks mõistlik ära kasutada eelnevalt loodud funktsioone. Tagastab sõnastiku, mille võtmeks on liini nimetus ja väärtus OEE protsent ühe komakoha täpsusega.

{'Sildistaja': 76.8}

write_results_to_file(production_data: dict, filename: str) - Võtab sisse tootmisandmete sõnastiku, arvutab eelnevalt loodud funktsioonidega OEE andmed ning salvestab need parameetri filename all etteantud faili csv kujul. Erinevalt sisendandmetest, on sellel csv failil oluline ka lisada esimeseks reaks päis kujul Liin,Saadavus,Tootlus,Kvaliteet,OEE.

## PR06 - Twitter

Ülesande eesmärgiks on tutvustada objekte. Selleks tuleb teostada programm, mis organiseerib säutse.

Klass Tweet
__init__(self, user: str, content: str, time: int, retweets: int)
Loob objekti vastavalt klassi nõuetele.

Funktsioonid
find_fastest_growing(tweets: list) -> Tweet
Leiab säutsu, mis on oma eluperioodi peale kõige kiiremini levinud. Indeks, mida võrrelda: retweets/time.

sort_by_popularity(tweets: list) -> list
Sorteerib säutsud kõigepealt retweetide koguse järgi, populaarseimast alates, ja siis ajaliselt, värskeimast alates.

filter_by_hashtag(tweets: list, hashtag: str) -> list
Tagastab listi ainult nendest säutsudest, mis on hashtagiga seotud.

sort_hashtags_by_all_time_popularity
Tagastab listi hashtagidest populaarsuse järgi, populaarseimast alates. Hashtagi populaarsus on sellega seotud säutsude retweetide summa.

Tingimused, nõuded, vihjed
Säutsud antakse ette listina. Seda listi ei tohi muuta.
Igal säutsul on sellised väärtused: user: str, content: str, time: float, retweets: int. Neid väärtusi ei tohi muuta. Julgustatud on aga enda väärtuste lisamine.

## EX06 - Messenger

Ülesanne on realiseerida lihtne süsteem sõnumite haldamiseks

Klassid
Nendega ei ole vaja teha midagi muud kui aru saada.

User - sõnumite kirjutaja/autor

name: str - kasutaja nimi
Chat - vestlus, kuhu saab sõnumeid kirjutada

name: str - vestluse nimi
users: list - nimekiri kasutajatest, kes vestluses on - koosneb User objektidest
messages: list - nimekiri sõnumitest, mis vestlusesse kirjutatud on - koosneb Message objektidest
Message - sõnum

user: User - sõnumi autor
content: str - sõnumi sisu
reactions: int - sõnumi reaktsioonide kogus
Igal klassil on __init__(self, ...)
See loob objekti vastavalt klassi nõuetele

Funktsioonid
write_message(user: User, chat: Chat, content: str) -> None
Loo uus sõnum, mille autor (user) ja sisu (content) on ette antud, ja pane see etteantud vestluse (chat) sõnumite hulka. Vanemad sõnumid peavad olema listis esimesed. Sõnumi saab kirjutada vestlusesse ainult siis kui autor on juba vestluses olemas.

delete_message(chat: Chat, message: Message) -> None
Kui sõnum on vestluses, siis kustuta see ära. (Sõnum ise ei pea ära kustuma - see lihtsalt ei tohi vestluses olla).

get_messages_by_user(user: User, chat: Chat) -> list
Tagasta vestlusest kõik sõnumid, mille autoriks on etteantud kasutaja.

react_to_last_message(chat: Chat) -> None
Kui vestluses on sõnumeid, siis suurenda viimase sõnumi reaktsioone ühe võrra.

find_most_reacted_message(chat: Chat) -> Message
Tagasta antud vestluse kõige rohkemate reaktsioonidega sõnum. Kui kahel sõnumil on võrdselt reaktsioone, tagasta nendest hilisem.

count_reactions_in_chat(chat: Chat) -> int
Tagasta vestluse kõikide sõnumite summaarne reaktsioonide arv.

count_reactions_by_chat(chats: list) -> dict
Tagasta sõnastik, kus võtmeteks on vestluste nimed ja väärtusteks iga vestluse summaarne reaktsioonide arv.

## PR07 - Train
Ülesande jaoks on realiseeride väga lihtustatud rongi "süsteemi" koos reisijatega.

Klass Train
__init__(self, passengers: list, carriages: int, seats_in_carriage: int): Konstruktor, mis salvestab rongi sisse tulevate reisijate nimekirja ning vagunite arvu ja ühes vagunis olevate istmete arvu instantsimuutujatesse.

get_seats_in_train(self) -> int: Meetod, mis tagastab istmete koguarvu terve rongi peale.

get_number_of_passengers(self) -> int: Meetod, mis tagastab rongi sisse tulevate reisijate arvu.

get_passengers_in_carriages(self) -> dict: Meetod, mis tagastab sõnastiku vagunite ja reisijate andmetega. Selle sõnastiku võtmeks peaks olema vaguni number stringina (algab 1-st) ning väärtuseks on list selles vagunis olevate reisijatega. NB! Siin reisija seat võtme väärtuseks peab jääma ainult istekoha number ilma vaguni numbrita. Reisija objekt peab olema "konverteeritud" sõnastikuks kujul {'id': (reisija objekti id), 'seat': (reisija objekti istekoht)}. Kui vagunis pole reisijaid, siis see kirje igal juhul peab sõnastikus olema, aga väärtuseks jääb lihtsalt tühi list.

Klass Passenger
__init__(self, passenger_id: str, seat: str) Konstruktor, mis salvestab reisija unikaalse identifikaatori (id) ning istekoha numbri.

__dict__(self): Spetsiaalne meetod (vt OOP: Spetsiaalsed Meetodid), mis võimaldab muuta klassi objekti soovitud kujuks, antud juhul sõnastiku kujuks. Meetodil on oma teatud loogika juba olemas, aga kui kirjutada see enda klassi, siis saab see loogika ümber kirjutada endale sobivaks. Antud ülesandes soovime, et sõnastikuks muutmisel saaksime reisija objekti kujul {'id': (reisija objekti id), 'seat': (reisija objekti istekoht)}. Kuigi sõnastikuks muutmise võib teha otse selles koodi osas, kus see on vajalik, õppime ikkagi selles ülesandes spetsiaalse meetodi kasutamist. Lisaks, see teeb koodi natuke ilusamaks :).
NB! Otse Passenger klassis ei tohiks implementeerida mingit erilist loogikat, millist võib olla sooviksite kasutada mõnes teises meetodis. Näiteks, istekoht peab vaikimisi olema salvestatud reisijal algsel kujul ehk vaguni_nr-istekoha_nr

Tingimused
Reisijad sattuvad rongi klassi sisse listina. Reisija on Passenger klassi instants, millel on olemas unikaalse id ja istekoha number. Istekoha number tuleb kujul vaguni_nr-istekoha_nr, näiteks 2-14.
Kui mingil reisijal on selline istekoha number, mida ei ole rongis olemas (nt vaguni number on suurem, kui vagunite arv üldse või istekoha number on suurem, kui istekohtade arv vagunis), siis see reisija eemaldatakse reisijate nimekirjast.
Nõuded ja vihjed
Instantsimuutujate väärtust tagastavatele ehk getter meetoditele tuleb lisada @property dekoraator. See võimaldab luua vastava property jaoks ka setter meetodi, mis kutsutakse välja klassi siseselt automaatselt, kui selle muutuja väärtus muudetakse. Selles setter meetodis tavaliselt kirjeldatakse sisendandmete töötlemise loogika, mille järgi eraldatakse näiteks valed/katkised jne andmed maha ära ning instantsimuutujasse salvestatakse need juba õigel kujul.
On soovitatav kirjeldada reisijate andmete kontrollimise loogika eraldi privaatse meetodina, mis kutsutakse välja nimekirja määramisel.
Andmete kuvamisel kõik numbrilised väärtused antud ülesande raames on stringi kujul (nt vaguni ja istekoha numbrid jne).

## EX07 - Train Station
Ülesande jaoks on realiseeride väga lihtustatud rongijaama süsteemi koos rongidega ja reisijatega

Klass Passenger
__init__(self, passenger_id: str, seat: str) Konstruktor, mis salvestab reisija unikaalse identifikaatori (id) ning istekoha numbri.
Klass Train
__init__(self, train_id: str, carriages: int, seats_in_carriage: int): Konstruktor, mis salvestab rongi unikaalse id ning vagunite arvu ja ühes vagunis olevate istmete arvu instantsimuutujatesse.

get_seats_in_train(self) -> int: Meetod, mis tagastab istmete koguarvu terve rongi peale.

get_number_of_passengers(self) -> int: Meetod, mis tagastab rongi reisijate arvu.

get_passengers_in_carriages(self) -> dict: Meetod, mis tagastab sõnastiku vagunite ja reisijate andmetega. Selle sõnastiku võtmeks peaks olema vaguni number stringina (algab 1-st) ning väärtuseks on list selles vagunis olevate reisijatega. Kui vagunis pole reisijaid, siis see võti peab sõnastikus olema, aga väärtuseks jääb lihtsalt tühi list.

add_passenger(self, passenger: Passenger): Meetod, mis lisab reisija rongi peale rongijaamast. Kui reisijad satuvad rongijaama, siis nad tuleb kohe jagada rongidesse kasutades seda meetodit vastavalt reisijal oleva rongi id väärtusele.

Klass TrainStation
__init__(self, trains: list, passengers: list): Konstruktor, mis salvestab rongijaama sisse tulevate rongide ja reisijate nimekirjad instantsimuutujatesse.
Kohe rongijaama loomisel tuleb hakata jagama reisijad rongidesse vastavalt reisija istekoha numbris oleva rongi identifikaatorile ehk otsida vastav rong nimekirjast. Kui sellist rongi ei ole olemas või reisija ei õnnestunud rongi lisada, siis see reisija eemaldatakse rongijaamas olevast reisijate nimekirjast.

get_station_overview(self) -> list: Meetod, mis tagastab hetke seisundi aruande kõikiest rongijaamas olevatest rongidest listi kujul ning rongi info on sõnastiku kujul: [{'train_id': 'AB', 'carriages': 5, 'seats': 'kinni/kokku'}, {...}]. Ise vali, kuidas teed rongi objekist sellise sõnastiku kuju - kas rongi klassis või otse selles meetodis. (Vt. OOP: spetsiaalsed meetodid)

get_number_of_passengers(self): -> int: Meetod, mis tagastab rongijaama (rongidesse paigutatud) reisijate koguarvu.

Tingimused
Reisijad satuvad rongi klassi sisse listina. Reisija on Passenger klassi instants, millel on olemas unikaalne id ja istekoha number. Istekoha number tuleb kujul rongi_id-vaguni_nr-istekoha_nr, näiteks AB-2-14.
Kui mingil reisijal on selline istekoha number, mida ei ole rongis olemas (nt vaguni number on suurem, kui vagunite arv üldse või istekoha number on suurem, kui istekohtade arv vagunis), siis see reisija eemaldatakse reisijate nimekirjast ning ei lisata konkreetse rongi reisijate nimekirja.
Kui lisatava reisja istekoht on juba mõne teise reisija poolt võetud, siis seda reisjat rongi ei lisata ning eemaldatakse rongijaama reisijate nimekirjast.
Nõuded ja vihjed
Instantsimuutujate väärtust tagastavatele ehk getter meetoditele tuleb lisada @property dekoraator. See võimaldab luua vastava property jaoks ka setter meetodi, mis kutsutakse välja klassi siseselt automaatselt, kui selle muutuja väärtus muudetakse. Selles setter meetodis tavaliselt kirjeldatakse sisendandmete töötlemise loogika, mille järgi eraldatakse näiteks valed/katkised jne andmed ning instantsimuutujasse salvestatakse need juba õigel kujul.
On soovitatav kirjeldada reisijate andmete kontrollimise loogika eraldi privaatse meetodina, mis kutsutakse välja nimekirja määramisel.
Andmete kuvamisel kõik numbrilised väärtused antud ülesande raames on stringi kujul (nt vaguni ja istekoha numbrid jne).

## PR08 - Secret Garden
Secret Garden
Sinu kätte on usaldatud salajane sõnum, milles on ära märgitud pääsud salajastesse paikadesse. Sõnumit saab lahti muukida ainult ühe kindla võtmega. Sinu ülesandeks on sõnum dešifreerida ning leida peidetud sissepääsud.

Testfaili võtmeks on 'Fat Chocobo'

Klass Decoder
__init__(self, file: str, key: str) Konstruktor, mis salvestab faili ning salavõtme instantsimuutujatesse.

read_code_from_file(self) -> list Meetod, mis loeb read failist listi. Faili kodeering on utf-8. Iga rea lõpus olev tühja rea märk ('\n') tuleb eemaldada.

decode_from_base64(data: str) -> str Staatiline meetod, mis dekodeerib base64 kodeeringus sõne utf-8 formaati.

calculate_cipher_step(self) -> int Meetod, mis arvutab šifri nihke. Nihke arvutamiseks tuleb võtta võtme iga tähe UNICODE väärtus ning need kokku liita.

decode(self) -> list Meetod, mis dešifreerib failis olevad read vastava võtmega ning tagastab dešifreeritud sõned listina. Faili sisu on base64 formaadis. Sõne dešifreerimiseks tuleb igast sõne tähest leida tema UNICODE väärtus ning sellest lahutada nihke väärtus. Saadud vahest tuleb leida jääk jagades 255-ga. Edasi tuleb saadud arv uuesti karakteriks teha ning uus sõne moodustada. Meetod tagastab listi nendest sõnedest.

Klass SecretGarden
__init__(self, file: str, key: str) Konstruktor, mis salvestab faili ning salavõtme instantsimuutujatesse.

decode_messages(self) -> list Meetod, mis kasutab dekoodrit ja tagastab listi dešifreeritud sõnedest.

find_secret_locations(self) -> list Meetod, mis tagastab listi leitud peidetud sissepääsudest tuple kujul. Kõikide juhiste (sõnede) formaat on sama.

Esimesel real on alguspunkt (nt: 1;4). Esimene koordinaat näitab asukohta ida-lääs suunal. Teine koordinaat näitab asukohta põhi-lõuna suunal. Koordinaadid kasvavad põhi-ida suunas.
Teine rida on tühi.
Kolmandal real on hulk ühetähelisi käskusid, mis suunas tuleb liikuda. Alguspunkti ja käskude abiga tuleb leida salajane sissepääs ning see lisada ennikute listi.
Käskudeks on:
N - põhjasuunas liikumiseks
E - idasuunas liikumiseks
W - läänesuunas liikumiseks
S - lõunasuunas liikumiseks

## PR09 - Inception

Tuleb kirjutada viis funktsiooni(rekursioon).

countdown(n: int): Funktsioon saab ette arvu ja tagastab stardiloenduse listi sellest arvust kuni nullini. Negatiivsed arvud tagastavad tühja listi.
add_commas(n: int) Funktsioon saab ette täisarvu ning tagastab sõne kus iga kolmas suurusjärk on eraldatud komaga.
stonks(coins: float, rate: int, years: int): Funktsioon saab ette raha algväärtuse, tootluse ja aastad, palju raha väärtust kogub, ning tagastab raha lõppväärtuse.
quic_mafs(a: int, b: int): Funktsioon saab ette kaks täisarvu a ja b ning järgib selliseid reegleid:
i) Kui a = 0 või b = 0, tagasta [a,b]. Vastasel korral, mine punkt (ii) juurde;
ii) Kui a ≥ 2*b, siis a = a - 2*b, ja korda sammu (i). Vastasel korral, mine punkt (iii) juurde;
iii) Kui b ≥ 2*a, siis b = b - 2*a, ja korda sammu (i). Vastasel korral, tagasta [a,b].
sum_squares(nested_list): Funktsioon saab ette juhuslikult pesastatud listi listidest ja täisarvudest ja tagastab kõikide täisarvude ruutude summa.

NB! selles ülesandes on keelatud kasutada for ja while tsükleid!

## EX09 - Meta
Üks koht kus rekursioon tuleb kasuks on fraktaalide joonistamine, sest see on visuaalne viis näida rekursiooni metamaagilisest võlust.

Sisu
See ülesanne koosneb kahest osast. Ülesanne poleks raske kui saaks kasutada for ja while tsükleid, aga ei saa, see on keelatud. Eesmärk on kasutada rekursiooni igal pool kuni see lõpuks loogiline tundub. Veel on keelatud kasutada replace() sõne funktsiooni, muidu poleks lõbus.

I
Esimeses osas tuleb sul genereerida pilt kahendpuust. tree(length): Peab joonistama oma otsa kaks 3/5 korda väisemat puud mille vahel on 120 kraadi, välja arvatud siis kui pikkus on väiksem kui 5 pikslit.

II
Teises osas tuleb joonistada Dragon Curve gerereerides rekursiivselt juhised Turtlele järgimiseks kasutades Lindenmayer'i süsteemi

Start lause: "Fa"
Reegel 1: "a" -> "aRbFR"
Reegel 2: "b" -> "LFaLb"
Rekursiooni sügavusega 1 oleks lause: "FaRbFR"
Rekursiooni sügavusega 2 oleks lause: "FaRbFRRLFaLbFR"
Turtle saab sisse lause kus on eemaldatud "a" ja "b" tähed, ning hakkab järgima reegleid.

F -> Otse
R -> Mine paremale
L -> Mine vasakule
Selleks tuleb kirjutada neli rekursiivset funktsiooni

apply_dragon_rules(string): Vahetab lihtsalt rekursiivselt kõik "a" ja "b" tähed vastavalt "aRbFR" ja "LFaLb" vastu välja ning tagastab saadud sõne.
curve(string, depth): Söödab seda sõne rekursiivselt depth korda apply_dragon_rules() funktsiooni.
format_curve(string): eemaldab rekursiivselt sõnest kõik "a" ja "b" tähed
draw_dragon(s, l): Käib rekursiivselt kõik sõne tähed läbi ja vastavalt tähele liigutab Turtle't

## PR11 - Shapes

Ülesandes vaatleme alamklasside kasutamist Paint programmi ja kujundite näitel.

Klass Shape
See on üldine kujundi klass. Kõik teised kujundid on selle kujundi alamklassid. Ehk siis võib mõelda nii, et see klass on justkui ühisosa kõikide kujundite jaoks. Meie ülesandes on igal kujundil värv. Seega hoiame värvi info selles klassis. Samuti kirjeldame ära meetodi get_area, aga selle sisu me siin ei oska kirjeldada (sest see sõltub konkreetsest kujundist). Seega, siin kirjeldame ära meetodi, mida alamklassid saavad üle kirjutada (override). See tähendab seda, et kui ma näiteks kutsun ringi objektil välja get_area meetodit, siis kasutatakse Circle klassis kirjeldatud sisu. Üle kirjutamisega n-ö peidame ülemklassi sama nimega meetodi ära (katame justkui ära).

Meetodid:

__init__(self, color: str) - värv (sõne) salvestatakse kujundi külge
set_color(self, color: str) - muudab kujundi värvi
get_color(self) -> str - tagastab kujundi värvi
get_area(self) -> float - arvutab kujundi pindala ja tagasab selle

Kujundi alamklass ring Circle
Ülemklass märgitakse klassi kirjeldades ära selle nime taga sulgudes: class Circle(Shape). Üldiselt saab ülemklassi muutujate ja meetodite poole pöörduda self.name ja self.method(). Aga see ei õnnestu, kui alamklassis on sama nimega meetod method(). Sellisel juhul tuleb kasutada: super().method()

Meetodid:

__init__(self, color: str, radius: float) - Värv ja raadius salvestatakse ringi objektis. Kuna ülemklassis on värv olemas, kasutame seda. Selleks, et pöörduda ülemklassi mõne meetodi poole, saame kasutada abifunktsioon super(). See ise viitab ülemklassile ja sealt saame välja kutsuda näiteks super().__init__(). See siis pöördub ülemklassi konstruktori poole. Sinna konstruktorisse tuleb värv ette anda.
get_area(self) -> float - siin implementeerime ringi pindala arvutamise: PI * R^2
__repr__(self) -> str - tagastab Circle (r: {radius}, color: {color}).

Kujundi alamklass Square
Meetodid:

__init__(self, color: str, side: float) - värv ja küljepikkus salvestatakse objektis.
get_area(self) -> float - pindala arvutatakse side * side
__repr__(self) -> str - tagastab Square (a: {side}, color: {color})

Ristkülik Rectangle
See klass puudub mallis, tuleb luua analoogselt eelmisele kahele.
Meetodid:

__init__(self, color: str, length: float, width: float) - värv, pikkus ja laius salvestatakse objektis.
get_area(self) -> float - pindala arvutatakse length * width
__repr__(self) -> str - tagastab Rectangle (l: {length}, w: {width}, color: {color})

Paint
Siin opereerime kujunditega.

Meetodid:

__init__(self) - siin tuleks luua valmis kujundite list. Kõik kujundid tuleks hoida ühes listis.
add_shape(self, shape: Shape) -> None - kujund lisatakse antud Paint objekti kujundite listi.
get_shapes(self) -> list - tagastab kõik kujundid nende lisamise järjekorras
calculate_total_area(self) -> float - arvutab ja tagastab kõikide kujundite pindalade summa
get_circles(self) -> list, get_squares(self) -> list, get_rectangles(self) -> list - tagastavad vastavalt ringide, ruutude ja ristkülikute listid nende lisamise järjekorras

## EX11 - Bank
Bank
Ülesande eesmärgiks oleks realiseerida üks väike infosüsteem panga jaoks.


Klass Person
__init__(self, first_name: str, last_name: str, age: int): Konstruktor, mis salvestab isiku ees- ja perekonnanime ning vanuse samanimelistesse instantsimuutujatesse. Isikul peab olema ka self.bank_account muutuja, mis on vaikimisi None.

Kui objekti loomisel või pärast muudetakse vanuse väärtus nulliks või sellest väiksemaks, siis tuleb visata PersonError erind. Seda tuleks kontrollida vanuse setteri sees.

full_name Tagastab inimese täisnime. See atribuut on read-only ehk selle väärtust otse muuta ei saa.

Person objekti printides peab nägema sellist sõnet: Eesnimi Perekonnanimi. Selle jaoks on kasulik __repr__(self) funktsioon.

Klass Bank
__init__(self, name: str): Konstruktor, mis salvestab panga nime samanimelisse instantsimuutujatesse. Tuleb deklareerida ka self.customers ja self.transactions muutujaid, mis on tühjad järjendid.

add_customer(self, person: Person) -> bool: Lisab panka uue kliendi ning määrab person objekti pangakontoks uue konto null euroga. Lisada saab ainult juhul, kui inimene ei ole juba self.customers nimekirjas. Edukal lisamisel tuleb tagastada True, muul juhul False.

remove_customer(self, person: Person) -> bool: Eemaldab kliendi pangast ning muudab person objekti bank_account muutuja None'iks. Edukal eemaldamisel (kui inimene on self.customers nimekirjas) tuleb tagastada True, muul juhul False.

__repr__(self) -> str: Tagastab panga nime.

Klass Transaction
__init__(self, amount: float, date: datetime.date, sender_account: 'Account', receiver_account: 'Account', from_atm: bool): Argumendid tuleb salvestada samanimelistesse instantsimuutujatesse.

__repr__(self) -> str: Kui tehing on pangaautomaadis tehtud, siis tuleb tagasta sõne kujul ([summa] €) ATM. Vastasel juhul tuleb tagastada sõne ([summa] €) [saatja täisnimi] -> [saaja täisnimi].

Klass Account
__init__(self, balance: float, person: Person, bank: 'Bank'): Argumendi balance väärtus tuleb salvestada read-only (ilma setterita) samanimelisse @property atribuuti. Ülejäänud argumendid tuleb salvestada samanimelistesse instantsimuutujatesse. Lisaks on vaja deklareerida tühi järjend self.transactions.

Samuti tuleb luua kontonumbri jaoks self.number instantsimuutuja ning konstruktoris määrata ka sellele suvaline väärtus. Kõik kontonumbrid peaksid olema unikaalsed (vihje: tuleb kasutada random moodulit). Samas ei pea garanteerima, et absoluutselt igaüks oleks unikaalne, piisab kui nendest on vähemalt 99% erinev. Kontonumber peab olema 20 tähemärki pikk ja algama tähtedega EE, ülejäänud tähemärgid on numbrid (nt EE042296257446649537).

deposit(self, amount: float, from_atm: bool = True): Meetod kontojäägi suurendamiseks. Kui amount on väiksem või võrdne nulliga, siis tuleb visata TransactionError erind.

Kui tehing on tehtud sularahaautomaadi kaudu, siis tuleb luua uus Transaction objekt ning tehingu saatjaks ja saajaks tuleb määrata see sama Account objekt. Tehingu date'iks tuleb määrata antud hetkel tänane kuupäev kasutades datetime'i moodulit. Seejärel tuleb tehingu objekt lisada praeguse konto ja selle panga transactions järjenditesse.

withdraw(self, amount: float, from_atm: bool = True): Meetod kontojäägi vähendamiseks. Kui amount on väiksem või võrdne nulliga või amount on kontojäägist suurem, siis tuleb visata TransactionError erind.

Kui tehing on tehtud sularahaautomaadi kaudu, siis tuleb luua uus Transaction objekt ning tehingu saatjaks ja saajaks tuleb määrata see sama Account objekt. Tehingu amount peab olema negatiivne ning date'iks tuleb määrata antud hetkel tänane kuupäev kasutades datetime'i moodulit. Seejärel tuleb tehingu objekt lisada praeguse konto ja selle panga transactions järjenditesse.

transfer(self, amount: float, receiver_account: 'Account'): Meetod pangaülekannete tegemiseks kahe inimese vahel.

Kui raha saaja asub teises pangas, siis tuleb saatjalt võtta 5 € teenustasu. Teenustasu kohta ei looda eraldi uut tehingu objekti ega suurendata selle võrra ühegi Transaction objekti amount väärtust (päris pangas pole ka näha teenustasu kontoväljavõttes eraldiseisva tehinguna). Kui saatjal pole teenustasu maksimiseks piisavalt raha või kui receiver_account on sama objekt, kui saatja, siis tuleb visata TransactionError erind.

Siin oleks mõistlik kasutada withdraw() ja deposit() meetodeid. Sel juhul tuleks withdraw() välja kutsuda praeguses objektis ja deposit() saaja objektis.

Loob uue Transaction objekti ning tehingu saatjaks tuleb määrata see sama Account objekt ja saajaks receiver_account objekt. Tehingu amount peab olema alati positiivne. Tehingu objekt tuleb lisada saatja, raha saaja ning panga/pankade transactions järjenditesse. Kui saaja ja saatja on eri pankades, siis tuleb tehing lisada mõlemasse panka. Kuupäeva kohta kehtib sama reegel, mis varemgi.

account_statement(self, from_date: datetime.date, to_date: datetime.date) -> list: Meetod konto väljavõtte/ülevaate jaoks. Tagastab kõik tehingud antud perioodi vältel (otspunktid kaasaarvatud).

debit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float: Meetod, mis tagastab kõikide sissetulekute summa antud perioodi vältel (otspunktid kaasaarvatud).

credit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float: Meetod, mis tagastab kõikide väljaminekute summa antud perioodi vältel (otspunktid kaasaarvatud). Tagastatav arv peab olema negatiivne.

net_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float: Meetod, mis tagastab sissetulekute ja väljaminekute vahe antud perioodi vältel (otspunktid kaasaarvatud). Siin oleks mõistlik kasutada kahte eelmist meetodit.

__repr__(self) -> str: Tagastab pangakonto numbri

## PR12 - Zoo

Sisseehitatud funktsioonid ja anonüümsed funktsioonid
Listides olevate andmete töötlemine on programmerimise maailmas üks üsna igapäevane tegevus, mistõttu on erinevate listi töötlemist hõlmavate tegevuste jaoks väga paljudes programmeerimiskeeltes olemas erinevad sisseehitatud funktsioonid. Selles ülesandes tutvume mõnega neist funktsioonidest ja harjutame nende kasutamist. Sisseehitatud meetodite hingeeluga hästi kursis olemine võib päästa nii mõnestki tsüklite pusast, parandades koodi loetavust ja võimaldades soovitud asjad kiiremini kirja saada.

Siin ülesandes käsiteldavad sisseehitatud funktsioonid:

map()
filter()
reduce()
max()
min()
sorted()
Nende sisseehitatud funktsioonide edukaks kasutamiseks tuleb teadlik olla ka anonüümse funktsiooni mõistest.

NB: Siin ülesandes ära palun kasuta list comprehensionit ega for-tsüklit. Kõik funktsioonid tuleks lahendada üherealise lahendusega, mis kasutab nimetatud sisseehitatud funktsioone ja anonüümseid funktsioone.

Selles ülesandes on meil tegemist loomaaiaga, kus elavad erinevad loomaliigid. Selleks, et kõik loomad saaks ära kirjeldatud, on defineeritud Animal objekt, mis kannab endas infot loomaliigi kohta. Ülesandes tuleb realiseerida järgmised funktsioonid:

find_smallest_animal_by_weight - tuleb leida kõige väiksem (kõige vähem kaaluv) loom. Kuna soovime kõige väiksemat võimalikku varianti, siis võtame võrdlusel aluseks looma kaaluvahemiku alguse. Kui mitme looma kaal on sama suur, tuleks tagastada see loom, kes esineb listis enne.

list_species_and_scientific_names - tuleb teha list tuple'itest, kus esimesel kohal on looma liigi nimi ja teisel kohal liigi teaduslik nimi.

find_how_many_pumpkins_are_needed_to_feed_animals - meie loomaaed kogub headelt inimestelt talveks loomadele kõrvitsaid. Kuigi loomad kindlasti ainult kõrvitsatest ei toitu, oleks huvitav teada, mitu kõrvitsat meil läheks vaja, et loomad ainult nendega üle talve ära toita. Kõrvitsa keskmine kaal on 3kg, talv kestab 90 päeva. Selle arvutuse jaoks võtame arvesse, et meil on igast liigist looma loomaaias 2 tükki ja et iga loom sööb 6% jagu oma (kaaluvahemiku keskmine) kehakaalust kõrvitsaid. Lihatoidulised loomad kõrvitsaid ei söö. Tagastada tuleb kõrvitsate hulk (ümmardatud üles).

sort_alphabetically_by_scientific_name - tuleb tagastada loomade nimekiri sorteerituna teadusliku nime alusel tähestiku järjekorras.

find_animals_whose_height_is_less_than - tuleb tagastada loomad, kelle turjakõrgus on väiksem või võrdne etteantud kõrgusega (meetrites)

filter_animals_based_on_diet - tuleb tagastada vastava toitumisharjumusega loomad. Toitumisharjumustest on võimalikud 3 varianti - herbivorous, omnivorous ja carnivorous.

find_animal_with_longest_lifespan - tuleb tagastada kõige pikema võimaliku elueaga loom. Kui mitmel loomal on sama pikim võimalik eluiga, siis tuleb tagastada see, kes leitakse listist esimesena.

create_animal_descriptions - tahame loomaaias loomade juurde panna nende kohta väikesed kirjeldused. Selleks tuleks teha iga loomaliigi kohta kirjeldav sõne järgmises formaadis. Nurksulgudes olev parameeter tuleks asendada infoga Animal objektist. "[Species name] ([Scientific name]) lives in [habitat] and its diet is [diet]. These animals can live up to [max age] years and they weigh between [min weight] kg and [max weight] kg as adults."

## PR13 - Google API
Sul on üks Google Spreadsheetsi tabel, kuhu on kirjutatud suur hulk linke erinevatele Youtube playlistidele ning sa tahad kõik neis sisalduvad laulud panna kokku üheks suureks playlistiks. Sinu ülesandeks on teha programm, mis suudaks nende playlistide linkide põhjal leida lingid iga lauluni, mis nendes plalistides sisaldub. Selleks on vaja implementeerida kaks funktsiooni.

Spreadsheetist playlistid
get_links_from_spreadsheet(id: str, token: str): Funktsioon peab tagastama listi stringidest, kus iga string on link Youtube playlistile
id: Spreadsheeti ID, kust on vaja linke lugeda
token: failinimi, kust saab lugeda spreadsheetile ligi pääsemiseks vajalikud andmed (pickle abil)
Spreadsheetis on üks table ning kõik lingid on tulbas A ridadel 1-n.

Google Spreadsheetsi API kasutamise õpetuse leiad siit: https://developers.google.com/sheets/api/quickstart/python

Playlistist laulud
get_links_from_playlist(link: str, developer_key: str): Funktsioon peab tagastama listi videote linkidest, mis on antud lingiga playlistis.

Youtube Data API kasutamise õpetuse leiad siit: https://developers.google.com/youtube/v3/docs
Developer key / API key kohta saad lugeda siit: https://developers.google.com/maps/documentation/javascript/get-api-key

NB: Kuigi antud on lingid API kasutamise õpetusteni, ei ole nende kasutamine otseselt kohustuslik.

## PR14 - Robot API

Selle ülesande eesmärgiks on kasutada roboti programmeerimiseliidest, et juhtida virtuaalset robotit.

Virtuaalse robotiga tuleb sõita otse kuni on ületatud roboti algse suunaga risti olev joon. Seejärel tuleb jääda seisma maksimaalselt 10 cm kaugusel joonest. Kuna joone täpne kaugus ei ole teada, siis tuleb kasutada andureid, et seda sõites tuvastada. Joone tuvastamiseks on teada, et joon on musta värvi ja taust on valget värvi.

Ülesande detailid
Selle ülesande eesmärk on õppida selgeks järgnevad oskused:

API kirjeldusest ja näidiskoodist endale vajalike meetodite leidmine,
roboti tegevustsükli disainimine,
Lihtsustused
Antud ülesandes jookseb kood simuleeritud keskkonnas. Keskkonnas on rakendatud lihtsustusi ja kaugusandureid ei ole võimalik kasutada. Samuti puudub robotil käpp antud ülesandes.

Koodi ülesehitus
Tester impordib teie koodi otse sisse, mis tähendab, et jooksevad ka funktsioonide välised koodi osad. Koodi osad mis pn if __name__ == "__main__" sees ei jookse testris. Samuti ei ole konkreetsete funktsioonide implementeerimine siin ülesandes kohustuslik.

Selleks, et saada informatsiooni platsi kohta on vaja lugeda line_sensor'eid. Saadud tulemuste alusel tuleb määrata roboti rataste kiirused. Kui teie kood on lõpetanud ülesande täitmise, siis peab kutsuma PiBot objektil done() meetodit.

Tagasiside
Seda, kas kood töötab, saab teada alles siis kui see testrisse saata. Katseeksitus meetodil roboti toimimisest aru saamine on selle ülesande osa.

Koodi esitamisel tagastab tester teie meilile lisaks tavalistele testide tulemustele ka 2 faili.

Oma koodi toimimist saab analüüsida läbi tagastatavate failide:

robot_path.png - pilt roboti teekonnast ja maailmast roboti ümber. (Punane joon on roboti teekond, rohelised täpid on joone anduri mõõtmiste kohad)
robot_output.txt - teksti fail koodi poolt välja prinditud väärtustega (maksimaalselt 500 rida või 40000 tähemärki).

## EX14 - Line Following
Selle ülesandes tuleb kasutada roboti programmeerimisliidest, et juhtida virtuaalset robotit.

Virtuaalse robotiga tuleb sõita mööda musta joont kuni joone lõpuni. Arvestama peab sellega, et joon ei ole sirge. Seega tuleb vältida joonest eemale sõitmist. Joone lõpus tuleb jääda seisma ja kutsuda PiBot objektil done() meetodit. Joone tuvastamiseks on teada, et joon on musta värvi ja taust on valget värvi. Samuti lihtsustab ülesannet teadmine, et robot alustab joone peal ja õiges suunas.

Ülesande detailid
Lihtsustused
Antud ülesandes jookseb kood simuleeritud keskkonnas. Keskkonnas on rakendatud lihtsustusi ning kaugusandureid ei ole võimalik kasutada. Samuti puudub robotil käpp antud ülesandes.

Koodi ülesehitus
Tester impordib teie koodi otse sisse, mis tähendab, et jooksevad ka funktsioonide välised koodi osad. Koodi osad, mis on if __name__ == "__main__" sees, ei jookse testris. Samuti ei ole konkreetsete funktsioonide implementeerimine siin ülesandes kohustuslik.

Selleks, et saada informatsiooni platsi kohta, on vaja lugeda line_sensor'eid. Saadud tulemuste alusel tuleb määrata roboti rataste kiirused. Kui teie kood on lõpetanud ülesande täitmise, siis peab kutsuma PiBot objektil done() meetodit.

Tagasiside
Seda, kas kood töötab, saab teada alles siis, kui see testrisse saata. Katseeksitus meetodil roboti toimimisest aru saamine on selle ülesande osa.

Koodi esitamisel tagastab tester teie meilile lisaks tavalistele testide tulemustele ka 2 faili.

Oma koodi toimimist saab analüüsida läbi tagastatavate failide:

robot_path.png - pilt roboti teekonnast ja maailmast roboti ümber. (Punane joon on roboti teekond, rohelised täpid on joone anduri mõõtmiste kohad)
robot_output.txt - teksti fail koodi poolt välja prinditud väärtustega (maksimaalselt 500 rida või 40000 tähemärki).
