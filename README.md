
Vad som är testat:

*Att det går att öppna sidan och klicka på alla 3 flikar. 
*Att det går att markera sina favoritbok.
*Att favoritboken går att se i listan under fliken "Mina Böcker".
*Att det går att lägga till en bok när både titel och författare är ifylld.
*Att det inte går att lägga till en bok/författare ifall något av inmatningsfälten är tomma. 
*Att den tillagda boken är synlig i listan under katalogfliken. 

Gör så här: 

Skapa ett nytt projekt med PyCharm
GitHub repository finns här: URL..
clona repot
Starta sedan terminalen i projektets rotmapp och skriv:
pip install pytest-playwright
playwright install
pip install behave


För att köra alla tester, skriv behave i projektets rotmap i terminalfönstret i PyCharm.

Om du endast vill köra några av testerna använd taggarna.
