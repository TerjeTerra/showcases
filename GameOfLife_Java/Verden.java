class Verden {
    Rutenett rutenett;
    int antRader;
    int antKolonner;
    int genNr; // brukes ikke i Utsyn, men kunne vaert lagt innn som opplysning

    public Verden(int rader, int kolonner) {
        genNr = 0;
        antRader = rader;
        antKolonner = kolonner;
        rutenett = new Rutenett(antRader, antKolonner);
        // fylle med tilfeldige celler
        rutenett.fyllMedTilfeldigeCeller();
        // koble sammen
        rutenett.kobleAlleCeller();
    }

    // GAMMEL METODE (Brukes ikke i GUI)
    public void tegn() {
        rutenett.tegnRutenett(); // tegne verden
        System.out.println("Generasjonsnummer: " + genNr); // skrive ut generasjonsnummeret
        System.out.println("Levende celler: " + rutenett.antallLevende());// skrive ut antall levende celler.
    }

    public Rutenett hentRutenett(){
        return rutenett;
    }

    public void oppdatering() {
        // Gaa gjennom alle celler i rutenettet og telle og oppdatere antallet levende naboer for hver celle.
        for (int r = 0; r < antRader; r++){
            for (int k = 0; k < antKolonner; k++){
                rutenett.hentCelle(r, k).tellLevendeNaboer();
            }
        }
        // Gaa gjennom alle celler i rutenettet og oppdatere status (dvs om den erlevende eller død) på hver celle.
        for (int r = 0; r < antRader; r++){
            for (int k = 0; k < antKolonner; k++){
                rutenett.hentCelle(r, k).oppdaterStatus();
            }
        }
        genNr++; // Oppdatere telleren for antall generasjoner.
    }
}
