/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package idadevoto;

import java.util.Calendar;
import java.util.Scanner;

/**
 *
 * @author devshi
 */
public class IdadeVoto {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner t = new Scanner(System.in);
        int anoAtual = Calendar.getInstance().get(Calendar.YEAR);
        System.out.print("Digite o ano do seu nascimento: ");
        int anoNasc = t.nextInt();
        int i = anoAtual - anoNasc;
        System.out.print("Com " + i + " anos, ");
        if (i < 16) {
            System.out.print("não vota!\n");
        } else {
            if ((i >= 16 && i < 18) || (i > 70)) {
                System.out.print("voto opcional!\n");
        } else {
                System.out.print("voto obrigatório!\n");
        }
        }
        
        
             
    }
    
}
