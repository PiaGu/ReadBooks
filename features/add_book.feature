# User Stories:
# - US-004: Som användare av Läslistan vill jag kunna lägga till böcker med titel och författare
# - US-005: Som ägare vill jag att det inte går att lägga till en bok med tomma fält

  @book_add


  Feature: Lägga till en ny bok
    För att hålla ordning på vilka böcker jag läst eller vill läsa
    Som användare
    Vill jag kunna lägga till nya titlar med både titel och författare

    Scenario: Lägga till en ny bok med både titel och författare
      Given att användaren är på sidan "Läslistan"
      When användaren klickar på knappen "Lägg till bok"
      And användaren fyller i fältet "Titel" med en boktitel
      And användaren fyller i fältet "Författare" med bokens författare
      And användaren klickar på knappen "Lägg till ny bok"
      And användaren klickar på knappen "Katalog"
      Then ska boken visas i katalogen

    Scenario: Försök att lägga till en bok med enbart titel
      Given att användaren är på sidan "Läslistan"
      When användaren klickar på knappen "Lägg till bok"
      And användaren fyller i fältet "Titel" med en boktitel
      Then ska knappen "Lägg till ny bok" vara inaktiv

    Scenario: Försök att lägga till en bok med enbart författare
      Given att användaren är på sidan "Läslistan"
      When användaren klickar på knappen "Lägg till bok"
      And användaren fyller i fältet "Författare" med bokens författare
      Then ska knappen "Lägg till ny bok" vara inaktiv
