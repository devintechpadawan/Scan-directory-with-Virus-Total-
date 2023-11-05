# Scan-directory-with-Virus-Total-

This script will take any directory you point it to, walk the path, hash all of the files, display them in a PrettyTable, run them through Virus Total and display output from each security provider. You must get a Virus Total API key and add it to line 14. You can only scan 4 documents per minute with the free API key. 




Sample Output


Starting directory: C:\Users\Administrator\Desktop\TARGET


Hashing Files:  C:\Users\Administrator\Desktop\TARGET 



+----------------------------------+------------------------------------------------------+

| MD-5 Hash                        | Path                                                 |

+----------------------------------+------------------------------------------------------+

| 9F08258A80D578A0F1CC38FE4C2AEBB5 | C:\Users\Administrator\Desktop\TARGET\Camouflage.exe |

| CB43A221C8543267BA7710B99EDC9EE2 | C:\Users\Administrator\Desktop\TARGET\HIP.EXE        |

| F06794A70A2BF4A471B175AF23FBC59E | C:\Users\Administrator\Desktop\TARGET\Jphswin.exe    |

| 13AE5DB51BDDD590B1E56D6A479ECE16 | C:\Users\Administrator\Desktop\TARGET\mp3stegz.exe   |

| 6470FBBC7952B5EFD2B07230DEC99C86 | C:\Users\Administrator\Desktop\TARGET\StegSpy2.1     |

+----------------------------------+------------------------------------------------------+



FILEPATH

C:\Users\Administrator\Desktop\TARGET\Camouflage.exe



