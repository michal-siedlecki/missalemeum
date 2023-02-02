import re

from constants import common as constants

TITLES = {
    constants.FERIA: 'Feria',
    constants.TEMPORA_EPI1_0: 'Uroczystość Świętej Rodziny Jezusa, Maryi i Józefa',
    constants.TEMPORA_EPI1_1: 'Poniedziałek po 1 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI1_2: 'Wtorek po 1 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI1_3: 'Środa po 1 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI1_4: 'Czwartek po 1 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI1_5: 'Piątek po 1 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI1_6: 'Sobota po 1 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI2_0: '2 Niedziela po Objawieniu',
    constants.TEMPORA_EPI2_1: 'Poniedziałek po 2 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI2_2: 'Wtorek po 2 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI2_3: 'Środa po 2 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI2_4: 'Czwartek po 2 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI2_5: 'Piątek po 2 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI2_6: 'Sobota po 2 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI3_0: '3 Niedziela po Objawieniu',
    constants.TEMPORA_EPI3_1: 'Poniedziałek po 3 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI3_2: 'Wtorek po 3 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI3_3: 'Środa po 3 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI3_4: 'Czwartek po 3 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI3_5: 'Piątek po 3 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI3_6: 'Sobota po 3 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI4_0: '4 Niedziela po Objawieniu',
    constants.TEMPORA_EPI4_1: 'Poniedziałek po 4 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI4_2: 'Wtorek po 4 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI4_3: 'Środa po 4 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI4_4: 'Czwartek po 4 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI4_5: 'Piątek po 4 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI4_6: 'Sobota po 4 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI5_0: '5 Niedziela po Objawieniu',
    constants.TEMPORA_EPI5_1: 'Poniedziałek po 5 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI5_2: 'Wtorek po 5 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI5_3: 'Środa po 5 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI5_4: 'Czwartek po 5 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI5_5: 'Piątek po 5 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI5_6: 'Sobota po 5 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI6_0: '6 Niedziela po Objawieniu',
    constants.TEMPORA_EPI6_1: 'Poniedziałek po 6 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI6_2: 'Wtorek po 6 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI6_3: 'Środa po 6 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI6_4: 'Czwartek po 6 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI6_5: 'Piątek po 6 Niedzieli po Objawieniu',
    constants.TEMPORA_EPI6_6: 'Sobota po 6 Niedzieli po Objawieniu',
    constants.TEMPORA_QUADP1_0: 'Niedziela Siedemdziesiątnicy',
    constants.TEMPORA_QUADP1_1: 'Poniedziałek po Niedzieli Siedemdziesiątnicy',
    constants.TEMPORA_QUADP1_2: 'Wtorek po Niedzieli Siedemdziesiątnicy',
    constants.TEMPORA_QUADP1_3: 'Środa po Niedzieli Siedemdziesiątnicy',
    constants.TEMPORA_QUADP1_4: 'Czwartek po Niedzieli Siedemdziesiątnicy',
    constants.TEMPORA_QUADP1_5: 'Piątek po Niedzieli Siedemdziesiątnicy',
    constants.TEMPORA_QUADP1_6: 'Sobota po Niedzieli Siedemdziesiątnicy',
    constants.TEMPORA_QUADP2_0: 'Niedziela Sześćdziesiątnicy',
    constants.TEMPORA_QUADP2_1: 'Poniedziałek po Niedzieli Sześćdziesiątnicy',
    constants.TEMPORA_QUADP2_2: 'Wtorek po Niedzieli Sześćdziesiątnicy',
    constants.TEMPORA_QUADP2_3: 'Środa po Niedzieli Sześćdziesiątnicy',
    constants.TEMPORA_QUADP2_4: 'Czwartek po Niedzieli Sześćdziesiątnicy',
    constants.TEMPORA_QUADP2_5: 'Piątek po Niedzieli Sześćdziesiątnicy',
    constants.TEMPORA_QUADP2_6: 'Sobota po Niedzieli Sześćdziesiątnicy',
    constants.TEMPORA_QUADP3_0: 'Niedziela Pięćdziesiątnicy',
    constants.TEMPORA_QUADP3_1: 'Poniedziałek po Niedzieli Pięćdziesiątnicy',
    constants.TEMPORA_QUADP3_2: 'Wtorek po Niedzieli Pięćdziesiątnicy',
    constants.TEMPORA_QUADP3_3: 'Środa Popielcowa',
    constants.TEMPORA_QUADP3_4: 'Czwartek po Popielcu',
    constants.TEMPORA_QUADP3_5: 'Piątek po Popielcu',
    constants.TEMPORA_QUADP3_6: 'Sobota po Popielcu',
    constants.TEMPORA_QUAD1_0: '1 Niedziela Wielkiego Postu',
    constants.TEMPORA_QUAD1_1: 'Poniedziałek po 1 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD1_2: 'Wtorek po 1 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD1_3: 'Środa Suchych Dni Wielkiego Postu',
    constants.TEMPORA_QUAD1_4: 'Czwartek po 1 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD1_5: 'Piątek Suchych Dni Wielkiego Postu',
    constants.TEMPORA_QUAD1_6: 'Sobota Suchych Dni Wielkiego Postu',
    constants.TEMPORA_QUAD2_0: '2 Niedziela Wielkiego Postu',
    constants.TEMPORA_QUAD2_1: 'Poniedziałek po 2 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD2_2: 'Wtorek po 2 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD2_3: 'Środa po 2 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD2_4: 'Czwartek po 2 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD2_5: 'Piątek po 2 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD2_6: 'Sobota po 2 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD3_0: '3 Niedziela Wielkiego Postu',
    constants.TEMPORA_QUAD3_1: 'Poniedziałek po 3 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD3_2: 'Wtorek po 3 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD3_3: 'Środa po 3 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD3_4: 'Czwartek po 3 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD3_5: 'Piątek po 3 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD3_6: 'Sobota po 3 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD4_0: '4 Niedziela Wielkiego Postu (Niedziela Laetare)',
    constants.TEMPORA_QUAD4_1: 'Poniedziałek po 4 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD4_2: 'Wtorek po 4 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD4_3: 'Środa po 4 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD4_4: 'Czwartek po 4 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD4_5: 'Piątek po 4 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD4_6: 'Sobota po 4 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD5_0: '1 Niedziela Męki Pańskiej',
    constants.TEMPORA_QUAD5_1: 'Poniedziałek po Niedzieli Męki Pańskiej',
    constants.TEMPORA_QUAD5_2: 'Wtorek po Niedzieli Męki Pańskiej',
    constants.TEMPORA_QUAD5_3: 'Środa po Niedzieli Męki Pańskiej',
    constants.TEMPORA_QUAD5_4: 'Czwartek po Niedzieli Męki Pańskiej',
    constants.TEMPORA_QUAD5_5: 'Piątek po Niedzieli Męki Pańskiej',
    constants.TEMPORA_QUAD5_6: 'Sobota po Niedzieli Męki Pańskiej',
    constants.TEMPORA_QUAD6_0: 'Niedziela Palmowa',
    constants.TEMPORA_QUAD6_1: 'Wielki Poniedziałek',
    constants.TEMPORA_QUAD6_2: 'Wielki Wtorek',
    constants.TEMPORA_QUAD6_3: 'Wielka Środa',
    constants.TEMPORA_QUAD6_4: 'Wielki Czwartek',
    constants.TEMPORA_QUAD6_5: 'Wielki Piątek',
    constants.TEMPORA_QUAD6_6: 'Wielka Sobota',
    constants.TEMPORA_PASC0_0: 'Niedziela Zmartwychwstania',
    constants.TEMPORA_PASC0_1: 'Poniedziałek Wielkanocny',
    constants.TEMPORA_PASC0_2: 'Wtorek Wielkanocny',
    constants.TEMPORA_PASC0_3: 'Środa Wielkanocna',
    constants.TEMPORA_PASC0_4: 'Czwartek Wielkanocny',
    constants.TEMPORA_PASC0_5: 'Piątek Wielkanocny',
    constants.TEMPORA_PASC0_6: 'Sobota Biała',
    constants.TEMPORA_PASC1_0: 'Niedziela Biała',
    constants.TEMPORA_PASC1_1: 'Poniedziałek po Niedzieli Białej',
    constants.TEMPORA_PASC1_2: 'Wtorek po Niedzieli Białej',
    constants.TEMPORA_PASC1_3: 'Środa po Niedzieli Białej',
    constants.TEMPORA_PASC1_4: 'Czwartek po Niedzieli Białej',
    constants.TEMPORA_PASC1_5: 'Piątek po Niedzieli Białej',
    constants.TEMPORA_PASC1_6: 'Sobota po Niedzieli Białej',
    constants.TEMPORA_PASC2_0: '2 Niedziela po Wielkanocy',
    constants.TEMPORA_PASC2_1: 'Poniedziałek po 2 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC2_2: 'Wtorek po 2 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC2_3: 'Środa po 2 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC2_4: 'Czwartek po 2 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC2_5: 'Piątek po 2 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC2_6: 'Sobota po 2 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC3_0: '3 Niedziela po Wielkanocy',
    constants.TEMPORA_PASC3_1: 'Poniedziałek po 3 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC3_2: 'Wtorek po 3 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC3_3: 'Środa po 3 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC3_4: 'Czwartek po 3 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC3_5: 'Piątek po 3 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC3_6: 'Sobota po 3 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC4_0: '4 Niedziela po Wielkanocy',
    constants.TEMPORA_PASC4_1: 'Poniedziałek po 4 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC4_2: 'Wtorek po 4 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC4_3: 'Środa po 4 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC4_4: 'Czwartek po 4 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC4_5: 'Piątek po 4 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC4_6: 'Sobota po 4 Niedzieli po Wielkanocy',
    constants.TEMPORA_PASC5_0: '5 Niedziela po Wielkanocy',
    constants.TEMPORA_PASC5_1: 'Litanie mniejsze',
    constants.TEMPORA_PASC5_2: 'Litanie mniejsze',
    constants.TEMPORA_PASC5_3: 'Wigilia Wniebowstąpienia Pańskiego',
    constants.TEMPORA_PASC5_4: 'Wniebowstąpienie Pańskie',
    constants.TEMPORA_PASC5_5: 'Piątek po Wniebowstąpieniu',
    constants.TEMPORA_PASC5_6: 'Sobota po Wniebowstąpieniu',
    constants.TEMPORA_PASC6_0: 'Niedziela po Wniebowstąpieniu',
    constants.TEMPORA_PASC6_1: 'Poniedziałek po Niedzieli po Wniebowstąpieniu',
    constants.TEMPORA_PASC6_2: 'Wtorek po Niedzieli po Wniebowstąpieniu',
    constants.TEMPORA_PASC6_3: 'Środa po Niedzieli po Wniebowstąpieniu',
    constants.TEMPORA_PASC6_4: 'Czwartek po Niedzieli po Wniebowstąpieniu',
    constants.TEMPORA_PASC6_5: 'Piątek po Niedzieli po Wniebowstąpieniu',
    constants.TEMPORA_PASC6_6: 'Wigilia Zesłania Ducha Świętego',
    constants.TEMPORA_PASC7_0: 'Niedziela Zesłania Ducha Świętego',
    constants.TEMPORA_PASC7_1: 'Poniedziałek w Oktawie Zesłania Ducha Świętego',
    constants.TEMPORA_PASC7_2: 'Wtorek w Oktawie Zesłania Ducha Świętego',
    constants.TEMPORA_PASC7_3: 'Środa Suchych Dni po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PASC7_4: 'Czwartek w Oktawie Zesłania Ducha Świętego',
    constants.TEMPORA_PASC7_5: 'Piątek Suchych Dni po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PASC7_6: 'Sobota Suchych Dni po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT01_0: 'Uroczystość Trójcy Przenajświętszej',
    constants.TEMPORA_PENT01_1: 'Poniedziałek po Niedzieli w Oktawie Zesłania Ducha Świętego',
    constants.TEMPORA_PENT01_2: 'Wtorek po Niedzieli w Oktawie Zesłania Ducha Świętego',
    constants.TEMPORA_PENT01_3: 'Środa po Niedzieli w Oktawie Zesłania Ducha Świętego',
    constants.TEMPORA_PENT01_4: 'Uroczystość Bożego Ciała',
    constants.TEMPORA_PENT01_5: 'Piątek po Niedzieli w Oktawie Zesłania Ducha Świętego',
    constants.TEMPORA_PENT01_6: 'Sobota po Niedzieli w Oktawie Zesłania Ducha Świętego',
    constants.TEMPORA_PENT02_0: '2 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT02_1: 'Poniedziałek po 2 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT02_2: 'Wtorek po 2 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT02_3: 'Środa po 2 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT02_4: 'Czwartek po 2 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT02_5: 'Uroczystość Najświętszego Serca Pana Jezusa',
    constants.TEMPORA_PENT02_6: 'Sobota po 2 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT03_0: '3 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT03_1: 'Poniedziałek po 3 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT03_2: 'Wtorek po 3 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT03_3: 'Środa po 3 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT03_4: 'Czwartek po 3 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT03_5: 'Piątek po 3 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT03_6: 'Sobota po 3 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT04_0: '4 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT04_1: 'Poniedziałek po 4 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT04_2: 'Wtorek po 4 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT04_3: 'Środa po 4 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT04_4: 'Czwartek po 4 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT04_5: 'Piątek po 4 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT04_6: 'Sobota po 4 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT05_0: '5 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT05_1: 'Poniedziałek po 5 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT05_2: 'Wtorek po 5 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT05_3: 'Środa po 5 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT05_4: 'Czwartek po 5 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT05_5: 'Piątek po 5 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT05_6: 'Sobota po 5 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT06_0: '6 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT06_1: 'Poniedziałek po 6 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT06_2: 'Wtorek po 6 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT06_3: 'Środa po 6 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT06_4: 'Czwartek po 6 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT06_5: 'Piątek po 6 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT06_6: 'Sobota po 6 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT07_0: '7 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT07_1: 'Poniedziałek po 7 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT07_2: 'Wtorek po 7 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT07_3: 'Środa po 7 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT07_4: 'Czwartek po 7 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT07_5: 'Piątek po 7 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT07_6: 'Sobota po 7 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT08_0: '8 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT08_1: 'Poniedziałek po 8 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT08_2: 'Wtorek po 8 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT08_3: 'Środa po 8 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT08_4: 'Czwartek po 8 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT08_5: 'Piątek po 8 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT08_6: 'Sobota po 8 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT09_0: '9 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT09_1: 'Poniedziałek po 9 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT09_2: 'Wtorek po 9 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT09_3: 'Środa po 9 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT09_4: 'Czwartek po 9 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT09_5: 'Piątek po 9 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT09_6: 'Sobota po 9 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT10_0: '10 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT10_1: 'Poniedziałek po 10 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT10_2: 'Wtorek po 10 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT10_3: 'Środa po 10 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT10_4: 'Czwartek po 10 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT10_5: 'Piątek po 10 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT10_6: 'Sobota po 10 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT11_0: '11 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT11_1: 'Poniedziałek po 11 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT11_2: 'Wtorek po 11 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT11_3: 'Środa po 11 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT11_4: 'Czwartek po 11 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT11_5: 'Piątek po 11 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT11_6: 'Sobota po 11 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT12_0: '12 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT12_1: 'Poniedziałek po 12 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT12_2: 'Wtorek po 12 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT12_3: 'Środa po 12 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT12_4: 'Czwartek po 12 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT12_5: 'Piątek po 12 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT12_6: 'Sobota po 12 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT13_0: '13 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT13_1: 'Poniedziałek po 13 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT13_2: 'Wtorek po 13 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT13_3: 'Środa po 13 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT13_4: 'Czwartek po 13 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT13_5: 'Piątek po 13 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT13_6: 'Sobota po 13 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT14_0: '14 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT14_1: 'Poniedziałek po 14 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT14_2: 'Wtorek po 14 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT14_3: 'Środa po 14 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT14_4: 'Czwartek po 14 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT14_5: 'Piątek po 14 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT14_6: 'Sobota po 14 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT15_0: '15 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT15_1: 'Poniedziałek po 15 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT15_2: 'Wtorek po 15 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT15_3: 'Środa po 15 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT15_4: 'Czwartek po 15 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT15_5: 'Piątek po 15 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT15_6: 'Sobota po 15 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT16_0: '16 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT16_1: 'Poniedziałek po 16 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT16_2: 'Wtorek po 16 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT16_3: 'Środa po 16 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT16_4: 'Czwartek po 16 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT16_5: 'Piątek po 16 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT16_6: 'Sobota po 16 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT17_0: '17 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT17_1: 'Poniedziałek po 17 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT17_2: 'Wtorek po 17 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT17_3: 'Środa po 17 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT17_4: 'Czwartek po 17 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT17_5: 'Piątek po 17 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT17_6: 'Sobota po 17 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT18_0: '18 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT18_1: 'Poniedziałek po 18 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT18_2: 'Wtorek po 18 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT18_3: 'Środa po 18 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT18_4: 'Czwartek po 18 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT18_5: 'Piątek po 18 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT18_6: 'Sobota po 18 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT19_0: '19 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT19_1: 'Poniedziałek po 19 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT19_2: 'Wtorek po 19 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT19_3: 'Środa po 19 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT19_4: 'Czwartek po 19 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT19_5: 'Piątek po 19 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT19_6: 'Sobota po 19 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT20_0: '20 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT20_1: 'Poniedziałek po 20 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT20_2: 'Wtorek po 20 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT20_3: 'Środa po 20 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT20_4: 'Czwartek po 20 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT20_5: 'Piątek po 20 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT20_6: 'Sobota po 20 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT21_0: '21 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT21_1: 'Poniedziałek po 21 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT21_2: 'Wtorek po 21 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT21_3: 'Środa po 21 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT21_4: 'Czwartek po 21 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT21_5: 'Piątek po 21 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT21_6: 'Sobota po 21 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT22_0: '22 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT22_1: 'Poniedziałek po 22 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT22_2: 'Wtorek po 22 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT22_3: 'Środa po 22 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT22_4: 'Czwartek po 22 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT22_5: 'Piątek po 22 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT22_6: 'Sobota po 22 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT23_0: '23 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT23_1: 'Poniedziałek po 23 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT23_2: 'Wtorek po 23 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT23_3: 'Środa po 23 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT23_4: 'Czwartek po 23 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT23_5: 'Piątek po 23 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT23_6: 'Sobota po 23 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT_3: 'Środa Suchych Dni Wrześniowych',
    constants.TEMPORA_PENT_5: 'Piątek Suchych Dni Wrześniowych',
    constants.TEMPORA_PENT_6: 'Sobota Suchych Dni Wrześniowych',
    constants.TEMPORA_PENT24_0: '24 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT24_1: 'Poniedziałek po 24 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT24_2: 'Wtorek po 24 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT24_3: 'Środa po 24 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT24_4: 'Czwartek po 24 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT24_5: 'Piątek po 24 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT24_6: 'Sobota po 24 Niedzieli po Zesłaniu Ducha Świętego',
    constants.TEMPORA_ADV1_0: '1 Niedziela Adwentu',
    constants.TEMPORA_ADV1_1: 'Poniedziałek po 1 Niedzieli Adwentu',
    constants.TEMPORA_ADV1_2: 'Wtorek po 1 Niedzieli Adwentu',
    constants.TEMPORA_ADV1_3: 'Środa po 1 Niedzieli Adwentu',
    constants.TEMPORA_ADV1_4: 'Czwartek po 1 Niedzieli Adwentu',
    constants.TEMPORA_ADV1_5: 'Piątek po 1 Niedzieli Adwentu',
    constants.TEMPORA_ADV1_6: 'Sobota po 1 Niedzieli Adwentu',
    constants.TEMPORA_ADV2_0: '2 Niedziela Adwentu',
    constants.TEMPORA_ADV2_1: 'Poniedziałek po 2 Niedzieli Adwentu',
    constants.TEMPORA_ADV2_2: 'Wtorek po 2 Niedzieli Adwentu',
    constants.TEMPORA_ADV2_3: 'Środa po 2 Niedzieli Adwentu',
    constants.TEMPORA_ADV2_4: 'Czwartek po 2 Niedzieli Adwentu',
    constants.TEMPORA_ADV2_5: 'Piątek po 2 Niedzieli Adwentu',
    constants.TEMPORA_ADV2_6: 'Sobota po 2 Niedzieli Adwentu',
    constants.TEMPORA_ADV3_0: '3 Niedziela Adwentu (Niedziela Gaudete)',
    constants.TEMPORA_ADV3_1: 'Poniedziałek po 3 Niedzieli Adwentu',
    constants.TEMPORA_ADV3_2: 'Wtorek po 3 Niedzieli Adwentu',
    constants.TEMPORA_ADV3_3: 'Środa Suchych Dni Adwentu',
    constants.TEMPORA_ADV3_4: 'Czwartek po 3 Niedzieli Adwentu',
    constants.TEMPORA_ADV3_5: 'Piątek Suchych Dni Adwentu',
    constants.TEMPORA_ADV3_6: 'Sobota Suchych Dni Adwentu',
    constants.TEMPORA_ADV4_0: '4 Niedziela Adwentu',
    constants.TEMPORA_ADV4_1: 'Poniedziałek po 4 Niedzieli Adwentu',
    constants.TEMPORA_ADV4_2: 'Wtorek po 4 Niedzieli Adwentu',
    constants.TEMPORA_ADV4_3: 'Środa po 4 Niedzieli Adwentu',
    constants.TEMPORA_ADV4_4: 'Czwartek po 4 Niedzieli Adwentu',
    constants.TEMPORA_ADV4_5: 'Piątek po 4 Niedzieli Adwentu',
    constants.TEMPORA_NAT1_0: 'Niedziela w Oktawie Bożego Narodzenia',
    constants.TEMPORA_NAT1_1: 'Dzień w Oktawie Bożego Narodzenia',
    constants.TEMPORA_NAT2_0: 'Najświętszego Imienia Jezus',
    constants.SANCTI_10_DU: 'Chrystusa Króla',
    constants.TEMPORA_EPI1_0A: '1 Niedziela po Objawieniu',
    constants.TEMPORA_PENT01_0A: '1 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_C_10A: '1 Msza o N. M. P. – Rorate',
    constants.COMMUNE_C_10A: '1 Msza o N. M. P. – Rorate',
    constants.TEMPORA_C_10B: '2 Msza o N. M. P. – Vultum Tuum',
    constants.COMMUNE_C_10B: '2 Msza o N. M. P. – Vultum Tuum',
    constants.TEMPORA_C_10C: '3 Msza o N. M. P. – Salve, Sancta Parens',
    constants.COMMUNE_C_10C: '3 Msza o N. M. P. – Salve, Sancta Parens',
    constants.TEMPORA_C_10PASC: '4 Msza o N. M. P. – Salve, Sancta Parens',
    constants.COMMUNE_C_10PASC: '4 Msza o N. M. P. – Salve, Sancta Parens',
    constants.TEMPORA_C_10T: '5 Msza o N. M. P. – Salve, Sancta Parens',
    constants.COMMUNE_C_10T: '5 Msza o N. M. P. – Salve, Sancta Parens',
    constants.SANCTI_01_01: 'Oktawa Bożego Narodzenia',
    constants.SANCTI_01_06: 'Objawienie Pańskie',
    constants.SANCTI_01_13: 'Wspomnienie Chrztu Pańskiego',
    constants.SANCTI_01_14: 'Św. Hilarego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_01_15: 'Św. Pawła, Pierwszego Pustelnika, Wyznawcy',
    constants.SANCTI_01_16: 'Św. Marcelego I, Papieża i Męczennika',
    constants.SANCTI_01_17: 'Św. Antoniego, Opata',
    constants.SANCTI_01_18: 'Św. Pryski, Dziewicy',
    constants.SANCTI_01_19: 'Śś. Mariusza, Marty, Audifaksa i Abachuma',
    constants.SANCTI_01_20: 'Śś. Fabiana, Papieża i Sebastiana, Męczenników',
    constants.SANCTI_01_21: 'Św. Agnieszki, Dziewicy i Męczennicy',
    constants.SANCTI_01_22: 'Śś. Wincentego i Anastazego, Męczenników',
    constants.SANCTI_01_23: 'Św. Rajmunda z Pennafort, Wyznawcy',
    constants.SANCTI_01_24: 'Św. Tymoteusza, Biskupa i Męczennika',
    constants.SANCTI_01_25: 'Nawrócenie św. Pawła, Apostoła',
    constants.SANCTI_01_26: 'Św. Polikarpa, Biskupa i Męczennika',
    constants.SANCTI_01_27: 'Św. Jana Chryzostoma, Wyznawcy, Biskupa i Doktora Kościoła',
    constants.SANCTI_01_28: 'Św. Piotra Nolasco, Wyznawcy',
    constants.SANCTI_01_29: 'Św. Franciszka Salezego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_01_30: 'Św. Martyny, Dziewicy i Męczennicy',
    constants.SANCTI_01_31: 'Św. Jana Bosco, Wyznawcy',
    constants.SANCTI_02_01: 'Św. Ignacego, Biskupa i Męczennika',
    constants.SANCTI_02_02: 'Oczyszczenie N. M. P.',
    constants.SANCTI_02_03: 'Św. Błażeja, Biskupa i Męczennika',
    constants.SANCTI_02_04: 'Św. Andrzeja Corsini, Biskupa i Wyznawcy',
    constants.SANCTI_02_05: 'Św. Agaty, Dziewicy i Męczennicy',
    constants.SANCTI_02_06: 'Św. Tytusa, Biskupa i Wyznawcy',
    constants.SANCTI_02_07: 'Św. Romualda, Opata',
    constants.SANCTI_02_08: 'Św. Jana z Maty, Wyznawcy',
    constants.SANCTI_02_09: 'Św. Cyryla Aleksandryjskiego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_02_10: 'Św. Scholastyki',
    constants.SANCTI_02_11: 'Objawienie się N. M. P. Niepokalanie Poczętej w Lourdes',
    constants.SANCTI_02_12: 'Siedmiu Założycieli Zakonu Serwitów N. M. P., Wyznawców',
    constants.SANCTI_02_14: 'Św. Walentego, Kapłana i Męczennika',
    constants.SANCTI_02_15: 'Śś. Faustyna i Jowity, Męczenników',
    constants.SANCTI_02_18: 'Św. Symeona, Biskupa i Męczennika',
    constants.SANCTI_02_22: 'Katedry św. Piotra Apostoła',
    constants.SANCTI_02_23: 'Św. Piotra Damiana, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_02_24: 'Św. Macieja Apostoła',
    constants.SANCTI_02_27: 'Św. Gabriela od Matki Bożej Bolesnej',
    constants.SANCTI_03_04: 'Św. Kazimierza, Wyznawcy',
    constants.SANCTI_03_06: 'Śś. Perpetui i Felicyty, Męczennic',
    constants.SANCTI_03_07: 'Św. Tomasza z Akwinu, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_03_08: 'Św. Jana Bożego, Wyznawcy',
    constants.SANCTI_03_09: 'Św. Franciszki Rzymianki, Wdowy',
    constants.SANCTI_03_10: 'Śś. Czterdziestu Męczenników',
    constants.SANCTI_03_12: 'Św. Grzegorza Wielkiego, Papieża, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_03_15PL: 'Św. Klemensa Marii Dworzaka (Hofbauera)',
    constants.SANCTI_03_17: 'Św. Patryka, Biskupa i Wyznawcy',
    constants.SANCTI_03_18: 'Św. Cyryla Jerozolimskiego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_03_19: 'Św. Józefa, Oblubieńca N. M. P.',
    constants.SANCTI_03_21: 'Św. Benedykta, Opata',
    constants.SANCTI_03_24: 'Św. Gabriela Archanioła',
    constants.SANCTI_03_25: 'Zwiastowanie N. M. P.',
    constants.SANCTI_03_27: 'Św. Jana Damasceńskiego, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_03_28: 'Św. Jana Kapistrana, Wyznawcy',
    constants.SANCTI_04_02: 'Św. Franciszka z Pauli, Wyznawcy',
    constants.SANCTI_04_04: 'Św. Izydora, Biskupa, Wyznawcy i Dokotra Kościoła',
    constants.SANCTI_04_05: 'Św. Wincentego Fereriusza, Wyznawcy',
    constants.SANCTI_04_11: 'Św. Leona Wielkiego, Papieża, Wyznawcy i Dokotra Kościoła',
    constants.SANCTI_04_13: 'Św. Hermenegilda, Męczennika',
    constants.SANCTI_04_14: 'Św. Justyna, Męczennika',
    constants.SANCTI_04_17: 'Św. Aniceta, Papieża i Męczennika',
    constants.SANCTI_04_21: 'Św. Anzelma, Biskupa, Wyznawcy i Dokotra Kościoła',
    constants.SANCTI_04_22: 'Śś. Sotera i Kajusa, Papieży i Męczenników',
    constants.SANCTI_04_23: 'Św. Jerzego, Męczennika',
    constants.SANCTI_04_23PL: 'Św. Wojciecha, Biskupa i Męczennika',
    constants.SANCTI_04_24: 'Św. Fidelisa z Sigmaringen, Męczennika',
    constants.SANCTI_04_25: 'Św. Marka Ewangelisty',
    constants.SANCTI_04_26: 'Śś. Kleta i Marcelina, Papieży i Męczenników',
    constants.SANCTI_04_27: 'Św. Piotra Kanizjusza, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_04_28: 'Św. Pawła od Krzyża, Wyznawcy',
    constants.SANCTI_04_29: 'Piotra z Werony, Męczenika',
    constants.SANCTI_04_30: 'Św. Katarzyny Sieneńskiej, Dziewicy',
    constants.SANCTI_05_01: 'Św. Józefa Robotnika, Oblubieńca N. M. P',
    constants.SANCTI_05_02: 'Św. Atanazego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_05_03: 'Śś. Aleksandra, Ewencjusza i Teodula, Męczenników',
    constants.SANCTI_05_03PL: 'N. M. P., Królowej Polski, Głównej Patronki Polski',
    constants.SANCTI_05_04: 'Św. Moniki, Wdowy',
    constants.SANCTI_05_05: 'Św. Piusa V, Papieża i Wyznawcy',
    constants.SANCTI_05_07: 'Św. Stanisława, Biskupa i Męczennika',
    constants.SANCTI_05_08PL: 'Św. Stanisława, Biskupa i Męczennika',
    constants.SANCTI_05_09: 'Św. Grzegorza z Nazjanu, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_05_10: 'Św. Antonina, Biskupa i Wyznawcy',
    constants.SANCTI_05_11: 'Świętych Filipa i Jakuba, Apostołów',
    constants.SANCTI_05_12: 'Świętych Nereusza, Achillesa, Domicylli i Pankracego, Męczenników',
    constants.SANCTI_05_13: 'Św. Roberta Bellarmina, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_05_14: 'Św. Bonifacego, Męczennika',
    constants.SANCTI_05_15: 'Św. Jana Chrzciciela de la Salle, Wyznawcy',
    constants.SANCTI_05_16: 'Św. Ubalda, Biskupa i Wyznawcy',
    constants.SANCTI_05_16PL: 'Św. Andrzeja Boboli, Męczennika',
    constants.SANCTI_05_17: 'Św. Paschalisa Baylon, Wyznawcy',
    constants.SANCTI_05_18: 'Św. Wenancjusza, Męczennika',
    constants.SANCTI_05_19: 'Św. Piotra Celestyna, Papieża i Wyznawcy',
    constants.SANCTI_05_20: 'Św. Bernardyna ze Sieny, Wyznawcy',
    constants.SANCTI_05_24PL: 'N. M. P. Wspomożycielki Wiernych',
    constants.SANCTI_05_25: 'Św. Grzegorza VII, Papieża i Wyznawcy',
    constants.SANCTI_05_26: 'Św. Filipa Nereusza, Wyznawcy',
    constants.SANCTI_05_27: 'Św. Bedy Czcigodnego, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_05_28: 'Św. Augustyna z Canterbury, Biskupa i Wyznawcy',
    constants.SANCTI_05_29: 'Św. Marii Magdaleny Pazzi, Dziewicy',
    constants.SANCTI_05_30: 'Św. Feliksa I, Papieża i Męczennika',
    constants.SANCTI_05_31: 'N. M. P. Królowej',
    constants.SANCTI_06_01: 'Św. Anieli Merici, Dziewicy',
    constants.SANCTI_06_01PL: 'Bł. Jakuba Strzemię, Biskupa i Wyznawcy',
    constants.SANCTI_06_02: 'Śś. Marcelina i Piotra, Męczenników oraz Erazma, Biskupa',
    constants.SANCTI_06_04: 'Św. Franciszka Caracciolo, Wyznawcy',
    constants.SANCTI_06_05: 'Św. Bonifacego, Biskupa i Męczennika',
    constants.SANCTI_06_06: 'Św. Norberta, Biskupa i Wyznawcy',
    constants.SANCTI_06_09: 'Śś. Pryma i Felicjana, Męczenników',
    constants.SANCTI_06_10: 'Św. Małgorzaty, Królowej Szkockiej, Wdowy',
    constants.SANCTI_06_10PL: 'Bł. Bogumiła, Biskupa i Wyznawcy',
    constants.SANCTI_06_11: 'Św. Barnaby, Apostoła',
    constants.SANCTI_06_12: 'Św. Jana z Facundo, Wyznawcy',
    constants.SANCTI_06_13: 'Św. Antoniego z Padwy, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_06_14: 'Św. Bazylego Wielkiego, Wyznawcy, Biskupa i Doktora Kościoła',
    constants.SANCTI_06_15: 'Śś. Wita, Modesta i Krescencji, Męczenników',
    constants.SANCTI_06_17: 'Św. Grzegorza Barbarigo, Biskupa i Wyznawcy',
    constants.SANCTI_06_18: 'Św. Efrema, Diakona, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_06_19: 'Św. Juliany Falconieri, Dziewicy',
    constants.SANCTI_06_20: 'Św. Sylweriusza, Papieża i Męczennika',
    constants.SANCTI_06_21: 'Św. Alojzego Gonzagi, Wyznawcy',
    constants.SANCTI_06_22: 'Św. Paulina, Biskupa i Wyznawcy',
    constants.SANCTI_06_23: 'Wigilia Narodzenia Św. Jana Chrzciciela',
    constants.SANCTI_06_24: 'Narodzenie Św. Jana Chrzciciela',
    constants.SANCTI_06_25: 'Św. Wilhelma, Opata',
    constants.SANCTI_06_26: 'Śś. Jana i Pawła, Męczenników',
    constants.SANCTI_06_28: 'Wigilia śś. Apostołów Piotra i Pawła',
    constants.SANCTI_06_29: 'Świętych Piotra i Pawła, Apostołów',
    constants.SANCTI_06_30: 'Wspomnienie św. Pawła, Apostoła',
    constants.SANCTI_07_01: 'Uroczystość Najdroższej Krwi Pana Naszego Jezusa Chrystusa',
    constants.SANCTI_07_02: 'Nawiedzenia N. M. P.',
    constants.SANCTI_07_03: 'Św. Ireneusza, Biskupa i Męczennika',
    constants.SANCTI_07_05: 'Św. Antoniego Marii Zaccaria, Wyznawcy',
    constants.SANCTI_07_07: 'Śś. Cyryla i Metodego, Biskupów i Wyznawców',
    constants.SANCTI_07_08: 'Św. Elżbiety, Królowej i Wdowy',
    constants.SANCTI_07_10: 'Siedmiu Braci Męczenników oraz Śś. Rufiny i Sekundy, Dziewic i Męczennic',
    constants.SANCTI_07_11: 'Św. Piusa I, Papieża i Męczennika',
    constants.SANCTI_07_12: 'Św. Jana Gwalberta, Opata',
    constants.SANCTI_07_14: 'Św. Bonawentury, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_07_15: 'Św. Henryka, Cesarza i Wyznawcy',
    constants.SANCTI_07_16: 'Wspomnienie N. M. P. z Góry Karmelu',
    constants.SANCTI_07_17: 'Św. Aleksego, Wyznawcy',
    constants.SANCTI_07_18: 'Św. Kamila de Lellis',
    constants.SANCTI_07_18PL: 'Bł. Szymona z Lipnicy, Wyznawcy',
    constants.SANCTI_07_19: 'Św. Wincentego a Paulo, Wyznawcy',
    constants.SANCTI_07_20: 'Św. Hieronima Emiliani, Wyznawcy',
    constants.SANCTI_07_20PL: 'Bł. Czesława, Wyznawcy',
    constants.SANCTI_07_21: 'Św. Wawrzyńca z Brindisi, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_07_22: 'Św. Marii Magdaleny, Pokutnicy',
    constants.SANCTI_07_23: 'Św. Apolinarego, Biskupa i Męczennika',
    constants.SANCTI_07_24: 'Św. Krystyny, Dziewicy i Męczennicy',
    constants.SANCTI_07_24PL: 'Bł. Kingi, Dziewicy',
    constants.SANCTI_07_25: 'Św. Jakuba, Apostoła',
    constants.SANCTI_07_26: 'Św. Anny, Matki N. M. P.',
    constants.SANCTI_07_27: 'Św. Pantaleona, Męczennika',
    constants.SANCTI_07_28: 'Śś. Nazariusza i Celsa, Męczenników, Wiktora I, Papieża i Męczennika, oraz Innocentego I, Papieża i Wyznawcy',
    constants.SANCTI_07_29: 'Św. Marty, Dziewicy',
    constants.SANCTI_07_30: 'Śś. Abdona i Sennena, Męczenników',
    constants.SANCTI_07_31: 'Św. Ignacego Loyoli, Wyznawcy',
    constants.SANCTI_08_01: 'Siedmiu Braci Machabejskich, Męczenników',
    constants.SANCTI_08_02: 'Św. Alfonsa Marii Liguori, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_08_04: 'Św. Dominika, Wyznawcy',
    constants.SANCTI_08_05: 'Rocznica Konsekracji N. M. P. Śnieżnej',
    constants.SANCTI_08_06: 'Przemienienie Pańskie',
    constants.SANCTI_08_07: 'Św. Kajetana, Wyznawcy',
    constants.SANCTI_08_08: 'Św. Jana Marii Vianney, Wyznawcy',
    constants.SANCTI_08_09: 'Wigilia św. Wawrzyńca, Męczennika',
    constants.SANCTI_08_10: 'Św. Wawrzyńca',
    constants.SANCTI_08_11: 'Śś. Tyburcjusza i Zuzanny, Męczenników',
    constants.SANCTI_08_12: 'Św. Klary, Dziewicy',
    constants.SANCTI_08_13: 'Śś. Hipolita i Kasjana, Męczenników',
    constants.SANCTI_08_14: 'Wigilia Wniebowzięcia N. M. P.',
    constants.SANCTI_08_15: 'Wniebowzięcie N. M. P.',
    constants.SANCTI_08_16: 'Św. Joachima, Ojca N. M. P.',
    constants.SANCTI_08_17: 'Św. Jacka, Wyznawcy',
    constants.SANCTI_08_18: 'Św. Agapita, Męczennika',
    constants.SANCTI_08_19: 'Św. Jana Eudes, Wyznawcy',
    constants.SANCTI_08_20: 'Św. Bernarda, Opata i Doktora Kościoła',
    constants.SANCTI_08_21: 'Św. Joanny Franciszki Frémiot de Chantal, Wdowy',
    constants.SANCTI_08_22: 'Uroczystość Niepokalanego Serca N. M. P.',
    constants.SANCTI_08_23: 'Św. Filipa Benicjusza, Wyznawcy',
    constants.SANCTI_08_24: 'Św. Bartłomieja, Apostoła',
    constants.SANCTI_08_25: 'Św. Ludwika, Króla i Wyznawcy',
    constants.SANCTI_08_26: 'Św. Zefiryna, Papieża i Męczennika',
    constants.SANCTI_08_26PL: 'N. M. P. Jasnogórskiej czyli Częstochowskiej',
    constants.SANCTI_08_27: 'Św. Józefa Kalasantego, Wyznawcy',
    constants.SANCTI_08_28: 'Św. Augustyna, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_08_29: 'Ścięcie Św. Jana Chrzciciela',
    constants.SANCTI_08_30: 'Św. Róży z Limy, Dziewicy',
    constants.SANCTI_08_31: 'Św. Rajmunda Nonnata, Wyznawcy',
    constants.SANCTI_09_01: 'Św. Idziego, Opata oraz Śś. Dwunastu Braci, Męczenników',
    constants.SANCTI_09_01PL: 'Bł. Bronisławy, Dziewicy',
    constants.SANCTI_09_02: 'Św. Stefana, Króla i Wyznawcy',
    constants.SANCTI_09_03: 'Św. Piusa X, Papieża i Wyznawcy',
    constants.SANCTI_09_05: 'Św. Wawrzyńca Justiniani, Biskupa i Wyznawcy',
    constants.SANCTI_09_07PL: 'Bł. Melchiora Grodzieckiego, Męczennika',
    constants.SANCTI_09_08: 'Narodzenie N. M. P.',
    constants.SANCTI_09_09: 'Św. Gorgoniusza, Męczennika',
    constants.SANCTI_09_10: 'Św. Mikołaja z Tolentynu, Wyznawcy',
    constants.SANCTI_09_11: 'Św. Prota i Jacka, Męczenników',
    constants.SANCTI_09_12: 'Najświętszego Imienia Maryi',
    constants.SANCTI_09_14: 'Podwyższenia Świętego Krzyża',
    constants.SANCTI_09_15: 'Siedmiu Boleści N. M. P.',
    constants.SANCTI_09_16: 'Św. Korneliusza, Papieża i Cypriana, Męczenników',
    constants.SANCTI_09_17: 'Stygmatów św. Franciszka, Wyznawcy',
    constants.SANCTI_09_18: 'Św. Józefa z Kupertynu, Wyznawcy',
    constants.SANCTI_09_19: 'Św. Januarego i Towarzyszy, Męczenników',
    constants.SANCTI_09_20: 'Św. Eustachego i Towarzyszy, Męczenników',
    constants.SANCTI_09_21: 'Św. Mateusza, Apostoła i Ewangelisty',
    constants.SANCTI_09_22: 'Św. Tomasza z Villanueva, Biskupa i Wyznawcy',
    constants.SANCTI_09_23: 'Św. Linusa, Papieża i Męczennika',
    constants.SANCTI_09_24: 'N. M. P. od Wykupu Jeńców',
    constants.SANCTI_09_25PL: 'Bł. Władysława z Gielniowa, Wyznawcy',
    constants.SANCTI_09_26: 'Śś. Cypriana i Justyny, Męczenników',
    constants.SANCTI_09_27: 'Św. Kosmy i Damiana, Męczenników',
    constants.SANCTI_09_28: 'Św. Wacława, Księcia i Męczennika',
    constants.SANCTI_09_29: 'Świętego Michała Archanioła',
    constants.SANCTI_09_30: 'Św. Hieronima, Kapłana, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_10_01: 'Św. Remigiusza, Biskupa i Wyznawcy',
    constants.SANCTI_10_01PL: 'Bł. Jana z Dukli',
    constants.SANCTI_10_02: 'Świętych Aniołów Stróżów',
    constants.SANCTI_10_03: 'Św. Teresy od Dzieciątka Jezus, Dziewicy',
    constants.SANCTI_10_04: 'Św. Franciszka, Wyznawcy',
    constants.SANCTI_10_05: 'Śś. Placyda i Towarzyszy, Męczenników',
    constants.SANCTI_10_06: 'Św. Brunona, Wyznawcy',
    constants.SANCTI_10_07: 'N. M. P. Różańcowej',
    constants.SANCTI_10_08: 'Św. Brygidy, Wdowy',
    constants.SANCTI_10_09: 'Św. Jana Leonardi, Wyznawcy',
    constants.SANCTI_10_10: 'Św. Franciszka Borgiasza, Wyznawcy',
    constants.SANCTI_10_11: 'Macierzyństwa N. M. P.',
    constants.SANCTI_10_13: 'Św. Edwarda, króla i wyznawcy',
    constants.SANCTI_10_14: 'Św. Kaliksta, papieża i męczennika',
    constants.SANCTI_10_15: 'Św. Teresy z Avili, Dziewicy',
    constants.SANCTI_10_16: 'Św. Jadwigi, Wdowy',
    constants.SANCTI_10_17: 'Św. Małgorzaty Marii Alacoque, Dziewicy',
    constants.SANCTI_10_18: 'Św. Łukasza, Ewangelisty',
    constants.SANCTI_10_19: 'Św. Piotra z Alkantary, Wyznawcy',
    constants.SANCTI_10_20: 'Św. Jana Kantego, Wyznawcy',
    constants.SANCTI_10_21: 'Św. Hilariona, Opata',
    constants.SANCTI_10_23: 'Św. Antoniego Marii Claret, Biskupa i Wyznawcy',
    constants.SANCTI_10_24: 'Św. Rafała Archanioła',
    constants.SANCTI_10_25: 'Śś. Chryzanta i Darii, Męczenników',
    constants.SANCTI_10_28: 'Świętych Szymona i Judy Tadeusza, Apostołow',
    constants.SANCTI_11_01: 'Uroczystość Wszystkich Świętych',
    constants.SANCTI_11_02_1: 'Dzień Zaduszny',
    constants.SANCTI_11_02_2: 'Dzień Zaduszny – Druga Msza',
    constants.SANCTI_11_02_3: 'Dzień Zaduszny – Trzecia Msza',
    constants.SANCTI_11_04: 'Św. Karola Boromeusza, Biskupa i Wyznawcy',
    constants.SANCTI_11_08: 'Świętych Czterech Ukoronowanych Męczenników',
    constants.SANCTI_11_09: 'Rocznica Konsekracji Bazyliki Najświętszego Zbawiciela na Lateranie',
    constants.SANCTI_11_10: 'Św. Andrzeja z Avellino, Wyznawcy',
    constants.SANCTI_11_11: 'Św. Marcina, Biskupa i Wyznawcy',
    constants.SANCTI_11_12: 'Św. Marcina I, Papieża i Męczennika',
    constants.SANCTI_11_13: 'Św. Dydaka, Wyznawcy',
    constants.SANCTI_11_13PL: 'Św. Stanisława Kostki, Wyznawcy',
    constants.SANCTI_11_14: 'Św. Jozafata, Biskupa i Męczennika',
    constants.SANCTI_11_15: 'Św. Alberta Wielkiego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_11_16: 'Św. Gertrudy, Dziewicy',
    constants.SANCTI_11_17: 'Św. Grzegorza Cudotwórcy, Biskupa i Wyznawcy',
    constants.SANCTI_11_18: 'Rocznica Konsekracji Bazylik Świętych Apostołów Piotra i Pawła, Apostołów',
    constants.SANCTI_11_19: 'Św. Elżbiety, Wdowy',
    constants.SANCTI_11_20: 'Św. Feliksa Walezego, Wyznawcy',
    constants.SANCTI_11_21: 'Ofiarowanie N. M. P.',
    constants.SANCTI_11_22: 'Św. Cecylii, Dziewicy i Męczennicy',
    constants.SANCTI_11_23: 'Św. Klemensa I, Papieża i Męczennika',
    constants.SANCTI_11_24: 'Św. Jana od Krzyża, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_11_25: 'Św. Katarzyny, Dziewicy i Męczennicy',
    constants.SANCTI_11_26: 'Św. Sylwestra, Opata',
    constants.SANCTI_11_29: 'Św. Saturnina, Męczennika',
    constants.SANCTI_11_30: 'Św. Andrzeja, Apostoła',
    constants.SANCTI_12_02: 'Św. Bibiany, Dziewicy i Męczennicy',
    constants.SANCTI_12_03: 'Św. Franciszka Ksawerego, Wyznawcy',
    constants.SANCTI_12_04: 'Św. Piotra Chryzologa, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_12_05: 'Św. Saby, Opata',
    constants.SANCTI_12_06: 'Św. Mikołaja, Biskupa i Wyznawcy',
    constants.SANCTI_12_07: 'Św. Ambrożego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_12_08: 'Niepokalane Poczęcie N. M. P.',
    constants.SANCTI_12_10: 'Św. Melchiadesa, Papieża i Męczennika',
    constants.SANCTI_12_11: 'Św. Damazego, Papieża i Wyznawcy',
    constants.SANCTI_12_13: 'Św. Łucji, Dziewicy i Męczennicy',
    constants.SANCTI_12_16: 'Św. Euzebiusza, Biskupa i Męczennika',
    constants.SANCTI_12_21: 'Św. Tomasza, Apostoła',
    constants.SANCTI_12_24: 'Wigilia Bożego Narodzenia',
    constants.SANCTI_12_25_1: 'Boże Narodzenie',
    constants.SANCTI_12_25_2: 'Boże Narodzenie — Msza o świcie',
    constants.SANCTI_12_25_3: 'Boże Narodzenie — Msza w dzień',
    constants.SANCTI_12_26: 'Św. Szczepana, Pierwszego Męczennika',
    constants.SANCTI_12_27: 'Św. Jana, Apostoła i Ewangelisty',
    constants.SANCTI_12_28: 'Świętych Młodzianków',
    constants.SANCTI_12_29: 'Św. Tomasza z Canterbury, Biskupa i Męczennika',
    constants.SANCTI_12_31: 'Św. Sylwestra I, papieża i wyznawcy',
    constants.VOTIVE_ANGELS: 'Msza o Aniołach',
    constants.VOTIVE_JOSEPH: 'Msza o św. Józefie',
    constants.VOTIVE_PETERPAUL: 'Msza o śś. Piotrze i Pawle Apostołach',
    constants.VOTIVE_PETERPAULP: 'Msza o śś. Piotrze i Pawle Apostołach',
    constants.VOTIVE_APOSTLES: 'Msza o wszystkich śś. Apostołach',
    constants.VOTIVE_APOSTLESP: 'Msza o wszystkich śś. Apostołach',
    constants.VOTIVE_HOLYSPIRIT: 'Msza o Duchu Świętym',
    constants.VOTIVE_HOLYSPIRIT2: 'Msza dla uproszenia łask Ducha Świętego',
    constants.VOTIVE_BLESSEDSACRAMENT: 'Msza o Najświętszym Sakramencie',
    constants.VOTIVE_JESUSETERNALPRIEST: 'Msza o Chrystusie, Najwyższym i Wiecznym Kapłanie',
    constants.VOTIVE_CROSS: 'Msza o Krzyżu Świętym',
    constants.VOTIVE_PASSION: 'Msza o Męce Pańskiej',
    constants.VOTIVE_PENT01_0: 'Msza o Trójcy Przenajświętszej',
    constants.VOTIVE_PENT02_5: 'Msza o Najświętszym Sercu Pana Jezusa',
    constants.VOTIVE_08_22: 'Msza o Niepokalanym Sercu N. M. P.',
    constants.VOTIVE_DEFUNCTORUM: 'Msza Codzienna za Zmarłych',
    constants.VOTIVE_MORTALITATIS: 'Tempore Mortalitatis',
    constants.VOTIVE_FIDEI_PROPAGATIONE: 'Msza o Rozkrzewienie Wiary',
    constants.VOTIVE_MATRIMONIUM: 'Msza za Nowożeńców'
}

