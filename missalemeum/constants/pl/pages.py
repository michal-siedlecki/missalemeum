from typing import List

from constants import common as constants

# Pages in paper missal/s


def get_pages(pallotinum: int) -> List[str]:
    return [
        f"Pallotinum s. {pallotinum}"
    ]


PAGES = {

    constants.TEMPORA_EPI1_0: get_pages(111),  # 'Uroczystość Świętej Rodziny Jezusa, Maryi i Józefa',
    constants.TEMPORA_EPI2_0: get_pages(118),  # '2 Niedziela po Objawieniu',
    constants.TEMPORA_EPI3_0: get_pages(121),  # '3 Niedziela po Objawieniu',
    constants.TEMPORA_EPI4_0: get_pages(124),  # '4 Niedziela po Objawieniu',
    constants.TEMPORA_EPI5_0: get_pages(126),  # '5 Niedziela po Objawieniu',
    constants.TEMPORA_EPI6_0: get_pages(129),  # '6 Niedziela po Objawieniu',
    constants.TEMPORA_QUADP1_0: get_pages(134),  # 'Niedziela Siedemdziesiątnicy',
    constants.TEMPORA_QUADP2_0: get_pages(138),  # 'Niedziela Sześćdziesiątnicy',
    constants.TEMPORA_QUADP3_0: get_pages(142),  # 'Niedziela Pięćdziesiątnicy',
    constants.TEMPORA_QUADP3_3: get_pages(149),  # 'Środa Popielcowa',
    constants.TEMPORA_QUADP3_4: get_pages(156),  # 'Czwartek po Popielcu',
    constants.TEMPORA_QUADP3_5: get_pages(159),  # 'Piątek po Popielcu',
    constants.TEMPORA_QUADP3_6: get_pages(162),  # 'Sobota po Popielcu',
    constants.TEMPORA_QUAD1_0: get_pages(165),  # '1 Niedziela Wielkiego Postu',
    constants.TEMPORA_QUAD1_1: get_pages(168),  # 'Poniedziałek po 1 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD1_2: get_pages(171),  # 'Wtorek po 1 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD1_3: get_pages(174),  # 'Środa Suchych Dni Wielkiego Postu',
    constants.TEMPORA_QUAD1_4: get_pages(178),  # 'Czwartek po 1 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD1_5: get_pages(180),  # 'Piątek Suchych Dni Wielkiego Postu',
    constants.TEMPORA_QUAD1_6: get_pages(183),  # 'Sobota Suchych Dni Wielkiego Postu',
    constants.TEMPORA_QUAD2_0: get_pages(189),  # '2 Niedziela Wielkiego Postu',
    constants.TEMPORA_QUAD2_1: get_pages(192),  # 'Poniedziałek po 2 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD2_2: get_pages(195),  # 'Wtorek po 2 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD2_3: get_pages(197),  # 'Środa po 2 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD2_4: get_pages(200),  # 'Czwartek po 2 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD2_5: get_pages(203),  # 'Piątek po 2 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD2_6: get_pages(207),
    constants.TEMPORA_QUAD3_0: get_pages(212),
    constants.TEMPORA_QUAD3_1: get_pages(215),
    constants.TEMPORA_QUAD3_2: get_pages(218),
    constants.TEMPORA_QUAD3_3: get_pages(221),
    constants.TEMPORA_QUAD3_4: get_pages(224),
    constants.TEMPORA_QUAD3_5: get_pages(226),
    constants.TEMPORA_QUAD3_6: get_pages(230),
    constants.TEMPORA_QUAD4_0: get_pages(235),
    constants.TEMPORA_QUAD4_1: get_pages(238),  # 'Poniedziałek po 4 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD4_2: get_pages(241),  # 'Wtorek po 4 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD4_3: get_pages(244),  # 'Środa po 4 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD4_4: get_pages(249),  # 'Czwartek po 4 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD4_5: get_pages(252),  # 'Piątek po 4 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD4_6: get_pages(256),  # 'Sobota po 4 Niedzieli Wielkiego Postu',
    constants.TEMPORA_QUAD5_0: get_pages(263),  # '1 Niedziela Męki Pańskiej',
    constants.TEMPORA_QUAD5_1: get_pages(266),  # 'Poniedziałek po Niedzieli Męki Pańskiej',
    constants.TEMPORA_QUAD5_2: get_pages(269),  # 'Wtorek po Niedzieli Męki Pańskiej',
    constants.TEMPORA_QUAD5_3: get_pages(272),  # 'Środa po Niedzieli Męki Pańskiej',
    constants.TEMPORA_QUAD5_4: get_pages(275),  # 'Czwartek po Niedzieli Męki Pańskiej',
    constants.TEMPORA_QUAD5_5: get_pages(278),  # 'Piątek po Niedzieli Męki Pańskiej',
    constants.TEMPORA_QUAD5_6: get_pages(281),  # 'Sobota po Niedzieli Męki Pańskiej',
    constants.TEMPORA_QUAD6_0: get_pages(288),  # 'Niedziela Palmowa',
    constants.TEMPORA_QUAD6_1: get_pages(304),  # 'Wielki Poniedziałek',
    constants.TEMPORA_QUAD6_2: get_pages(307),  # 'Wielki Wtorek',
    constants.TEMPORA_QUAD6_3: get_pages(313),  # 'Wielka Środa',
    constants.TEMPORA_QUAD6_4: get_pages(323),  # 'Wielki Czwartek',
    constants.TEMPORA_QUAD6_5: get_pages(349),  # 'Wielki Piątek',
    constants.TEMPORA_QUAD6_6: get_pages(377),  # 'Wielka Sobota',
    constants.TEMPORA_PASC0_0: get_pages(413),  # 'Niedziela Zmartwychwstania',
    constants.TEMPORA_PASC0_1: get_pages(418),  # 'Poniedziałek Wielkanocny',
    constants.TEMPORA_PASC0_2: get_pages(422),  # 'Wtorek Wielkanocny',
    constants.TEMPORA_PASC0_3: get_pages(424),  # 'Środa Wielkanocna',
    constants.TEMPORA_PASC0_4: get_pages(427),  # 'Czwartek Wielkanocny',
    constants.TEMPORA_PASC0_5: get_pages(430),  # 'Piątek Wielkanocny',
    constants.TEMPORA_PASC0_6: get_pages(432),  # 'Sobota Biała',
    constants.TEMPORA_PASC1_0: get_pages(435),  # 'Niedziela Biała',
    constants.TEMPORA_PASC2_0: get_pages(438),  # '2 Niedziela po Wielkanocy',
    constants.TEMPORA_PASC3_0: get_pages(440),  # '3 Niedziela po Wielkanocy',
    constants.TEMPORA_PASC4_0: get_pages(442),  # '4 Niedziela po Wielkanocy',
    constants.TEMPORA_PASC5_0: get_pages(445),  # '5 Niedziela po Wielkanocy',
    constants.TEMPORA_PASC5_1: get_pages(447),  # 'Litanie mniejsze',
    constants.TEMPORA_PASC5_2: get_pages(447),  # 'Litanie mniejsze',
    constants.TEMPORA_PASC5_3: get_pages(451),  # 'Wigilia Wniebowstąpienia Pańskiego',
    constants.TEMPORA_PASC5_4: get_pages(453),  # 'Wniebowstąpienie Pańskie',
    constants.TEMPORA_PASC6_0: get_pages(457),  # 'Niedziela po Wniebowstąpieniu',
    constants.TEMPORA_PASC6_6: get_pages(462),  # 'Wigilia Zesłania Ducha Świętego',
    constants.TEMPORA_PASC7_0: get_pages(465),  # 'Niedziela Zesłania Ducha Świętego',
    constants.TEMPORA_PASC7_1: get_pages(470),  # 'Poniedziałek w Oktawie Zesłania Ducha Świętego',
    constants.TEMPORA_PASC7_2: get_pages(473),  # 'Wtorek w Oktawie Zesłania Ducha Świętego',
    constants.TEMPORA_PASC7_3: get_pages(475),  # 'Środa Suchych Dni po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PASC7_4: get_pages(478),  # 'Czwartek w Oktawie Zesłania Ducha Świętego',
    constants.TEMPORA_PASC7_5: get_pages(479),  # 'Piątek Suchych Dni po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PASC7_6: get_pages(481),  # 'Sobota Suchych Dni po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT01_0: get_pages(491),  # 'Uroczystość Trójcy Przenajświętszej',
    constants.TEMPORA_PENT01_4: get_pages(497),  # 'Uroczystość Bożego Ciała',
    constants.TEMPORA_PENT02_0: get_pages(504),  # '2 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT02_5: get_pages(506),  # 'Uroczystość Najświętszego Serca Pana Jezusa',
    constants.TEMPORA_PENT03_0: get_pages(510),  # '3 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT04_0: get_pages(512),  # '4 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT05_0: get_pages(515),  # '5 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT06_0: get_pages(517),  # '6 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT07_0: get_pages(520),  # '7 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT08_0: get_pages(522),  # '8 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT09_0: get_pages(525),  # '9 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT10_0: get_pages(528),  # '10 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT11_0: get_pages(530),  # '11 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT12_0: get_pages(533),  # '12 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT13_0: get_pages(536),  # '13 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT14_0: get_pages(539),  # '14 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT15_0: get_pages(541),  # '15 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT16_0: get_pages(544),  # '16 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT17_0: get_pages(547),  # '17 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT18_0: get_pages(562),  # '18 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT19_0: get_pages(565),  # '19 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT20_0: get_pages(567),  # '20 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT21_0: get_pages(570),  # '21 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT22_0: get_pages(573),  # '22 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT23_0: get_pages(575),  # '23 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_PENT_3: get_pages(549),  # 'Środa Suchych Dni Wrześniowych',
    constants.TEMPORA_PENT_5: get_pages(553),  # 'Piątek Suchych Dni Wrześniowych',
    constants.TEMPORA_PENT_6: get_pages(556),  # 'Sobota Suchych Dni Wrześniowych',
    constants.TEMPORA_PENT24_0: get_pages(579),  # '24 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_ADV1_0: get_pages(43),  # '1 Niedziela Adwentu',
    constants.TEMPORA_ADV2_0: get_pages(47),  # '2 Niedziela Adwentu',
    constants.TEMPORA_ADV3_0: get_pages(51),  # '3 Niedziela Adwentu (Niedziela Gaudete)',
    constants.TEMPORA_ADV3_3: get_pages(55),  # 'Środa Suchych Dni Adwentu',
    constants.TEMPORA_ADV3_5: get_pages(58),  # 'Piątek Suchych Dni Adwentu',
    constants.TEMPORA_ADV3_6: get_pages(60),  # 'Sobota Suchych Dni Adwentu',
    constants.TEMPORA_ADV4_0: get_pages(67),  # '4 Niedziela Adwentu',
    constants.TEMPORA_NAT1_0: get_pages(86),  # 'Niedziela w Oktawie Bożego Narodzenia',
    constants.TEMPORA_NAT2_0: get_pages(102),  # 'Najświętszego Imienia Jezus',
    constants.SANCTI_10_DU: get_pages(1167),  # 'Chrystusa Króla',
    constants.TEMPORA_EPI1_0A: get_pages(114),  # '1 Niedziela po Objawieniu',
    constants.TEMPORA_PENT01_0A: get_pages(494),  # '1 Niedziela po Zesłaniu Ducha Świętego',
    constants.TEMPORA_C_10A: get_pages(649),
    constants.COMMUNE_C_10A: get_pages(649),
    constants.TEMPORA_C_10B: get_pages(652),
    constants.COMMUNE_C_10B: get_pages(652),
    constants.TEMPORA_C_10C: get_pages(654),
    constants.COMMUNE_C_10C: get_pages(654),
    constants.TEMPORA_C_10PASC: get_pages(654),
    constants.COMMUNE_C_10PASC: get_pages(654),
    constants.TEMPORA_C_10T: get_pages(655),
    constants.COMMUNE_C_10T: get_pages(655),
    constants.COMMUNE_C5: get_pages(693),  # 21 os iusti
    constants.COMMUNE_C5B: get_pages(696),  # 22 iustus ut palma
    constants.COMMUNE_C2C: get_pages(659),  # statuit
    constants.COMMUNE_C2B: get_pages(662),  # Sacerdotes Dei
    constants.SANCTI_01_01: get_pages(100),  # 'Oktawa Bożego Narodzenia',
    constants.SANCTI_01_06: get_pages(107),  # 'Objawienie Pańskie',
    constants.SANCTI_01_13: get_pages(116),  # 'Wspomnienie Chrztu Pańskiego',
    constants.SANCTI_01_14: get_pages(740),  # 'Św. Hilarego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_01_15: get_pages(741),  # 'Św. Pawła, Pierwszego Pustelnika, Wyznawcy',
    constants.SANCTI_01_16: get_pages(744),  # 'Św. Marcelego I, Papieża i Męczennika',
    constants.SANCTI_01_17: get_pages(745),  # 'Św. Antoniego, Opata',
    constants.SANCTI_01_18: get_pages(745),  # 'Św. Pryski, Dziewicy',
    constants.SANCTI_01_19: get_pages(746),  # 'Śś. Mariusza, Marty, Audifaksa i Abachuma',
    constants.SANCTI_01_20: get_pages(749),  # 'Śś. Fabiana, Papieża i Sebastiana, Męczenników',
    constants.SANCTI_01_21: get_pages(751),  # 'Św. Agnieszki, Dziewicy i Męczennicy',
    constants.SANCTI_01_22: get_pages(753),  # 'Śś. Wincentego i Anastazego, Męczenników',
    constants.SANCTI_01_23: get_pages(754),  # 'Św. Rajmunda z Pennafort, Wyznawcy',
    constants.SANCTI_01_24: get_pages(755),  # 'Św. Tymoteusza, Biskupa i Męczennika',
    constants.SANCTI_01_25: get_pages(756),  # 'Nawrócenie św. Pawła, Apostoła',
    constants.SANCTI_01_26: get_pages(759),  # 'Św. Polikarpa, Biskupa i Męczennika',
    constants.SANCTI_01_27: get_pages(761),  # 'Św. Jana Chryzostoma, Wyznawcy, Biskupa i Doktora Kościoła',
    constants.SANCTI_01_28: get_pages(761),  # 'Św. Piotra Nolasco, Wyznawcy',
    constants.SANCTI_01_29: get_pages(763),  # 'Św. Franciszka Salezego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_01_30: get_pages(764),  # 'Św. Martyny, Dziewicy i Męczennicy',
    constants.SANCTI_01_31: get_pages(764),  # 'Św. Jana Bosco, Wyznawcy',
    constants.SANCTI_02_01: get_pages(767),  # 'Św. Ignacego, Biskupa i Męczennika',
    constants.SANCTI_02_02: get_pages(769),  # 'Oczyszczenie N. M. P.',
    constants.SANCTI_02_03: get_pages(778),  # 'Św. Błażeja, Biskupa i Męczennika',
    constants.SANCTI_02_04: get_pages(778),  # 'Św. Andrzeja Corsini, Biskupa i Wyznawcy',
    constants.SANCTI_02_05: get_pages(779),  # 'Św. Agaty, Dziewicy i Męczennicy',
    constants.SANCTI_02_06: get_pages(782),  # 'Św. Tytusa, Biskupa i Wyznawcy',
    constants.SANCTI_02_07: get_pages(783),  # 'Św. Romualda, Opata',
    constants.SANCTI_02_08: get_pages(783),  # 'Św. Jana z Maty, Wyznawcy',
    constants.SANCTI_02_09: get_pages(784),  # 'Św. Cyryla Aleksandryjskiego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_02_10: get_pages(785),  # 'Św. Scholastyki',
    constants.SANCTI_02_11: get_pages(786),  # 'Objawienie się N. M. P. Niepokalanie Poczętej w Lourdes',
    constants.SANCTI_02_12: get_pages(788),  # 'Siedmiu Założycieli Zakonu Serwitów N. M. P., Wyznawców',
    constants.SANCTI_02_14: get_pages(791),  # 'Św. Walentego, Kapłana i Męczennika',
    constants.SANCTI_02_15: get_pages(792),  # 'Śś. Faustyna i Jowity, Męczenników',
    constants.SANCTI_02_18: get_pages(793),  # 'Św. Symeona, Biskupa i Męczennika',
    constants.SANCTI_02_22: get_pages(793),  # 'Katedry św. Piotra Apostoła',
    constants.SANCTI_02_23: get_pages(796),  # 'Św. Piotra Damiana, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_02_24: get_pages(796),  # 'Św. Macieja Apostoła',
    constants.SANCTI_02_27: get_pages(799),  # 'Św. Gabriela od Matki Bożej Bolesnej',
    constants.SANCTI_03_04: get_pages(802),  # 'Św. Kazimierza, Wyznawcy',
    constants.SANCTI_03_06: get_pages(805),  # 'Śś. Perpetui i Felicyty, Męczennic',
    constants.SANCTI_03_07: get_pages(806),  # 'Św. Tomasza z Akwinu, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_03_08: get_pages(807),  # 'Św. Jana Bożego, Wyznawcy',
    constants.SANCTI_03_09: get_pages(809),  # 'Św. Franciszki Rzymianki, Wdowy',
    constants.SANCTI_03_10: get_pages(809),  # 'Śś. Czterdziestu Męczenników',
    constants.SANCTI_03_12: get_pages(811),  # 'Św. Grzegorza Wielkiego, Papieża, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_03_15PL: get_pages(812),  # 'Św. Klemensa Marii Dworzaka (Hofbauera)',
    constants.SANCTI_03_17: get_pages(813),  # 'Św. Patryka, Biskupa i Wyznawcy',
    constants.SANCTI_03_18: get_pages(814),  # 'Św. Cyryla Jerozolimskiego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_03_19: get_pages(816),  # 'Św. Józefa, Oblubieńca N. M. P.',
    constants.SANCTI_03_21: get_pages(819),  # 'Św. Benedykta, Opata',
    constants.SANCTI_03_24: get_pages(823),  # 'Św. Gabriela Archanioła',
    constants.SANCTI_03_25: get_pages(827),  # 'Zwiastowanie N. M. P.',
    constants.SANCTI_03_27: get_pages(833),  # 'Św. Jana Damasceńskiego, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_03_28: get_pages(836),  # 'Św. Jana Kapistrana, Wyznawcy',
    constants.SANCTI_04_02: get_pages(839),  # 'Św. Franciszka z Pauli, Wyznawcy',
    constants.SANCTI_04_04: get_pages(840),  # 'Św. Izydora, Biskupa, Wyznawcy i Dokotra Kościoła',
    constants.SANCTI_04_05: get_pages(840),  # 'Św. Wincentego Fereriusza, Wyznawcy',
    constants.SANCTI_04_11: get_pages(840),  # 'Św. Leona Wielkiego, Papieża, Wyznawcy i Dokotra Kościoła',
    constants.SANCTI_04_13: get_pages(841),  # 'Św. Hermenegilda, Męczennika',
    constants.SANCTI_04_14: get_pages(841),  # 'Św. Justyna, Męczennika',
    constants.SANCTI_04_17: get_pages(846),  # 'Św. Aniceta, Papieża i Męczennika',
    constants.SANCTI_04_21: get_pages(846),  # 'Św. Anzelma, Biskupa, Wyznawcy i Dokotra Kościoła',
    constants.SANCTI_04_22: get_pages(846),  # 'Śś. Sotera i Kajusa, Papieży i Męczenników',
    constants.SANCTI_04_23: get_pages(849),  # 'Św. Jerzego, Męczennika',
    constants.SANCTI_04_23PL: get_pages(847),  # 'Św. Wojciecha, Biskupa i Męczennika',
    constants.SANCTI_04_24: get_pages(850),  # 'Św. Fidelisa z Sigmaringen, Męczennika',
    constants.SANCTI_04_25: get_pages(851),  # 'Św. Marka Ewangelisty',
    constants.SANCTI_04_26: get_pages(854),  # 'Śś. Kleta i Marcelina, Papieży i Męczenników',
    constants.SANCTI_04_27: get_pages(854),  # 'Św. Piotra Kanizjusza, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_04_28: get_pages(855),  # 'Św. Pawła od Krzyża, Wyznawcy',
    constants.SANCTI_04_29: get_pages(857),  # 'Piotra z Werony, Męczenika',
    constants.SANCTI_04_30: get_pages(858),  # 'Św. Katarzyny Sieneńskiej, Dziewicy',
    constants.SANCTI_05_01: get_pages(860),  # 'Św. Józefa Robotnika, Oblubieńca N. M. P',
    constants.SANCTI_05_02: get_pages(863),  # 'Św. Atanazego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_05_03PL: get_pages(867),  # 'N. M. P., Królowej Polski, Głównej Patronki Polski',
    constants.SANCTI_05_04: get_pages(872),  # 'Św. Moniki, Wdowy',
    constants.SANCTI_05_04PL: get_pages(873),  # 'Św. Floriana, Męczennika',
    constants.SANCTI_05_05: get_pages(872),  # 'Św. Piusa V, Papieża i Wyznawcy',
    constants.SANCTI_05_07: get_pages(876),  # 'Św. Stanisława, Biskupa i Męczennika',
    constants.SANCTI_05_08PL: get_pages(876),  # 'Św. Stanisława, Biskupa i Męczennika',
    constants.SANCTI_05_09: get_pages(877),  # 'Św. Grzegorza z Nazjanu, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_05_10: get_pages(877),  # 'Św. Antonina, Biskupa i Wyznawcy',
    constants.SANCTI_05_11: get_pages(882),  # 'Świętych Filipa i Jakuba, Apostołów',
    constants.SANCTI_05_12: get_pages(884),  # 'Świętych Nereusza, Achillesa, Domicylli i Pankracego, Męczenników',
    constants.SANCTI_05_13: get_pages(886),  # 'Św. Roberta Bellarmina, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_05_14: get_pages(888),  # 'Św. Bonifacego, Męczennika',
    constants.SANCTI_05_15: get_pages(888),  # 'Św. Jana Chrzciciela de la Salle, Wyznawcy',
    constants.SANCTI_05_16: get_pages(890),  # 'Św. Ubalda, Biskupa i Wyznawcy',
    constants.SANCTI_05_16PL: get_pages(889),  # 'Św. Andrzeja Boboli, Męczennika',
    constants.SANCTI_05_17: get_pages(891),  # 'Św. Paschalisa Baylon, Wyznawcy',
    constants.SANCTI_05_18: get_pages(891),  # 'Św. Wenancjusza, Męczennika',
    constants.SANCTI_05_19: get_pages(892),  # 'Św. Piotra Celestyna, Papieża i Wyznawcy',
    constants.SANCTI_05_20: get_pages(893),  # 'Św. Bernardyna ze Sieny, Wyznawcy',
    constants.SANCTI_05_24PL: get_pages(896),  # 'N. M. P. Wspomożycielki Wiernych',
    constants.SANCTI_05_25: get_pages(897),  # 'Św. Grzegorza VII, Papieża i Wyznawcy',
    constants.SANCTI_05_26: get_pages(898),  # 'Św. Filipa Nereusza, Wyznawcy',
    constants.SANCTI_05_27: get_pages(900),  # 'Św. Bedy Czcigodnego, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_05_28: get_pages(901),  # 'Św. Augustyna z Canterbury, Biskupa i Wyznawcy',
    constants.SANCTI_05_29: get_pages(902),  # 'Św. Marii Magdaleny Pazzi, Dziewicy',
    constants.SANCTI_05_30: get_pages(903),  # 'Św. Feliksa I, Papieża i Męczennika',
    constants.SANCTI_05_31: get_pages(903),  # 'N. M. P. Królowej',
    constants.SANCTI_06_01: get_pages(908),  # 'Św. Anieli Merici, Dziewicy',
    constants.SANCTI_06_02: get_pages(911),  # 'Śś. Marcelina i Piotra, Męczenników oraz Erazma, Biskupa',
    constants.SANCTI_06_04: get_pages(913),  # 'Św. Franciszka Caracciolo, Wyznawcy',
    constants.SANCTI_06_05: get_pages(915),  # 'Św. Bonifacego, Biskupa i Męczennika',
    constants.SANCTI_06_06: get_pages(918),  # 'Św. Norberta, Biskupa i Wyznawcy',
    constants.SANCTI_06_09: get_pages(918),  # 'Śś. Pryma i Felicjana, Męczenników',
    constants.SANCTI_06_10: get_pages(922),  # 'Św. Małgorzaty, Królowej Szkockiej, Wdowy',
    constants.SANCTI_06_10PL: get_pages(920),  # 'Bł. Bogumiła, Biskupa i Wyznawcy',
    constants.SANCTI_06_11: get_pages(922),  # 'Św. Barnaby, Apostoła',
    constants.SANCTI_06_12: get_pages(925),  # 'Św. Jana z Facundo, Wyznawcy',
    constants.SANCTI_06_13: get_pages(927),  # 'Św. Antoniego z Padwy, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_06_14: get_pages(928),  # 'Św. Bazylego Wielkiego, Wyznawcy, Biskupa i Doktora Kościoła',
    constants.SANCTI_06_15: get_pages(931),  # 'Śś. Wita, Modesta i Krescencji, Męczenników',
    constants.SANCTI_06_15PL: get_pages(930),  # 'Bł. Jolanty',
    constants.SANCTI_06_17: get_pages(933),  # 'Św. Grzegorza Barbarigo, Biskupa i Wyznawcy',
    constants.SANCTI_06_18: get_pages(934),  # 'Św. Efrema, Diakona, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_06_19: get_pages(936),  # 'Św. Juliany Falconieri, Dziewicy',
    constants.SANCTI_06_20: get_pages(939),  # 'Św. Sylweriusza, Papieża i Męczennika',
    constants.SANCTI_06_21: get_pages(940),  # 'Św. Alojzego Gonzagi, Wyznawcy',
    constants.SANCTI_06_22: get_pages(942),  # 'Św. Paulina, Biskupa i Wyznawcy',
    constants.SANCTI_06_23: get_pages(944),  # 'Wigilia Narodzenia Św. Jana Chrzciciela',
    constants.SANCTI_06_24: get_pages(947),  # 'Narodzenie Św. Jana Chrzciciela',
    constants.SANCTI_06_25: get_pages(950),  # 'Św. Wilhelma, Opata',
    constants.SANCTI_06_26: get_pages(950),  # 'Śś. Jana i Pawła, Męczenników',
    constants.SANCTI_06_28: get_pages(953),  # 'Wigilia śś. Apostołów Piotra i Pawła',
    constants.SANCTI_06_29: get_pages(956),  # 'Świętych Piotra i Pawła, Apostołów',
    constants.SANCTI_06_30: get_pages(959),  # 'Wspomnienie św. Pawła, Apostoła',
    constants.SANCTI_07_01: get_pages(963),  # 'Uroczystość Najdroższej Krwi Pana Naszego Jezusa Chrystusa',
    constants.SANCTI_07_02: get_pages(966),  # 'Nawiedzenia N. M. P.',
    constants.SANCTI_07_03: get_pages(969),  # 'Św. Ireneusza, Biskupa i Męczennika',
    constants.SANCTI_07_05: get_pages(972),  # 'Św. Antoniego Marii Zaccaria, Wyznawcy',
    constants.SANCTI_07_07: get_pages(975),  # 'Śś. Cyryla i Metodego, Biskupów i Wyznawców',
    constants.SANCTI_07_08: get_pages(977),  # 'Św. Elżbiety, Królowej i Wdowy',
    constants.SANCTI_07_10: get_pages(978),  # 'Siedmiu Braci Męczenników oraz Śś. Rufiny i Sekundy, Dziewic i Męczennic',
    constants.SANCTI_07_11: get_pages(980),  # 'Św. Piusa I, Papieża i Męczennika',
    constants.SANCTI_07_12: get_pages(980),  # 'Św. Jana Gwalberta, Opata',
    constants.SANCTI_07_14: get_pages(981),  # 'Św. Bonawentury, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_07_15: get_pages(982),  # 'Św. Henryka, Cesarza i Wyznawcy',
    constants.SANCTI_07_16: get_pages(983),  # 'Wspomnienie N. M. P. z Góry Karmelu',
    constants.SANCTI_07_17: get_pages(985),  # 'Św. Aleksego, Wyznawcy',
    constants.SANCTI_07_18: get_pages(989),  # 'Św. Kamila de Lellis',
    constants.SANCTI_07_18PL: get_pages(986),  # 'Bł. Szymona z Lipnicy, Wyznawcy',
    constants.SANCTI_07_19: get_pages(990),  # 'Św. Wincentego a Paulo, Wyznawcy',
    constants.SANCTI_07_20: get_pages(991),  # 'Św. Hieronima Emiliani, Wyznawcy',
    constants.SANCTI_07_20PL: get_pages(991),  # 'Bł. Czesława, Wyznawcy',
    constants.SANCTI_07_21: get_pages(994),  # 'Św. Wawrzyńca z Brindisi, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_07_22: get_pages(999),  # 'Św. Marii Magdaleny, Pokutnicy',
    constants.SANCTI_07_23: get_pages(1001),  # 'Św. Apolinarego, Biskupa i Męczennika',
    constants.SANCTI_07_24: get_pages(1005),  # 'Św. Krystyny, Dziewicy i Męczennicy',
    constants.SANCTI_07_24PL: get_pages(1004),  # 'Bł. Kingi, Dziewicy',
    constants.SANCTI_07_25: get_pages(1005),  # 'Św. Jakuba, Apostoła',
    constants.SANCTI_07_26: get_pages(1008),  # 'Św. Anny, Matki N. M. P.',
    constants.SANCTI_07_27: get_pages(1010),  # 'Św. Pantaleona, Męczennika',
    constants.SANCTI_07_28: get_pages(1010),  # 'Śś. Nazariusza i Celsa, Męczenników, Wiktora I, Papieża i Męczennika, oraz Innocentego I, Papieża i Wyznawcy',
    constants.SANCTI_07_29: get_pages(1011),  # 'Św. Marty, Dziewicy',
    constants.SANCTI_07_30: get_pages(1013),  # 'Śś. Abdona i Sennena, Męczenników',
    constants.SANCTI_07_31: get_pages(1015),  # 'Św. Ignacego Loyoli, Wyznawcy',
    constants.SANCTI_08_01: get_pages(1018),  # 'Siedmiu Braci Machabejskich, Męczenników',
    constants.SANCTI_08_02: get_pages(1019),  # 'Św. Alfonsa Marii Liguori, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_08_04: get_pages(1022),  # 'Św. Dominika, Wyznawcy',
    constants.SANCTI_08_05: get_pages(1024),  # 'Rocznica Konsekracji N. M. P. Śnieżnej',
    constants.SANCTI_08_06: get_pages(1025),  # 'Przemienienie Pańskie',
    constants.SANCTI_08_07: get_pages(1028),  # 'Św. Kajetana, Wyznawcy',
    constants.SANCTI_08_08: get_pages(1032),  # 'Św. Jana Marii Vianney, Wyznawcy',
    constants.SANCTI_08_09: get_pages(1034),  # 'Wigilia św. Wawrzyńca, Męczennika',
    constants.SANCTI_08_10: get_pages(1037),  # 'Św. Wawrzyńca',
    constants.SANCTI_08_11: get_pages(1039),  # 'Śś. Tyburcjusza i Zuzanny, Męczenników',
    constants.SANCTI_08_12: get_pages(1040),  # 'Św. Klary, Dziewicy',
    constants.SANCTI_08_13: get_pages(1040),  # 'Śś. Hipolita i Kasjana, Męczenników',
    constants.SANCTI_08_14: get_pages(1041),  # 'Wigilia Wniebowzięcia N. M. P.',
    constants.SANCTI_08_15: get_pages(1045),  # 'Wniebowzięcie N. M. P.',
    constants.SANCTI_08_16: get_pages(1047),  # 'Św. Joachima, Ojca N. M. P.',
    constants.SANCTI_08_17: get_pages(1050),  # 'Św. Jacka, Wyznawcy',
    constants.SANCTI_08_18: get_pages(1052),  # 'Św. Agapita, Męczennika',
    constants.SANCTI_08_19: get_pages(1054),  # 'Św. Jana Eudes, Wyznawcy',
    constants.SANCTI_08_20: get_pages(1054),  # 'Św. Bernarda, Opata i Doktora Kościoła',
    constants.SANCTI_08_21: get_pages(1055),  # 'Św. Joanny Franciszki Frémiot de Chantal, Wdowy',
    constants.SANCTI_08_22: get_pages(1056),  # 'Uroczystość Niepokalanego Serca N. M. P.',
    constants.SANCTI_08_23: get_pages(1060),  # 'Św. Filipa Benicjusza, Wyznawcy',
    constants.SANCTI_08_24: get_pages(1060),  # 'Św. Bartłomieja, Apostoła',
    constants.SANCTI_08_25: get_pages(1063),  # 'Św. Ludwika, Króla i Wyznawcy',
    constants.SANCTI_08_26PL: get_pages(1066),  # 'N. M. P. Jasnogórskiej czyli Częstochowskiej',
    constants.SANCTI_08_27: get_pages(1069),  # 'Św. Józefa Kalasantego, Wyznawcy',
    constants.SANCTI_08_28: get_pages(1071),  # 'Św. Augustyna, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_08_29: get_pages(1073),  # 'Ścięcie Św. Jana Chrzciciela',
    constants.SANCTI_08_30: get_pages(1076),  # 'Św. Róży z Limy, Dziewicy',
    constants.SANCTI_08_31: get_pages(1078),  # 'Św. Rajmunda Nonnata, Wyznawcy',
    constants.SANCTI_09_01: get_pages(1080),  # 'Św. Idziego, Opata oraz Śś. Dwunastu Braci, Męczenników',
    constants.SANCTI_09_01PL: get_pages(1079),  # 'Bł. Bronisławy, Dziewicy',
    constants.SANCTI_09_02: get_pages(1081),  # 'Św. Stefana, Króla i Wyznawcy',
    constants.SANCTI_09_03: get_pages(1082),  # 'Św. Piusa X, Papieża i Wyznawcy',
    constants.SANCTI_09_05: get_pages(1085),  # 'Św. Wawrzyńca Justiniani, Biskupa i Wyznawcy',
    constants.SANCTI_09_07PL: get_pages(1086),  # 'Bł. Melchiora Grodzieckiego, Męczennika',
    constants.SANCTI_09_08: get_pages(1086),  # 'Narodzenie N. M. P.',
    constants.SANCTI_09_09: get_pages(1089),  # 'Św. Gorgoniusza, Męczennika',
    constants.SANCTI_09_10: get_pages(1090),  # 'Św. Mikołaja z Tolentynu, Wyznawcy',
    constants.SANCTI_09_11: get_pages(1090),  # 'Św. Prota i Jacka, Męczenników',
    constants.SANCTI_09_12: get_pages(1091),  # 'Najświętszego Imienia Maryi',
    constants.SANCTI_09_14: get_pages(1093),  # 'Podwyższenia Świętego Krzyża',
    constants.SANCTI_09_15: get_pages(1095),  # 'Siedmiu Boleści N. M. P.',
    constants.SANCTI_09_16: get_pages(1101),  # 'Św. Korneliusza, Papieża i Cypriana, Męczenników',
    constants.SANCTI_09_17: get_pages(1102),  # 'Stygmatów św. Franciszka, Wyznawcy',
    constants.SANCTI_09_18: get_pages(1102),  # 'Św. Józefa z Kupertynu, Wyznawcy',
    constants.SANCTI_09_19: get_pages(1104),  # 'Św. Januarego i Towarzyszy, Męczenników',
    constants.SANCTI_09_20: get_pages(1105),  # 'Św. Eustachego i Towarzyszy, Męczenników',
    constants.SANCTI_09_21: get_pages(1105),  # 'Św. Mateusza, Apostoła i Ewangelisty',
    constants.SANCTI_09_22: get_pages(1107),  # 'Św. Tomasza z Villanueva, Biskupa i Wyznawcy',
    constants.SANCTI_09_23: get_pages(1110),  # 'Św. Linusa, Papieża i Męczennika',
    constants.SANCTI_09_24: get_pages(1110),  # 'N. M. P. od Wykupu Jeńców',
    constants.SANCTI_09_25PL: get_pages(1111),  # 'Bł. Władysława z Gielniowa, Wyznawcy',
    constants.SANCTI_09_26: get_pages(1112),  # 'Śś. Cypriana i Justyny, Męczenników',
    constants.SANCTI_09_27: get_pages(1113),  # 'Św. Kosmy i Damiana, Męczenników',
    constants.SANCTI_09_28: get_pages(1115),  # 'Św. Wacława, Księcia i Męczennika',
    constants.SANCTI_09_29: get_pages(1117),  # 'Świętego Michała Archanioła',
    constants.SANCTI_09_30: get_pages(1121),  # 'Św. Hieronima, Kapłana, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_10_01: get_pages(1122),  # 'Św. Remigiusza, Biskupa i Wyznawcy',
    constants.SANCTI_10_01PL: get_pages(1122),  # 'Bł. Jana z Dukli',
    constants.SANCTI_10_02: get_pages(1123),  # 'Świętych Aniołów Stróżów',
    constants.SANCTI_10_03: get_pages(1125),  # 'Św. Teresy od Dzieciątka Jezus, Dziewicy',
    constants.SANCTI_10_04: get_pages(1127),  # 'Św. Franciszka, Wyznawcy',
    constants.SANCTI_10_05: get_pages(1130),  # 'Śś. Placyda i Towarzyszy, Męczenników',
    constants.SANCTI_10_06: get_pages(1130),  # 'Św. Brunona, Wyznawcy',
    constants.SANCTI_10_07: get_pages(1131),  # 'N. M. P. Różańcowej',
    constants.SANCTI_10_08: get_pages(1133),  # 'Św. Brygidy, Wdowy',
    constants.SANCTI_10_09: get_pages(1135),  # 'Św. Jana Leonardi, Wyznawcy',
    constants.SANCTI_10_09PL: get_pages(808),  # 'Bł. Wincentego Kadłubka',
    constants.SANCTI_10_10: get_pages(1142),  # 'Św. Franciszka Borgiasza, Wyznawcy',
    constants.SANCTI_10_11: get_pages(1143),  # 'Macierzyństwa N. M. P.',
    constants.SANCTI_10_13: get_pages(1146),  # 'Św. Edwarda, króla i wyznawcy',
    constants.SANCTI_10_14: get_pages(1146),  # 'Św. Kaliksta, papieża i męczennika',
    constants.SANCTI_10_15: get_pages(1147),  # 'Św. Teresy z Avili, Dziewicy',
    constants.SANCTI_10_16: get_pages(1147),  # 'Św. Jadwigi, Wdowy',
    constants.SANCTI_10_17: get_pages(1149),  # 'Św. Małgorzaty Marii Alacoque, Dziewicy',
    constants.SANCTI_10_18: get_pages(1151),  # 'Św. Łukasza, Ewangelisty',
    constants.SANCTI_10_19: get_pages(1054),  # 'Św. Piotra z Alkantary, Wyznawcy',
    constants.SANCTI_10_20: get_pages(1054),  # 'Św. Jana Kantego, Wyznawcy',
    constants.SANCTI_10_21: get_pages(1156),  # 'Św. Hilariona, Opata',
    constants.SANCTI_10_21PL: get_pages(906),  # 'Bł. Jakuba Strzemię, Biskupa i Wyznawcy',
    constants.SANCTI_10_23: get_pages(1159),  # 'Św. Antoniego Marii Claret, Biskupa i Wyznawcy',
    constants.SANCTI_10_24: get_pages(1159),  # 'Św. Rafała Archanioła',
    constants.SANCTI_10_25: get_pages(1162),  # 'Śś. Chryzanta i Darii, Męczenników',
    constants.SANCTI_10_28: get_pages(1163),  # 'Świętych Szymona i Judy Tadeusza, Apostołow',
    constants.SANCTI_11_01: get_pages(1171),  # 'Uroczystość Wszystkich Świętych',
    constants.SANCTI_11_02_1: get_pages(1174),  # 'Dzień Zaduszny',
    constants.SANCTI_11_02_2: get_pages(1177),  # 'Dzień Zaduszny – Druga Msza',
    constants.SANCTI_11_02_3: get_pages(1178),  # 'Dzień Zaduszny – Trzecia Msza',
    constants.SANCTI_11_04: get_pages(1179),  # 'Św. Karola Boromeusza, Biskupa i Wyznawcy',
    constants.SANCTI_11_08: get_pages(1182),  # 'Świętych Czterech Ukoronowanych Męczenników',
    constants.SANCTI_11_09: get_pages(1183),  # 'Rocznica Konsekracji Bazyliki Najświętszego Zbawiciela na Lateranie',
    constants.SANCTI_11_10: get_pages(1184),  # 'Św. Andrzeja z Avellino, Wyznawcy',
    constants.SANCTI_11_11: get_pages(1186),  # 'Św. Marcina, Biskupa i Wyznawcy',
    constants.SANCTI_11_12: get_pages(1190),  # 'Św. Marcina I, Papieża i Męczennika',
    constants.SANCTI_11_12PL: get_pages(1188),  # 'Śś. Benedykta, Jana, Mateusza, Izaaka i Krystyna, Męczenników',
    constants.SANCTI_11_13: get_pages(1193),  # 'Św. Dydaka, Wyznawcy',
    constants.SANCTI_11_13PL: get_pages(1190),  # 'Św. Stanisława Kostki, Wyznawcy',
    constants.SANCTI_11_14: get_pages(1194),  # 'Św. Jozafata, Biskupa i Męczennika',
    constants.SANCTI_11_15: get_pages(1196),  # 'Św. Alberta Wielkiego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_11_16: get_pages(1197),  # 'Św. Gertrudy, Dziewicy',
    constants.SANCTI_11_17: get_pages(1200),  # 'Św. Grzegorza Cudotwórcy, Biskupa i Wyznawcy',
    constants.SANCTI_11_17PL: get_pages(1199),  # 'Bł. Salomea',
    constants.SANCTI_11_18: get_pages(1200),  # 'Rocznica Konsekracji Bazylik Świętych Apostołów Piotra i Pawła, Apostołów',
    constants.SANCTI_11_19: get_pages(1201),  # 'Św. Elżbiety, Wdowy',
    constants.SANCTI_11_20: get_pages(1201),  # 'Św. Feliksa Walezego, Wyznawcy',
    constants.SANCTI_11_20PL: get_pages(1190),  # 'Św. Marcina I, Papieża i Męczennika',
    constants.SANCTI_11_21: get_pages(1202),  # 'Ofiarowanie N. M. P.',
    constants.SANCTI_11_22: get_pages(1202),  # 'Św. Cecylii, Dziewicy i Męczennicy',
    constants.SANCTI_11_23: get_pages(1204),  # 'Św. Klemensa I, Papieża i Męczennika',
    constants.SANCTI_11_24: get_pages(1206),  # 'Św. Jana od Krzyża, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_11_25: get_pages(1207),  # 'Św. Katarzyny, Dziewicy i Męczennicy',
    constants.SANCTI_11_26: get_pages(1208),  # 'Św. Sylwestra, Opata',
    constants.SANCTI_11_29: get_pages(1209),  # 'Św. Saturnina, Męczennika',
    constants.SANCTI_11_30: get_pages(1210),  # 'Św. Andrzeja, Apostoła',
    constants.SANCTI_12_02: get_pages(721),  # 'Św. Bibiany, Dziewicy i Męczennicy',
    constants.SANCTI_12_02PL: get_pages(724),  # 'Św. Piotra Chryzologa, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_12_03: get_pages(721),  # 'Św. Franciszka Ksawerego, Wyznawcy',
    constants.SANCTI_12_04: get_pages(724),  # 'Św. Piotra Chryzologa, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_12_04PL: get_pages(725),  # 'Św. Barbary',
    constants.SANCTI_12_05: get_pages(726),  # 'Św. Saby, Opata',
    constants.SANCTI_12_06: get_pages(726),  # 'Św. Mikołaja, Biskupa i Wyznawcy',
    constants.SANCTI_12_07: get_pages(728),  # 'Św. Ambrożego, Biskupa, Wyznawcy i Doktora Kościoła',
    constants.SANCTI_12_08: get_pages(731),  # 'Niepokalane Poczęcie N. M. P.',
    constants.SANCTI_12_10: get_pages(735),  # 'Św. Melchiadesa, Papieża i Męczennika',
    constants.SANCTI_12_11: get_pages(735),  # 'Św. Damazego, Papieża i Wyznawcy',
    constants.SANCTI_12_13: get_pages(735),  # 'Św. Łucji, Dziewicy i Męczennicy',
    constants.SANCTI_12_16: get_pages(737),  # 'Św. Euzebiusza, Biskupa i Męczennika',
    constants.SANCTI_12_21: get_pages(737),  # 'Św. Tomasza, Apostoła',
    constants.SANCTI_12_24: get_pages(71),  # 'Wigilia Bożego Narodzenia',
    constants.SANCTI_12_25_1: get_pages(77),  # 'Boże Narodzenie',
    constants.SANCTI_12_25_2: get_pages(79),  # 'Boże Narodzenie — Msza o świcie',
    constants.SANCTI_12_25_3: get_pages(82),  # 'Boże Narodzenie — Msza w dzień',
    constants.SANCTI_12_26: get_pages(88),  # 'Św. Szczepana, Pierwszego Męczennika',
    constants.SANCTI_12_27: get_pages(92),  # 'Św. Jana, Apostoła i Ewangelisty',
    constants.SANCTI_12_28: get_pages(94),  # 'Świętych Młodzianków',
    constants.SANCTI_12_29: get_pages(97),  # 'Św. Tomasza z Canterbury, Biskupa i Męczennika',
    constants.SANCTI_12_31: get_pages(99),  # 'Św. Sylwestra I, papieża i wyznawcy',
    constants.VOTIVE_ANGELS: get_pages(1216),  # 'Msza o Aniołach',
    constants.VOTIVE_JOSEPH: get_pages(1219),  # 'Msza o św. Józefie',
    constants.VOTIVE_PETERPAUL: get_pages(1222),  # 'Msza o śś. Piotrze i Pawle Apostołach',
    constants.VOTIVE_PETERPAULP: get_pages(1222),  # 'Msza o śś. Piotrze i Pawle Apostołach',
    constants.VOTIVE_APOSTLES: get_pages(1224),  # 'Msza o wszystkich śś. Apostołach',
    constants.VOTIVE_APOSTLESP: get_pages(1224),  # 'Msza o wszystkich śś. Apostołach',
    constants.VOTIVE_HOLYSPIRIT: get_pages(1224),  # 'Msza o Duchu Świętym',
    constants.VOTIVE_HOLYSPIRIT2: get_pages(1225),  # 'Msza dla uproszenia łask Ducha Świętego',
    constants.VOTIVE_BLESSEDSACRAMENT: get_pages(1226),  # 'Msza o Najświętszym Sakramencie',
    constants.VOTIVE_JESUSETERNALPRIEST: get_pages(1227),  # 'Msza o Chrystusie, Najwyższym i Wiecznym Kapłanie',
    constants.VOTIVE_CROSS: get_pages(1230),  # 'Msza o Krzyżu Świętym',
    constants.VOTIVE_PASSION: get_pages(1233),  # 'Msza o Męce Pańskiej',
    constants.VOTIVE_PENT01_0: get_pages(1215),  # 'Msza o Trójcy Przenajświętszej',
    constants.VOTIVE_PENT02_5: get_pages(506),  # 'Msza o Najświętszym Sercu Pana Jezusa',
    constants.VOTIVE_08_22: get_pages(1056),  # 'Msza o Niepokalanym Sercu N. M. P.',
    constants.VOTIVE_DEFUNCTORUM: get_pages(1301),  # 'Msza Codzienna za Zmarłych',
    constants.VOTIVE_FIDEI_PROPAGATIONE: get_pages(1252),  # 'Msza o Rozkrzewienie Wiary',
    constants.VOTIVE_MATRIMONIUM: get_pages(1396),  # 'Msza za Nowożeńców',
}