let desenvolvedor = document.querySelector('#dev');
let instituicao = document.querySelector('#inst');
let form = document.querySelector('#frm1');
let div = document.querySelector('#dev');

function trocar1() {
    form.action = 'logininst';
}

function trocar2() {
    form.action = 'logindev';
}
desenvolvedor.onclick = trocar2;
instituicao.onclick = trocar1;