VOTIVE_MASSES = [
    {'ref': 'rorate', 'id': constants.COMMUNE_C_10A, 'title': TITLES[constants.COMMUNE_C_10A],
     'tags': ['Adwent']},
    {'ref': 'vultum-tuum', 'id': constants.COMMUNE_C_10B, 'title': TITLES[constants.COMMUNE_C_10B],
     'tags': ['Od B. Narodzenia do Oczyszczenia']},
    {'ref': 'salve-sancta-parens-3', 'id': constants.COMMUNE_C_10C, 'title': TITLES[constants.COMMUNE_C_10C],
     'tags': ['Od 3 II do W. Środy']},
    {'ref': 'salve-sancta-parens-4', 'id': constants.COMMUNE_C_10PASC, 'title': TITLES[constants.COMMUNE_C_10PASC],
     'tags': ['Okres Wielkanocny']},
    {'ref': 'salve-sancta-parens-5', 'id': constants.COMMUNE_C_10T, 'title': TITLES[constants.COMMUNE_C_10T],
     'tags': ['Od Trójcy Przenajśw. do Adwentu']},
    {'ref': 'trinitas', 'id': constants.VOTIVE_PENT01_0, 'title': TITLES[constants.VOTIVE_PENT01_0],
     'tags': ['Wotywna', 'Poniedziałek']},
    {'ref': 'angelis', 'id': constants.VOTIVE_ANGELS, 'title': TITLES[constants.VOTIVE_ANGELS],
     'tags': ['Wotywna', 'Wtorek']},
    {'ref': 'joseph', 'id': constants.VOTIVE_JOSEPH, 'title': TITLES[constants.VOTIVE_JOSEPH],
     'tags': ['Wotywna', 'Środa']},
    {'ref': 'petrus-et-paulus', 'id': constants.VOTIVE_PETERPAUL, 'title': TITLES[constants.VOTIVE_PETERPAUL],
     'tags': ['Wotywna', 'Środa', 'Poza Okresem Wielkanocnym']},
    {'ref': 'petrus-et-paulus-p', 'id': constants.VOTIVE_PETERPAULP, 'title': TITLES[constants.VOTIVE_PETERPAUL],
     'tags': ['Wotywna', 'Środa', 'W Okresie Wielkanocnym']},
    {'ref': 'apostolorum', 'id': constants.VOTIVE_APOSTLES, 'title': TITLES[constants.VOTIVE_APOSTLES],
     'tags': ['Wotywna', 'Środa', 'Poza Okresem Wielkanocnym']},
    {'ref': 'apostolorum-p', 'id': constants.VOTIVE_APOSTLESP, 'title': TITLES[constants.VOTIVE_APOSTLES],
     'tags': ['Wotywna', 'Środa', 'W Okresie Wielkanocnym']},
    {'ref': 'spiritus-sanctus', 'id': constants.VOTIVE_HOLYSPIRIT, 'title': TITLES[constants.VOTIVE_HOLYSPIRIT],
     'tags': ['Wotywna', 'Czwartek']},
    {'ref': 'spiritus-sanctus-2', 'id': constants.VOTIVE_HOLYSPIRIT2, 'title': TITLES[constants.VOTIVE_HOLYSPIRIT2],
     'tags': ['Wotywna', 'Czwartek']},
    {'ref': 'eucharistiae-sacramento', 'id': constants.VOTIVE_BLESSEDSACRAMENT, 'title': TITLES[constants.VOTIVE_BLESSEDSACRAMENT],
     'tags': ['Wotywna', 'Czwartek']},
    {'ref': 'aeterno-sacerdote', 'id': constants.VOTIVE_JESUSETERNALPRIEST, 'title': TITLES[constants.VOTIVE_JESUSETERNALPRIEST],
     'tags': ['Wotywna', 'Czwartek']},
    {'ref': 'sancta-cruce', 'id': constants.VOTIVE_CROSS, 'title': TITLES[constants.VOTIVE_CROSS],
     'tags': ['Wotywna', 'Piątek']},
    {'ref': 'passio', 'id': constants.VOTIVE_PASSION, 'title': TITLES[constants.VOTIVE_PASSION],
     'tags': ['Wotywna', 'Piątek']},
    {'ref': 'cordis-jesu', 'id': constants.VOTIVE_PENT02_5, 'title': TITLES[constants.VOTIVE_PENT02_5],
     'tags': ['Wotywna', 'Piątek']},
    {'ref': 'cordis-mariae', 'id': constants.VOTIVE_08_22, 'title': TITLES[constants.VOTIVE_08_22],
     'tags': ['Wotywna', 'Pierwsza sobota']},
    {'ref': 'fidei-propagatione', 'id': constants.VOTIVE_FIDEI_PROPAGATIONE, 'title': TITLES[constants.VOTIVE_FIDEI_PROPAGATIONE],
     'tags': ['Wotywna', 'W różnych potrzebach']},
    {'ref': 'matrimonium', 'id': constants.VOTIVE_MATRIMONIUM, 'title': TITLES[constants.VOTIVE_MATRIMONIUM],
     'tags': ['Wotywna']},
    {'ref': 'defunctorum', 'id': constants.VOTIVE_DEFUNCTORUM, 'title': TITLES[constants.VOTIVE_DEFUNCTORUM],
     'tags': []},
    {'ref': 'tempore-mortalitatis', 'id': constants.VOTIVE_MORTALITATIS, 'title': TITLES[constants.VOTIVE_MORTALITATIS],
     'tags': ['W czasie śmiertelności lub zarazy']}
]

