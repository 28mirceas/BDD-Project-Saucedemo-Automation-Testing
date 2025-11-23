=== LIBRARII  DE  INSTALAT ===
- selenium
- behave
- behave-html-formatter

=== PLUGINS  DE  INSTALAT ===
- gherkin
- ini

=== STRUCTURA  FOLDERE  SI  FISIERE  SUPLIMENTARE ===
- features
- pages
- steps
- browser.py
- environment.py
- behave.ini

=== COMENZI  EXECUTIE  TESTE ===
- behave   (executa toate testele)
- behave --no-skipped --no-summary -f plain --tags=login(executa toate testele si afiseaza rezultatul detaliat  pentru tagul login)
- behave --tags=login  (executa toate testele cu tag-ul 'login')
- behave --tags=login, smoke  (executa toate testele cu tag-ul 'login' sau 'smoke')
- behave -f html -o report.html --tags=login  (executa toate testele cu tag-ul 'login' si adauga rezultatul executie intr-un raport cu formatul 'html' si output cu numele 'report.html')