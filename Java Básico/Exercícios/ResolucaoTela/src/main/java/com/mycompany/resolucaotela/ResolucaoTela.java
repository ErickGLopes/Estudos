package com.mycompany.resolucaotela;

import java.awt.Dimension;
import java.awt.Toolkit;

public class ResolucaoTela {

    public static void main(String[] args) {
        Toolkit tk = Toolkit.getDefaultToolkit();
        Dimension res = tk.getScreenSize();
        int lar = res.width;
        int alt = res.height;
        System.out.print("Sua resolução está em "+lar+"x"+alt);
    }
}
