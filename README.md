
Vad som är testat:

*Att det går att öppna sidan och klicka på alla 3 flikar. 
*Att det går att markera sina favoritbok.
*Att favoritboken går att se i listan under fliken "Mina Böcker".
*Att det går att lägga till en bok när både titel och författare är ifylld och boken är synlig i kataloglistan.  
*Att det inte går att lägga till en bok/författare ifall något av inmatningsfälten är tomma. 
*Att den tillagda boken är synlig i listan under katalogfliken. 

Gör så här: 

Öppna PyCharm
Klona repot genom att köra:
git clone https://github.com/PiaGu/ReadBooks.git
Gå till projektets rotkatalog ReadBooks
(Alla kommandon körs i terminalen i projektets rotmapp.)

Installera beroenden: 

pip install pytest-playwright

playwright install

pip install behave

För att exekvera testerna:

behave

(Testerna går även att köra med taggar tex taggen @favorit_add. Taggarna står i respektive feature fil.)

behave --tags="@favorit_add"





