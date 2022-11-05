let res = document.querySelector('div#res')
let seltab = document.getElementById('txtres')
let valores = []

function isNumero(n) {
    if (n >= 1 && n <= 100) {
        return true
    } else {
        return false
    }
}

function inLista(lista, n) {
    if (lista.indexOf(Number(n)) != -1) {
        return true
    } else {
        return false
    }
}


function adicionar() {
    let txtnum = document.getElementById('txtnum')
    if (isNumero(txtnum.value) && !inLista(valores, txtnum.value)) {
        let num = Number(txtnum.value)
        valores.push(num)
        let item = document.createElement('option')
        item.text = `Valor ${num} adicionado`
        seltab.appendChild(item)
    } else {
        window.alert('[ERRO] Valor inválido ou repetido!')
    }
    txtnum.value = ''
    txtnum.focus()
        
}


function finalizar() {
    if (valores.length != 0) {
        res.innerHTML = ''
        let aoTodo = valores.length
        let maior 
        let menor
        let soma = 0
        for (let c in valores) {
            soma += valores[c]
            maior = valores[0]
            menor = valores[0]
            if (valores[c] > maior) {
                maior = valores[c]
            } else {
                if (valores[c] < menor) {
                menor = valores[c]
            }
            }
        }
        let média = soma / aoTodo
        res.innerHTML = `<p>Ao todo, temos ${aoTodo} números cadastrados.</p>
                         <p>O maior número foi ${maior}.</p>
                         <p>O menor número foi ${menor}.</p>
                         <p>Somando todos os valores temos ${soma}</p>                  
                         <p>A média dos valores digitados é ${média}</p>
                         `        
    } else {
        window.alert('[ERRO] Não há nenhum valor digitado!')
    }
}