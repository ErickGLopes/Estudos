/*// For in, indexOf, push(<var ou valor>), sort(), 
let num = [8, 9, 1, 0]
console.log(`Vetor num inicial -> ${num}`)
console.log(`O vetor num ordenado fica assim -> ${num.sort()}`)
num.push(7)
console.log(`O número 7 foi adicionado -> ${num}`)
console.log(`O número 8 está na posição ${num.indexOf(8)}`)
console.log('=-=-=-=-==-=-=-=-=-=-=-=-=-=')
console.log('Exibindo o vetor por For-in:')
for (let c in num) {
    console.log(`${num[c]}`)
}*/

// POO em JavaScript
let amigo = {nome: 'Marcos', idade: 26, sexo: 'masculino', fazerAniv() {this.idade ++}}
amigo.fazerAniv()
console.log(`O ${amigo.nome} tem ${amigo.idade} anos e é do sexo ${amigo.sexo}`)
console.log(typeof amigo)