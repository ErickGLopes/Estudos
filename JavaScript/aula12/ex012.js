var now = new Date()
var h = now.getHours()
var m = now.getMinutes()
var s = now.getSeconds()
console.log(`Agora são ${h}:${m}:${s}`)
if (h < 12) {
    console.log('Bom dia!')
}
else if (h < 18) {
    console.log('Boa tarde!')
} else {
    console.log('Boa noite!')
}