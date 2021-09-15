function positionHelper(head, nivel, descendientes) {
    if(!head) {
        return
    }
    if ( head.child.length === 0 ){
        nivel -= 1
        return 
    }
    nivel += 1
    head.child.forEach(hijo => {
        descendientes.push({hijo, nivel: nivel, padre: head.process.PID.toString()})
        positionHelper(hijo, nivel, descendientes)
    });
}

function calcularPosicionPorNivel(descendientes, cantidadEnNiveles, numeroNiveles) {
    const alturaMaxima = 500
    const largoMaximo = 600
    const step = alturaMaxima/numeroNiveles
    alturaPorNiveles = Array.apply(null, Array(numeroNiveles)).map(function () {return 0})
    for(var i = 0; i < numeroNiveles; i++) {
        if ( i === 0 ) {
            console.log("Aqui")
            alturaPorNiveles[0] = 170 + step
        } else {
            console.log("here")
            alturaPorNiveles[i] = 170 + step * (i + 1)
        }
    }

    const elementos = Array.apply(null, Array(descendientes.length)).map(function () {})
    cantidadTotal = 0
    for (var i = 0; i < cantidadEnNiveles.length; i++) {
        for (var j = 0; j < cantidadEnNiveles[i]; j++ ) {
            const elem = descendientes[cantidadTotal]
            const levelAux = elem.nivel - 1
            const y = alturaPorNiveles[levelAux]
            const stepX = largoMaximo/cantidadEnNiveles[levelAux] 
            const x = 50 + stepX * j 
            elementos[cantidadTotal] = {data: {id : elem.hijo.process.PID.toString()}, position: {x: x, y: y }}
            cantidadTotal += 1
        }
    }

    aristasHijos = Array.apply(null, Array(descendientes.length)).map(function () {})
    for( var k = 0; k < descendientes.length; k++) {
      const pidHijo = descendientes[k].hijo.process.PID.toString()
      const pidPadre = descendientes[k].padre
      aristasHijos[k] = {data: {id: pidHijo + pidPadre, source: pidPadre, target: pidHijo }}
    }
    return {nodosHijos: elementos, aristasHijos}
}

const obtenerPosicionHijosFibonacci = (head) => {
 let descendientes = [];
 positionHelper(head, 0, descendientes);
 descendientes =  descendientes.sort(function(a, b) {
     return a.nivel - b.nivel
 })
 if(!descendientes.length) {
   return []
 }
 const numeroNiveles = descendientes[descendientes.length-1].nivel
 const cantidadEnNiveles = Array.apply(null, Array(numeroNiveles)).map(function () {return 0})
 descendientes.forEach(descendiente => {
     cantidadEnNiveles[descendiente.nivel -1] += 1
 })
return calcularPosicionPorNivel(descendientes, cantidadEnNiveles, numeroNiveles)
}

module.exports = obtenerPosicionHijosFibonacci