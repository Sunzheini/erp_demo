function solve() {

    // Selections
    let tableForm1 = document.getElementsByClassName('table-form')[2]
    let tableForm2 = document.getElementsByClassName('table-form')[3]
    let tableForm3 = document.getElementsByClassName('table-form')[4]

    let tableFormBody1 = Array.from(tableForm1.children)[1]
    let tableFormBody2 = Array.from(tableForm2.children)[1]
    let tableFormBody3 = Array.from(tableForm3.children)[1]

    let tableFormBodyElements1 = Array.from(tableFormBody1.children)
    let tableFormBodyElements2 = Array.from(tableFormBody2.children)
    let tableFormBodyElements3 = Array.from(tableFormBody3.children)

    // Hiding empty1
    for (let i = 0; i < tableFormBodyElements1.length; i++) {
        let currentElement = tableFormBodyElements1[i]
        let currentElementChildren = Array.from(currentElement.children)  // tr * 6

        let currentElementTd = currentElementChildren[1]                           // td.when-1.showing
        let currentInput = currentElementTd.innerHTML

        if (currentInput === 'None') {
            currentElement.style.display = 'none'
        }
    }

    // Hiding empty2
    for (let i = 0; i < tableFormBodyElements2.length; i++) {
        let currentElement = tableFormBodyElements2[i]
        let currentElementChildren = Array.from(currentElement.children)  // tr * 6

        let currentElementTd = currentElementChildren[1]                           // td.when-1.showing
        let currentInput = currentElementTd.innerHTML

        if (currentInput === 'None') {
            currentElement.style.display = 'none'
        }
    }

    // Hiding empty3
    for (let i = 0; i < tableFormBodyElements3.length; i++) {
        let currentElement = tableFormBodyElements3[i]
        let currentElementChildren = Array.from(currentElement.children)  // tr * 6

        let currentElementTd = currentElementChildren[1]                           // td.when-1.showing
        let currentInput = currentElementTd.innerHTML

        if (currentInput === 'None') {
            currentElement.style.display = 'none'
        }
    }
}

solve()