{

    "results": {

        "scans": {

            "Bkav": {

                "detected": false,

                "version": "1.3.0.9899",

                "result": null,

                "update": "20220629"

            },

            "Lionic": {

                "detected": false,

                "version": "7.5",

                "result": null,

                "update": "20220629"

            },

            "Elastic": {

                "detected": false,

                "version": "4.0.40",

                "result": null,

                "update": "20220623"

            },

            "DrWeb": {

                "detected": false,

                "version": "7.0.56.4040",

                "result": null,

                "update": "20220629"

            },

            "MicroWorld-eScan": {

                "detected": false,

                "version": "14.0.409.0",

                "result": null,

                "update": "20220628"

            },

            "FireEye": {

                "detected": false,

                "version": "35.24.1.0",

                "result": null,

                "update": "20220628"

            },

            "CAT-QuickHeal": {

                "detected": false,

                "version": "14.00",

                "result": null,

                "update": "20220628"

            },

            "ALYac": {

                "detected": false,

                "version": "1.1.3.1",

                "result": null,

                "update": "20220628"

            },

            "Cylance": {

                "detected": false,

                "version": "2.3.1.101",

                "result": null,

                "update": "20220629"

            },

            "Sangfor": {

                "detected": false,

                "version": "2.14.0.0",

                "result": null,

                "update": "20220602"

            },

            "K7AntiVirus": {

                "detected": false,

                "version": "12.22.43068",

                "result": null,

                "update": "20220629"

            },

            "Alibaba": {

                "detected": false,

                "version": "0.3.0.5",

                "result": null,

                "update": "20190527"

            },

            "K7GW": {

                "detected": false,

                "version": "12.22.43066",

                "result": null,

                "update": "20220628"

            },

            "CrowdStrike": {

                "detected": false,

                "version": "1.0",

                "result": null,

                "update": "20220418"

            },

            "BitDefenderTheta": {

                "detected": false,

                "version": "7.2.37796.0",

                "result": null,

                "update": "20220614"

            },

            "VirIT": {

                "detected": false,

                "version": "9.5.226",

                "result": null,

                "update": "20220628"

            },

            "Cyren": {

                "detected": false,

                "version": "6.5.1.2",

                "result": null,

                "update": "20220628"

            },

            "Symantec": {

                "detected": false,

                "version": "1.17.0.0",

                "result": null,

                "update": "20220628"

            },

            "tehtris": {

                "detected": false,

                "version": "v0.1.4",

                "result": null,

                "update": "20220629"

            },

            "ESET-NOD32": {

                "detected": false,

                "version": "25511",

                "result": null,

                "update": "20220629"

            },

            "Zoner": {

                "detected": false,

                "version": "2.2.2.0",

                "result": null,

                "update": "20220628"

            },

            "TrendMicro-HouseCall": {

                "detected": false,

                "version": "10.0.0.1040",

                "result": null,

                "update": "20220629"

            },

            "Paloalto": {

                "detected": false,

                "version": "0.9.0.1003",

                "result": null,

                "update": "20220629"

            },

            "ClamAV": {

                "detected": false,

                "version": "0.105.0.0",

                "result": null,

                "update": "20220628"

            },

            "Kaspersky": {

                "detected": false,

                "version": "21.0.1.45",

                "result": null,

                "update": "20220629"

            },

            "BitDefender": {

                "detected": false,

                "version": "7.2",

                "result": null,

                "update": "20220629"

            },

            "NANO-Antivirus": {

                "detected": false,

                "version": "1.0.146.25588",

                "result": null,

                "update": "20220629"

            },

            "SUPERAntiSpyware": {

                "detected": false,

                "version": "5.6.0.1032",

                "result": null,

                "update": "20220625"

            },

            "Avast": {

                "detected": false,

                "version": "21.1.5827.0",

                "result": null,

                "update": "20220628"

            },

            "Tencent": {

                "detected": false,

                "version": "1.0.0.1",

                "result": null,

                "update": "20220629"

            },

            "Ad-Aware": {

                "detected": false,

                "version": "3.0.21.193",

                "result": null,

                "update": "20220629"

            },

            "Emsisoft": {

                "detected": false,

                "version": "2021.5.0.7597",

                "result": null,

                "update": "20220629"

            },

            "Comodo": {

                "detected": false,

                "version": "34757",

                "result": null,

                "update": "20220629"

            },

            "F-Secure": {

                "detected": false,

                "version": "18.10.978.51",

                "result": null,

                "update": "20220628"

            },

            "Baidu": {

                "detected": false,

                "version": "1.0.0.2",

                "result": null,

                "update": "20190318"

            },

            "Zillya": {

                "detected": false,

                "version": "2.0.0.4660",

                "result": null,

                "update": "20220628"

            },

            "TrendMicro": {

                "detected": false,

                "version": "11.0.0.1006",

                "result": null,

                "update": "20220629"

            },

            "McAfee-GW-Edition": {

                "detected": false,

                "version": "v2019.1.2+3728",

                "result": null,

                "update": "20220629"

            },

            "Trapmine": {

                "detected": false,

                "version": "3.5.48.98",

                "result": null,

                "update": "20220628"

            },

            "Sophos": {

                "detected": false,

                "version": "1.4.1.0",

                "result": null,

                "update": "20220628"

            },

            "Ikarus": {

                "detected": false,

                "version": "6.0.24.0",

                "result": null,

                "update": "20220628"

            },

            "GData": {

                "detected": false,

                "version": "A:25.33381B:27.27887",

                "result": null,

                "update": "20220629"

            },

            "Jiangmin": {

                "detected": false,

                "version": "16.0.100",

                "result": null,

                "update": "20220629"

            },

            "Webroot": {

                "detected": false,

                "version": "1.0.0.403",

                "result": null,

                "update": "20220629"

            },

            "Avira": {

                "detected": false,

                "version": "8.3.3.14",

                "result": null,

                "update": "20220629"

            },

            "MAX": {

                "detected": false,

                "version": "2019.9.16.1",

                "result": null,

                "update": "20220629"

            },

            "Kingsoft": {

                "detected": false,

                "version": "2017.9.26.565",

                "result": null,

                "update": "20220629"

            },

            "Gridinsoft": {

                "detected": false,

                "version": "1.0.82.174",

                "result": null,

                "update": "20220629"

            },

            "Arcabit": {

                "detected": false,

                "version": "1.0.0.889",

                "result": null,

                "update": "20220628"

            },

            "ViRobot": {

                "detected": false,

                "version": "2014.3.20.0",

                "result": null,

                "update": "20220628"

            },

            "ZoneAlarm": {

                "detected": false,

                "version": "1.0",

                "result": null,

                "update": "20220629"

            },

            "Microsoft": {

                "detected": false,

                "version": "1.1.19300.2",

                "result": null,

                "update": "20220629"

            },

            "Cynet": {

                "detected": false,

                "version": "4.0.0.27",

                "result": null,

                "update": "20220629"

            },

            "AhnLab-V3": {

                "detected": false,

                "version": "3.22.1.10283",

                "result": null,

                "update": "20220629"

            },

            "Acronis": {

                "detected": false,

                "version": "1.2.0.108",

                "result": null,

                "update": "20220426"

            },

            "McAfee": {

                "detected": false,

                "version": "6.0.6.653",

                "result": null,

                "update": "20220628"

            },

            "TACHYON": {

                "detected": false,

                "version": "2022-06-29.01",

                "result": null,

                "update": "20220629"

            },

            "VBA32": {

                "detected": true,

                "version": "5.0.0",

                "result": "TScope.Trojan.VB",

                "update": "20220628"

            },

            "Malwarebytes": {

                "detected": false,

                "version": "4.3.3.37",

                "result": null,

                "update": "20220628"

            },

            "APEX": {

                "detected": false,

                "version": "6.307",

                "result": null,

                "update": "20220628"

            },

            "Rising": {

                "detected": false,

                "version": "25.0.0.27",

                "result": null,

                "update": "20220628"

            },

            "Yandex": {

                "detected": false,

                "version": "5.5.2.24",

                "result": null,

                "update": "20220628"

            },

            "SentinelOne": {

                "detected": false,

                "version": "22.2.1.2",

                "result": null,

                "update": "20220330"

            },

            "MaxSecure": {

                "detected": true,

                "version": "1.0.0.1",

                "result": "Trojan.Malware.300983.susgen",

                "update": "20220628"

            },

            "Fortinet": {

                "detected": false,

                "version": "6.2.142.0",

                "result": null,

                "update": "20220629"

            },

            "Cybereason": {

                "detected": false,

                "version": "1.2.449",

                "result": null,

                "update": "20210330"

            },

            "Panda": {

                "detected": false,

                "version": "4.6.4.2",

                "result": null,

                "update": "20220628"

            }

        },

        "scan_id": "c0644197ad9104fc15b3cbe80e4473c03fbbff05baf19776446a9522c596ac1d-1656472618",

        "sha1": "0d386f5e293235a315a1e573835d8672002e0c51",

        "resource": "9F08258A80D578A0F1CC38FE4C2AEBB5",

        "response_code": 1,

        "scan_date": "2022-06-29 03:16:58",

        "permalink": "https://www.virustotal.com/gui/file/c0644197ad9104fc15b3cbe80e4473c03fbbff05baf19776446a9522c596ac1d/detection/f-c0644197ad9104fc15b3cbe80e4473c03fbbff05baf19776446a9522c596ac1d-1656472618",

        "verbose_msg": "Scan finished, information embedded",

        "total": 67,

        "positives": 2,

        "sha256": "c0644197ad9104fc15b3cbe80e4473c03fbbff05baf19776446a9522c596ac1d",

        "md5": "9f08258a80d578a0f1cc38fe4c2aebb5"

    },

    "response_code": 200

}



