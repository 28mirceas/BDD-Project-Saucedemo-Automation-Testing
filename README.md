# Proiect BDD – Automatizare Testare cu Behave & Selenium

## Descriere

Acest proiect reprezintă o suită de teste automate scrise folosind
Behavior-Driven Development (BDD) cu Behave, împreună cu modelul  Page Object Model (POM).
Testele validează funcționalitățile esențiale ale unei aplicații web:
Login, Produse, Coș și Checkout.
Proiectul este structurat astfel încât să fie ușor de extins, întreținut și integrat
într-un mediu real de QA Automation.

## Tehnologii folosite

- Python 3.13
- Behave – framework BDD
- Selenium WebDriver
- Page Object Model (POM)
- Chrome / Edge / Firefox WebDriver

## Instalare

1. Clonează proiectul:
```bash
   git clone https://github.com/28mirceas/Proiect-BDD.git
   cd Proiect-BDD
```
2. Instalează dependențele:
```bash   
pip install -r requirements.txt
```
3. Asigură-te că ai instalat WebDriver-ul potrivit
- ChromeDriver / EdgeDriver / GeckoDriver
             - Poate fi configurat în browser.py

## Rularea testelor

```bash  
Rulare simplă:
behave
Rulare cu afișare detaliată:
behave -v
Rulare pe un anumit feature:
behave features/login.feature
```
## Scenarii de test incluse
      Login
•	Autentificare cu credențiale valide
•	Autentificare cu email invalid
•	Eroare la parolă greșită
     Produse
•	Navigare pagina produse
•	Vizualizare listă produse
•	Adăugare produs în coș
      Coș de cumparaturi
•	Verificarea produselor din coș
•	Modificare cantitate
•	Eliminare produse
     Checkout
•	Completare date utilizator
•	Validare câmpuri obligatorii
•	Confirmare comandă

##  Structura proiectului
```bash 
Proiect-BDD/
│
│ behave.ini # Configurarea Behave (setări pentru rapoarte, limbă etc.)
│ browser.py # Inițializarea driverului Selenium
│ environment.py # Hook-urile Behave (before_all, after_scenario etc.)
│ requirements.txt # Dependențe Python
│ README.md # Documentația proiectului
│
├───features/ # Scenarii BDD (fișiere .feature)
│ cart.feature
│ checkout.feature
│ login.feature
│ products.feature
│
├───pages/ # Page Object Model
│ base_page.py
│ cart_page.py
│ checkout_page.py
│ login_page.py
│ products_page.py
│
├───steps/ # Implementarea pașilor Behave
│ cart_steps.py
│ checkout_steps.py
│ login_steps.py
│ products_steps.py
│
└───pycache/ # Fișiere generate automat
```
Page Object Model
Toate paginile sunt definite în folderul:
pages/
Fiecare fișier conține:
•	locatorii elementelor
•	acțiunile disponibile pe pagină
•	metode reutilizabile pentru scenarii
Exemple:
•	login_page.py
•	products_page.py
•	cart_page.py
•	checkout_page.py
________________________________________
Configurarea Behave
Fișierul behave.ini permite configurarea implicită:
•	limbă (Gherkin)
•	format rapoarte
•	opțiuni pentru rulare
________________________________________
Hook-uri Behave
În environment.py sunt definite:
•	before_all
•	before_scenario
•	after_scenario
•	after_all
Acestea asigură:
•	inițializarea și distrugerea driverului
•	atașarea capturilor la rapoarte (dacă este activată)
•	curățarea resurselor
________________________________________
Rapoarte
În funcție de configurarea din behave.ini, poți genera:
•	rapoarte HTML
•	rapoarte JSON
•	capturi de ecran la eșecuri

## Licenta

[MIT](https://choosealicense.com/licenses/mit/)
