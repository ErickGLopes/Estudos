function gerar() {
    let txtnum = document.getElementById('txtnum')
    let seltab = document.getElementById('seltab')
    if (txtnum.value.length == 0) {
        window.alert('[ERRO] Faltam dados!')
    } else {

        let n = Number(txtnum.value)
        let c = 1
        seltab.innerHTML = ''
        while (c <= 10) {
            let item = document.createElement('option')
            item.text = `${n} x ${c} = ${n * c}`
            seltab.appendChild(item)    
            c++
        }
    }
}