SECTION_LABELS = {
    'Communicantes': 'Communicantes',
    'CommunioP': 'Antyfona na Komunię (Okres Wielkanocny)',
    'Communio': 'Antyfona na Komunię',
    'Evangelium': 'Ewangelia',
    'GradualeP': 'Graduał',
    'Graduale': 'Graduał',
    'Introitus': 'Introit',
    'Lectio': 'Lekcja',
    'OffertoriumP': 'Antyfona na Ofiarowanie (Okres Wielkanocny)',
    'Offertorium': 'Antyfona na Ofiarowanie',
    'Oratio': 'Kolekta',
    'Commemoratio Oratio': 'Kolekta Wspomnienia',
    'Postcommunio': 'Pokomunia',
    'Commemoratio Postcommunio': 'Pokomunia Wspomnienia',
    'Secreta': 'Sekreta',
    'Commemoratio Secreta': 'Sekreta Wspomnienia',
    'Sequentia': 'Sekwencja',
    'Super populum': 'Modlitwa nad ludem',
    'Prefatio': 'Prefacja',
    'Tractus': 'Graduał',
    # 02-02, feast of the Purification of the B.V.M.
    'De Benedictione Candelarum': 'Poświęcenie Świec',
    'De Distributione Candelarum': 'Rozdawanie Świec',
    'De Processione': 'Procesja',
    # Quad6-0r, Dominica II Passionis seu in Palmis
    'Benedictio Palmorum': 'Poświęcenie Palm',
    'De distributione ramorum': 'Rozdawanie Gałązek',
    'De lectione Evangelica': 'Czytanie Ewangelii',
    'De processione cum ramis benedictis': 'Procesja z Poświęconymi Palmami',
    'Hymnus ad Christum Regem': 'Hymn ku Czci Chrystusa Króla',
    # Quad6-4r, Feria Quinta in Coena Domini
    'Maundi': 'Mandatum, czyli Umywanie Nóg',
    'Post Missam': 'Po Mszy',
    'Denudatione altaris': 'Obnażenie Ołtarzy',
    # Quad6-5r, Feria Sexta in Parasceve
    'Lectiones': 'Część Pierwsza: Czytania',
    'Passio': 'Pasja',
    'Oratio Fidelium': 'Część Druga: Uroczyste Modły zwane «Modlitwą Wiernych»',
    'Crucis Adoratione': 'Część Trzecia: Uroczysta Adoracja Krzyża',
    'CommunioQ': 'Część Czwarta: Komunia Święta',
    # Quad6-5r, Sabbato Sancto
    'Benedictio ignis': 'Poświęcenie nowego ognia',
    'De benedictione cerei Paschalis': 'Poświęcenie Paschału',
    'De solemni processione': 'Uroczysta Procesja',
    'De praeconio paschali': 'Orędzie Wielkanocne',
    'De lectionibus': 'Czytania',
    'De prima parte Litaniarum': 'Pierwsza Część Litanii',
    'De benedictione aquae baptismalis': 'Poświęcenie Wody Chrzcielnej',
    'De renovatione promissionum baptismatis': 'Odnowienie Przyrzeczeń Chrztu Świętego',
    'De altera parte Litaniarum': 'Druga Część Litanii',
    'De Missa solemni Vigiliae paschalis': 'Uroczysta Msza Rezurekcyjna',
    'Pro Laudibus': 'Laudes',
    'Conclusio': 'Zakończenie',
    'Benedictio cinerum': 'Poświęcenie Popiołu'

}

