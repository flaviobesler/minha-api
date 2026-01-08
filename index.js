console.log('js carregou')

document.getElementById('addDivida').addEventListener('click', addDivida);
async function addDivida() {
    const despesa = document.getElementById('despesa').value;
    const valorDespesa = parseFloat(document.getElementById('valor').value);
    const pagParcial = parseFloat(document.getElementById('pagParcial').value);
    
    
    const response = await fetch('http://127.0.0.1:8000/api/dividas',{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            despesa: despesa,
            pagValor: valorDespesa,
            pagParcial:pagParcial,
        })

    });
    console.log('response funcionando',response);

}
