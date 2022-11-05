package com.mycompany.idiomasistema;

import java.util.Locale;

public class IdiomaSistema {

    public static void main(String[] args) {
        Locale idioma = Locale.getDefault();
        System.out.print("O seu sistema está em ");
        System.out.print(idioma.getDisplayLanguage());
    }
}