SECTION_LABELS_MULTI = {
    'GradualeL1': 'Graduał',
    'GradualeL2': 'Graduał',
    'GradualeL3': 'Graduał',
    'GradualeL4': 'Graduał',
    'GradualeL5': 'Graduał',
    'Graduale': 'Graduał',
    'LectioL1': 'Lekcja',
    'LectioL2': 'Lekcja',
    'LectioL3': 'Lekcja',
    'LectioL4': 'Lekcja',
    'LectioL5': 'Lekcja',
    'Lectio': 'Lekcja',
    'OratioL1': 'Kolekta',
    'OratioL2': 'Kolekta',
    'OratioL3': 'Kolekta',
    'OratioL4': 'Kolekta',
    'OratioL5': 'Kolekta',
    'Oratio': 'Kolekta'
}

PATERNOSTER = \
    "Ojcze nasz, któryś jest w niebie:\n" \
    "Święć się Imię Twoje,\n" \
    "Przyjdź królestwo Twoje,\n" \
    "Bądź wola Twoja jako w niebie tak i na ziemi.\n" \
    "Chleba naszego powszedniego daj nam dzisiaj\n" \
    "I odpuść nam nasze winy, jako i my odpuszczamy naszym winowajcom.\n" \
    "I nie wódź nas na pokuszenie.\n" \
    "Ale nas zbaw ode złego. Amen."


