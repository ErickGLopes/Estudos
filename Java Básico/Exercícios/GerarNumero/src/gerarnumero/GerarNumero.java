/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package gerarnumero;

/**
 *
 * @author devshi
 */
public class GerarNumero {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
            double num[] = new double[10];
            String n = "";
            for (int i = 0; i < 10; i++) {
                num[i] = 1 + Math.random() * (10 - 1);
            }
            for (int i = 0; i < 10; i++) {
                n += Integer.toString((int) num[i]);
            }
            System.out.println(Long.parseLong(n));
            
        
    }
    
}