FILEPATH

C:\Users\Administrator\Desktop\TARGET\HIP.EXE



{

    "results": {

        "scans": {

            "Bkav": {

                "detected": false,

                "version": "1.3.0.4959",

                "result": null,

                "update": "20140612"

            },

            "Lionic": {

                "detected": false,

                "version": "1.5",

                "result": null,

                "update": "20140612"

            },

            "MicroWorld-eScan": {

                "detected": false,

                "version": "12.0.250.0",

                "result": null,

                "update": "20140612"

            },

            "nProtect": {

                "detected": false,

                "version": "2014-06-12.01",

                "result": null,

                "update": "20140612"

            },

            "CMC": {

                "detected": false,

                "version": "1.1.0.977",

                "result": null,

                "update": "20140610"

            },

            "CAT-QuickHeal": {

                "detected": false,

                "version": "14.00",

                "result": null,

                "update": "20140612"

            },

            "McAfee": {

                "detected": false,

                "version": "6.0.4.564",

                "result": null,

                "update": "20140612"

            },

            "Malwarebytes": {

                "detected": false,

                "version": "1.75.0.1",

                "result": null,

                "update": "20140612"

            },

            "Zillya": {

                "detected": false,

                "version": "2.0.0.1822",

                "result": null,

                "update": "20140612"

            },

            "K7AntiVirus": {

                "detected": false,

                "version": "9.179.12387",

                "result": null,

                "update": "20140612"

            },

            "K7GW": {

                "detected": false,

                "version": "9.179.12387",

                "result": null,

                "update": "20140612"

            },

            "TheHacker": {

                "detected": false,

                "version": "6.8.0.5.466",

                "result": null,

                "update": "20140612"

            },

            "NANO-Antivirus": {

                "detected": true,

                "version": "0.28.0.60253",

                "result": "Virus.Dos.HLLO.fosn",

                "update": "20140612"

            },

            "F-Prot": {

                "detected": false,

                "version": "4.7.1.166",

                "result": null,

                "update": "20140612"

            },

            "Symantec": {

                "detected": false,

                "version": "20131.1.5.61",

                "result": null,

                "update": "20140612"

            },

            "Norman": {

                "detected": false,

                "version": "7.04.04",

                "result": null,

                "update": "20140612"

            },

            "TotalDefense": {

                "detected": false,

                "version": "37.0.10995",

                "result": null,

                "update": "20140612"

            },

            "TrendMicro-HouseCall": {

                "detected": false,

                "version": "9.700.0.1001",

                "result": null,

                "update": "20140612"

            },

            "Avast": {

                "detected": false,

                "version": "8.0.1489.320",

                "result": null,

                "update": "20140612"

            },

            "ClamAV": {

                "detected": false,

                "version": "0.98.3.0",

                "result": null,

                "update": "20140612"

            },

            "Kaspersky": {

                "detected": false,

                "version": "12.0.0.1225",

                "result": null,

                "update": "20140612"

            },

            "BitDefender": {

                "detected": false,

                "version": "7.2",

                "result": null,

                "update": "20140612"

            },

            "Agnitum": {

                "detected": false,

                "version": "5.5.1.3",

                "result": null,

                "update": "20140610"

            },

            "SUPERAntiSpyware": {

                "detected": false,

                "version": "5.6.0.1032",

                "result": null,

                "update": "20140612"

            },

            "ByteHero": {

                "detected": false,

                "version": "1.0.0.1",

                "result": null,

                "update": "20140612"

            },

            "Tencent": {

                "detected": false,

                "version": "1.0.0.1",

                "result": null,

                "update": "20140612"

            },

            "Ad-Aware": {

                "detected": false,

                "version": "12.0.163.0",

                "result": null,

                "update": "20140612"

            },

            "Sophos": {

                "detected": false,

                "version": "4.98.0",

                "result": null,

                "update": "20140612"

            },

            "Comodo": {

                "detected": false,

                "version": "18527",

                "result": null,

                "update": "20140612"

            },

            "F-Secure": {

                "detected": false,

                "version": "11.0.19100.45",

                "result": null,

                "update": "20140612"

            },

            "DrWeb": {

                "detected": false,

                "version": "7.0.7.12100",

                "result": null,

                "update": "20140612"

            },

            "VIPRE": {

                "detected": false,

                "version": "30236",

                "result": null,

                "update": "20140612"

            },

            "AntiVir": {

                "detected": false,

                "version": "7.11.154.158",

                "result": null,

                "update": "20140612"

            },

            "TrendMicro": {

                "detected": false,

                "version": "9.740.0.1012",

                "result": null,

                "update": "20140612"

            },

            "McAfee-GW-Edition": {

                "detected": false,

                "version": "2013",

                "result": null,

                "update": "20140612"

            },

            "Emsisoft": {

                "detected": false,

                "version": "3.0.0.599",

                "result": null,

                "update": "20140612"

            },

            "Jiangmin": {

                "detected": false,

                "version": "16.0.100",

                "result": null,

                "update": "20140612"

            },

            "Antiy-AVL": {

                "detected": true,

                "version": "1.0.0.1",

                "result": "Virus/DOS.Helforia",

                "update": "20140611"

            },

            "Kingsoft": {

                "detected": false,

                "version": "2013.4.9.267",

                "result": null,

                "update": "20140612"

            },

            "Microsoft": {

                "detected": false,

                "version": "1.10600",

                "result": null,

                "update": "20140612"

            },

            "ViRobot": {

                "detected": false,

                "version": "2011.4.7.4223",

                "result": null,

                "update": "20140612"

            },

            "GData": {

                "detected": false,

                "version": "24",

                "result": null,

                "update": "20140612"

            },

            "Commtouch": {

                "detected": false,

                "version": "5.4.1.7",

                "result": null,

                "update": "20140612"

            },

            "AhnLab-V3": {

                "detected": false,

                "version": "2014.06.13.00",

                "result": null,

                "update": "20140612"

            },

            "VBA32": {

                "detected": false,

                "version": "3.12.26.0",

                "result": null,

                "update": "20140612"

            },

            "Baidu-International": {

                "detected": false,

                "version": "3.5.1.41473",

                "result": null,

                "update": "20140612"

            },

            "Zoner": {

                "detected": false,

                "version": "1.0",

                "result": null,

                "update": "20140611"

            },

            "ESET-NOD32": {

                "detected": false,

                "version": "9936",

                "result": null,

                "update": "20140612"

            },

            "Rising": {

                "detected": false,

                "version": "25.0.0.11",

                "result": null,

                "update": "20140612"

            },

            "Ikarus": {

                "detected": false,

                "version": "T3.1.6.1.0",

                "result": null,

                "update": "20140612"

            },

            "Fortinet": {

                "detected": false,

                "version": "5.1.152.0",

                "result": null,

                "update": "20140612"

            },

            "AVG": {

                "detected": false,

                "version": "14.0.0.3964",

                "result": null,

                "update": "20140612"

            },

            "Panda": {

                "detected": false,

                "version": "10.0.3.5",

                "result": null,

                "update": "20140612"

            },

            "Qihoo-360": {

                "detected": false,

                "version": "1.0.0.1015",

                "result": null,

                "update": "20140612"

            }

        },

        "scan_id": "ce76ca850d8509417edc46aedb1ec854dae883eae31163dce157121b6404463f-1402607311",

        "sha1": "fc678795d666b8b6af26f96b8b4dd1a2261c98bb",

        "resource": "CB43A221C8543267BA7710B99EDC9EE2",

        "response_code": 1,

        "scan_date": "2014-06-12 21:08:31",

        "permalink": "https://www.virustotal.com/gui/file/ce76ca850d8509417edc46aedb1ec854dae883eae31163dce157121b6404463f/detection/f-ce76ca850d8509417edc46aedb1ec854dae883eae31163dce157121b6404463f-1402607311",

        "verbose_msg": "Scan finished, information embedded",

        "total": 54,

        "positives": 2,

        "sha256": "ce76ca850d8509417edc46aedb1ec854dae883eae31163dce157121b6404463f",

        "md5": "cb43a221c8543267ba7710b99edc9ee2"

    },

    "response_code": 200

}