TRANSFORMATIONS = (
    (re.compile(r'\+\+'), '☩'),
    (re.compile(r'\+'), '☩'),
    (re.compile(r'V\.'), '℣.'),
    (re.compile(r'R\.'), '℟.'),
    (re.compile(r'\+'), '☩'),
    (re.compile(r'^#'), '##'),
    (re.compile(r'^!x!'), '!'),
    (re.compile(r'^!! *(.*)'), '### \\1'),
    (re.compile(r'^\[([^\]^]*)\]'), '### \\1'),
    (re.compile(r'^! *(.*)'), '*\\1*'),
    (re.compile(r'^v\. *'), ''),
    (re.compile(r'^_'), ''),
    (re.compile(r'\(\('), '('),
    (re.compile(r'\)\)'), ')'),
    (re.compile(r'\['), '('),
    (re.compile(r'\]'), ')'),
    (re.compile(r'\((\^\d+)\)'), '[\\1]'),  # preserving footnotes, like [^1], [^1]:
    (re.compile(r'^.*`.*$'), ''),
    (re.compile(r'^[&$]Gloria\.*'), 'Chwała Ojcu…'),
    (re.compile(r'^\$Oremus\.*'), 'Módlmy się.'),
    (re.compile(r'^\$Per Dominum eiusdem\.*'), 'Przez Pana…'),
    (re.compile(r'^\$Per Dominum\.*'), 'Przez Pana…'),
    (re.compile(r'^\$Per eu[mn]dem\.*'), 'Przez tegoż Pana…'),
    (re.compile(r'^\$Qui tecum eiusdem\.*'), 'Który z Tobą…'),
    (re.compile(r'^\$Qui tecum\.*'), 'Który z Tobą…'),
    (re.compile(r'^\$Qui vivis\.*'), 'Który żyjesz…'),
    (re.compile(r'^\$Deo [Gg]ratias\.*'), 'Bogu dzięki.'),
    (re.compile(r'^[&$]Dominus *[Vv]obiscum\.*'), '℣. Pan z wami.    \n\r℟. I z duchem twoim.'),
    (re.compile(r'^\*Modlitwa nad ludem\*.*'), ''),
    (re.compile(r'^\$Pater noster.*'), PATERNOSTER),
    (re.compile(r'\(rubrica 1955 aut rubrica 1960 dicitur\)'), ''),
    (re.compile(r'\(deinde dicuntur semper\)'), ''),
)

