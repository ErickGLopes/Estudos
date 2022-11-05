/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package exercicorepita;

import javax.swing.JOptionPane;

/**
 *
 * @author devshi
 */
public class ExercicoRepita {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here 
        int totVals = 0, totPar = 0, totImp = 0, mQc = 0, n, s = 0;
        float m = 0;
        do {
            n = Integer.parseInt(JOptionPane.showInputDialog(null, "<html>"
                    + "Informe um número:<br><em>(0 interrompe)<em></html>"
                    + "", "Entrada de dados", JOptionPane.WARNING_MESSAGE));
            if (n == 0) break;
            totVals += 1;
            s += n;
            if (n % 2 == 0) totPar += 1;
            else totImp += 1;  
            if (n > 100) mQc += 1;
        } while (true);
        m = (float) s / (float)totVals;
        JOptionPane.showMessageDialog(null, String.format("<html>Resultado:"
                + "<br>-----------------------<br>Total de valores: %d<br>Total d"
                + "e Pares: %d<br>Total de Ímpares: %d<br>Acima de 100: %d<"
                + "br>Média dos valores: %.2f</html>", totVals, totPar, totImp, mQc, m), "R"
                + "esultado Final", JOptionPane.WARNING_MESSAGE);
    }
    
}