FILEPATH

C:\Users\Administrator\Desktop\TARGET\Jphswin.exe



{

    "results": {

        "scans": {

            "Bkav": {

                "detected": false,

                "version": "1.3.0.9899",

                "result": null,

                "update": "20230424"

            },

            "Lionic": {

                "detected": false,

                "version": "7.5",

                "result": null,

                "update": "20230424"

            },

            "tehtris": {

                "detected": false,

                "version": "v0.1.4",

                "result": null,

                "update": "20230424"

            },

            "MicroWorld-eScan": {

                "detected": false,

                "version": "14.0.409.0",

                "result": null,

                "update": "20230424"

            },

            "ClamAV": {

                "detected": false,

                "version": "1.0.1.0",

                "result": null,

                "update": "20230424"

            },

            "CMC": {

                "detected": false,

                "version": "2.4.2022.1",

                "result": null,

                "update": "20230424"

            },

            "CAT-QuickHeal": {

                "detected": false,

                "version": "22.00",

                "result": null,

                "update": "20230423"

            },

            "McAfee": {

                "detected": false,

                "version": "6.0.6.653",

                "result": null,

                "update": "20230424"

            },

            "Malwarebytes": {

                "detected": false,

                "version": "4.5.5.54",

                "result": null,

                "update": "20230424"

            },

            "Zillya": {

                "detected": false,

                "version": "2.0.0.4859",

                "result": null,

                "update": "20230424"

            },

            "Sangfor": {

                "detected": false,

                "version": "2.23.0.0",

                "result": null,

                "update": "20230421"

            },

            "CrowdStrike": {

                "detected": false,

                "version": "1.0",

                "result": null,

                "update": "20220812"

            },

            "Alibaba": {

                "detected": false,

                "version": "0.3.0.5",

                "result": null,

                "update": "20190527"

            },

            "K7GW": {

                "detected": false,

                "version": "12.82.47907",

                "result": null,

                "update": "20230424"

            },

            "K7AntiVirus": {

                "detected": false,

                "version": "12.82.47904",

                "result": null,

                "update": "20230424"

            },

            "Baidu": {

                "detected": false,

                "version": "1.0.0.2",

                "result": null,

                "update": "20190318"

            },

            "VirIT": {

                "detected": false,

                "version": "9.5.435",

                "result": null,

                "update": "20230424"

            },

            "Cyren": {

                "detected": false,

                "version": "6.5.1.2",

                "result": null,

                "update": "20230424"

            },

            "Symantec": {

                "detected": false,

                "version": "1.19.0.0",

                "result": null,

                "update": "20230424"

            },

            "Elastic": {

                "detected": false,

                "version": "4.0.85",

                "result": null,

                "update": "20230413"

            },

            "ESET-NOD32": {

                "detected": false,

                "version": "27123",

                "result": null,

                "update": "20230424"

            },

            "Zoner": {

                "detected": false,

                "version": "2.2.2.0",

                "result": null,

                "update": "20230424"

            },

            "APEX": {

                "detected": false,

                "version": "6.408",

                "result": null,

                "update": "20230416"

            },

            "Paloalto": {

                "detected": false,

                "version": "0.9.0.1003",

                "result": null,

                "update": "20230424"

            },

            "Cynet": {

                "detected": false,

                "version": "4.0.0.27",

                "result": null,

                "update": "20230424"

            },

            "Kaspersky": {

                "detected": false,

                "version": "22.0.1.28",

                "result": null,

                "update": "20230424"

            },

            "BitDefender": {

                "detected": false,

                "version": "7.2",

                "result": null,

                "update": "20230424"

            },

            "NANO-Antivirus": {

                "detected": true,

                "version": "1.0.146.25755",

                "result": "Trojan.Win32.Dzan.dhaecr",

                "update": "20230424"

            },

            "SUPERAntiSpyware": {

                "detected": false,

                "version": "5.6.0.1032",

                "result": null,

                "update": "20230423"

            },

            "Avast": {

                "detected": false,

                "version": "22.11.7701.0",

                "result": null,

                "update": "20230424"

            },

            "Tencent": {

                "detected": false,

                "version": "1.0.0.1",

                "result": null,

                "update": "20230424"

            },

            "TACHYON": {

                "detected": false,

                "version": "2023-04-24.02",

                "result": null,

                "update": "20230424"

            },

            "Sophos": {

                "detected": false,

                "version": "2.1.2.0",

                "result": null,

                "update": "20230424"

            },

            "F-Secure": {

                "detected": false,

                "version": "18.10.1137.128",

                "result": null,

                "update": "20230424"

            },

            "DrWeb": {

                "detected": false,

                "version": "7.0.59.12300",

                "result": null,

                "update": "20230424"

            },

            "VIPRE": {

                "detected": false,

                "version": "6.0.0.35",

                "result": null,

                "update": "20230424"

            },

            "TrendMicro": {

                "detected": false,

                "version": "11.0.0.1006",

                "result": null,

                "update": "20230424"

            },

            "McAfee-GW-Edition": {

                "detected": false,

                "version": "v2021.2.0+4045",

                "result": null,

                "update": "20230424"

            },

            "Trapmine": {

                "detected": false,

                "version": "4.0.14.446",

                "result": null,

                "update": "20230412"

            },

            "FireEye": {

                "detected": false,

                "version": "35.24.1.0",

                "result": null,

                "update": "20230424"

            },

            "Emsisoft": {

                "detected": false,

                "version": "2022.6.0.32461",

                "result": null,

                "update": "20230424"

            },

            "SentinelOne": {

                "detected": false,

                "version": "23.2.0.1",

                "result": null,

                "update": "20230404"

            },

            "GData": {

                "detected": false,

                "version": "A:25.35708B:27.31452",

                "result": null,

                "update": "20230424"

            },

            "Jiangmin": {

                "detected": false,

                "version": "16.0.100",

                "result": null,

                "update": "20230423"

            },

            "Webroot": {

                "detected": false,

                "version": "1.0.0.403",

                "result": null,

                "update": "20230424"

            },

            "Avira": {

                "detected": false,

                "version": "8.3.3.16",

                "result": null,

                "update": "20230424"

            },

            "Antiy-AVL": {

                "detected": false,

                "version": "3.0",

                "result": null,

                "update": "20230424"

            },

            "Gridinsoft": {

                "detected": false,

                "version": "1.0.114.174",

                "result": null,

                "update": "20230424"

            },

            "Xcitium": {

                "detected": false,

                "version": "35585",

                "result": null,

                "update": "20230423"

            },

            "Arcabit": {

                "detected": false,

                "version": "2022.0.0.18",

                "result": null,

                "update": "20230424"

            },

            "ViRobot": {

                "detected": false,

                "version": "2014.3.20.0",

                "result": null,

                "update": "20230424"

            },

            "ZoneAlarm": {

                "detected": false,

                "version": "1.0",

                "result": null,

                "update": "20230424"

            },

            "Microsoft": {

                "detected": false,

                "version": "1.1.20200.4",

                "result": null,

                "update": "20230424"

            },

            "Google": {

                "detected": false,

                "version": "1682370048",

                "result": null,

                "update": "20230424"

            },

            "AhnLab-V3": {

                "detected": false,

                "version": "3.23.2.10388",

                "result": null,

                "update": "20230424"

            },

            "Acronis": {

                "detected": false,

                "version": "1.2.0.114",

                "result": null,

                "update": "20230219"

            },

            "BitDefenderTheta": {

                "detected": false,

                "version": "7.2.37796.0",

                "result": null,

                "update": "20230418"

            },

            "ALYac": {

                "detected": false,

                "version": "1.1.3.1",

                "result": null,

                "update": "20230424"

            },

            "MAX": {

                "detected": false,

                "version": "2023.1.4.1",

                "result": null,

                "update": "20230424"

            },

            "VBA32": {

                "detected": false,

                "version": "5.0.0",

                "result": null,

                "update": "20230421"

            },

            "Cylance": {

                "detected": false,

                "version": "2.0.0.0",

                "result": null,

                "update": "20230419"

            },

            "Panda": {

                "detected": false,

                "version": "4.6.4.2",

                "result": null,

                "update": "20230424"

            },

            "TrendMicro-HouseCall": {

                "detected": false,

                "version": "10.0.0.1040",

                "result": null,

                "update": "20230424"

            },

            "Rising": {

                "detected": false,

                "version": "25.0.0.27",

                "result": null,

                "update": "20230424"

            },

            "Yandex": {

                "detected": false,

                "version": "5.5.2.24",

                "result": null,

                "update": "20230424"

            },

            "Ikarus": {

                "detected": false,

                "version": "6.1.14.0",

                "result": null,

                "update": "20230424"

            },

            "MaxSecure": {

                "detected": true,

                "version": "1.0.0.1",

                "result": "Trojan.Malware.300983.susgen",

                "update": "20230424"

            },

            "Fortinet": {

                "detected": false,

                "version": "6.4.258.0",

                "result": null,

                "update": "20230424"

            },

            "AVG": {

                "detected": false,

                "version": "22.11.7701.0",

                "result": null,

                "update": "20230424"

            },

            "DeepInstinct": {

                "detected": false,

                "version": "3.1.0.15",

                "result": null,

                "update": "20230420"

            }

        },

        "scan_id": "6276936e570c4618448803ec9fd9665b06a37d7bf3a34c2a2ec22f9526464845-1682375746",

        "sha1": "63a44fe41465c920c0507907a7bda91d53f91810",

        "resource": "F06794A70A2BF4A471B175AF23FBC59E",

        "response_code": 1,

        "scan_date": "2023-04-24 22:35:46",

        "permalink": "https://www.virustotal.com/gui/file/6276936e570c4618448803ec9fd9665b06a37d7bf3a34c2a2ec22f9526464845/detection/f-6276936e570c4618448803ec9fd9665b06a37d7bf3a34c2a2ec22f9526464845-1682375746",

        "verbose_msg": "Scan finished, information embedded",

        "total": 70,

        "positives": 2,

        "sha256": "6276936e570c4618448803ec9fd9665b06a37d7bf3a34c2a2ec22f9526464845",

        "md5": "f06794a70a2bf4a471b175af23fbc59e"

    },

    "response_code": 200

}