COMMEMORATIONS = {
    constants.COMMEMORATION: "Wspomnienie",
    constants.COMMEMORATED_ORATIO: "Kolekta wspomnienia",
    constants.COMMEMORATED_SECRETA: "Sekreta wspomnienia",
    constants.COMMEMORATED_POSTCOMMUNIO: "Pokomunia wspomnienia",
}

KDE = "Komentarz do Ewangelii"
SUPPLEMENTS = {
    constants.TEMPORA_ADV1_0: [
        {"label": "Adwent", "path": "/pl/supplement/2-adwent"},
        {"label": f"{KDE} na 1 Niedzielę Adwentu", "path": "http://vetusordo.pl/objasnienia1na/"}
    ],
    constants.TEMPORA_ADV2_0: [
        {"label": f"{KDE} na 2 Niedzielę Adwentu", "path": "http://vetusordo.pl/objasnienia2na/"}
    ],
    constants.TEMPORA_ADV3_0: [
        {"label": f"{KDE} na 3 Niedzielę Adwentu", "path": "http://vetusordo.pl/objasnienia3na/"}
    ],
    constants.TEMPORA_ADV4_0: [
        {"label": f"{KDE} na 4 Niedzielę Adwentu", "path": "http://vetusordo.pl/objasnienia4na/"}
    ],
    constants.SANCTI_12_24: [
        {"label": "Boże Narodzenie", "path": "/pl/supplement/3-boze-narodzenie"}
        ],
    constants.SANCTI_12_25_1: [
        {"label": "Boże Narodzenie", "path": "/pl/supplement/3-boze-narodzenie"},
        {"label": f"{KDE} pierwszej na uroczystość Bożego Narodzenia", "path": "http://vetusordo.pl/objasnieniaenubn/"}
    ],
    constants.SANCTI_12_25_2: [
        {"label": f"{KDE} drugiej na uroczystość Bożego Narodzenia", "path": "http://vetusordo.pl/objasnieniaenubn2/"}
    ],
    constants.SANCTI_12_25_3: [
        {"label": f"{KDE} trzeciej na uroczystość Bożego Narodzenia", "path": "http://vetusordo.pl/objasnieniaenubn3/"}
    ],
    constants.SANCTI_12_26: [
        {"label": f"{KDE} na uroczystość pierwszego męczennika św. Szczepana", "path": "http://vetusordo.pl/objasnieniaupmss/"}
    ],
    constants.TEMPORA_NAT1_0: [
        {"label": f"{KDE} na niedzielę po Bożym Narodzeniu", "path": "http://vetusordo.pl/objasnieniaennpbn/"}
    ],
    constants.SANCTI_01_01: [
        {"label": f"{KDE} na Oktawę Bożego Narodzenia", "path": "http://vetusordo.pl/objasnieniaenunr/"}
    ],
    constants.SANCTI_01_06: [
        {"label": f"{KDE} na Objawienia Pańskie", "path": "http://vetusordo.pl/objasnieniaenustk/"}
    ],
    constants.TEMPORA_EPI1_0: [
        {"label": "Okres po Objawieniu", "path": "/pl/supplement/4-okres-po-objawieniu"}
    ],
    constants.TEMPORA_EPI2_0: [
        {"label": f"{KDE} na 2 niedzielę po Objawieniu", "path": "http://vetusordo.pl/objasnieniaenndpstk/"}
    ],
    constants.TEMPORA_EPI3_0: [
        {"label": f"{KDE} na 3 niedzielę po Objawieniu", "path": "http://vetusordo.pl/objasnieniaenntpstk/"}
    ],
    constants.TEMPORA_EPI4_0: [
        {"label": f"{KDE} na 4 niedzielę po Objawieniu", "path": "http://vetusordo.pl/objasnieniaenncpstk/"}
    ],
    constants.TEMPORA_EPI5_0: [
        {"label": f"{KDE} na 5 niedzielę po Objawieniu", "path": "http://vetusordo.pl/objasnieniaennppstk-2/"}
    ],
    constants.TEMPORA_QUADP1_0: [
        {"label": "Przedpoście", "path": "/pl/supplement/5-przedposcie"},
        {"label": f"{KDE} na niedzielę Siedemdziesiątnicy", "path": "http://vetusordo.pl/oenns/"}
    ],
    constants.TEMPORA_QUADP2_0: [
        {"label": f"{KDE} na niedzielę Sześćdziesiątnicy", "path": "http://vetusordo.pl/objasnieniaennmpna/"}
    ],
    constants.TEMPORA_QUADP3_0: [
        {"label": f"{KDE} na niedzielę Pięćdziesiątnicy", "path": "http://vetusordo.pl/objasnieniannzpna/"}
    ],
    constants.TEMPORA_QUADP3_3: [
        {"label": "Wielki Post", "path": "/pl/supplement/6-wielki-post"}
    ],
    constants.TEMPORA_QUAD1_0: [
        {"label": f"{KDE} na 1 niedzielę Wielkiego Postu", "path": "http://vetusordo.pl/objasnieniann1p/"}
    ],
    constants.TEMPORA_QUAD2_0: [
        {"label": f"{KDE} na 2 niedzielę Wielkiego Postu", "path": "http://vetusordo.pl/2019oenndp/"}
    ],
    constants.TEMPORA_QUAD3_0: [
        {"label": f"{KDE} na 3 niedzielę Wielkiego Postu", "path": "http://vetusordo.pl/2019oenntp/"}
    ],
    constants.TEMPORA_QUAD4_0: [
        {"label": f"{KDE} na 4 niedzielę Wielkiego Postu", "path": "http://vetusordo.pl/2019oenncp/"}
    ],
    constants.TEMPORA_QUAD5_0: [
        {"label": "Okres Męki Pańskiej", "path": "/pl/supplement/8-okres-meki-panskiej"},
        {"label": f"{KDE} na 1 niedzielę Męki Pańskiej", "path": "http://vetusordo.pl/objasnieniaennpp/"}
    ],
    constants.TEMPORA_QUAD6_0: [
        {"label": "Wielki Tydzień", "path": "/pl/supplement/7-wielki-tydzien"},
        {"label": f"{KDE} na 2 niedzielę Męki Pańskiej (Palmową)", "path": "http://vetusordo.pl/objasnieniaennk/"}
    ],
    constants.TEMPORA_QUAD6_6: [
        {"label": "Okres Wielkanocny", "path": "/pl/supplement/9-okres-wielkanocny"}
    ],
    constants.TEMPORA_PASC0_0: [
        {"label": f"{KDE} na Wielkanoc", "path": "http://vetusordo.pl/objasnieniaenw/"}
    ],
    constants.TEMPORA_PASC0_1: [
        {"label": f"{KDE} na poniedziałek Wielkanocny", "path": "http://vetusordo.pl/2019oenpw/"}
    ],
    constants.TEMPORA_PASC1_0: [
        {"label": f"{KDE} na niedzielę Białą", "path": "http://vetusordo.pl/2019oennp/"}
    ],
    constants.TEMPORA_PASC2_0: [
        {"label": f"{KDE} na 2 niedzielę po Wielkanocy", "path": "http://vetusordo.pl/2019oenn2pw/"}
    ],
    constants.TEMPORA_PASC3_0: [
        {"label": f"{KDE} na 3 niedzielę po Wielkanocy", "path": "http://vetusordo.pl/2019oenn3pw/"}
    ],
    constants.TEMPORA_PASC4_0: [
        {"label": f"{KDE} na 4 niedzielę po Wielkanocy", "path": "http://vetusordo.pl/2019oenn4pw/"}
    ],
    constants.TEMPORA_PASC5_0: [
        {"label": f"{KDE} na 5 niedzielę po Wielkanocy", "path": "http://vetusordo.pl/2019oenn5pw/"}
    ],
    constants.TEMPORA_PASC5_4: [
        {"label": f"{KDE} na Wniebowstąpienie Pańskie", "path": "http://vetusordo.pl/2019oenwp/"}
    ],
    constants.TEMPORA_PASC6_0: [
        {"label": f"{KDE} na niedzielę po Wniebostąpieniu", "path": "http://vetusordo.pl/objasnieniaenn6pw/"}
    ],
    constants.TEMPORA_PASC6_6: [
        {"label": "Zesłanie Ducha św.", "path": "/pl/supplement/10-zeslanie-ducha-sw"}
    ],
    constants.TEMPORA_PASC7_0: [
        {"label": f"{KDE} na niedzielę Zesłania Ducha św.", "path": "http://vetusordo.pl/objasnieniaenuzds/"}
    ],
    constants.TEMPORA_PASC7_1: [
        {"label": f"{KDE} na poniedzialek w Oktawie Zesłania Ducha św.", "path": "/pl/supplement/commentary/poniedzialek-po-zeslaniu"}
    ],
    constants.TEMPORA_PENT01_0: [
        {"label": "Okres po Zesłaniu Ducha św.", "path": "/pl/supplement/11-okres-po-zeslaniu-ducha-sw"},
        {"label": f"{KDE} na uroczystość Trójcy Przenajświętszej", "path": "http://vetusordo.pl/objasnienia2019enuts/"}
    ],
    constants.TEMPORA_PENT01_4: [
        {"label": f"{KDE} na uroczystość Bożego Ciała", "path": "http://vetusordo.pl/objasnienia2019enubc/"}
    ],
    constants.TEMPORA_PENT02_0: [
        {"label": f"{KDE} na 2 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienia2019enndps/"}
    ],
    constants.TEMPORA_PENT03_0: [
        {"label": f"{KDE} na 3 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienia2019enntps/"}
    ],
    constants.TEMPORA_PENT04_0: [
        {"label": f"{KDE} na 4 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienie2019enn4ps/"}
    ],
    constants.TEMPORA_PENT05_0: [
        {"label": f"{KDE} na 5 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienia2019enn5ps/"}
    ],
    constants.TEMPORA_PENT06_0: [
        {"label": f"{KDE} na 6 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienie2019enn6ps/"}
    ],
    constants.TEMPORA_PENT07_0: [
        {"label": f"{KDE} na 7 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienia2019nn7ps/"}
    ],
    constants.TEMPORA_PENT08_0: [
        {"label": f"{KDE} na 8 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienia2019nn8ps/"}
    ],
    constants.TEMPORA_PENT09_0: [
        {"label": f"{KDE} na 9 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienia2019nn9ps/"}
    ],
    constants.TEMPORA_PENT10_0: [
        {"label": f"{KDE} na 10 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienia2019nn10ps/"}
    ],
    constants.TEMPORA_PENT11_0: [
        {"label": f"{KDE} na 11 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienie2019nn11ps/"}
    ],
    constants.TEMPORA_PENT12_0: [
        {"label": f"{KDE} na 12 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienie2019nn12ps/"}
    ],
    constants.TEMPORA_PENT13_0: [
        {"label": f"{KDE} na 13 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienie2019nn13ps/"}
    ],
    constants.TEMPORA_PENT14_0: [
        {"label": f"{KDE} na 14 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienie2019nn14ps/"}
    ],
    constants.TEMPORA_PENT15_0: [
        {"label": f"{KDE} na 15 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnienie2019nn15ps/"}
    ],
    constants.TEMPORA_PENT16_0: [
        {"label": f"{KDE} na 16 niedzielę po Zesłaniu Ducha św.", "path": "/pl/supplement/commentary/16-niedziela-po-zeslaniu"}
    ],
    constants.TEMPORA_PENT17_0: [
        {"label": f"{KDE} na 17 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnieniaenn17ps/"}
    ],
    constants.TEMPORA_PENT18_0: [
        {"label": f"{KDE} na 18 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnieniaenn18ps/"}
    ],
    constants.TEMPORA_PENT19_0: [
        {"label": f"{KDE} na 19 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/objasnieniaenn19ps/"}
    ],
    constants.TEMPORA_PENT20_0: [
        {"label": f"{KDE} na 20 niedzielę po Zesłaniu Ducha św.", "path": "/pl/supplement/commentary/20-niedziela-po-zeslaniu"}
    ],
    constants.TEMPORA_PENT21_0: [
        {"label": f"{KDE} na 21 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/2019oenn21ps/"}
    ],
    constants.TEMPORA_PENT22_0: [
        {"label": f"{KDE} na 22 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/2019oenn22ps/"}
    ],
    constants.TEMPORA_PENT23_0: [
        {"label": f"{KDE} na 23 niedzielę po Zesłaniu Ducha św.", "path": "http://vetusordo.pl/2019oenn23ps/"}
    ],
    constants.TEMPORA_PENT24_0: [
        {"label": f"{KDE} na 24 niedzielę po Zesłaniu Ducha św.", "path": "/pl/supplement/commentary/24-niedziela-po-zeslaniu"}
    ],
    constants.SANCTI_12_08: [
        {"label": f"{KDE} na uroczystość Niepokalanego Poczęcia N. M. P.", "path": "http://vetusordo.pl/oenunmp/"}
    ],
    constants.SANCTI_02_02: [
        {"label": f"{KDE} na uroczystość Oczyszczenia N. M. P.", "path": "http://vetusordo.pl/2019uroczystosconmp/"}
    ],
    constants.SANCTI_03_25: [
        {"label": f"{KDE} na uroczystość Zwiastowania N. M. P.", "path": "http://vetusordo.pl/2019oenuznmp/"}
    ],
    constants.SANCTI_06_29: [
        {"label": f"{KDE} na uroczystość śś. Apostołów Piotra i Pawła", "path": "http://vetusordo.pl/objasnienia2019enussapip/"}
    ],
    constants.SANCTI_08_15: [
        {"label": f"{KDE} na Wniebowzięcie N. M. P.", "path": "/pl/supplement/commentary/wniebowziecie-nmp"}
    ],
    constants.SANCTI_09_08: [
        {"label": f"{KDE} na Narodzenie N. M. P.", "path": "/pl/supplement/commentary/narodzenie-nmp"}
    ],
    constants.SANCTI_11_01: [
        {"label": f"{KDE} na uroczystość Wszystkich Świętych", "path": "http://vetusordo.pl/2019oenuws/"}
    ]
}


