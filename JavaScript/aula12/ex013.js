var now = new Date()
var diaSem = now.getDay()
var p = 'Hoje é '
switch(diaSem) {
    case 0:
        console.log(`${p}Domingo`)
        break
    case 1:
        console.log(`${p}Segunda-Feira`)
        break
    case 2:
        console.log(`${p}Terça-Feira`)
        break
    case 3:
        console.log(`${p}Quarta-Feira`)
        break
    case 4:
        console.log(`${p}Quinta-Feira`)
        break
    case 5:
        console.log(`${p}Sexta-Feira`)
        break
    case 6:
        console.log(`${p}Sábado`)
        break
    default:
        console.log('[ERRO] Dia inválido!')
}