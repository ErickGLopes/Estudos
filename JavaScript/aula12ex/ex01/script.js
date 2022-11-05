function recarregar() {
    var now = new Date();
    var hora = now.getHours();
    var min = now.getMinutes();
    var corpo = document.getElementById('corpo')
    t = document.getElementById('titulo')
    var imagem = document.getElementById('img')
    t.innerText = `Horário: ${hora} h`
    imagem.src = 'imagens/manha-300.jpg'
    if (hora < 12) {
        imagem.src = 'imagens/manha-300.jpg'
        corpo.style.background = '#d08c2b'
    }
    else if (hora <= 18) {
        imagem.src = 'imagens/tarde-300.jpg'
        corpo.style.background = '#e56d4a'
    } else {
        imagem.src = 'imagens/noite-300.jpg'
        corpo.style.background = '#425365'
    }

}