OE = "Objaśnienia Ewangelii"
SUPPLEMENTS_V4 = {
    constants.TEMPORA_ADV1_0: [
        {"label": "Adwent", "path": "/pl/supplement/2-adwent"},
        {"label": OE, "path": "/pl/supplement/objasnienia-Adv1-0"}
    ],
    constants.TEMPORA_ADV2_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Adv2-0"}
    ],
    constants.TEMPORA_ADV3_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Adv3-0"}
    ],
    constants.TEMPORA_ADV4_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Adv4-0"}
    ],
    constants.SANCTI_12_24: [
        {"label": "Boże Narodzenie", "path": "/pl/supplement/3-boze-narodzenie"}
        ],
    constants.SANCTI_12_25_1: [
        {"label": "Boże Narodzenie", "path": "/pl/supplement/3-boze-narodzenie"},
        {"label": OE, "path": "/pl/supplement/objasnienia-12-25m1"}
    ],
    constants.SANCTI_12_25_2: [
        {"label": OE, "path": "/pl/supplement/objasnienia-12-25m2"}
    ],
    constants.SANCTI_12_25_3: [
        {"label": OE, "path": "/pl/supplement/objasnienia-"}
    ],
    constants.SANCTI_12_26: [
        {"label": OE, "path": "/pl/supplement/objasnienia-12-25m3"}
    ],
    constants.TEMPORA_NAT1_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Nat1-0"}
    ],
    constants.SANCTI_01_01: [
        {"label": OE, "path": "/pl/supplement/objasnienia-01-01"}
    ],
    constants.SANCTI_01_06: [
        {"label": OE, "path": "/pl/supplement/objasnienia-01-06"}
    ],
    constants.TEMPORA_EPI1_0: [
        {"label": "Okres po Objawieniu", "path": "/pl/supplement/4-okres-po-objawieniu"}
    ],
    constants.TEMPORA_EPI2_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Epi2-0"}
    ],
    constants.TEMPORA_EPI3_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Epi3-0"}
    ],
    constants.TEMPORA_EPI4_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Epi4-0"}
    ],
    constants.TEMPORA_EPI5_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Epi5-0"}
    ],
    constants.TEMPORA_QUADP1_0: [
        {"label": "Przedpoście", "path": "/pl/supplement/5-przedposcie"},
        {"label": OE, "path": "/pl/supplement/objasnienia-Quadp1-0"}
    ],
    constants.TEMPORA_QUADP2_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Quadp2-0"}
    ],
    constants.TEMPORA_QUADP3_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Quadp3-0"}
    ],
    constants.TEMPORA_QUADP3_3: [
        {"label": "Wielki Post", "path": "/pl/supplement/6-wielki-post"}
    ],
    constants.TEMPORA_QUAD1_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Quad1-0"}
    ],
    constants.TEMPORA_QUAD2_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Quad2-0"}
    ],
    constants.TEMPORA_QUAD3_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Quad3-0"}
    ],
    constants.TEMPORA_QUAD4_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Quad4-0"}
    ],
    constants.TEMPORA_QUAD5_0: [
        {"label": "Okres Męki Pańskiej", "path": "/pl/supplement/8-okres-meki-panskiej"},
        {"label": OE, "path": "/pl/supplement/objasnienia-Quad5-0"}
    ],
    constants.TEMPORA_QUAD6_0: [
        {"label": "Wielki Tydzień", "path": "/pl/supplement/7-wielki-tydzien"},
        {"label": OE, "path": "/pl/supplement/objasnienia-Quad6-0"}
    ],
    constants.TEMPORA_QUAD6_6: [
        {"label": "Okres Wielkanocny", "path": "/pl/supplement/9-okres-wielkanocny"}
    ],
    constants.TEMPORA_PASC0_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pasc0-0"}
    ],
    constants.TEMPORA_PASC0_1: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pasc0-1"}
    ],
    constants.TEMPORA_PASC1_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pasc1-0"}
    ],
    constants.TEMPORA_PASC2_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pasc2-0"}
    ],
    constants.TEMPORA_PASC3_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pasc3-0r"}
    ],
    constants.TEMPORA_PASC4_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pasc4-0"}
    ],
    constants.TEMPORA_PASC5_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pasc5-0"}
    ],
    constants.TEMPORA_PASC5_4: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pasc5-4"}
    ],
    constants.TEMPORA_PASC6_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pasc6-0"}
    ],
    constants.TEMPORA_PASC6_6: [
        {"label": "Zesłanie Ducha św.", "path": "/pl/supplement/10-zeslanie-ducha-sw"}
    ],
    constants.TEMPORA_PASC7_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pasc7-0"}
    ],
    constants.TEMPORA_PASC7_1: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pasc7-1"}
    ],
    constants.TEMPORA_PENT01_0: [
        {"label": "Okres po Zesłaniu Ducha św.", "path": "/pl/supplement/11-okres-po-zeslaniu-ducha-sw"},
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent01-0r"}
    ],
    constants.TEMPORA_PENT01_4: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent01-4"}
    ],
    constants.TEMPORA_PENT02_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent02-0r"}
    ],
    constants.TEMPORA_PENT03_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent03-0r"}
    ],
    constants.TEMPORA_PENT04_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent04-0"}
    ],
    constants.TEMPORA_PENT05_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent05-0"}
    ],
    constants.TEMPORA_PENT06_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent06-0"}
    ],
    constants.TEMPORA_PENT07_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent07-0"}
    ],
    constants.TEMPORA_PENT08_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent08-0"}
    ],
    constants.TEMPORA_PENT09_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent09-0"}
    ],
    constants.TEMPORA_PENT10_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent10-0"}
    ],
    constants.TEMPORA_PENT11_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent11-0"}
    ],
    constants.TEMPORA_PENT12_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent12-0"}
    ],
    constants.TEMPORA_PENT13_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent13-0"}
    ],
    constants.TEMPORA_PENT14_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent14-0"}
    ],
    constants.TEMPORA_PENT15_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent15-0"}
    ],
    constants.TEMPORA_PENT16_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent16-0"}
    ],
    constants.TEMPORA_PENT17_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent17-0"}
    ],
    constants.TEMPORA_PENT18_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent18-0"}
    ],
    constants.TEMPORA_PENT19_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent19-0"}
    ],
    constants.TEMPORA_PENT20_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent20-0"}
    ],
    constants.TEMPORA_PENT21_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent21-0"}
    ],
    constants.TEMPORA_PENT22_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent22-0"}
    ],
    constants.TEMPORA_PENT23_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent23-0"}
    ],
    constants.TEMPORA_PENT24_0: [
        {"label": OE, "path": "/pl/supplement/objasnienia-Pent24-0"}
    ],
    constants.SANCTI_12_08: [
        {"label": OE, "path": "/pl/supplement/objasnienia-12-08"}
    ],
    constants.SANCTI_02_02: [
        {"label": OE, "path": "/pl/supplement/objasnienia-02-02"}
    ],
    constants.SANCTI_03_25: [
        {"label": OE, "path": "/pl/supplement/objasnienia-03-25"}
    ],
    constants.SANCTI_06_29: [
        {"label": OE, "path": "/pl/supplement/objasnienia-06-29"}
    ],
    constants.SANCTI_08_15: [
        {"label": OE, "path": "/pl/supplement/objasnienia-08-15r"}
    ],
    constants.SANCTI_09_08: [
        {"label": OE, "path": "/pl/supplement/objasnienia-09-08"}
    ],
    constants.SANCTI_11_01: [
        {"label": OE, "path": "/pl/supplement/objasnienia-11-01"}
    ]
}