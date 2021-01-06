# COVID-19

![1](https://github.com/edoardottt/COVID-19/blob/master/Images/1.png)
Coronavirus disease 2019 (COVID-19) is a contagious respiratory and vascular disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). First identified in Wuhan, China, it has caused an ongoing pandemic.

Common symptoms of COVID-19 include fever, cough, fatigue, breathing difficulties, and loss of smell and taste. Symptoms begin one to fourteen days after exposure to the virus. While most people have mild symptoms, some people develop acute respiratory distress syndrome (ARDS). ARDS can be precipitated by cytokine storms, multi-organ failure, septic shock, and blood clots. Longer-term damage to organs (in particular, the lungs and heart) has been observed. There is concern about a significant number of patients who have recovered from the acute phase of the disease but continue to experience a range of effects—known as long COVID—for months afterwards. These effects include severe fatigue, memory loss and other cognitive issues, low grade fever, muscle weakness, and breathlessness.

COVID-19 mainly spreads through the air when people are near each other long enough, primarily via small droplets or aerosols, as an infected person breathes, coughs, sneezes, sings, or speaks. Transmission via fomites (contaminated surfaces) has not been conclusively demonstrated. It can spread as early as two days before infected persons show symptoms (presymptomatic), and from asymptomatic (no symptoms) individuals. People remain infectious for up to ten days in moderate cases, and two weeks in severe cases. The standard diagnosis method is by real-time reverse transcription polymerase chain reaction (rRT-PCR) from a nasopharyngeal swab.

Preventive measures include social distancing, quarantining, ventilation of indoor spaces, covering coughs and sneezes, hand washing, and keeping unwashed hands away from the face. The use of face masks or coverings has been recommended in public settings to minimise the risk of transmissions.

There are currently no proven vaccines or specific treatments for COVID-19, though several are in development. Management involves the treatment of symptoms, supportive care, isolation, and experimental measures.

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

**Use python3.x**

It's the same for global.py. Execute python(3.x) global.py. 

**Screenshot of the output of italy.py on 20/3/2020**
![2](https://github.com/edoardottt/COVID-19/blob/master/Images/2.png)

##### From [https://github.com/pcm-dpc/COVID-19](https://github.com/pcm-dpc/COVID-19)
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
