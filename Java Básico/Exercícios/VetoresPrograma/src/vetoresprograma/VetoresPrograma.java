/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package vetoresprograma;

import java.util.Calendar;
import java.util.Scanner;

/**
 *
 * @author devshi
 */
public class VetoresPrograma {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int anoAtual = Calendar.getInstance().get(Calendar.YEAR);
        String mes[] = {"Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"};
        String tot[] = {"31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"};
        if ((anoAtual % 400 == 0) || (anoAtual % 4 == 0 && anoAtual % 100 != 0)) {
            tot[1] = "29";
        }
        Scanner t = new Scanner(System.in);
        System.out.print("Digite um valor (1 a 12) (0 para mostrar todos): ");
        int n = t.nextInt();
        int i;
        switch (n) {
            case 1:
                System.out.println(mes[0] + ": com " + tot[0] + " dias");
                break;
            case 2:
                System.out.println(mes[1] + ": com " + tot[1] + " dias");
                break;
            case 3:
                System.out.println(mes[2] + ": com " + tot[2] + " dias");
                break;
            case 4:
                System.out.println(mes[3] + ": com " + tot[3] + " dias");
                break;
            case 5:
                System.out.println(mes[4] + ": com " + tot[4] + " dias");
                break;
            case 6:
                System.out.println(mes[5] + ": com " + tot[5] + " dias");
                break;
            case 7:
                System.out.println(mes[6] + ": com " + tot[6] + " dias");
                break; 
            case 8:
                System.out.println(mes[7] + ": com " + tot[7] + " dias");
                break;
            case 9:
                System.out.println(mes[8] + ": com " + tot[8] + " dias");
                break;
            case 10:
                System.out.println(mes[9] + ": com " + tot[9] + " dias");
                break;
            case 11:
                System.out.println(mes[10] + ": com " + tot[10] + " dias");
                break;
            case 12:
                System.out.println(mes[11] + ": com " + tot[11] + " dias");
                break;
            case 0:
                for (i = 0; i < mes.length; i++) {
                    System.out.println(mes[i] + ": com " + tot[i] + " dias");
             
                }
                break;
            default:
                System.out.println("Número inválido!");
        }
        
    }
    
}