FILEPATH

C:\Users\Administrator\Desktop\TARGET\mp3stegz.exe



{

    "results": {

        "scans": {

            "Lionic": {

                "detected": false,

                "version": "7.5",

                "result": null,

                "update": "20220914"

            },

            "tehtris": {

                "detected": false,

                "version": "v0.1.4",

                "result": null,

                "update": "20220914"

            },

            "DrWeb": {

                "detected": false,

                "version": "7.0.58.8230",

                "result": null,

                "update": "20220914"

            },

            "MicroWorld-eScan": {

                "detected": false,

                "version": "14.0.409.0",

                "result": null,

                "update": "20220914"

            },

            "FireEye": {

                "detected": false,

                "version": "35.24.1.0",

                "result": null,

                "update": "20220914"

            },

            "CAT-QuickHeal": {

                "detected": false,

                "version": "14.00",

                "result": null,

                "update": "20220914"

            },

            "ALYac": {

                "detected": false,

                "version": "1.1.3.1",

                "result": null,

                "update": "20220914"

            },

            "Cylance": {

                "detected": false,

                "version": "2.3.1.101",

                "result": null,

                "update": "20220914"

            },

            "Zillya": {

                "detected": false,

                "version": "2.0.0.4709",

                "result": null,

                "update": "20220914"

            },

            "Sangfor": {

                "detected": false,

                "version": "2.21.0.0",

                "result": null,

                "update": "20220914"

            },

            "K7AntiVirus": {

                "detected": false,

                "version": "12.37.44337",

                "result": null,

                "update": "20220914"

            },

            "Alibaba": {

                "detected": false,

                "version": "0.3.0.5",

                "result": null,

                "update": "20190527"

            },

            "K7GW": {

                "detected": false,

                "version": "12.34.44289",

                "result": null,

                "update": "20220912"

            },

            "Cybereason": {

                "detected": false,

                "version": "1.2.449",

                "result": null,

                "update": "20210330"

            },

            "Arcabit": {

                "detected": false,

                "version": "1.0.0.889",

                "result": null,

                "update": "20220914"

            },

            "BitDefenderTheta": {

                "detected": false,

                "version": "7.2.37796.0",

                "result": null,

                "update": "20220905"

            },

            "VirIT": {

                "detected": false,

                "version": "9.5.282",

                "result": null,

                "update": "20220914"

            },

            "Cyren": {

                "detected": false,

                "version": "6.5.1.2",

                "result": null,

                "update": "20220914"

            },

            "Symantec": {

                "detected": false,

                "version": "1.18.0.0",

                "result": null,

                "update": "20220914"

            },

            "Elastic": {

                "detected": false,

                "version": "4.0.45",

                "result": null,

                "update": "20220913"

            },

            "ESET-NOD32": {

                "detected": false,

                "version": "25926",

                "result": null,

                "update": "20220914"

            },

            "Zoner": {

                "detected": false,

                "version": "2.2.2.0",

                "result": null,

                "update": "20220913"

            },

            "TrendMicro-HouseCall": {

                "detected": false,

                "version": "10.0.0.1040",

                "result": null,

                "update": "20220914"

            },

            "Paloalto": {

                "detected": false,

                "version": "0.9.0.1003",

                "result": null,

                "update": "20220914"

            },

            "ClamAV": {

                "detected": false,

                "version": "0.105.1.0",

                "result": null,

                "update": "20220914"

            },

            "Kaspersky": {

                "detected": false,

                "version": "21.0.1.45",

                "result": null,

                "update": "20220914"

            },

            "BitDefender": {

                "detected": false,

                "version": "7.2",

                "result": null,

                "update": "20220914"

            },

            "NANO-Antivirus": {

                "detected": false,

                "version": "1.0.146.25623",

                "result": null,

                "update": "20220914"

            },

            "SUPERAntiSpyware": {

                "detected": false,

                "version": "5.6.0.1032",

                "result": null,

                "update": "20220910"

            },

            "Avast": {

                "detected": false,

                "version": "21.1.5827.0",

                "result": null,

                "update": "20220914"

            },

            "Tencent": {

                "detected": false,

                "version": "1.0.0.1",

                "result": null,

                "update": "20220914"

            },

            "Ad-Aware": {

                "detected": false,

                "version": "3.0.21.193",

                "result": null,

                "update": "20220914"

            },

            "Emsisoft": {

                "detected": false,

                "version": "2022.6.0.32461",

                "result": null,

                "update": "20220914"

            },

            "Comodo": {

                "detected": false,

                "version": "34990",

                "result": null,

                "update": "20220914"

            },

            "F-Secure": {

                "detected": false,

                "version": "18.10.978.51",

                "result": null,

                "update": "20220914"

            },

            "Baidu": {

                "detected": false,

                "version": "1.0.0.2",

                "result": null,

                "update": "20190318"

            },

            "VIPRE": {

                "detected": false,

                "version": "6.0.0.35",

                "result": null,

                "update": "20220914"

            },

            "TrendMicro": {

                "detected": false,

                "version": "11.0.0.1006",

                "result": null,

                "update": "20220914"

            },

            "McAfee-GW-Edition": {

                "detected": false,

                "version": "v2019.1.2+3728",

                "result": null,

                "update": "20220914"

            },

            "Trapmine": {

                "detected": false,

                "version": "4.0.1.119",

                "result": null,

                "update": "20220907"

            },

            "Sophos": {

                "detected": false,

                "version": "1.4.1.0",

                "result": null,

                "update": "20220914"

            },

            "SentinelOne": {

                "detected": false,

                "version": "22.2.1.2",

                "result": null,

                "update": "20220330"

            },

            "Jiangmin": {

                "detected": false,

                "version": "16.0.100",

                "result": null,

                "update": "20220913"

            },

            "Webroot": {

                "detected": false,

                "version": "1.0.0.403",

                "result": null,

                "update": "20220914"

            },

            "Google": {

                "detected": false,

                "version": "1663178457",

                "result": null,

                "update": "20220914"

            },

            "Avira": {

                "detected": false,

                "version": "8.3.3.16",

                "result": null,

                "update": "20220914"

            },

            "MAX": {

                "detected": false,

                "version": "2019.9.16.1",

                "result": null,

                "update": "20220914"

            },

            "Antiy-AVL": {

                "detected": false,

                "version": "3.0",

                "result": null,

                "update": "20220914"

            },

            "Kingsoft": {

                "detected": false,

                "version": "2017.9.26.565",

                "result": null,

                "update": "20220914"

            },

            "Gridinsoft": {

                "detected": false,

                "version": "1.0.93.174",

                "result": null,

                "update": "20220914"

            },

            "Microsoft": {

                "detected": false,

                "version": "1.1.19600.3",

                "result": null,

                "update": "20220914"

            },

            "ViRobot": {

                "detected": false,

                "version": "2014.3.20.0",

                "result": null,

                "update": "20220914"

            },

            "ZoneAlarm": {

                "detected": false,

                "version": "1.0",

                "result": null,

                "update": "20220914"

            },

            "GData": {

                "detected": false,

                "version": "A:25.33997B:27.28815",

                "result": null,

                "update": "20220914"

            },

            "Cynet": {

                "detected": false,

                "version": "4.0.0.27",

                "result": null,

                "update": "20220914"

            },

            "AhnLab-V3": {

                "detected": false,

                "version": "3.22.2.10299",

                "result": null,

                "update": "20220914"

            },

            "Acronis": {

                "detected": false,

                "version": "1.2.0.108",

                "result": null,

                "update": "20220426"

            },

            "McAfee": {

                "detected": false,

                "version": "6.0.6.653",

                "result": null,

                "update": "20220914"

            },

            "TACHYON": {

                "detected": false,

                "version": "2022-09-14.02",

                "result": null,

                "update": "20220914"

            },

            "VBA32": {

                "detected": false,

                "version": "5.0.0",

                "result": null,

                "update": "20220914"

            },

            "Malwarebytes": {

                "detected": false,

                "version": "4.3.3.37",

                "result": null,

                "update": "20220914"

            },

            "APEX": {

                "detected": true,

                "version": "6.334",

                "result": "Malicious",

                "update": "20220913"

            },

            "Rising": {

                "detected": false,

                "version": "25.0.0.27",

                "result": null,

                "update": "20220914"

            },

            "Yandex": {

                "detected": false,

                "version": "5.5.2.24",

                "result": null,

                "update": "20220914"

            },

            "Ikarus": {

                "detected": false,

                "version": "6.0.26.0",

                "result": null,

                "update": "20220914"

            },

            "MaxSecure": {

                "detected": false,

                "version": "1.0.0.1",

                "result": null,

                "update": "20220914"

            },

            "Fortinet": {

                "detected": false,

                "version": "6.4.258.0",

                "result": null,

                "update": "20220914"

            },

            "Panda": {

                "detected": false,

                "version": "4.6.4.2",

                "result": null,

                "update": "20220914"

            },

            "CrowdStrike": {

                "detected": false,

                "version": "1.0",

                "result": null,

                "update": "20220418"

            }

        },

        "scan_id": "f7c5e4fa7f1f4cc63a362419f6abf335ef9266d4d2ce3ac033f6d536d4ba19d3-1663176235",

        "sha1": "215e3efde0263effde7729e460eb774730747fd4",

        "resource": "13AE5DB51BDDD590B1E56D6A479ECE16",

        "response_code": 1,

        "scan_date": "2022-09-14 17:23:55",

        "permalink": "https://www.virustotal.com/gui/file/f7c5e4fa7f1f4cc63a362419f6abf335ef9266d4d2ce3ac033f6d536d4ba19d3/detection/f-f7c5e4fa7f1f4cc63a362419f6abf335ef9266d4d2ce3ac033f6d536d4ba19d3-1663176235",

        "verbose_msg": "Scan finished, information embedded",

        "total": 69,

        "positives": 1,

        "sha256": "f7c5e4fa7f1f4cc63a362419f6abf335ef9266d4d2ce3ac033f6d536d4ba19d3",

        "md5": "13ae5db51bddd590b1e56d6a479ece16"

    },

    "response_code": 200

}



FILEPATH

C:\Users\Administrator\Desktop\TARGET\StegSpy2.1



{

    "error": "You exceeded the public API request rate limit (4 requests of any nature per minute)",

    "response_code": 204

}
