

function verificar() {

    var anoAtual = new Date().getFullYear()
    var txtRes = document.getElementById('res')
    var masc = document.getElementById('masc')
    var femi = document.getElementById('femi')
    var valorAno = document.getElementById('anoNasc')
    var anoN = Number(valorAno.value)
    var i = anoAtual - anoN
    if (anoN == 0 || anoN > anoAtual || !masc.checked && !femi.checked || i > 120) {
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    } else {
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')

        if (masc.checked) {
           var s = 'Homem'
           if (i >= 0 && i <= 5) {
                // Bebê
                img.setAttribute('src', 'imagens/bebe-m.png')
           } else if (i <= 12) {
                // Criança
                img.setAttribute('src', 'imagens/crianca-m.png')
             }
            else if (i <= 21) {
                // Jovem
                img.setAttribute('src', 'imagens/jovem-m.png')
            }
            else if (i <= 45) {
                // Adulto
                img.setAttribute('src', 'imagens/adulto-m.png')
            }
            else if (i < 60) {
                // Meia idade
                img.setAttribute('src', 'imagens/meiaidade-m.png')
            } else {
                    // Idoso
                    img.setAttribute('src', 'imagens/idoso-m.png')
              }
        }
        else if (femi.checked) {
            var s = 'Mulher'
            if (i >= 0 && i <= 5) {
                // Bebê
                img.setAttribute('src', 'imagens/bebe-f.png')
            } else if (i <= 12) {
                // Criança  
                img.setAttribute('src', 'imagens/crianca-f.png')
              }
            else if (i <= 21) {
                // Jovem
                img.setAttribute('src', 'imagens/jovem-f.png')
            }
            else if (i <= 45) {
                // Adulto
                img.setAttribute('src', 'imagens/adulto-f.png')
            }
            else if (i < 60) {
                // Meia idade
                img.setAttribute('src', 'imagens/meiaidade-f.png')
            } else {
                    // Idoso
                    img.setAttribute('src', 'imagens/idoso-f.png')
              }
        }
        txtRes.innerText = `Detectamos ${s} de ${i} ano(s)`
        txtRes.appendChild(img)
      }
    
}