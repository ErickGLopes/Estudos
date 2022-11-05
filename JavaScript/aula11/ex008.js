var vel = 60
console.log(`\nA velocidade do seu carro é de ${vel.toFixed(1).replace('.', ',')}Km/h`)
if (vel > 60) {
    console.log('Você ultrapassou o limite de velocidade. MULTADO!')
} else {
    console.log('Boa viagem!')
}
console.log('Dirija sempre usando cinto de segurança!\n')
