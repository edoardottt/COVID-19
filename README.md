# COVID-19

![1](https://github.com/edoardottt/COVID-19/blob/master/Images/1.png)
Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The disease was first identified in December 2019 in Wuhan, the capital of China's Hubei province, and has since spread globally, resulting in the ongoing 2019–20 coronavirus pandemic. As of 26 April 2020, more than 2.89 million cases have been reported across 185 countries and territories, resulting in more than 203,000 deaths. More than 822,000 people have recovered.

Common symptoms include fever, cough, fatigue, shortness of breath and loss of smell. While the majority of cases result in mild symptoms, some progress to viral pneumonia, multi-organ failure, or cytokine storm. More concerning symptoms include difficulty breathing, persistent chest pain, confusion, difficulty waking, and bluish skin. The time from exposure to onset of symptoms is typically around five days but may range from two to fourteen days.

The virus is primarily spread between people during close contact,[a] often via small droplets produced by coughing,[b] sneezing, or talking. The droplets usually fall to the ground or onto surfaces rather than remaining in the air over long distances. People may also become infected by touching a contaminated surface and then touching their face. In experimental settings, the virus may survive on surfaces for up to 72 hours. It is most contagious during the first three days after the onset of symptoms, although spread may be possible before symptoms appear and in later stages of the disease. The standard method of diagnosis is by real-time reverse transcription polymerase chain reaction (rRT-PCR) from a nasopharyngeal swab. Chest CT imaging may also be helpful for diagnosis in individuals where there is a high suspicion of infection based on symptoms and risk factors; however, guidelines do not recommend using it for routine screening.

Recommended measures to prevent infection include frequent hand washing, maintaining physical distance from others (especially from those with symptoms), covering coughs, and keeping unwashed hands away from the face. In addition, the use of a face covering is recommended for those who suspect they have the virus and their caregivers. Recommendations for face covering use by the general public vary, with some authorities recommending against their use, some recommending their use, and others requiring their use. Currently, there is not enough evidence for or against the use of masks (medical or other) in healthy individuals in the wider community. Also masks purchased by the public may impact availability for health care providers.

Currently, there is no vaccine or specific antiviral treatment for COVID-19. Management involves the treatment of symptoms, supportive care, isolation, and experimental measures. The World Health Organization (WHO) declared the 2019–20 coronavirus outbreak a Public Health Emergency of International Concern (PHEIC) on 30 January 2020 and a pandemic on 11 March 2020. Local transmission of the disease has occurred in most countries across all six WHO regions.


                                                                From Wikipedia, the free encyclopedia ©


- [Here the reports from World Health Organization](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports)
- [OurWorldInData CoronaVirus](https://ourworldindata.org/coronavirus)
- [Coronavirus disease (COVID-19) advice for the public: Myth busters](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters)
- [Global research database COVID-19](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/global-research-on-novel-coronavirus-2019-ncov)
- [Public Tableau COVID-19 Database](https://public.tableau.com/profile/anya.#!/vizhome/COVID-19Cases_15835248531800/COVID-19Cases)
- [HumData COVID-19 Dataset](https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases)
- [Italy daily cases map](https://observablehq.com/@jashkenas/italy-coronavirus-daily-cases-map-covid-19)
- [Dati Json e Csv della Protezione Civile Italiana](https://github.com/pcm-dpc/COVID-19)
- [Open Source projects about COVID-19](https://weileizeng.github.io/Open-Source-COVID-19/)
- [WHO advices for public](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public)
- [Italian Situation](http://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?lingua=italiano&id=5351&area=nuovoCoronavirus&menu=vuoto)
- [COVID-19 Geographical distribution](https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases)
- [COVID-19 Open Research Dataset (CORD-19)](https://pages.semanticscholar.org/coronavirus-research)

----------------------------------------------------------------------------------------------------------

**EXPLANATION OF SCRIPT.PY**

The italy.py script retrieves data from the official GitHub link of Italian Civil Protection.

    USAGE: python italy.py [-h]

           It shows the data on the command line.

    -h or --help:

            Help doc

**Use python3 instead of python command if you are on Linux.**

It's the same for global.py. Execute python(3 if Linux) global.py. 

**Screenshot of the output of italy.py on 20/3/2020**
![2](https://github.com/edoardottt/COVID-19/blob/master/Images/2.png)

From [https://github.com/pcm-dpc/COVID-19](https://github.com/pcm-dpc/COVID-19)
| Nome campo                  | Descrizione                       | Description                            | Formato                       | Esempio             |
|-----------------------------|-----------------------------------|----------------------------------------|-------------------------------|---------------------|
| **data**                        | Data dell'informazione            | Date of notification                   | YYYY-MM-DD HH:MM:SS (ISO 8601) Ora italiana | 2020-03-05 12:15:45 |
| **stato**                       | Stato di riferimento              | Country of reference                   | XYZ (ISO 3166-1 alpha-3)      | ITA                 |
| **codice_regione**              | Codice della Regione (ISTAT 2019) | Code of the Region (ISTAT 2019)        | Numero                        | 13                  |
| **denominazione_regione**       | Denominazione della Regione       | Name of the Region                     | Testo                         | Abruzzo             |
| **lat**                         | Latitudine                        | Latitude                               | WGS84                         | 42.6589177          |
| **long**                        | Longitudine                       | Longitude                              | WGS84                         | 13.70439971         |
| **ricoverati_con_sintomi**      | Ricoverati con sintomi            | Hospitalised patients with symptoms    | Numero                        | 3                   |
| **terapia_intensiva**           | Ricoverati in terapia intensiva   | Intensive Care                         | Numero                        | 3                   |
| **totale_ospedalizzati**        | Totale ospedalizzati              | Total hospitalised patients            | Numero                        | 3                   |
| **isolamento_domiciliare**      | Persone in isolamento domiciliare | Home confinement                       | Numero                        | 3                   |
| **totale_positivi** | Totale attualmente positivi (ospedalizzati + isolamento domiciliare)      | Total amount of current positive cases (Hospitalised patients + Home confinement)  | Numero                        | 3                   |
| **variazione_totale_positivi**  | Variazione del totale positivi (totale_positivi giorno corrente - totale_positivi giorno precedente)       | News amount of current positive cases (totale_positivi current day - totale_positivi previous day)  | Numero                        | 3                   |
| **nuovi_positivi**  | Nuovi attualmente positivi (totale_casi giorno corrente - totale_casi giorno precedente)       | News amount of current positive cases (totale_casi current day - totale_casi previous day)  | Numero                        | 3                   |
| **dimessi_guariti**             | Persone dimesse guarite           | Recovered                              | Numero                        | 3                   |
| **deceduti**                    | Persone decedute                  | Death                                  | Numero                        | 3                   |
| **totale_casi**                 | Totale casi positivi              | Total amount of positive cases         | Numero                        | 3                   |
| **tamponi**                     | Totale tamponi                    | Tests performed                        | Numero                        | 3                   |
| **note_it**                     | Note in lingua italiana (separate da ;)                   | Notes in italian language (separated by ;)                       | Testo                        | pd-IT-000                   |
| **note_en**                     | Note in lingua inglese (separate da ;)                    | Notes in english language (separated by ;)                       | Testo                        | pd-EN-000                   |


--------------------------
If you liked it drop a :star:
--------------------------

https://www.edoardoottavianelli.it for contact me.


                                                                      Edoardo Ottavianelli
