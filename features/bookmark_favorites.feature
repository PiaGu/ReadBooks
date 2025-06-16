#User Story 003:
#Som användare av "Läslistan" vill jag kunna markera mina favoritböcker med ett hjärta så de sparas i en lista under
#fliken "Mina böcker" så att jag kan se alla mina favoritböcker.

#User Story 0031:
#Som användare av "Läslistan" vill jag kunna avmarkera mina favoritböcker så de tas bort från lista under
#fliken "Mina böcker" så att jag inte behöver se böcker som jag redan har läst.

@favorit_add
  Feature: Favoriter

    Scenario: Favoritmarkera böcker
      Given att användaren är på sidan "Läslistan"
      When användaren hovrar över boken "100 sätt att undvika måndagar"
      Then visas ett hjärta i början av raden för boken
      When användaren klickar på hjärtat för boken "100 sätt att undvika måndagar"
      Then favoritmarkeras boken med ett hjärta
      When användaren klickar på knappen "Mina böcker"
      Then ska boken "100 sätt att undvika måndagar" visas i listan på sidan "Mina Böcker"