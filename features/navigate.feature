# User Story 001:
 # Som användare av "Läslistan" vill jag kunna navigera runt på sidan och klicka på alla flikar så att jag har åtkomst till allt.
 # User Story 002:
 # Som ägare av "Läslistan" vill jag inte att användaren ska kunna klicka på samma flik som hen är på så att det blir tydligt för användaren var hen befinner sig.

  @navi

Feature: Navigering på sidan Läslistan


  Scenario: Navigering mellan flikar och visuell koll ifall knapp är aktiv/inaktiv.
    Given att användaren är på sidan "Läslistan"
    Then knappen "Katalog" ska vara inaktiv
    And knappen "Lägg till bok" ska vara aktiv

    When användaren klickar på knappen "Lägg till bok"
    Then knappen "Lägg till bok" ska vara inaktiv
    And knappen "Katalog" ska vara aktiv

    When användaren klickar på knappen "Mina böcker"
    Then knappen "Mina böcker" ska vara inaktiv
    And knappen "Lägg till bok" ska vara aktiv