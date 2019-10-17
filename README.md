Niniejszy projekt jest aplikacją do generowania Curriculum Vitae przez odgórny szablon
napisany w Python 3.7.4.
Aplikacja składa się z 4 oddzielnych plików. Plik yaml_data_gen.py odpowiada za tworzenie pliku
yaml, który później będzie użyty do stworzenia pliku html z gotowym CV. Korzysta on z swoistego
szablonu pliku yaml - data_str.yaml . Następnie plik cv_gen.py odpowiada za stworzenie pliku html z
szablonu zawartego w pliku cv_template i bezpośrednie przekonwertowanie go na plik pdf.
Korzysta on z danych zawartych w pliku ur_data.yaml , który użytkownik wcześniej stworzył za
pomocą pliku yaml_data_gen.py . Dodatkowo dla użytkownika dostępny jest podgląd zarówno
stworzonego plku yaml jak i wygenerowanego próbnego szablonu CV( html_temp ).
Projekt wymaga do działania poniższych programów i pakietów:
- Python 3.7.4
- wkhtmltopdf
- Pakiety:
- ruamel.yaml
- PyYAML
- jinja 2
- pdfkit
