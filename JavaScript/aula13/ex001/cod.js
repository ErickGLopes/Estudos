function contar() {
    let divRes = document.getElementById('res')
    let txtInicio = document.getElementById('txtinicio')
    let txtFim = document.getElementById('txtfim')
    let txtPasso = document.getElementById('txtpasso')
    
    if (txtInicio.value.length == 0 || txtFim.value.length == 0 || txtPasso.value.length == 0) {
        window.alert('[ERRO] Faltam dados!')
    } else {
        divRes.innerHTML = 'Contando: <br>'
        let i = Number.parseInt(txtInicio.value)
        let f = Number.parseInt(txtFim.value)
        let p = Number.parseInt(txtPasso.value)
        if (i < f) {
            for (let c = i; c <= f; c += p) {
                divRes.innerHTML += `${c} \u{1F449}`
            }
        } else {
            for (let c = i; c >= f; c -= p) {
                divRes.innerHTML += `${c} \u{1F449}`
            }
        }
        divRes.innerHTML += ' \u{1F3C1}'
    }
}